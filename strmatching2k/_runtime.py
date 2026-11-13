"""Small VBA compatibility layer for this recovered algorithm, not a VBA VM."""
from copy import deepcopy
from decimal import Decimal, ROUND_HALF_UP
import math
import re
import struct


class VBAError(ValueError):
    pass


class _Empty:
    def __deepcopy__(self, memo):
        return self


EMPTY = _Empty()
MISSING = object()


class Single(float):
    def __new__(cls, value=0):
        return super().__new__(cls, struct.unpack('<f', struct.pack('<f', float(number(value))))[0])


class Integer(int):
    def __new__(cls, value=0):
        value = round(number(value))
        if not -32768 <= value <= 32767:
            raise VBAError('Integer overflow')
        return super().__new__(cls, value)


class Long(int):
    def __new__(cls, value=0):
        value = round(number(value))
        if not -2147483648 <= value <= 2147483647:
            raise VBAError('Long overflow')
        return super().__new__(cls, value)


def number(value):
    if value is EMPTY:
        return 0
    if value is None or value is MISSING:
        raise VBAError('Invalid use of Null or missing argument')
    if isinstance(value, bool):
        return -1 if value else 0
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError as exc:
            raise VBAError('Type mismatch: ' + repr(value)) from exc
    return value


def string(value):
    if value is EMPTY:
        return ''
    if value is None or value is MISSING or isinstance(value, Array):
        raise VBAError('Invalid String conversion')
    if isinstance(value, bool):
        return 'True' if value else 'False'
    return str(value)


def truth(value):
    return False if value is None or value is EMPTY else bool(value)


def default(typ):
    if typ == 'integer': return Integer(0)
    if typ == 'long': return Long(0)
    if typ == 'single': return Single(0)
    if typ == 'double': return 0.0
    if typ == 'string': return ''
    if typ == 'boolean': return False
    if typ == 'object': return None
    return EMPTY


def coerce(value, typ):
    converters = {'integer': Integer, 'long': Long, 'single': Single,
                  'double': lambda x: float(number(x)), 'string': string,
                  'boolean': lambda x: bool(number(x))}
    if typ in converters:
        return converters[typ](value)
    return deepcopy(value) if isinstance(value, Array) else value


class Cell:
    def __init__(self, value=EMPTY, typ='variant'):
        self.typ = typ
        self.value = value

    def set(self, value):
        self.value = coerce(value, self.typ)


class Array:
    def __init__(self, bounds, typ='variant'):
        self.bounds = tuple((int(lo), int(hi)) for lo, hi in bounds)
        if any(hi < lo for lo, hi in self.bounds):
            raise VBAError('Subscript out of range: invalid bounds')
        self.typ = typ
        self.values = {}

    def key(self, indices):
        indices = tuple(int(number(i)) for i in indices)
        if len(indices) != len(self.bounds) or any(not lo <= i <= hi for i, (lo, hi) in zip(indices, self.bounds)):
            raise VBAError('Subscript out of range: ' + repr(indices))
        return indices

    def get(self, *indices):
        return self.values.get(self.key(indices), default(self.typ))

    def set(self, indices, value):
        self.values[self.key(indices)] = coerce(value, self.typ)


def chars(value):
    data = string(value).encode('utf-16-le', errors='surrogatepass')
    return [data[i:i + 2].decode('utf-16-le', errors='surrogatepass') for i in range(0, len(data), 2)]


