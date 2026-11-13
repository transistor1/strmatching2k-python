"""Translate this project's smoke-tested VBA candidates into Python blocks.

Fails on unfamiliar syntax. The generated module has no VBA source dependency.
This is intentionally a translator for the recovered subset, not general VBA.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r'\s*("(?:[^"\n]|"")*"|\d+(?:\.\d+)?(?:[Ee][+-]?\d+)?|[A-Za-z_][A-Za-z_0-9.]*|<>|<=|>=|[()+*/&,=<>-])')
PRECEDENCE = {'or': 1, 'and': 2, '=': 3, '<>': 3, '<': 3, '>': 3,
              '<=': 3, '>=': 3, 'like': 3, '&': 4, '+': 5, '-': 5,
              '*': 6, '/': 6, 'mod': 6}


def split_top(text, separator=','):
    depth, quote, start, parts, i = 0, False, 0, [], 0
    while i < len(text):
        char = text[i]
        if char == '"':
            if quote and i + 1 < len(text) and text[i + 1] == '"':
                i += 2
                continue
            quote = not quote
        elif not quote:
            if char == '(': depth += 1
            elif char == ')': depth -= 1
            elif char == separator and not depth:
                parts.append(text[start:i].strip())
                start = i + 1
        i += 1
    return parts + [text[start:].strip()]


def strip_comment(text):
    quote = False
    for i, char in enumerate(text):
        if char == '"': quote = not quote
        elif char == "'" and not quote: return text[:i].strip()
    return text.strip()


class Expression:
    def __init__(self, text):
        self.tokens = []
        pos = 0
        while pos < len(text):
            match = TOKEN.match(text, pos)
            if not match:
                raise ValueError('Unparsed expression: ' + text[pos:])
            self.tokens.append(match[1])
            pos = match.end()
        self.position = 0

    def take(self):
        token = self.tokens[self.position]
        self.position += 1
        return token

    def peek(self):
        return self.tokens[self.position].lower() if self.position < len(self.tokens) else ''

    def parse(self, minimum=0):
        token = self.take()
        low = token.lower()
        if token == '(':
            left = self.parse()
            assert self.take() == ')'
        elif low in ('not', '-'):
            left = ('unary', low, self.parse(3 if low == 'not' else 7))
        elif token.startswith('"'):
            left = ('string', token[1:-1].replace('""', '"'))
        elif token[0].isdigit():
            left = ('number', token)
        else:
            left = ('variable', low)
            if self.peek() == '(':
                self.take()
                args = []
                if self.peek() != ')':
                    while True:
                        args.append(self.parse())
                        if self.peek() != ',': break
                        self.take()
                assert self.take() == ')'
                left = ('call', low, args)
        while self.peek() in PRECEDENCE and PRECEDENCE[self.peek()] >= minimum:
            op = self.take().lower()
            left = ('binary', op, left, self.parse(PRECEDENCE[op] + 1))
        return left


def parse(text):
    parser = Expression(text.strip())
    node = parser.parse()
    assert parser.position == len(parser.tokens), text
    return node


def emit(node, variables, functions):
    kind, value, *rest = node
    if kind == 'string': return repr(value)
    if kind == 'number':
        if any(c in value.lower() for c in '.e'): return value
        return f'{"Integer" if int(value) <= 32767 else "Long"}({value})'
    if kind == 'variable':
        if value in ('null', 'true', 'false', 'nothing'):
            return {'null': 'None', 'true': 'True', 'false': 'False', 'nothing': 'None'}[value]
        assert value in variables, 'Undeclared variable: ' + value
        return f'f.get({value!r})'
    if kind == 'binary':
        return f'c.binary({value!r}, {emit(rest[0], variables, functions)}, {emit(rest[1], variables, functions)})'
    if kind == 'unary':
        return f'c.unary({value!r}, {emit(rest[0], variables, functions)})'
    if value in functions:
        args = []
        for index, arg in enumerate(rest[0]):
            signature = functions[value]['signature'][index]
            if not signature[2] and arg[0] == 'variable':
                args.append(f'f.ref({arg[1]!r})')
            else:
                args.append(emit(arg, variables, functions))
        return f'c.call({value!r}, [{", ".join(args)}])'
    args = ', '.join(emit(arg, variables, functions) for arg in rest[0])
    if value in variables:
        return f'f.index({value!r}, {args})'
    return f'c.builtin({value!r}, [{args}])'


def load_functions():
    functions, globals_, hashes = {}, {}, {}
    for file in sorted((ROOT / 'access-import').glob('*.bas')):
        hashes[file.name] = hashlib.sha256(file.read_bytes()).hexdigest()
        current = None
        for raw in file.read_text(encoding='cp1252').splitlines():
            text = strip_comment(raw)
            if not text: continue
            match = re.fullmatch(r'Public (Function|Sub) (\w+)\((.*)\)(?: As (\w+))?', text)
            if match:
                kind, name, arguments, result = match.groups()
                current = dict(name=name.lower(), signature=[], declarations={}, array_types={},
                               result=result.lower() if result else None, statements=[], labels={})
                for param in split_top(arguments) if arguments else []:
                    arg = re.fullmatch(r'(Optional )?(ByVal|ByRef) (\w+)(\(\))? As (\w+)(?: = (.*))?', param)
                    assert arg, param
                    optional, mode, identifier, array, typ, fallback = arg.groups()
                    current['signature'].append((identifier.lower(), typ.lower(), mode == 'ByVal', bool(optional), fallback))
                functions[name.lower()] = current
            elif text.startswith(('End Function', 'End Sub')):
                current = None
            elif current is not None:
                declaration = re.fullmatch(r'Dim (\w+)(\(\))? As (\w+)', text)
                if declaration:
                    name, array, typ = declaration.groups()
                    current['declarations'][name.lower()] = 'variant' if array else typ.lower()
                    if array:
                        current['array_types'][name.lower()] = typ.lower()
                elif text.endswith(':'):
                    current['labels'][text[:-1]] = len(current['statements'])
                else:
                    current['statements'].append(text)
            else:
                global_ = re.fullmatch(r'Public (\w+) As (\w+)', text)
                if global_: globals_[global_[1].lower()] = global_[2].lower()
    return functions, globals_, hashes


def generate():
    functions, globals_, hashes = load_functions()
    output = ['"""Generated Python translation of the reconstructed VBA. Do not hand edit."""',
              'from ._runtime import EMPTY, MISSING, Integer, Long, truth, run', '']
    for name, data in functions.items():
        variables = set(data['declarations']) | {x[0] for x in data['signature']} | set(globals_) | {name}
        expression = lambda text: emit(parse(text), variables, functions)
        lines, labels = data['statements'], data['labels']
        starts = {0, len(lines)} | set(labels.values())
        for_stack, pairs = [], {}
        for i, line in enumerate(lines):
            if line.startswith('For '): for_stack.append(i)
            elif line.startswith('Next '):
                begin = for_stack.pop()
                pairs[begin], pairs[i] = i, begin
            if line.startswith(('If ', 'GoTo ', 'For ', 'Next ', 'Resume ', 'Exit ')):
                starts.add(i + 1)
        assert not for_stack
        blocks = []
        for start, stop in zip(sorted(starts), sorted(starts)[1:]):
            block_name = f'_{name}_{start}'
            blocks.append((start, block_name))
            output.append(f'def {block_name}(f, c):')
            terminated = False
            for i in range(start, stop):
                line = lines[i]
                output.append('    # ' + line)
                if line.startswith('If '):
                    match = re.fullmatch(r'If (.*) Then GoTo (\w+) Else GoTo (\w+)', line)
                    assert match, line
                    output.append(f'    return {labels[match[2]]} if truth({expression(match[1])}) else {labels[match[3]]}')
                    terminated = True
                elif line.startswith('GoTo '):
                    output.append(f'    return {labels[line[5:]]}')
                    terminated = True
                elif line.startswith('For '):
                    match = re.fullmatch(r'For (\w+) = (.*) To (.*?)(?: Step (.*))?', line)
                    variable, lower, upper, step = match.groups()
                    output.append(f'    return {i + 1} if f.begin_loop({i}, {variable.lower()!r}, {expression(lower)}, {expression(upper)}, {expression(step or "1")}) else {pairs[i] + 1}')
                    terminated = True
                elif line.startswith('Next '):
                    begin = pairs[i]
                    output.append(f'    return {begin + 1} if f.next_loop({begin}) else {i + 1}')
                    terminated = True
                elif line.startswith('On Error GoTo '):
                    target = line.removeprefix('On Error GoTo ')
                    output.append(f'    f.handler = {labels[target] if target != "0" else None}')
                elif line.startswith('Resume '):
                    output += ['    f.handling_error = False', f'    return {labels[line[7:]]}']
                    terminated = True
                elif line.startswith('Exit '):
                    output.append('    return None')
                    terminated = True
                elif line.startswith('ReDim '):
                    match = re.fullmatch(r'ReDim (Preserve )?(\w+)\((.*)\)', line)
                    preserve, variable, bounds = match.groups()
                    dimensions = []
                    for dimension in split_top(bounds):
                        lower, upper = dimension.split(' To ')
                        dimensions.append(f'({expression(lower)}, {expression(upper)})')
                    typ = data['array_types'].get(variable.lower())
                    output.append(f'    f.redim({variable.lower()!r}, [{", ".join(dimensions)}], {bool(preserve)}, {typ!r})')
                elif line.startswith('Erase '):
                    output.append(f'    f.ref({line[6:].lower()!r}).value = EMPTY')
                elif line.startswith('Set '):
                    output.append('    pass  # Access form-object plumbing has no numeric effect.')
                elif line.startswith('Call '):
                    output.append('    ' + expression(line[5:]))
                else:
                    target, value = line.split(' = ', 1)
                    lhs = parse(target)
                    if lhs[0] == 'variable':
                        output.append(f'    f.set({lhs[1]!r}, {expression(value)})')
                    else:
                        assert lhs[0] == 'call' and lhs[1] in variables
                        indices = ', '.join(emit(arg, variables, functions) for arg in lhs[2])
                        output.append(f'    f.put({lhs[1]!r}, [{indices}], {expression(value)})')
            if not terminated: output.append(f'    return {stop if stop < len(lines) else None}')
            output.append('')
        # Branches can target the position just past the last statement.
        output += [f'def _{name}_end(f, c):', '    return None', '']
        entries = ', '.join(f'{i}: {block}' for i, block in blocks)
        output.append(f'_blocks_{name} = {{{entries}, {len(lines)}: _{name}_end}}')
        signature = '[' + ', '.join(f'({p!r}, {t!r}, {byval}, {optional}, {expression(fallback) if fallback is not None else "MISSING"})'
                                  for p, t, byval, optional, fallback in data['signature']) + ']'
        output += [f'def vb_{name}(c, arguments):',
                   f'    return run(c, {name!r}, {signature}, {data["declarations"]!r}, {data["result"]!r}, _blocks_{name}, arguments)', '']
    output.append('FUNCTIONS = {' + ', '.join(f'{name!r}: vb_{name}' for name in functions) + '}')
    target = ROOT / 'strmatching2k/_generated.py'
    target.write_text('\n'.join(output) + '\n')
    (ROOT / 'strmatching2k/provenance.json').write_text(json.dumps(dict(vba_sha256=hashes, procedures=list(functions)), indent=2) + '\n')
    compile(target.read_text(), str(target), 'exec')
    print('Generated', len(functions), 'Python procedures;', len(output), 'lines')


if __name__ == '__main__':
    generate()