class Frame:
    def __init__(self, context, name, declarations, signature, arguments, result_type):
        self.context = context
        self.name = name
        self.cells = {n: Cell(default(t), t) for n, t in declarations.items()}
        for index, (param, typ, byval, optional, fallback) in enumerate(signature):
            arg = arguments[index] if index < len(arguments) else MISSING
            if arg is MISSING:
                if not optional:
                    raise VBAError('Missing required argument ' + param)
                value = fallback if fallback is not MISSING else (MISSING if typ == 'variant' else default(typ))
                self.cells[param] = Cell(value, typ)
            elif not byval and isinstance(arg, Cell):
                self.cells[param] = arg
            else:
                value = arg.value if isinstance(arg, Cell) else arg
                self.cells[param] = Cell(coerce(value, typ), typ)
        if result_type:
            self.cells[name] = Cell(default(result_type), result_type)
        self.result_type = result_type
        self.loops = {}
        self.handler = None
        self.handling_error = False

    def ref(self, name):
        if name in self.context.globals:
            return self.context.globals[name]
        return self.cells[name]

    def get(self, name):
        return self.ref(name).value

    def set(self, name, value):
        self.ref(name).set(value)

    def index(self, name, *indices):
        value = self.get(name)
        if not isinstance(value, Array):
            raise VBAError('Array required: ' + name)
        return value.get(*indices)

    def put(self, name, indices, value):
        self.get(name).set(indices, value)

    def redim(self, name, bounds, preserve, typ):
        old = self.get(name)
        array = Array(bounds, typ or (old.typ if preserve and isinstance(old, Array) else 'variant'))
        if preserve and isinstance(old, Array):
            if len(old.bounds) != len(array.bounds) or old.bounds[:-1] != array.bounds[:-1] or old.bounds[-1][0] != array.bounds[-1][0]:
                raise VBAError('ReDim Preserve can change only the final upper bound')
            array.values = {k: v for k, v in old.values.items()
                            if all(lo <= i <= hi for i, (lo, hi) in zip(k, array.bounds))}
        self.ref(name).value = array

    def begin_loop(self, key, variable, lower, upper, step):
        self.set(variable, lower)
        self.loops[key] = (variable, upper, step)
        return number(lower) <= number(upper) if number(step) >= 0 else number(lower) >= number(upper)

    def next_loop(self, key):
        variable, upper, step = self.loops[key]
        self.set(variable, self.context.binary('+', self.get(variable), step))
        current = number(self.get(variable))
        return current <= number(upper) if number(step) >= 0 else current >= number(upper)


class Context:
    def __init__(self, functions, text_key=str.casefold):
        self.functions = functions
        self.text_key = text_key
        self.globals = {'cache_m8_0000': Cell(Integer(0), 'integer'),
                        'cache_m8_0004': Cell(), 'cache_m8_0014': Cell()}

    def call(self, name, arguments):
        return self.functions[name](self, arguments)

    def binary(self, op, left, right):
        if op in ('and', 'or'):
            if left is None or right is None:
                other = right if left is None else left
                if op == 'and' and other is not None and number(other) == 0:
                    return False
                if op == 'or' and other is not None and number(other) == -1:
                    return True
                return None
            value = int(number(left)) & int(number(right)) if op == 'and' else int(number(left)) | int(number(right))
            return bool(value) if isinstance(left, bool) and isinstance(right, bool) else Long(value)
        if op == '&':
            if left is None and right is None:
                return None
            return ('' if left is None else string(left)) + ('' if right is None else string(right))
        if left is None or right is None:
            return None
        if op == 'like':
            pattern = string(right)
            pieces = []
            i = 0
            while i < len(pattern):
                char = pattern[i]
                if char == '*': pieces.append('.*')
                elif char == '?': pieces.append('.')
                elif char == '#': pieces.append('[0-9]')
                elif char == '[':
                    end = pattern.find(']', i + 1)
                    if end < 0: raise VBAError('Invalid Like pattern')
                    group = pattern[i + 1:end]
                    pieces.append('[' + ('^' + group[1:] if group.startswith('!') else group) + ']')
                    i = end
                else: pieces.append(re.escape(char))
                i += 1
            return re.fullmatch(''.join(pieces), string(left), re.IGNORECASE | re.DOTALL) is not None
        if op in ('=', '<>', '<', '>', '<=', '>='):
            if left is EMPTY: left = '' if isinstance(right, str) else 0
            if right is EMPTY: right = '' if isinstance(left, str) else 0
            if isinstance(left, str) and isinstance(right, str):
                left, right = self.text_key(left), self.text_key(right)
            else:
                left, right = number(left), number(right)
            if op == '=': return left == right
            if op == '<>': return left != right
            if op == '<': return left < right
            if op == '>': return left > right
            if op == '<=': return left <= right
            return left >= right
        if op == '+' and isinstance(left, str) and isinstance(right, str):
            return left + right
        a, b = number(left), number(right)
        if op == '+': result = a + b
        elif op == '-': result = a - b
        elif op == '*': result = a * b
        elif op == '/': return float(a) / float(b)
        elif op == 'mod': result = round(a) - math.trunc(round(a) / round(b)) * round(b)
        else: raise VBAError('Unsupported operator ' + op)
        if isinstance(left, float) and not isinstance(left, Single) or isinstance(right, float) and not isinstance(right, Single):
            return float(result)
        if isinstance(left, Single) or isinstance(right, Single):
            return Single(result)
        if isinstance(left, Long) or isinstance(right, Long):
            return Long(result)
        return Integer(result)

    def unary(self, op, value):
        if value is None: return None
        if op == 'not':
            return not value if isinstance(value, bool) else Long(~int(number(value)))
        return self.binary('-', Integer(0), value)

    def builtin(self, name, args):
        if name == 'cint': return Integer(args[0])
        if name == 'clng': return Long(args[0])
        if name == 'csng': return Single(args[0])
        if name == 'cdbl': return float(number(args[0]))
        if name == 'cstr': return string(args[0])
        if name == 'cbool': return bool(number(args[0]))
        if name == 'isnull': return args[0] is None
        if name == 'isempty': return args[0] is EMPTY
        if name == 'ismissing': return args[0] is MISSING
        if name == 'iif': return args[1] if truth(args[0]) else args[2]
        if name == 'vba.array':
            result = Array([(0, len(args) - 1)])
            for i, value in enumerate(args): result.set([i], value)
            return result
        if name == 'ubound':
            if not isinstance(args[0], Array): raise VBAError('Array required for UBound')
            dim = int(number(args[1])) if len(args) > 1 else 1
            if not 1 <= dim <= len(args[0].bounds): raise VBAError('Invalid array dimension')
            return Long(args[0].bounds[dim - 1][1])
        if name in ('mid', 'left', 'len', 'trim'):
            if args[0] is None: return None
            units = chars(args[0])
            if name == 'len': return Long(len(units))
            if name == 'trim': return string(args[0]).strip(' ')
            start = 0 if name == 'left' else int(number(args[1])) - 1
            count = int(number(args[1])) if name == 'left' else (int(number(args[2])) if len(args) > 2 else len(units))
            if start < 0 or count < 0: raise VBAError('Invalid Mid/Left argument')
            return ''.join(units[start:start + count])
        if name == 'instr':
            start, source, part = args[:3]
            if source is None or part is None: return None
            start = int(number(start))
            if start < 1: raise VBAError('Invalid InStr start')
            source, part = ''.join(chars(source)), ''.join(chars(part))
            compare = int(number(args[3])) if len(args) > 3 else 2
            if compare:
                source, part = self.text_key(source), self.text_key(part)
            return Long(source.find(part, start - 1) + 1)
        if name == 'format':
            value, pattern = args[:2]
            if value is None: return ''
            if pattern not in ('0.00', '#.##'):
                raise VBAError('Unsupported numeric format ' + repr(pattern))
            # Numeric formatting is distinct from CInt/CLng's ties-to-even.
            # Automation-style decimal rendering followed by decimal half-up.
            rounded = Decimal(format(float(number(value)), '.15g')).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
            text = format(rounded, '.2f')
            if pattern == '#.##':
                text = text.rstrip('0').rstrip('.')
                if text.startswith('0.'): text = text[1:]
                if text == '0': text = ''
            return text
        raise VBAError('Unsupported intrinsic ' + name)


def run(context, name, signature, declarations, result_type, blocks, arguments):
    frame = Frame(context, name, declarations, signature, arguments, result_type)
    pc = 0
    while pc is not None:
        try:
            pc = blocks[pc](frame, context)
        except (VBAError, ZeroDivisionError, OverflowError) as exc:
            if frame.handler is None or frame.handling_error:
                raise VBAError(f'{name}, block {pc}: {exc}') from exc
            frame.handling_error = True
            pc = frame.handler
    return frame.get(name) if result_type else EMPTY
