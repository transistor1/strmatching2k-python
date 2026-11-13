"""Generated Python translation of the reconstructed VBA. Do not hand edit."""
from ._runtime import EMPTY, MISSING, Integer, Long, truth, run

def _bigram_0(f, c):
    # pStr = input_pStr
    f.set('pstr', f.get('input_pstr'))
    # tmp_FF44 = ("%" & pStr)
    f.set('tmp_ff44', c.binary('&', '%', f.get('pstr')))
    # tmp_FF24 = (tmp_FF44 & "#")
    f.set('tmp_ff24', c.binary('&', f.get('tmp_ff44'), '#'))
    # pStr = tmp_FF24
    f.set('pstr', f.get('tmp_ff24'))
    # tmp_FF44 = Len(pStr)
    f.set('tmp_ff44', c.builtin('len', [f.get('pstr')]))
    # StrLen = CInt(CInt(tmp_FF44))
    f.set('strlen', c.builtin('cint', [c.builtin('cint', [f.get('tmp_ff44')])]))
    # BGCount = CInt((StrLen - 1))
    f.set('bgcount', c.builtin('cint', [c.binary('-', f.get('strlen'), Integer(1))]))
    # ReDim BGArray(0 To CLng(BGCount))
    f.redim('bgarray', [(Integer(0), c.builtin('clng', [f.get('bgcount')]))], False, None)
    # For X = 0 To (BGCount - 1)
    return 9 if f.begin_loop(8, 'x', Integer(0), c.binary('-', f.get('bgcount'), Integer(1)), Integer(1)) else 12

def _bigram_9(f, c):
    # tmp_FF24 = Mid(pStr, CLng((X + 1)), 2)
    f.set('tmp_ff24', c.builtin('mid', [f.get('pstr'), c.builtin('clng', [c.binary('+', f.get('x'), Integer(1))]), Integer(2)]))
    # BGArray(CLng(X)) = tmp_FF24
    f.put('bgarray', [c.builtin('clng', [f.get('x')])], f.get('tmp_ff24'))
    # Next X
    return 9 if f.next_loop(8) else 12

def _bigram_12(f, c):
    # Exit Sub
    return None

def _bigram_end(f, c):
    return None

_blocks_bigram = {0: _bigram_0, 9: _bigram_9, 12: _bigram_12, 13: _bigram_end}
def vb_bigram(c, arguments):
    return run(c, 'bigram', [('input_pstr', 'variant', True, False, MISSING), ('bgarray', 'variant', False, False, MISSING)], {'tmp_ff24': 'variant', 'tmp_ff44': 'variant', 'strlen': 'integer', 'bgcount': 'integer', 'x': 'integer', 'pstr': 'variant'}, None, _blocks_bigram, arguments)

def _levdist_0(f, c):
    # pStr1 = input_pStr1
    f.set('pstr1', f.get('input_pstr1'))
    # pStr2 = input_pStr2
    f.set('pstr2', f.get('input_pstr2'))
    # n = CInt(CInt(UBound(pStr1, 1)))
    f.set('n', c.builtin('cint', [c.builtin('cint', [c.builtin('ubound', [f.get('pstr1'), Integer(1)])])]))
    # m = CInt(CInt(UBound(pStr2, 1)))
    f.set('m', c.builtin('cint', [c.builtin('cint', [c.builtin('ubound', [f.get('pstr2'), Integer(1)])])]))
    # If (n = 0) Then GoTo L0039 Else GoTo L0045
    return 5 if truth(c.binary('=', f.get('n'), Integer(0))) else 7

def _levdist_5(f, c):
    # LevDist = CInt(0)
    f.set('levdist', c.builtin('cint', [Integer(0)]))
    # GoTo L0308
    return 57

def _levdist_7(f, c):
    # If (m = 0) Then GoTo L0052 Else GoTo L005E
    return 8 if truth(c.binary('=', f.get('m'), Integer(0))) else 10

def _levdist_8(f, c):
    # LevDist = CInt(0)
    f.set('levdist', c.builtin('cint', [Integer(0)]))
    # GoTo L0308
    return 57

def _levdist_10(f, c):
    # ReDim matrix(0 To CLng((n + 1)), 0 To CLng((m + 1)))
    f.redim('matrix', [(Integer(0), c.builtin('clng', [c.binary('+', f.get('n'), Integer(1))])), (Integer(0), c.builtin('clng', [c.binary('+', f.get('m'), Integer(1))]))], False, 'integer')
    # For i = 0 To n
    return 12 if f.begin_loop(11, 'i', Integer(0), f.get('n'), Integer(1)) else 14

def _levdist_12(f, c):
    # matrix(CLng(i), 0) = CInt(i)
    f.put('matrix', [c.builtin('clng', [f.get('i')]), Integer(0)], c.builtin('cint', [f.get('i')]))
    # Next i
    return 12 if f.next_loop(11) else 14

def _levdist_14(f, c):
    # For j = 0 To m
    return 15 if f.begin_loop(14, 'j', Integer(0), f.get('m'), Integer(1)) else 17

def _levdist_15(f, c):
    # matrix(0, CLng(j)) = CInt(j)
    f.put('matrix', [Integer(0), c.builtin('clng', [f.get('j')])], c.builtin('cint', [f.get('j')]))
    # Next j
    return 15 if f.next_loop(14) else 17

def _levdist_17(f, c):
    # For i = 1 To n
    return 18 if f.begin_loop(17, 'i', Integer(1), f.get('n'), Integer(1)) else 56

def _levdist_18(f, c):
    # tmp_FF00 = CInt((i - 1))
    f.set('tmp_ff00', c.builtin('cint', [c.binary('-', f.get('i'), Integer(1))]))
    # tmp_FEE0 = pStr1(tmp_FF00)
    f.set('tmp_fee0', f.index('pstr1', f.get('tmp_ff00')))
    # s_i = tmp_FEE0
    f.set('s_i', f.get('tmp_fee0'))
    # For j = 1 To m
    return 22 if f.begin_loop(21, 'j', Integer(1), f.get('m'), Integer(1)) else 55

def _levdist_22(f, c):
    # tmp_FF00 = CInt((j - 1))
    f.set('tmp_ff00', c.builtin('cint', [c.binary('-', f.get('j'), Integer(1))]))
    # tmp_FEE0 = pStr2(tmp_FF00)
    f.set('tmp_fee0', f.index('pstr2', f.get('tmp_ff00')))
    # t_j = tmp_FEE0
    f.set('t_j', f.get('tmp_fee0'))
    # cost = CInt(0)
    f.set('cost', c.builtin('cint', [Integer(0)]))
    # If ((Not IsEmpty(s_i)) And (Not IsEmpty(t_j))) Then GoTo L015A Else GoTo L0170
    return 27 if truth(c.binary('and', c.unary('not', c.builtin('isempty', [f.get('s_i')])), c.unary('not', c.builtin('isempty', [f.get('t_j')])))) else 29

def _levdist_27(f, c):
    # If (s_i <> t_j) Then GoTo L0167 Else GoTo L016E
    return 28 if truth(c.binary('<>', f.get('s_i'), f.get('t_j'))) else 29

def _levdist_28(f, c):
    # cost = CInt(1)
    f.set('cost', c.builtin('cint', [Integer(1)]))
    return 29

def _levdist_29(f, c):
    # above = CInt(matrix(CLng((i - 1)), CLng(j)))
    f.set('above', c.builtin('cint', [f.index('matrix', c.builtin('clng', [c.binary('-', f.get('i'), Integer(1))]), c.builtin('clng', [f.get('j')]))]))
    # Left = CInt(matrix(CLng(i), CLng((j - 1))))
    f.set('left', c.builtin('cint', [f.index('matrix', c.builtin('clng', [f.get('i')]), c.builtin('clng', [c.binary('-', f.get('j'), Integer(1))]))]))
    # diag = CInt(matrix(CLng((i - 1)), CLng((j - 1))))
    f.set('diag', c.builtin('cint', [f.index('matrix', c.builtin('clng', [c.binary('-', f.get('i'), Integer(1))]), c.builtin('clng', [c.binary('-', f.get('j'), Integer(1))]))]))
    # tmp_FEAC = CInt((diag + cost))
    f.set('tmp_feac', c.builtin('cint', [c.binary('+', f.get('diag'), f.get('cost'))]))
    # tmp_FECC = CInt((Left + 1))
    f.set('tmp_fecc', c.builtin('cint', [c.binary('+', f.get('left'), Integer(1))]))
    # tmp_FEE0 = CInt((above + 1))
    f.set('tmp_fee0', c.builtin('cint', [c.binary('+', f.get('above'), Integer(1))]))
    # tmp_FE7C = Minimum(tmp_FEE0, tmp_FECC, tmp_FEAC)
    f.set('tmp_fe7c', c.call('minimum', [f.ref('tmp_fee0'), f.ref('tmp_fecc'), f.ref('tmp_feac')]))
    # cell = CInt(CInt(tmp_FE7C))
    f.set('cell', c.builtin('cint', [c.builtin('cint', [f.get('tmp_fe7c')])]))
    # If ((i > 1) And (j > 1)) Then GoTo L020F Else GoTo L02C6
    return 38 if truth(c.binary('and', c.binary('>', f.get('i'), Integer(1)), c.binary('>', f.get('j'), Integer(1)))) else 53

def _levdist_38(f, c):
    # trans = CInt((matrix(CLng((i - 2)), CLng((j - 2))) + 1))
    f.set('trans', c.builtin('cint', [c.binary('+', f.index('matrix', c.builtin('clng', [c.binary('-', f.get('i'), Integer(2))]), c.builtin('clng', [c.binary('-', f.get('j'), Integer(2))])), Integer(1))]))
    # tmp_FF00 = CInt((i - 2))
    f.set('tmp_ff00', c.builtin('cint', [c.binary('-', f.get('i'), Integer(2))]))
    # tmp_FEE0 = pStr1(tmp_FF00)
    f.set('tmp_fee0', f.index('pstr1', f.get('tmp_ff00')))
    # tmp_FEBC = CInt((j - 1))
    f.set('tmp_febc', c.builtin('cint', [c.binary('-', f.get('j'), Integer(1))]))
    # tmp_FECC = pStr2(tmp_FEBC)
    f.set('tmp_fecc', f.index('pstr2', f.get('tmp_febc')))
    # If (tmp_FEE0 <> tmp_FECC) Then GoTo L0262 Else GoTo L026D
    return 44 if truth(c.binary('<>', f.get('tmp_fee0'), f.get('tmp_fecc'))) else 45

def _levdist_44(f, c):
    # trans = CInt((trans + 1))
    f.set('trans', c.builtin('cint', [c.binary('+', f.get('trans'), Integer(1))]))
    return 45

def _levdist_45(f, c):
    # tmp_FF00 = CInt((i - 1))
    f.set('tmp_ff00', c.builtin('cint', [c.binary('-', f.get('i'), Integer(1))]))
    # tmp_FEE0 = pStr1(tmp_FF00)
    f.set('tmp_fee0', f.index('pstr1', f.get('tmp_ff00')))
    # tmp_FEBC = CInt((j - 2))
    f.set('tmp_febc', c.builtin('cint', [c.binary('-', f.get('j'), Integer(2))]))
    # tmp_FECC = pStr2(tmp_FEBC)
    f.set('tmp_fecc', f.index('pstr2', f.get('tmp_febc')))
    # If (tmp_FEE0 <> tmp_FECC) Then GoTo L02A3 Else GoTo L02AE
    return 50 if truth(c.binary('<>', f.get('tmp_fee0'), f.get('tmp_fecc'))) else 51

def _levdist_50(f, c):
    # trans = CInt((trans + 1))
    f.set('trans', c.builtin('cint', [c.binary('+', f.get('trans'), Integer(1))]))
    return 51

def _levdist_51(f, c):
    # If (cell > trans) Then GoTo L02BC Else GoTo L02C4
    return 52 if truth(c.binary('>', f.get('cell'), f.get('trans'))) else 53

def _levdist_52(f, c):
    # cell = CInt(trans)
    f.set('cell', c.builtin('cint', [f.get('trans')]))
    return 53

def _levdist_53(f, c):
    # matrix(CLng(i), CLng(j)) = CInt(cell)
    f.put('matrix', [c.builtin('clng', [f.get('i')]), c.builtin('clng', [f.get('j')])], c.builtin('cint', [f.get('cell')]))
    # Next j
    return 22 if f.next_loop(21) else 55

def _levdist_55(f, c):
    # Next i
    return 18 if f.next_loop(17) else 56

def _levdist_56(f, c):
    # LevDist = CInt(matrix(CLng(n), CLng(m)))
    f.set('levdist', c.builtin('cint', [f.index('matrix', c.builtin('clng', [f.get('n')]), c.builtin('clng', [f.get('m')]))]))
    return 57

def _levdist_57(f, c):
    # Exit Function
    return None

def _levdist_end(f, c):
    return None

_blocks_levdist = {0: _levdist_0, 5: _levdist_5, 7: _levdist_7, 8: _levdist_8, 10: _levdist_10, 12: _levdist_12, 14: _levdist_14, 15: _levdist_15, 17: _levdist_17, 18: _levdist_18, 22: _levdist_22, 27: _levdist_27, 28: _levdist_28, 29: _levdist_29, 38: _levdist_38, 44: _levdist_44, 45: _levdist_45, 50: _levdist_50, 51: _levdist_51, 52: _levdist_52, 53: _levdist_53, 55: _levdist_55, 56: _levdist_56, 57: _levdist_57, 58: _levdist_end}
def vb_levdist(c, arguments):
    return run(c, 'levdist', [('input_pstr1', 'variant', True, False, MISSING), ('input_pstr2', 'variant', True, False, MISSING)], {'tmp_fe7c': 'variant', 'tmp_feac': 'variant', 'tmp_febc': 'variant', 'tmp_fecc': 'variant', 'tmp_fee0': 'variant', 'tmp_ff00': 'variant', 'trans': 'integer', 'cell': 'integer', 'diag': 'integer', 'left': 'integer', 'above': 'integer', 's_i': 'variant', 't_j': 'variant', 'cost': 'integer', 'j': 'integer', 'i': 'integer', 'matrix': 'variant', 'm': 'integer', 'n': 'integer', 'pstr2': 'variant', 'pstr1': 'variant'}, 'integer', _blocks_levdist, arguments)

def _issimilar_0(f, c):
    # RefStr = inputRefStr
    f.set('refstr', f.get('inputrefstr'))
    # TestStr = inputTestStr
    f.set('teststr', f.get('inputteststr'))
    # If IsMissing(Alg2Use) Then GoTo L0020 Else GoTo L0029
    return 3 if truth(c.builtin('ismissing', [f.get('alg2use')])) else 4

def _issimilar_3(f, c):
    # Alg2Use = CStr("")
    f.set('alg2use', c.builtin('cstr', ['']))
    return 4

def _issimilar_4(f, c):
    # If (IsNull(RefStr) Or IsNull(TestStr)) Then GoTo L003F Else GoTo L0044
    return 5 if truth(c.binary('or', c.builtin('isnull', [f.get('refstr')]), c.builtin('isnull', [f.get('teststr')]))) else 6

def _issimilar_5(f, c):
    # GoTo L0B63
    return 233

def _issimilar_6(f, c):
    # If (Alg2Use = "") Then GoTo L0051 Else GoTo L0089
    return 7 if truth(c.binary('=', f.get('alg2use'), '')) else 11

def _issimilar_7(f, c):
    # tmp_FEBC = (RefStr = TestStr)
    f.set('tmp_febc', c.binary('=', f.get('refstr'), f.get('teststr')))
    # tmp_FEAC = tmp_FEBC
    f.set('tmp_feac', f.get('tmp_febc'))
    # tmp_FE6C = IIf(tmp_FEAC, 1, 0)
    f.set('tmp_fe6c', c.builtin('iif', [f.get('tmp_feac'), Integer(1), Integer(0)]))
    # IsSimilar = CSng(CDbl(tmp_FE6C))
    f.set('issimilar', c.builtin('csng', [c.builtin('cdbl', [f.get('tmp_fe6c')])]))
    return 11

def _issimilar_11(f, c):
    # If (IsSimilar = CDbl(1)) Then GoTo L0097 Else GoTo L009C
    return 12 if truth(c.binary('=', f.get('issimilar'), c.builtin('cdbl', [Integer(1)]))) else 13

def _issimilar_12(f, c):
    # GoTo L0B63
    return 233

def _issimilar_13(f, c):
    # tmp_FEBC = (RefStr Like "*.*")
    f.set('tmp_febc', c.binary('like', f.get('refstr'), '*.*'))
    # If tmp_FEBC Then GoTo L00AF Else GoTo L00F0
    return 15 if truth(f.get('tmp_febc')) else 21

def _issimilar_15(f, c):
    # tmp_FE64 = 0
    f.set('tmp_fe64', Integer(0))
    # tmp_FE68 = 1
    f.set('tmp_fe68', Integer(1))
    # tmp_FEAC = ""
    f.set('tmp_feac', '')
    # tmp_FEBC = "."
    f.set('tmp_febc', '.')
    # tmp_FE9C = StrReplace(RefStr, tmp_FEBC, tmp_FEAC, CLng(tmp_FE68), tmp_FE64)
    f.set('tmp_fe9c', c.call('strreplace', [f.ref('refstr'), f.ref('tmp_febc'), f.ref('tmp_feac'), c.builtin('clng', [f.get('tmp_fe68')]), f.ref('tmp_fe64')]))
    # RefStr = tmp_FE9C
    f.set('refstr', f.get('tmp_fe9c'))
    return 21

def _issimilar_21(f, c):
    # tmp_FEBC = (TestStr Like "*.*")
    f.set('tmp_febc', c.binary('like', f.get('teststr'), '*.*'))
    # If tmp_FEBC Then GoTo L0105 Else GoTo L0146
    return 23 if truth(f.get('tmp_febc')) else 29

def _issimilar_23(f, c):
    # tmp_FE64 = 0
    f.set('tmp_fe64', Integer(0))
    # tmp_FE68 = 1
    f.set('tmp_fe68', Integer(1))
    # tmp_FEAC = ""
    f.set('tmp_feac', '')
    # tmp_FEBC = "."
    f.set('tmp_febc', '.')
    # tmp_FE9C = StrReplace(TestStr, tmp_FEBC, tmp_FEAC, CLng(tmp_FE68), tmp_FE64)
    f.set('tmp_fe9c', c.call('strreplace', [f.ref('teststr'), f.ref('tmp_febc'), f.ref('tmp_feac'), c.builtin('clng', [f.get('tmp_fe68')]), f.ref('tmp_fe64')]))
    # TestStr = tmp_FE9C
    f.set('teststr', f.get('tmp_fe9c'))
    return 29

def _issimilar_29(f, c):
    # tmp_FEBC = (RefStr Like "*-*")
    f.set('tmp_febc', c.binary('like', f.get('refstr'), '*-*'))
    # If tmp_FEBC Then GoTo L015B Else GoTo L020E
    return 31 if truth(f.get('tmp_febc')) else 44

def _issimilar_31(f, c):
    # tmp_FE7C = InStr(1, RefStr, "-", 2)
    f.set('tmp_fe7c', c.builtin('instr', [Integer(1), f.get('refstr'), '-', Integer(2)]))
    # tmp_FE6C = (tmp_FE7C + 1)
    f.set('tmp_fe6c', c.binary('+', f.get('tmp_fe7c'), Integer(1)))
    # tmp_FE14 = Mid(RefStr, CLng(tmp_FE6C))
    f.set('tmp_fe14', c.builtin('mid', [f.get('refstr'), c.builtin('clng', [f.get('tmp_fe6c')])]))
    # tmp_FEBC = InStr(1, RefStr, "-", 2)
    f.set('tmp_febc', c.builtin('instr', [Integer(1), f.get('refstr'), '-', Integer(2)]))
    # tmp_FEAC = (tmp_FEBC + 1)
    f.set('tmp_feac', c.binary('+', f.get('tmp_febc'), Integer(1)))
    # tmp_FE9C = Left(RefStr, CLng(tmp_FEAC))
    f.set('tmp_fe9c', c.builtin('left', [f.get('refstr'), c.builtin('clng', [f.get('tmp_feac')])]))
    # tmp_FE64 = 0
    f.set('tmp_fe64', Integer(0))
    # tmp_FE68 = 1
    f.set('tmp_fe68', Integer(1))
    # tmp_FDD4 = ""
    f.set('tmp_fdd4', '')
    # tmp_FDF4 = "-"
    f.set('tmp_fdf4', '-')
    # tmp_FDC4 = StrReplace(tmp_FE14, tmp_FDF4, tmp_FDD4, CLng(tmp_FE68), tmp_FE64)
    f.set('tmp_fdc4', c.call('strreplace', [f.ref('tmp_fe14'), f.ref('tmp_fdf4'), f.ref('tmp_fdd4'), c.builtin('clng', [f.get('tmp_fe68')]), f.ref('tmp_fe64')]))
    # tmp_FDB4 = (tmp_FE9C & tmp_FDC4)
    f.set('tmp_fdb4', c.binary('&', f.get('tmp_fe9c'), f.get('tmp_fdc4')))
    # RefStr = tmp_FDB4
    f.set('refstr', f.get('tmp_fdb4'))
    return 44

def _issimilar_44(f, c):
    # tmp_FEBC = (TestStr Like "*-*")
    f.set('tmp_febc', c.binary('like', f.get('teststr'), '*-*'))
    # If tmp_FEBC Then GoTo L0223 Else GoTo L02D6
    return 46 if truth(f.get('tmp_febc')) else 59

def _issimilar_46(f, c):
    # tmp_FE7C = InStr(1, TestStr, "-", 2)
    f.set('tmp_fe7c', c.builtin('instr', [Integer(1), f.get('teststr'), '-', Integer(2)]))
    # tmp_FE6C = (tmp_FE7C + 1)
    f.set('tmp_fe6c', c.binary('+', f.get('tmp_fe7c'), Integer(1)))
    # tmp_FE14 = Mid(TestStr, CLng(tmp_FE6C))
    f.set('tmp_fe14', c.builtin('mid', [f.get('teststr'), c.builtin('clng', [f.get('tmp_fe6c')])]))
    # tmp_FEBC = InStr(1, TestStr, "-", 2)
    f.set('tmp_febc', c.builtin('instr', [Integer(1), f.get('teststr'), '-', Integer(2)]))
    # tmp_FEAC = (tmp_FEBC + 1)
    f.set('tmp_feac', c.binary('+', f.get('tmp_febc'), Integer(1)))
    # tmp_FE9C = Left(TestStr, CLng(tmp_FEAC))
    f.set('tmp_fe9c', c.builtin('left', [f.get('teststr'), c.builtin('clng', [f.get('tmp_feac')])]))
    # tmp_FE64 = 0
    f.set('tmp_fe64', Integer(0))
    # tmp_FE68 = 1
    f.set('tmp_fe68', Integer(1))
    # tmp_FDD4 = ""
    f.set('tmp_fdd4', '')
    # tmp_FDF4 = "-"
    f.set('tmp_fdf4', '-')
    # tmp_FDC4 = StrReplace(tmp_FE14, tmp_FDF4, tmp_FDD4, CLng(tmp_FE68), tmp_FE64)
    f.set('tmp_fdc4', c.call('strreplace', [f.ref('tmp_fe14'), f.ref('tmp_fdf4'), f.ref('tmp_fdd4'), c.builtin('clng', [f.get('tmp_fe68')]), f.ref('tmp_fe64')]))
    # tmp_FDB4 = (tmp_FE9C & tmp_FDC4)
    f.set('tmp_fdb4', c.binary('&', f.get('tmp_fe9c'), f.get('tmp_fdc4')))
    # TestStr = tmp_FDB4
    f.set('teststr', f.get('tmp_fdb4'))
    return 59

def _issimilar_59(f, c):
    # tmp_FEBC = (RefStr Like "*[/-]*")
    f.set('tmp_febc', c.binary('like', f.get('refstr'), '*[/-]*'))
    # If tmp_FEBC Then GoTo L02EB Else GoTo L036D
    return 61 if truth(f.get('tmp_febc')) else 73

def _issimilar_61(f, c):
    # tmp_FE64 = 0
    f.set('tmp_fe64', Integer(0))
    # tmp_FE68 = 1
    f.set('tmp_fe68', Integer(1))
    # tmp_FEAC = ""
    f.set('tmp_feac', '')
    # tmp_FEBC = "-"
    f.set('tmp_febc', '-')
    # tmp_FE9C = StrReplace(RefStr, tmp_FEBC, tmp_FEAC, CLng(tmp_FE68), tmp_FE64)
    f.set('tmp_fe9c', c.call('strreplace', [f.ref('refstr'), f.ref('tmp_febc'), f.ref('tmp_feac'), c.builtin('clng', [f.get('tmp_fe68')]), f.ref('tmp_fe64')]))
    # RefStr = tmp_FE9C
    f.set('refstr', f.get('tmp_fe9c'))
    # tmp_FE64 = 0
    f.set('tmp_fe64', Integer(0))
    # tmp_FE68 = 1
    f.set('tmp_fe68', Integer(1))
    # tmp_FEAC = ""
    f.set('tmp_feac', '')
    # tmp_FEBC = "/"
    f.set('tmp_febc', '/')
    # tmp_FE9C = StrReplace(RefStr, tmp_FEBC, tmp_FEAC, CLng(tmp_FE68), tmp_FE64)
    f.set('tmp_fe9c', c.call('strreplace', [f.ref('refstr'), f.ref('tmp_febc'), f.ref('tmp_feac'), c.builtin('clng', [f.get('tmp_fe68')]), f.ref('tmp_fe64')]))
    # RefStr = tmp_FE9C
    f.set('refstr', f.get('tmp_fe9c'))
    return 73

def _issimilar_73(f, c):
    # tmp_FEBC = (TestStr Like "*[/-]*")
    f.set('tmp_febc', c.binary('like', f.get('teststr'), '*[/-]*'))
    # If tmp_FEBC Then GoTo L0382 Else GoTo L0404
    return 75 if truth(f.get('tmp_febc')) else 87

def _issimilar_75(f, c):
    # tmp_FE64 = 0
    f.set('tmp_fe64', Integer(0))
    # tmp_FE68 = 1
    f.set('tmp_fe68', Integer(1))
    # tmp_FEAC = ""
    f.set('tmp_feac', '')
    # tmp_FEBC = "-"
    f.set('tmp_febc', '-')
    # tmp_FE9C = StrReplace(TestStr, tmp_FEBC, tmp_FEAC, CLng(tmp_FE68), tmp_FE64)
    f.set('tmp_fe9c', c.call('strreplace', [f.ref('teststr'), f.ref('tmp_febc'), f.ref('tmp_feac'), c.builtin('clng', [f.get('tmp_fe68')]), f.ref('tmp_fe64')]))
    # TestStr = tmp_FE9C
    f.set('teststr', f.get('tmp_fe9c'))
    # tmp_FE64 = 0
    f.set('tmp_fe64', Integer(0))
    # tmp_FE68 = 1
    f.set('tmp_fe68', Integer(1))
    # tmp_FEAC = ""
    f.set('tmp_feac', '')
    # tmp_FEBC = "/"
    f.set('tmp_febc', '/')
    # tmp_FE9C = StrReplace(TestStr, tmp_FEBC, tmp_FEAC, CLng(tmp_FE68), tmp_FE64)
    f.set('tmp_fe9c', c.call('strreplace', [f.ref('teststr'), f.ref('tmp_febc'), f.ref('tmp_feac'), c.builtin('clng', [f.get('tmp_fe68')]), f.ref('tmp_fe64')]))
    # TestStr = tmp_FE9C
    f.set('teststr', f.get('tmp_fe9c'))
    return 87

def _issimilar_87(f, c):
    # tmp_FEBC = Trim(RefStr)
    f.set('tmp_febc', c.builtin('trim', [f.get('refstr')]))
    # RefStr = tmp_FEBC
    f.set('refstr', f.get('tmp_febc'))
    # tmp_FEBC = Len(RefStr)
    f.set('tmp_febc', c.builtin('len', [f.get('refstr')]))
    # RefLen = CInt(CInt(tmp_FEBC))
    f.set('reflen', c.builtin('cint', [c.builtin('cint', [f.get('tmp_febc')])]))
    # tmp_FEBC = Trim(TestStr)
    f.set('tmp_febc', c.builtin('trim', [f.get('teststr')]))
    # TestStr = tmp_FEBC
    f.set('teststr', f.get('tmp_febc'))
    # tmp_FEBC = Len(TestStr)
    f.set('tmp_febc', c.builtin('len', [f.get('teststr')]))
    # TestLen = CInt(CInt(tmp_FEBC))
    f.set('testlen', c.builtin('cint', [c.builtin('cint', [f.get('tmp_febc')])]))
    # If ((RefLen = 0) Or (TestLen = 0)) Then GoTo L045A Else GoTo L045F
    return 96 if truth(c.binary('or', c.binary('=', f.get('reflen'), Integer(0)), c.binary('=', f.get('testlen'), Integer(0)))) else 97

def _issimilar_96(f, c):
    # GoTo L0B63
    return 233

def _issimilar_97(f, c):
    # tmp_FEBC = (RefStr = TestStr)
    f.set('tmp_febc', c.binary('=', f.get('refstr'), f.get('teststr')))
    # tmp_FECC = CBool((Alg2Use = ""))
    f.set('tmp_fecc', c.builtin('cbool', [c.binary('=', f.get('alg2use'), '')]))
    # tmp_FEAC = (tmp_FEBC And tmp_FECC)
    f.set('tmp_feac', c.binary('and', f.get('tmp_febc'), f.get('tmp_fecc')))
    # If tmp_FEAC Then GoTo L0485 Else GoTo L0492
    return 101 if truth(f.get('tmp_feac')) else 103

def _issimilar_101(f, c):
    # IsSimilar = CSng(CDbl(1))
    f.set('issimilar', c.builtin('csng', [c.builtin('cdbl', [Integer(1)])]))
    # GoTo L0B63
    return 233

def _issimilar_103(f, c):
    # ReDim RefArry(0 To CLng(RefLen))
    f.redim('refarry', [(Integer(0), c.builtin('clng', [f.get('reflen')]))], False, 'variant')
    # ReDim TestArry(0 To CLng(TestLen))
    f.redim('testarry', [(Integer(0), c.builtin('clng', [f.get('testlen')]))], False, 'variant')
    # For X = 0 To (RefLen - 1)
    return 106 if f.begin_loop(105, 'x', Integer(0), c.binary('-', f.get('reflen'), Integer(1)), Integer(1)) else 109

def _issimilar_106(f, c):
    # tmp_FEAC = Mid(RefStr, CLng((X + 1)), 1)
    f.set('tmp_feac', c.builtin('mid', [f.get('refstr'), c.builtin('clng', [c.binary('+', f.get('x'), Integer(1))]), Integer(1)]))
    # RefArry(CLng(X)) = tmp_FEAC
    f.put('refarry', [c.builtin('clng', [f.get('x')])], f.get('tmp_feac'))
    # Next X
    return 106 if f.next_loop(105) else 109

def _issimilar_109(f, c):
    # For X = 0 To (TestLen - 1)
    return 110 if f.begin_loop(109, 'x', Integer(0), c.binary('-', f.get('testlen'), Integer(1)), Integer(1)) else 113

def _issimilar_110(f, c):
    # tmp_FEAC = Mid(TestStr, CLng((X + 1)), 1)
    f.set('tmp_feac', c.builtin('mid', [f.get('teststr'), c.builtin('clng', [c.binary('+', f.get('x'), Integer(1))]), Integer(1)]))
    # TestArry(CLng(X)) = tmp_FEAC
    f.put('testarry', [c.builtin('clng', [f.get('x')])], f.get('tmp_feac'))
    # Next X
    return 110 if f.next_loop(109) else 113

def _issimilar_113(f, c):
    # Call Bigram(RefStr, RefQG)
    c.call('bigram', [f.get('refstr'), f.ref('refqg')])
    # Call Bigram(TestStr, TestQG)
    c.call('bigram', [f.get('teststr'), f.ref('testqg')])
    # tmp_FDA8 = CStr(Alg2Use)
    f.set('tmp_fda8', c.builtin('cstr', [f.get('alg2use')]))
    # If (tmp_FDA8 = "Lev") Then GoTo L0585 Else GoTo L058D
    return 117 if truth(c.binary('=', f.get('tmp_fda8'), 'Lev')) else 119

def _issimilar_117(f, c):
    # GoTo L0615
    return 132

def _issimilar_118(f, c):
    # GoTo L05B4
    return 124

def _issimilar_119(f, c):
    # If (tmp_FDA8 = "SSLCS") Then GoTo L059A Else GoTo L05A2
    return 120 if truth(c.binary('=', f.get('tmp_fda8'), 'SSLCS')) else 122

def _issimilar_120(f, c):
    # GoTo L0667
    return 137

def _issimilar_121(f, c):
    # GoTo L05B4
    return 124

def _issimilar_122(f, c):
    # If (tmp_FDA8 = "DblMetaPh") Then GoTo L05AF Else GoTo L05B4
    return 123 if truth(c.binary('=', f.get('tmp_fda8'), 'DblMetaPh')) else 124

def _issimilar_123(f, c):
    # GoTo L06C3
    return 142

def _issimilar_124(f, c):
    # tmp_FDA6 = 0
    f.set('tmp_fda6', Integer(0))
    # DiceValu = CSng(Dice(RefQG, TestQG, CBool(tmp_FDA6)))
    f.set('dicevalu', c.builtin('csng', [c.call('dice', [f.get('refqg'), f.get('testqg'), c.builtin('cbool', [f.get('tmp_fda6')])])]))
    # If (Alg2Use = "Dice") Then GoTo L05E4 Else GoTo L05F1
    return 127 if truth(c.binary('=', f.get('alg2use'), 'Dice')) else 129

def _issimilar_127(f, c):
    # IsSimilar = CSng(DiceValu)
    f.set('issimilar', c.builtin('csng', [f.get('dicevalu')]))
    # GoTo L0B63
    return 233

def _issimilar_129(f, c):
    # If (DiceValu < CSng(0.2)) Then GoTo L0606 Else GoTo L0613
    return 130 if truth(c.binary('<', f.get('dicevalu'), c.builtin('csng', [0.2]))) else 132

def _issimilar_130(f, c):
    # IsSimilar = CSng(CDbl(0))
    f.set('issimilar', c.builtin('csng', [c.builtin('cdbl', [Integer(0)])]))
    # GoTo L0B63
    return 233

def _issimilar_132(f, c):
    # LevDistValu = CSng(CDbl(LevDist(RefArry, TestArry)))
    f.set('levdistvalu', c.builtin('csng', [c.builtin('cdbl', [c.call('levdist', [f.get('refarry'), f.get('testarry')])])]))
    # If (Alg2Use = "Lev") Then GoTo L063F Else GoTo L064C
    return 134 if truth(c.binary('=', f.get('alg2use'), 'Lev')) else 136

def _issimilar_134(f, c):
    # IsSimilar = CSng(LevDistValu)
    f.set('issimilar', c.builtin('csng', [f.get('levdistvalu')]))
    # GoTo L0B63
    return 233

def _issimilar_136(f, c):
    # LevDistValu = CSng((CDbl(1) - ((LevDistValu / CDbl((RefLen + TestLen))) / CDbl(2))))
    f.set('levdistvalu', c.builtin('csng', [c.binary('-', c.builtin('cdbl', [Integer(1)]), c.binary('/', c.binary('/', f.get('levdistvalu'), c.builtin('cdbl', [c.binary('+', f.get('reflen'), f.get('testlen'))])), c.builtin('cdbl', [Integer(2)])))]))
    return 137

def _issimilar_137(f, c):
    # LCSValu = CSng(LCS(RefArry, TestArry, Alg2Use))
    f.set('lcsvalu', c.builtin('csng', [c.call('lcs', [f.get('refarry'), f.get('testarry'), f.ref('alg2use')])]))
    # If (Alg2Use = "SSLCS") Then GoTo L0698 Else GoTo L06A5
    return 139 if truth(c.binary('=', f.get('alg2use'), 'SSLCS')) else 141

def _issimilar_139(f, c):
    # IsSimilar = CSng(LCSValu)
    f.set('issimilar', c.builtin('csng', [f.get('lcsvalu')]))
    # GoTo L0B63
    return 233

def _issimilar_141(f, c):
    # If (CSng(((LevDistValu + LCSValu) / CDbl(2))) < CSng(0.84)) Then GoTo L06C3 Else GoTo L0B3B
    return 142 if truth(c.binary('<', c.builtin('csng', [c.binary('/', c.binary('+', f.get('levdistvalu'), f.get('lcsvalu')), c.builtin('cdbl', [Integer(2)]))]), c.builtin('csng', [0.84]))) else 231

def _issimilar_142(f, c):
    # If (DoubleMetaphone(RefArry, MetaPh1a, MetaPh1b) And DoubleMetaphone(TestArry, MetaPh2a, MetaPh2b)) Then GoTo L06F1 Else GoTo L0B36
    return 143 if truth(c.binary('and', c.call('doublemetaphone', [f.get('refarry'), f.ref('metaph1a'), f.ref('metaph1b')]), c.call('doublemetaphone', [f.get('testarry'), f.ref('metaph2a'), f.ref('metaph2b')]))) else 230

def _issimilar_143(f, c):
    # If (MetaPh1a <> "") Then GoTo L0701 Else GoTo L07F0
    return 144 if truth(c.binary('<>', f.get('metaph1a'), '')) else 160

def _issimilar_144(f, c):
    # tmp_FEBC = Len(MetaPh1a)
    f.set('tmp_febc', c.builtin('len', [f.get('metaph1a')]))
    # MPhLen = CInt(CInt(tmp_FEBC))
    f.set('mphlen', c.builtin('cint', [c.builtin('cint', [f.get('tmp_febc')])]))
    # ReDim aMetaPh1(0 To CLng(MPhLen))
    f.redim('ametaph1', [(Integer(0), c.builtin('clng', [f.get('mphlen')]))], False, 'variant')
    # For X = 0 To (MPhLen - 1)
    return 148 if f.begin_loop(147, 'x', Integer(0), c.binary('-', f.get('mphlen'), Integer(1)), Integer(1)) else 151

def _issimilar_148(f, c):
    # tmp_FEAC = Mid(MetaPh1a, CLng((X + 1)), 1)
    f.set('tmp_feac', c.builtin('mid', [f.get('metaph1a'), c.builtin('clng', [c.binary('+', f.get('x'), Integer(1))]), Integer(1)]))
    # aMetaPh1(CLng(X)) = tmp_FEAC
    f.put('ametaph1', [c.builtin('clng', [f.get('x')])], f.get('tmp_feac'))
    # Next X
    return 148 if f.next_loop(147) else 151

def _issimilar_151(f, c):
    # If (MetaPh1b <> "") Then GoTo L077E Else GoTo L07EB
    return 152 if truth(c.binary('<>', f.get('metaph1b'), '')) else 159

def _issimilar_152(f, c):
    # tmp_FEBC = Len(MetaPh1b)
    f.set('tmp_febc', c.builtin('len', [f.get('metaph1b')]))
    # MPhLen = CInt(CInt(tmp_FEBC))
    f.set('mphlen', c.builtin('cint', [c.builtin('cint', [f.get('tmp_febc')])]))
    # ReDim bMetaPh1(0 To CLng(MPhLen))
    f.redim('bmetaph1', [(Integer(0), c.builtin('clng', [f.get('mphlen')]))], False, 'variant')
    # For X = 0 To (MPhLen - 1)
    return 156 if f.begin_loop(155, 'x', Integer(0), c.binary('-', f.get('mphlen'), Integer(1)), Integer(1)) else 159

def _issimilar_156(f, c):
    # tmp_FEAC = Mid(MetaPh1b, CLng((X + 1)), 1)
    f.set('tmp_feac', c.builtin('mid', [f.get('metaph1b'), c.builtin('clng', [c.binary('+', f.get('x'), Integer(1))]), Integer(1)]))
    # bMetaPh1(CLng(X)) = tmp_FEAC
    f.put('bmetaph1', [c.builtin('clng', [f.get('x')])], f.get('tmp_feac'))
    # Next X
    return 156 if f.next_loop(155) else 159

def _issimilar_159(f, c):
    # GoTo L07F7
    return 161

def _issimilar_160(f, c):
    # GoTo L0B36
    return 230

def _issimilar_161(f, c):
    # If (MetaPh2a <> "") Then GoTo L0809 Else GoTo L08F8
    return 162 if truth(c.binary('<>', f.get('metaph2a'), '')) else 178

def _issimilar_162(f, c):
    # tmp_FEBC = Len(MetaPh2a)
    f.set('tmp_febc', c.builtin('len', [f.get('metaph2a')]))
    # MPhLen = CInt(CInt(tmp_FEBC))
    f.set('mphlen', c.builtin('cint', [c.builtin('cint', [f.get('tmp_febc')])]))
    # ReDim aMetaPh2(0 To CLng(MPhLen))
    f.redim('ametaph2', [(Integer(0), c.builtin('clng', [f.get('mphlen')]))], False, 'variant')
    # For X = 0 To (MPhLen - 1)
    return 166 if f.begin_loop(165, 'x', Integer(0), c.binary('-', f.get('mphlen'), Integer(1)), Integer(1)) else 169

def _issimilar_166(f, c):
    # tmp_FEAC = Mid(MetaPh2a, CLng((X + 1)), 1)
    f.set('tmp_feac', c.builtin('mid', [f.get('metaph2a'), c.builtin('clng', [c.binary('+', f.get('x'), Integer(1))]), Integer(1)]))
    # aMetaPh2(CLng(X)) = tmp_FEAC
    f.put('ametaph2', [c.builtin('clng', [f.get('x')])], f.get('tmp_feac'))
    # Next X
    return 166 if f.next_loop(165) else 169

def _issimilar_169(f, c):
    # If (MetaPh2b <> "") Then GoTo L0886 Else GoTo L08F3
    return 170 if truth(c.binary('<>', f.get('metaph2b'), '')) else 177

def _issimilar_170(f, c):
    # tmp_FEBC = Len(MetaPh2b)
    f.set('tmp_febc', c.builtin('len', [f.get('metaph2b')]))
    # MPhLen = CInt(CInt(tmp_FEBC))
    f.set('mphlen', c.builtin('cint', [c.builtin('cint', [f.get('tmp_febc')])]))
    # ReDim bMetaPh2(0 To CLng(MPhLen))
    f.redim('bmetaph2', [(Integer(0), c.builtin('clng', [f.get('mphlen')]))], False, 'variant')
    # For X = 0 To (MPhLen - 1)
    return 174 if f.begin_loop(173, 'x', Integer(0), c.binary('-', f.get('mphlen'), Integer(1)), Integer(1)) else 177

def _issimilar_174(f, c):
    # tmp_FEAC = Mid(MetaPh2b, CLng((X + 1)), 1)
    f.set('tmp_feac', c.builtin('mid', [f.get('metaph2b'), c.builtin('clng', [c.binary('+', f.get('x'), Integer(1))]), Integer(1)]))
    # bMetaPh2(CLng(X)) = tmp_FEAC
    f.put('bmetaph2', [c.builtin('clng', [f.get('x')])], f.get('tmp_feac'))
    # Next X
    return 174 if f.next_loop(173) else 177

def _issimilar_177(f, c):
    # GoTo L08FF
    return 179

def _issimilar_178(f, c):
    # GoTo L0B36
    return 230

def _issimilar_179(f, c):
    # If (Alg2Use = "DblMetaPh") Then GoTo L090E Else GoTo L0A98
    return 180 if truth(c.binary('=', f.get('alg2use'), 'DblMetaPh')) else 221

def _issimilar_180(f, c):
    # tmp_FEBC = "Dmph"
    f.set('tmp_febc', 'Dmph')
    # DblMetaPh = CSng(LCS(aMetaPh1, aMetaPh2, tmp_FEBC))
    f.set('dblmetaph', c.builtin('csng', [c.call('lcs', [f.get('ametaph1'), f.get('ametaph2'), f.ref('tmp_febc')])]))
    # Set tmp_FD90 = Application.Forms
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD8C = tmp_FD90.Item("Double Metaphone Input Compare")
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD88 = tmp_FD8C.Controls
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD84 = tmp_FD88.Item("MetaPh1")
    pass  # Access form-object plumbing has no numeric effect.
    # tmp_FD84 = MetaPh1a
    f.set('tmp_fd84', f.get('metaph1a'))
    # Set tmp_FD90 = Nothing
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD8C = Nothing
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD88 = Nothing
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD84 = Nothing
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD90 = Application.Forms
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD8C = tmp_FD90.Item("Double Metaphone Input Compare")
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD88 = tmp_FD8C.Controls
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD84 = tmp_FD88.Item("MetaPh2")
    pass  # Access form-object plumbing has no numeric effect.
    # tmp_FD84 = MetaPh2a
    f.set('tmp_fd84', f.get('metaph2a'))
    # Set tmp_FD90 = Nothing
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD8C = Nothing
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD88 = Nothing
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD84 = Nothing
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD90 = Application.Forms
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD8C = tmp_FD90.Item("Double Metaphone Input Compare")
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD88 = tmp_FD8C.Controls
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD84 = tmp_FD88.Item("Alt1")
    pass  # Access form-object plumbing has no numeric effect.
    # tmp_FD84 = MetaPh1b
    f.set('tmp_fd84', f.get('metaph1b'))
    # Set tmp_FD90 = Nothing
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD8C = Nothing
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD88 = Nothing
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD84 = Nothing
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD90 = Application.Forms
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD8C = tmp_FD90.Item("Double Metaphone Input Compare")
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD88 = tmp_FD8C.Controls
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD84 = tmp_FD88.Item("Alt2")
    pass  # Access form-object plumbing has no numeric effect.
    # tmp_FD84 = MetaPh2b
    f.set('tmp_fd84', f.get('metaph2b'))
    # Set tmp_FD90 = Nothing
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD8C = Nothing
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD88 = Nothing
    pass  # Access form-object plumbing has no numeric effect.
    # Set tmp_FD84 = Nothing
    pass  # Access form-object plumbing has no numeric effect.
    # IsSimilar = CSng(DblMetaPh)
    f.set('issimilar', c.builtin('csng', [f.get('dblmetaph')]))
    # GoTo L0B63
    return 233

def _issimilar_220(f, c):
    # GoTo L0B34
    return 230

def _issimilar_221(f, c):
    # DblMetaPh = CSng(LCS(aMetaPh1, aMetaPh2))
    f.set('dblmetaph', c.builtin('csng', [c.call('lcs', [f.get('ametaph1'), f.get('ametaph2')])]))
    # tmp_FEBC = (MetaPh1b <> "")
    f.set('tmp_febc', c.binary('<>', f.get('metaph1b'), ''))
    # tmp_FEAC = (MetaPh2b <> "")
    f.set('tmp_feac', c.binary('<>', f.get('metaph2b'), ''))
    # tmp_FE9C = (tmp_FEBC And tmp_FEAC)
    f.set('tmp_fe9c', c.binary('and', f.get('tmp_febc'), f.get('tmp_feac')))
    # If tmp_FE9C Then GoTo L0AE1 Else GoTo L0B32
    return 226 if truth(f.get('tmp_fe9c')) else 230

def _issimilar_226(f, c):
    # tmp_FE68 = CSng(LCS(bMetaPh1, bMetaPh2))
    f.set('tmp_fe68', c.builtin('csng', [c.call('lcs', [f.get('bmetaph1'), f.get('bmetaph2')])]))
    # tmp_FEAC = CSng(tmp_FE68)
    f.set('tmp_feac', c.builtin('csng', [f.get('tmp_fe68')]))
    # tmp_FE6C = Maximum(DblMetaPh, tmp_FEAC)
    f.set('tmp_fe6c', c.call('maximum', [f.ref('dblmetaph'), f.ref('tmp_feac')]))
    # DblMetaPh = CSng(CDbl(tmp_FE6C))
    f.set('dblmetaph', c.builtin('csng', [c.builtin('cdbl', [f.get('tmp_fe6c')])]))
    return 230

def _issimilar_230(f, c):
    # GoTo L0B4D
    return 232

def _issimilar_231(f, c):
    # DblMetaPh = CSng(((LevDistValu + LCSValu) / CDbl(2)))
    f.set('dblmetaph', c.builtin('csng', [c.binary('/', c.binary('+', f.get('levdistvalu'), f.get('lcsvalu')), c.builtin('cdbl', [Integer(2)]))]))
    return 232

def _issimilar_232(f, c):
    # IsSimilar = CSng((((LevDistValu + LCSValu) + DblMetaPh) / CDbl(3)))
    f.set('issimilar', c.builtin('csng', [c.binary('/', c.binary('+', c.binary('+', f.get('levdistvalu'), f.get('lcsvalu')), f.get('dblmetaph')), c.builtin('cdbl', [Integer(3)]))]))
    return 233

def _issimilar_233(f, c):
    # Erase RefArry
    f.ref('refarry').value = EMPTY
    # Erase TestArry
    f.ref('testarry').value = EMPTY
    # Erase aMetaPh1
    f.ref('ametaph1').value = EMPTY
    # Erase aMetaPh2
    f.ref('ametaph2').value = EMPTY
    # Erase bMetaPh1
    f.ref('bmetaph1').value = EMPTY
    # Erase bMetaPh2
    f.ref('bmetaph2').value = EMPTY
    # Erase RefQG
    f.ref('refqg').value = EMPTY
    # Erase TestQG
    f.ref('testqg').value = EMPTY
    # Exit Function
    return None

def _issimilar_end(f, c):
    return None

_blocks_issimilar = {0: _issimilar_0, 3: _issimilar_3, 4: _issimilar_4, 5: _issimilar_5, 6: _issimilar_6, 7: _issimilar_7, 11: _issimilar_11, 12: _issimilar_12, 13: _issimilar_13, 15: _issimilar_15, 21: _issimilar_21, 23: _issimilar_23, 29: _issimilar_29, 31: _issimilar_31, 44: _issimilar_44, 46: _issimilar_46, 59: _issimilar_59, 61: _issimilar_61, 73: _issimilar_73, 75: _issimilar_75, 87: _issimilar_87, 96: _issimilar_96, 97: _issimilar_97, 101: _issimilar_101, 103: _issimilar_103, 106: _issimilar_106, 109: _issimilar_109, 110: _issimilar_110, 113: _issimilar_113, 117: _issimilar_117, 118: _issimilar_118, 119: _issimilar_119, 120: _issimilar_120, 121: _issimilar_121, 122: _issimilar_122, 123: _issimilar_123, 124: _issimilar_124, 127: _issimilar_127, 129: _issimilar_129, 130: _issimilar_130, 132: _issimilar_132, 134: _issimilar_134, 136: _issimilar_136, 137: _issimilar_137, 139: _issimilar_139, 141: _issimilar_141, 142: _issimilar_142, 143: _issimilar_143, 144: _issimilar_144, 148: _issimilar_148, 151: _issimilar_151, 152: _issimilar_152, 156: _issimilar_156, 159: _issimilar_159, 160: _issimilar_160, 161: _issimilar_161, 162: _issimilar_162, 166: _issimilar_166, 169: _issimilar_169, 170: _issimilar_170, 174: _issimilar_174, 177: _issimilar_177, 178: _issimilar_178, 179: _issimilar_179, 180: _issimilar_180, 220: _issimilar_220, 221: _issimilar_221, 226: _issimilar_226, 230: _issimilar_230, 231: _issimilar_231, 232: _issimilar_232, 233: _issimilar_233, 242: _issimilar_end}
def vb_issimilar(c, arguments):
    return run(c, 'issimilar', [('inputrefstr', 'variant', True, False, MISSING), ('inputteststr', 'variant', True, False, MISSING), ('alg2use', 'string', False, True, '')], {'tmp_fd84': 'object', 'tmp_fd88': 'object', 'tmp_fd8c': 'object', 'tmp_fd90': 'object', 'tmp_fda6': 'boolean', 'tmp_fda8': 'string', 'tmp_fdb4': 'variant', 'tmp_fdc4': 'variant', 'tmp_fdd4': 'variant', 'tmp_fdf4': 'variant', 'tmp_fe14': 'variant', 'tmp_fe64': 'long', 'tmp_fe68': 'single', 'tmp_fe6c': 'variant', 'tmp_fe7c': 'variant', 'tmp_fe9c': 'variant', 'tmp_feac': 'variant', 'tmp_febc': 'variant', 'tmp_fecc': 'variant', 'bmetaph2': 'variant', 'bmetaph1': 'variant', 'ametaph2': 'variant', 'ametaph1': 'variant', 'testarry': 'variant', 'refarry': 'variant', 'x': 'integer', 'testqg': 'variant', 'refqg': 'variant', 'mphlen': 'integer', 'testlen': 'integer', 'reflen': 'integer', 'metaph2b': 'variant', 'metaph1b': 'variant', 'metaph2a': 'variant', 'metaph1a': 'variant', 'lcsvalu': 'single', 'dicevalu': 'single', 'dblmetaph': 'single', 'levdistvalu': 'single', 'teststr': 'variant', 'refstr': 'variant'}, 'single', _blocks_issimilar, arguments)

def _dice_0(f, c):
    # Qgram1 = input_Qgram1
    f.set('qgram1', f.get('input_qgram1'))
    # Qgram2 = input_Qgram2
    f.set('qgram2', f.get('input_qgram2'))
    # If IsMissing(DMPH) Then GoTo L0020 Else GoTo L0027
    return 3 if truth(c.builtin('ismissing', [f.get('dmph')])) else 4

def _dice_3(f, c):
    # DMPH = CInt(0)
    f.set('dmph', c.builtin('cint', [Integer(0)]))
    return 4

def _dice_4(f, c):
    # If (IsNull(Qgram1) Or IsNull(Qgram2)) Then GoTo L003D Else GoTo L0040
    return 5 if truth(c.binary('or', c.builtin('isnull', [f.get('qgram1')]), c.builtin('isnull', [f.get('qgram2')]))) else 6

def _dice_5(f, c):
    # Exit Function
    return None

def _dice_6(f, c):
    # QgramCount1 = CInt(CInt(UBound(Qgram1, 1)))
    f.set('qgramcount1', c.builtin('cint', [c.builtin('cint', [c.builtin('ubound', [f.get('qgram1'), Integer(1)])])]))
    # QgramCount2 = CInt(CInt(UBound(Qgram2, 1)))
    f.set('qgramcount2', c.builtin('cint', [c.builtin('cint', [c.builtin('ubound', [f.get('qgram2'), Integer(1)])])]))
    # If ((QgramCount1 = 0) Or (QgramCount2 = 0)) Then GoTo L0074 Else GoTo L0077
    return 9 if truth(c.binary('or', c.binary('=', f.get('qgramcount1'), Integer(0)), c.binary('=', f.get('qgramcount2'), Integer(0)))) else 10

def _dice_9(f, c):
    # Exit Function
    return None

def _dice_10(f, c):
    # For q1 = 0 To QgramCount1
    return 11 if f.begin_loop(10, 'q1', Integer(0), f.get('qgramcount1'), Integer(1)) else 21

def _dice_11(f, c):
    # tmp_FF08 = Qgram1(q1)
    f.set('tmp_ff08', f.index('qgram1', f.get('q1')))
    # BG1 = tmp_FF08
    f.set('bg1', f.get('tmp_ff08'))
    # For q2 = 0 To QgramCount2
    return 14 if f.begin_loop(13, 'q2', Integer(0), f.get('qgramcount2'), Integer(1)) else 20

def _dice_14(f, c):
    # tmp_FF08 = Qgram2(q2)
    f.set('tmp_ff08', f.index('qgram2', f.get('q2')))
    # BG2 = tmp_FF08
    f.set('bg2', f.get('tmp_ff08'))
    # If ((Not IsEmpty(BG1)) And (Not IsEmpty(BG2))) Then GoTo L00DB Else GoTo L00F5
    return 17 if truth(c.binary('and', c.unary('not', c.builtin('isempty', [f.get('bg1')])), c.unary('not', c.builtin('isempty', [f.get('bg2')])))) else 19

def _dice_17(f, c):
    # If (BG1 = BG2) Then GoTo L00E8 Else GoTo L00F3
    return 18 if truth(c.binary('=', f.get('bg1'), f.get('bg2'))) else 19

def _dice_18(f, c):
    # SharedQgrams = CInt((SharedQgrams + 1))
    f.set('sharedqgrams', c.builtin('cint', [c.binary('+', f.get('sharedqgrams'), Integer(1))]))
    return 19

def _dice_19(f, c):
    # Next q2
    return 14 if f.next_loop(13) else 20

def _dice_20(f, c):
    # Next q1
    return 11 if f.next_loop(10) else 21

def _dice_21(f, c):
    # tmp_FEE4 = "0.00"
    f.set('tmp_fee4', '0.00')
    # tmp_FF08 = CDbl((CDbl((2 * SharedQgrams)) / CDbl((QgramCount1 + QgramCount2))))
    f.set('tmp_ff08', c.builtin('cdbl', [c.binary('/', c.builtin('cdbl', [c.binary('*', Integer(2), f.get('sharedqgrams'))]), c.builtin('cdbl', [c.binary('+', f.get('qgramcount1'), f.get('qgramcount2'))]))]))
    # tmp_FED4 = Format(tmp_FF08, tmp_FEE4, 1, 1)
    f.set('tmp_fed4', c.builtin('format', [f.get('tmp_ff08'), f.get('tmp_fee4'), Integer(1), Integer(1)]))
    # Dice = CSng(CSng(tmp_FED4))
    f.set('dice', c.builtin('csng', [c.builtin('csng', [f.get('tmp_fed4')])]))
    # If DMPH Then GoTo L0159 Else GoTo L0190
    return 26 if truth(f.get('dmph')) else 28

def _dice_26(f, c):
    # tmp_FEA4 = Minimum(Dice, 0.75)
    f.set('tmp_fea4', c.call('minimum', [f.ref('dice'), 0.75]))
    # Dice = CSng(CDbl(tmp_FEA4))
    f.set('dice', c.builtin('csng', [c.builtin('cdbl', [f.get('tmp_fea4')])]))
    return 28

def _dice_28(f, c):
    # Exit Function
    return None

def _dice_end(f, c):
    return None

_blocks_dice = {0: _dice_0, 3: _dice_3, 4: _dice_4, 5: _dice_5, 6: _dice_6, 9: _dice_9, 10: _dice_10, 11: _dice_11, 14: _dice_14, 17: _dice_17, 18: _dice_18, 19: _dice_19, 20: _dice_20, 21: _dice_21, 26: _dice_26, 28: _dice_28, 29: _dice_end}
def vb_dice(c, arguments):
    return run(c, 'dice', [('input_qgram1', 'variant', True, False, MISSING), ('input_qgram2', 'variant', True, False, MISSING), ('dmph', 'boolean', False, True, MISSING)], {'tmp_fea4': 'variant', 'tmp_fed4': 'variant', 'tmp_fee4': 'variant', 'tmp_ff08': 'variant', 'q2': 'integer', 'q1': 'integer', 'sharedqgrams': 'integer', 'bg2': 'variant', 'bg1': 'variant', 'qgramcount2': 'integer', 'qgramcount1': 'integer', 'qgram2': 'variant', 'qgram1': 'variant'}, 'single', _blocks_dice, arguments)

def _namesimilarity_0(f, c):
    # tmp_FE30 = (RefStr Like "*.*")
    f.set('tmp_fe30', c.binary('like', f.get('refstr'), '*.*'))
    # If tmp_FE30 Then GoTo L0018 Else GoTo L0058
    return 2 if truth(f.get('tmp_fe30')) else 8

def _namesimilarity_2(f, c):
    # tmp_FE18 = 0
    f.set('tmp_fe18', Integer(0))
    # tmp_FE1C = 1
    f.set('tmp_fe1c', Integer(1))
    # tmp_FE20 = ""
    f.set('tmp_fe20', '')
    # tmp_FE30 = "."
    f.set('tmp_fe30', '.')
    # tmp_FE08 = StrReplace(RefStr, tmp_FE30, tmp_FE20, tmp_FE1C, tmp_FE18)
    f.set('tmp_fe08', c.call('strreplace', [f.ref('refstr'), f.ref('tmp_fe30'), f.ref('tmp_fe20'), f.ref('tmp_fe1c'), f.ref('tmp_fe18')]))
    # RefStr = tmp_FE08
    f.set('refstr', f.get('tmp_fe08'))
    return 8

def _namesimilarity_8(f, c):
    # tmp_FE30 = (TestStr Like "*.*")
    f.set('tmp_fe30', c.binary('like', f.get('teststr'), '*.*'))
    # If tmp_FE30 Then GoTo L0070 Else GoTo L00B0
    return 10 if truth(f.get('tmp_fe30')) else 16

def _namesimilarity_10(f, c):
    # tmp_FE18 = 0
    f.set('tmp_fe18', Integer(0))
    # tmp_FE1C = 1
    f.set('tmp_fe1c', Integer(1))
    # tmp_FE20 = ""
    f.set('tmp_fe20', '')
    # tmp_FE30 = "."
    f.set('tmp_fe30', '.')
    # tmp_FE08 = StrReplace(TestStr, tmp_FE30, tmp_FE20, tmp_FE1C, tmp_FE18)
    f.set('tmp_fe08', c.call('strreplace', [f.ref('teststr'), f.ref('tmp_fe30'), f.ref('tmp_fe20'), f.ref('tmp_fe1c'), f.ref('tmp_fe18')]))
    # TestStr = tmp_FE08
    f.set('teststr', f.get('tmp_fe08'))
    return 16

def _namesimilarity_16(f, c):
    # tmp_FE30 = (RefStr Like "*-*")
    f.set('tmp_fe30', c.binary('like', f.get('refstr'), '*-*'))
    # If tmp_FE30 Then GoTo L00C8 Else GoTo L0175
    return 18 if truth(f.get('tmp_fe30')) else 30

def _namesimilarity_18(f, c):
    # tmp_FE08 = InStr(1, RefStr, "-", 2)
    f.set('tmp_fe08', c.builtin('instr', [Integer(1), f.get('refstr'), '-', Integer(2)]))
    # tmp_FDC8 = (tmp_FE08 + 1)
    f.set('tmp_fdc8', c.binary('+', f.get('tmp_fe08'), Integer(1)))
    # tmp_FD98 = Mid(RefStr, CLng(tmp_FDC8))
    f.set('tmp_fd98', c.builtin('mid', [f.get('refstr'), c.builtin('clng', [f.get('tmp_fdc8')])]))
    # tmp_FE30 = InStr(1, RefStr, "-", 2)
    f.set('tmp_fe30', c.builtin('instr', [Integer(1), f.get('refstr'), '-', Integer(2)]))
    # tmp_FE20 = Left(RefStr, CLng(tmp_FE30))
    f.set('tmp_fe20', c.builtin('left', [f.get('refstr'), c.builtin('clng', [f.get('tmp_fe30')])]))
    # tmp_FE18 = 0
    f.set('tmp_fe18', Integer(0))
    # tmp_FE1C = 1
    f.set('tmp_fe1c', Integer(1))
    # tmp_FD58 = ""
    f.set('tmp_fd58', '')
    # tmp_FD78 = "-"
    f.set('tmp_fd78', '-')
    # tmp_FD48 = StrReplace(tmp_FD98, tmp_FD78, tmp_FD58, tmp_FE1C, tmp_FE18)
    f.set('tmp_fd48', c.call('strreplace', [f.ref('tmp_fd98'), f.ref('tmp_fd78'), f.ref('tmp_fd58'), f.ref('tmp_fe1c'), f.ref('tmp_fe18')]))
    # tmp_FD38 = (tmp_FE20 & tmp_FD48)
    f.set('tmp_fd38', c.binary('&', f.get('tmp_fe20'), f.get('tmp_fd48')))
    # RefStr = tmp_FD38
    f.set('refstr', f.get('tmp_fd38'))
    return 30

def _namesimilarity_30(f, c):
    # tmp_FE30 = (TestStr Like "*-*")
    f.set('tmp_fe30', c.binary('like', f.get('teststr'), '*-*'))
    # If tmp_FE30 Then GoTo L018D Else GoTo L023A
    return 32 if truth(f.get('tmp_fe30')) else 44

def _namesimilarity_32(f, c):
    # tmp_FE08 = InStr(1, TestStr, "-", 2)
    f.set('tmp_fe08', c.builtin('instr', [Integer(1), f.get('teststr'), '-', Integer(2)]))
    # tmp_FDC8 = (tmp_FE08 + 1)
    f.set('tmp_fdc8', c.binary('+', f.get('tmp_fe08'), Integer(1)))
    # tmp_FD98 = Mid(TestStr, CLng(tmp_FDC8))
    f.set('tmp_fd98', c.builtin('mid', [f.get('teststr'), c.builtin('clng', [f.get('tmp_fdc8')])]))
    # tmp_FE30 = InStr(1, TestStr, "-", 2)
    f.set('tmp_fe30', c.builtin('instr', [Integer(1), f.get('teststr'), '-', Integer(2)]))
    # tmp_FE20 = Left(TestStr, CLng(tmp_FE30))
    f.set('tmp_fe20', c.builtin('left', [f.get('teststr'), c.builtin('clng', [f.get('tmp_fe30')])]))
    # tmp_FE18 = 0
    f.set('tmp_fe18', Integer(0))
    # tmp_FE1C = 1
    f.set('tmp_fe1c', Integer(1))
    # tmp_FD58 = ""
    f.set('tmp_fd58', '')
    # tmp_FD78 = "-"
    f.set('tmp_fd78', '-')
    # tmp_FD48 = StrReplace(tmp_FD98, tmp_FD78, tmp_FD58, tmp_FE1C, tmp_FE18)
    f.set('tmp_fd48', c.call('strreplace', [f.ref('tmp_fd98'), f.ref('tmp_fd78'), f.ref('tmp_fd58'), f.ref('tmp_fe1c'), f.ref('tmp_fe18')]))
    # tmp_FD38 = (tmp_FE20 & tmp_FD48)
    f.set('tmp_fd38', c.binary('&', f.get('tmp_fe20'), f.get('tmp_fd48')))
    # TestStr = tmp_FD38
    f.set('teststr', f.get('tmp_fd38'))
    return 44

def _namesimilarity_44(f, c):
    # tmp_FE30 = InStr(1, RefStr, "~", 2)
    f.set('tmp_fe30', c.builtin('instr', [Integer(1), f.get('refstr'), '~', Integer(2)]))
    # tmp_FE20 = (tmp_FE30 - 1)
    f.set('tmp_fe20', c.binary('-', f.get('tmp_fe30'), Integer(1)))
    # tmp_FE08 = Left(RefStr, CLng(tmp_FE20))
    f.set('tmp_fe08', c.builtin('left', [f.get('refstr'), c.builtin('clng', [f.get('tmp_fe20')])]))
    # tmp_FDC8 = Trim(tmp_FE08)
    f.set('tmp_fdc8', c.builtin('trim', [f.get('tmp_fe08')]))
    # RefL = tmp_FDC8
    f.set('refl', f.get('tmp_fdc8'))
    # tmp_FE08 = "~"
    f.set('tmp_fe08', '~')
    # tmp_FD88 = CInt((GetLastChrPos(RefStr, tmp_FE08) - 1))
    f.set('tmp_fd88', c.builtin('cint', [c.binary('-', c.call('getlastchrpos', [f.ref('refstr'), f.ref('tmp_fe08')]), Integer(1))]))
    # tmp_FDC8 = InStr(1, RefStr, "~", 2)
    f.set('tmp_fdc8', c.builtin('instr', [Integer(1), f.get('refstr'), '~', Integer(2)]))
    # tmp_FDA8 = (tmp_FD88 - tmp_FDC8)
    f.set('tmp_fda8', c.binary('-', f.get('tmp_fd88'), f.get('tmp_fdc8')))
    # tmp_FD98 = tmp_FDA8
    f.set('tmp_fd98', f.get('tmp_fda8'))
    # tmp_FE30 = InStr(1, RefStr, "~", 2)
    f.set('tmp_fe30', c.builtin('instr', [Integer(1), f.get('refstr'), '~', Integer(2)]))
    # tmp_FE20 = (tmp_FE30 + 1)
    f.set('tmp_fe20', c.binary('+', f.get('tmp_fe30'), Integer(1)))
    # tmp_FD78 = Mid(RefStr, CLng(tmp_FE20), tmp_FD98)
    f.set('tmp_fd78', c.builtin('mid', [f.get('refstr'), c.builtin('clng', [f.get('tmp_fe20')]), f.get('tmp_fd98')]))
    # tmp_FD58 = Trim(tmp_FD78)
    f.set('tmp_fd58', c.builtin('trim', [f.get('tmp_fd78')]))
    # RefF = tmp_FD58
    f.set('reff', f.get('tmp_fd58'))
    # tmp_FE30 = "~"
    f.set('tmp_fe30', '~')
    # tmp_FD36 = CInt(GetLastChrPos(RefStr, tmp_FE30))
    f.set('tmp_fd36', c.builtin('cint', [c.call('getlastchrpos', [f.ref('refstr'), f.ref('tmp_fe30')])]))
    # tmp_FE08 = Mid(RefStr, CLng((tmp_FD36 + 1)))
    f.set('tmp_fe08', c.builtin('mid', [f.get('refstr'), c.builtin('clng', [c.binary('+', f.get('tmp_fd36'), Integer(1))])]))
    # tmp_FDC8 = Trim(tmp_FE08)
    f.set('tmp_fdc8', c.builtin('trim', [f.get('tmp_fe08')]))
    # RefM = tmp_FDC8
    f.set('refm', f.get('tmp_fdc8'))
    # tmp_FE30 = InStr(1, TestStr, "~", 2)
    f.set('tmp_fe30', c.builtin('instr', [Integer(1), f.get('teststr'), '~', Integer(2)]))
    # tmp_FE20 = (tmp_FE30 - 1)
    f.set('tmp_fe20', c.binary('-', f.get('tmp_fe30'), Integer(1)))
    # tmp_FE08 = Left(TestStr, CLng(tmp_FE20))
    f.set('tmp_fe08', c.builtin('left', [f.get('teststr'), c.builtin('clng', [f.get('tmp_fe20')])]))
    # tmp_FDC8 = Trim(tmp_FE08)
    f.set('tmp_fdc8', c.builtin('trim', [f.get('tmp_fe08')]))
    # TestL = tmp_FDC8
    f.set('testl', f.get('tmp_fdc8'))
    # tmp_FE08 = "~"
    f.set('tmp_fe08', '~')
    # tmp_FD88 = CInt((GetLastChrPos(TestStr, tmp_FE08) - 1))
    f.set('tmp_fd88', c.builtin('cint', [c.binary('-', c.call('getlastchrpos', [f.ref('teststr'), f.ref('tmp_fe08')]), Integer(1))]))
    # tmp_FDC8 = InStr(1, TestStr, "~", 2)
    f.set('tmp_fdc8', c.builtin('instr', [Integer(1), f.get('teststr'), '~', Integer(2)]))
    # tmp_FDA8 = (tmp_FD88 - tmp_FDC8)
    f.set('tmp_fda8', c.binary('-', f.get('tmp_fd88'), f.get('tmp_fdc8')))
    # tmp_FD98 = tmp_FDA8
    f.set('tmp_fd98', f.get('tmp_fda8'))
    # tmp_FE30 = InStr(1, TestStr, "~", 2)
    f.set('tmp_fe30', c.builtin('instr', [Integer(1), f.get('teststr'), '~', Integer(2)]))
    # tmp_FE20 = (tmp_FE30 + 1)
    f.set('tmp_fe20', c.binary('+', f.get('tmp_fe30'), Integer(1)))
    # tmp_FD78 = Mid(TestStr, CLng(tmp_FE20), tmp_FD98)
    f.set('tmp_fd78', c.builtin('mid', [f.get('teststr'), c.builtin('clng', [f.get('tmp_fe20')]), f.get('tmp_fd98')]))
    # tmp_FD58 = Trim(tmp_FD78)
    f.set('tmp_fd58', c.builtin('trim', [f.get('tmp_fd78')]))
    # TestF = tmp_FD58
    f.set('testf', f.get('tmp_fd58'))
    # tmp_FE30 = "~"
    f.set('tmp_fe30', '~')
    # tmp_FD36 = CInt(GetLastChrPos(TestStr, tmp_FE30))
    f.set('tmp_fd36', c.builtin('cint', [c.call('getlastchrpos', [f.ref('teststr'), f.ref('tmp_fe30')])]))
    # tmp_FE08 = Mid(TestStr, CLng((tmp_FD36 + 1)))
    f.set('tmp_fe08', c.builtin('mid', [f.get('teststr'), c.builtin('clng', [c.binary('+', f.get('tmp_fd36'), Integer(1))])]))
    # tmp_FDC8 = Trim(tmp_FE08)
    f.set('tmp_fdc8', c.builtin('trim', [f.get('tmp_fe08')]))
    # TestM = tmp_FDC8
    f.set('testm', f.get('tmp_fdc8'))
    # tmp_FE30 = Len(RefL)
    f.set('tmp_fe30', c.builtin('len', [f.get('refl')]))
    # RefLLen = tmp_FE30
    f.set('refllen', f.get('tmp_fe30'))
    # tmp_FE30 = Len(RefF)
    f.set('tmp_fe30', c.builtin('len', [f.get('reff')]))
    # RefFLen = tmp_FE30
    f.set('refflen', f.get('tmp_fe30'))
    # tmp_FE30 = Len(RefM)
    f.set('tmp_fe30', c.builtin('len', [f.get('refm')]))
    # RefMLen = tmp_FE30
    f.set('refmlen', f.get('tmp_fe30'))
    # tmp_FE30 = Len(TestL)
    f.set('tmp_fe30', c.builtin('len', [f.get('testl')]))
    # TestLLen = tmp_FE30
    f.set('testllen', f.get('tmp_fe30'))
    # tmp_FE30 = Len(TestF)
    f.set('tmp_fe30', c.builtin('len', [f.get('testf')]))
    # TestFLen = tmp_FE30
    f.set('testflen', f.get('tmp_fe30'))
    # tmp_FE30 = Len(TestM)
    f.set('tmp_fe30', c.builtin('len', [f.get('testm')]))
    # TestMLen = tmp_FE30
    f.set('testmlen', f.get('tmp_fe30'))
    # tmp_FE30 = (RefL Like "*-*")
    f.set('tmp_fe30', c.binary('like', f.get('refl'), '*-*'))
    # tmp_FE20 = (TestL Like "*-*")
    f.set('tmp_fe20', c.binary('like', f.get('testl'), '*-*'))
    # tmp_FE08 = (tmp_FE30 And tmp_FE20)
    f.set('tmp_fe08', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # DashInBoth = CInt(CBool(tmp_FE08))
    f.set('dashinboth', c.builtin('cint', [c.builtin('cbool', [f.get('tmp_fe08')])]))
    # If (Not DashInBoth) Then GoTo L04F8 Else GoTo L051B
    return 101 if truth(c.unary('not', f.get('dashinboth'))) else 105

def _namesimilarity_101(f, c):
    # tmp_FE30 = (RefL Like "*-*")
    f.set('tmp_fe30', c.binary('like', f.get('refl'), '*-*'))
    # tmp_FE20 = (TestL Like "*-*")
    f.set('tmp_fe20', c.binary('like', f.get('testl'), '*-*'))
    # tmp_FE08 = (tmp_FE30 Or tmp_FE20)
    f.set('tmp_fe08', c.binary('or', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # DashInOne = CInt(CBool(tmp_FE08))
    f.set('dashinone', c.builtin('cint', [c.builtin('cbool', [f.get('tmp_fe08')])]))
    return 105

def _namesimilarity_105(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # tmp_FE08 = (TestL & TestF)
    f.set('tmp_fe08', c.binary('&', f.get('testl'), f.get('testf')))
    # tmp_FDC8 = (tmp_FE08 & TestM)
    f.set('tmp_fdc8', c.binary('&', f.get('tmp_fe08'), f.get('testm')))
    # tmp_FE30 = (RefL & RefF)
    f.set('tmp_fe30', c.binary('&', f.get('refl'), f.get('reff')))
    # tmp_FE20 = (tmp_FE30 & RefM)
    f.set('tmp_fe20', c.binary('&', f.get('tmp_fe30'), f.get('refm')))
    # FullNameSimValu = CSng(IsSimilar(tmp_FE20, tmp_FDC8, tmp_FD30))
    f.set('fullnamesimvalu', c.builtin('csng', [c.call('issimilar', [f.get('tmp_fe20'), f.get('tmp_fdc8'), f.ref('tmp_fd30')])]))
    # If ((Not DashInBoth) And (Not DashInOne)) Then GoTo L0572 Else GoTo L0695
    return 112 if truth(c.binary('and', c.unary('not', f.get('dashinboth')), c.unary('not', f.get('dashinone')))) else 137

def _namesimilarity_112(f, c):
    # tmp_FE30 = (RefL = TestM)
    f.set('tmp_fe30', c.binary('=', f.get('refl'), f.get('testm')))
    # tmp_FE20 = (RefM = TestL)
    f.set('tmp_fe20', c.binary('=', f.get('refm'), f.get('testl')))
    # tmp_FE08 = (tmp_FE30 Or tmp_FE20)
    f.set('tmp_fe08', c.binary('or', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # If tmp_FE08 Then GoTo L0591 Else GoTo L05B7
    return 116 if truth(f.get('tmp_fe08')) else 120

def _namesimilarity_116(f, c):
    # LSimValu = CSng(0.81)
    f.set('lsimvalu', c.builtin('csng', [0.81]))
    # MSimValu = CSng(0.81)
    f.set('msimvalu', c.builtin('csng', [0.81]))
    # LastInMiddle = CInt(-1)
    f.set('lastinmiddle', c.builtin('cint', [c.unary('-', Integer(1))]))
    # GoTo L064C
    return 131

def _namesimilarity_120(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # LSimValu = CSng(IsSimilar(RefL, TestM, tmp_FD30))
    f.set('lsimvalu', c.builtin('csng', [c.call('issimilar', [f.get('refl'), f.get('testm'), f.ref('tmp_fd30')])]))
    # If (LSimValu > CSng(0.9)) Then GoTo L05EC Else GoTo L05FB
    return 123 if truth(c.binary('>', f.get('lsimvalu'), c.builtin('csng', [0.9]))) else 125

def _namesimilarity_123(f, c):
    # MSimValu = CSng(LSimValu)
    f.set('msimvalu', c.builtin('csng', [f.get('lsimvalu')]))
    # LastInMiddle = CInt(-1)
    f.set('lastinmiddle', c.builtin('cint', [c.unary('-', Integer(1))]))
    return 125

def _namesimilarity_125(f, c):
    # If (Not LastInMiddle) Then GoTo L0606 Else GoTo L064A
    return 126 if truth(c.unary('not', f.get('lastinmiddle'))) else 131

def _namesimilarity_126(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # LSimValu = CSng(IsSimilar(RefM, TestL, tmp_FD30))
    f.set('lsimvalu', c.builtin('csng', [c.call('issimilar', [f.get('refm'), f.get('testl'), f.ref('tmp_fd30')])]))
    # If (LSimValu > CSng(0.9)) Then GoTo L0639 Else GoTo L0648
    return 129 if truth(c.binary('>', f.get('lsimvalu'), c.builtin('csng', [0.9]))) else 131

def _namesimilarity_129(f, c):
    # MSimValu = CSng(LSimValu)
    f.set('msimvalu', c.builtin('csng', [f.get('lsimvalu')]))
    # LastInMiddle = CInt(-1)
    f.set('lastinmiddle', c.builtin('cint', [c.unary('-', Integer(1))]))
    return 131

def _namesimilarity_131(f, c):
    # If (Not LastInMiddle) Then GoTo L0657 Else GoTo L0693
    return 132 if truth(c.unary('not', f.get('lastinmiddle'))) else 137

def _namesimilarity_132(f, c):
    # If (RefL = TestL) Then GoTo L0664 Else GoTo L066F
    return 133 if truth(c.binary('=', f.get('refl'), f.get('testl'))) else 135

def _namesimilarity_133(f, c):
    # LSimValu = CSng(CDbl(1))
    f.set('lsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(1)])]))
    # GoTo L0691
    return 137

def _namesimilarity_135(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # LSimValu = CSng(IsSimilar(RefL, TestL, tmp_FD30))
    f.set('lsimvalu', c.builtin('csng', [c.call('issimilar', [f.get('refl'), f.get('testl'), f.ref('tmp_fd30')])]))
    return 137

def _namesimilarity_137(f, c):
    # If DashInBoth Then GoTo L069F Else GoTo L0916
    return 138 if truth(f.get('dashinboth')) else 181

def _namesimilarity_138(f, c):
    # tmp_FE30 = InStr(1, RefL, "-", 2)
    f.set('tmp_fe30', c.builtin('instr', [Integer(1), f.get('refl'), '-', Integer(2)]))
    # tmp_FE20 = (tmp_FE30 + 1)
    f.set('tmp_fe20', c.binary('+', f.get('tmp_fe30'), Integer(1)))
    # tmp_FDC8 = Mid(RefL, CLng(tmp_FE20))
    f.set('tmp_fdc8', c.builtin('mid', [f.get('refl'), c.builtin('clng', [f.get('tmp_fe20')])]))
    # tmp_FDA8 = Trim(tmp_FDC8)
    f.set('tmp_fda8', c.builtin('trim', [f.get('tmp_fdc8')]))
    # DashNameR = tmp_FDA8
    f.set('dashnamer', f.get('tmp_fda8'))
    # tmp_FE30 = InStr(1, RefL, "-", 2)
    f.set('tmp_fe30', c.builtin('instr', [Integer(1), f.get('refl'), '-', Integer(2)]))
    # tmp_FE20 = (tmp_FE30 - 1)
    f.set('tmp_fe20', c.binary('-', f.get('tmp_fe30'), Integer(1)))
    # tmp_FE08 = Left(RefL, CLng(tmp_FE20))
    f.set('tmp_fe08', c.builtin('left', [f.get('refl'), c.builtin('clng', [f.get('tmp_fe20')])]))
    # tmp_FDC8 = Trim(tmp_FE08)
    f.set('tmp_fdc8', c.builtin('trim', [f.get('tmp_fe08')]))
    # DashNameL = tmp_FDC8
    f.set('dashnamel', f.get('tmp_fdc8'))
    # If (RefL = TestL) Then GoTo L0741 Else GoTo L074C
    return 149 if truth(c.binary('=', f.get('refl'), f.get('testl'))) else 151

def _namesimilarity_149(f, c):
    # LSimValu = CSng(CDbl(1))
    f.set('lsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(1)])]))
    # GoTo L0789
    return 155

def _namesimilarity_151(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # LSimValu = CSng(IsSimilar(RefL, TestL, tmp_FD30))
    f.set('lsimvalu', c.builtin('csng', [c.call('issimilar', [f.get('refl'), f.get('testl'), f.ref('tmp_fd30')])]))
    # If (LSimValu < CSng(0.8)) Then GoTo L0781 Else GoTo L0789
    return 154 if truth(c.binary('<', f.get('lsimvalu'), c.builtin('csng', [0.8]))) else 155

def _namesimilarity_154(f, c):
    # LSimValu = CSng(CDbl(0))
    f.set('lsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(0)])]))
    return 155

def _namesimilarity_155(f, c):
    # If (LSimValu = CDbl(0)) Then GoTo L0797 Else GoTo L0833
    return 156 if truth(c.binary('=', f.get('lsimvalu'), c.builtin('cdbl', [Integer(0)]))) else 167

def _namesimilarity_156(f, c):
    # tmp_FE30 = InStr(1, TestL, "-", 2)
    f.set('tmp_fe30', c.builtin('instr', [Integer(1), f.get('testl'), '-', Integer(2)]))
    # tmp_FE20 = (tmp_FE30 - 1)
    f.set('tmp_fe20', c.binary('-', f.get('tmp_fe30'), Integer(1)))
    # tmp_FE08 = Left(TestL, CLng(tmp_FE20))
    f.set('tmp_fe08', c.builtin('left', [f.get('testl'), c.builtin('clng', [f.get('tmp_fe20')])]))
    # If (DashNameR = tmp_FE08) Then GoTo L07D7 Else GoTo L07E2
    return 160 if truth(c.binary('=', f.get('dashnamer'), f.get('tmp_fe08'))) else 162

def _namesimilarity_160(f, c):
    # LSimValu = CSng(CDbl(1))
    f.set('lsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(1)])]))
    # GoTo L0831
    return 167

def _namesimilarity_162(f, c):
    # tmp_FE30 = InStr(1, TestL, "-", 2)
    f.set('tmp_fe30', c.builtin('instr', [Integer(1), f.get('testl'), '-', Integer(2)]))
    # tmp_FE20 = (tmp_FE30 + 1)
    f.set('tmp_fe20', c.binary('+', f.get('tmp_fe30'), Integer(1)))
    # tmp_FDC8 = Mid(TestL, CLng(tmp_FE20))
    f.set('tmp_fdc8', c.builtin('mid', [f.get('testl'), c.builtin('clng', [f.get('tmp_fe20')])]))
    # If (DashNameL = tmp_FDC8) Then GoTo L0829 Else GoTo L0831
    return 166 if truth(c.binary('=', f.get('dashnamel'), f.get('tmp_fdc8'))) else 167

def _namesimilarity_166(f, c):
    # LSimValu = CSng(CDbl(1))
    f.set('lsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(1)])]))
    return 167

def _namesimilarity_167(f, c):
    # If (LSimValu = CDbl(0)) Then GoTo L0841 Else GoTo L0914
    return 168 if truth(c.binary('=', f.get('lsimvalu'), c.builtin('cdbl', [Integer(0)]))) else 181

def _namesimilarity_168(f, c):
    # tmp_FE30 = InStr(1, TestL, "-", 2)
    f.set('tmp_fe30', c.builtin('instr', [Integer(1), f.get('testl'), '-', Integer(2)]))
    # tmp_FE20 = (tmp_FE30 + 1)
    f.set('tmp_fe20', c.binary('+', f.get('tmp_fe30'), Integer(1)))
    # tmp_FDC8 = Mid(TestL, CLng(tmp_FE20))
    f.set('tmp_fdc8', c.builtin('mid', [f.get('testl'), c.builtin('clng', [f.get('tmp_fe20')])]))
    # tmp_FDA8 = InStr(1, TestL, "-", 2)
    f.set('tmp_fda8', c.builtin('instr', [Integer(1), f.get('testl'), '-', Integer(2)]))
    # tmp_FD98 = (tmp_FDA8 - 1)
    f.set('tmp_fd98', c.binary('-', f.get('tmp_fda8'), Integer(1)))
    # tmp_FD78 = Left(TestL, CLng(tmp_FD98))
    f.set('tmp_fd78', c.builtin('left', [f.get('testl'), c.builtin('clng', [f.get('tmp_fd98')])]))
    # tmp_FD2C = CStr(0)
    f.set('tmp_fd2c', c.builtin('cstr', [Integer(0)]))
    # tmp_FE1C = CSng(IsSimilar(DashNameR, tmp_FD78, tmp_FD2C))
    f.set('tmp_fe1c', c.builtin('csng', [c.call('issimilar', [f.get('dashnamer'), f.get('tmp_fd78'), f.ref('tmp_fd2c')])]))
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # LSimValu = CSng(((IsSimilar(DashNameL, tmp_FDC8, tmp_FD30) + tmp_FE1C) / CDbl(2)))
    f.set('lsimvalu', c.builtin('csng', [c.binary('/', c.binary('+', c.call('issimilar', [f.get('dashnamel'), f.get('tmp_fdc8'), f.ref('tmp_fd30')]), f.get('tmp_fe1c')), c.builtin('cdbl', [Integer(2)]))]))
    # If (LSimValu < CSng(0.8)) Then GoTo L0905 Else GoTo L0912
    return 179 if truth(c.binary('<', f.get('lsimvalu'), c.builtin('csng', [0.8]))) else 181

def _namesimilarity_179(f, c):
    # SimScore = CSng(CDbl(0))
    f.set('simscore', c.builtin('csng', [c.builtin('cdbl', [Integer(0)])]))
    # GoTo L19F9
    return 557

def _namesimilarity_181(f, c):
    # If DashInOne Then GoTo L0920 Else GoTo L0D6F
    return 182 if truth(f.get('dashinone')) else 271

def _namesimilarity_182(f, c):
    # tmp_FE30 = (RefL Like "*-*")
    f.set('tmp_fe30', c.binary('like', f.get('refl'), '*-*'))
    # tmp_FE20 = (TestL Like "*-*")
    f.set('tmp_fe20', c.binary('like', f.get('testl'), '*-*'))
    # tmp_FE08 = (Not tmp_FE20)
    f.set('tmp_fe08', c.unary('not', f.get('tmp_fe20')))
    # tmp_FDC8 = (tmp_FE30 And tmp_FE08)
    f.set('tmp_fdc8', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fe08')))
    # If tmp_FDC8 Then GoTo L0947 Else GoTo L0B48
    return 187 if truth(f.get('tmp_fdc8')) else 227

def _namesimilarity_187(f, c):
    # tmp_FE30 = InStr(1, RefL, "-", 2)
    f.set('tmp_fe30', c.builtin('instr', [Integer(1), f.get('refl'), '-', Integer(2)]))
    # tmp_FE20 = (tmp_FE30 + 1)
    f.set('tmp_fe20', c.binary('+', f.get('tmp_fe30'), Integer(1)))
    # tmp_FDC8 = Mid(RefL, CLng(tmp_FE20))
    f.set('tmp_fdc8', c.builtin('mid', [f.get('refl'), c.builtin('clng', [f.get('tmp_fe20')])]))
    # tmp_FDA8 = Trim(tmp_FDC8)
    f.set('tmp_fda8', c.builtin('trim', [f.get('tmp_fdc8')]))
    # DashNameR = tmp_FDA8
    f.set('dashnamer', f.get('tmp_fda8'))
    # tmp_FE30 = InStr(1, RefL, "-", 2)
    f.set('tmp_fe30', c.builtin('instr', [Integer(1), f.get('refl'), '-', Integer(2)]))
    # tmp_FE20 = (tmp_FE30 - 1)
    f.set('tmp_fe20', c.binary('-', f.get('tmp_fe30'), Integer(1)))
    # tmp_FE08 = Left(RefL, CLng(tmp_FE20))
    f.set('tmp_fe08', c.builtin('left', [f.get('refl'), c.builtin('clng', [f.get('tmp_fe20')])]))
    # tmp_FDC8 = Trim(tmp_FE08)
    f.set('tmp_fdc8', c.builtin('trim', [f.get('tmp_fe08')]))
    # DashNameL = tmp_FDC8
    f.set('dashnamel', f.get('tmp_fdc8'))
    # tmp_FE30 = (TestL Like "* *")
    f.set('tmp_fe30', c.binary('like', f.get('testl'), '* *'))
    # If tmp_FE30 Then GoTo L09EF Else GoTo L0A6D
    return 199 if truth(f.get('tmp_fe30')) else 209

def _namesimilarity_199(f, c):
    # tmp_FE18 = 0
    f.set('tmp_fe18', Integer(0))
    # tmp_FE1C = 1
    f.set('tmp_fe1c', Integer(1))
    # tmp_FE20 = " "
    f.set('tmp_fe20', ' ')
    # tmp_FE30 = "-"
    f.set('tmp_fe30', '-')
    # tmp_FE08 = StrReplace(RefL, tmp_FE30, tmp_FE20, tmp_FE1C, tmp_FE18)
    f.set('tmp_fe08', c.call('strreplace', [f.ref('refl'), f.ref('tmp_fe30'), f.ref('tmp_fe20'), f.ref('tmp_fe1c'), f.ref('tmp_fe18')]))
    # DashName = tmp_FE08
    f.set('dashname', f.get('tmp_fe08'))
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # LSimValu = CSng(IsSimilar(DashName, TestL, tmp_FD30))
    f.set('lsimvalu', c.builtin('csng', [c.call('issimilar', [f.get('dashname'), f.get('testl'), f.ref('tmp_fd30')])]))
    # If (LSimValu < CSng(0.8)) Then GoTo L0A63 Else GoTo L0A6B
    return 208 if truth(c.binary('<', f.get('lsimvalu'), c.builtin('csng', [0.8]))) else 209

def _namesimilarity_208(f, c):
    # LSimValu = CSng(CDbl(0))
    f.set('lsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(0)])]))
    return 209

def _namesimilarity_209(f, c):
    # If (LSimValu = CDbl(0)) Then GoTo L0A7B Else GoTo L0AAA
    return 210 if truth(c.binary('=', f.get('lsimvalu'), c.builtin('cdbl', [Integer(0)]))) else 215

def _namesimilarity_210(f, c):
    # If (DashNameR = TestL) Then GoTo L0A88 Else GoTo L0A93
    return 211 if truth(c.binary('=', f.get('dashnamer'), f.get('testl'))) else 213

def _namesimilarity_211(f, c):
    # LSimValu = CSng(CDbl(1))
    f.set('lsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(1)])]))
    # GoTo L0AA8
    return 215

def _namesimilarity_213(f, c):
    # If (DashNameL = TestL) Then GoTo L0AA0 Else GoTo L0AA8
    return 214 if truth(c.binary('=', f.get('dashnamel'), f.get('testl'))) else 215

def _namesimilarity_214(f, c):
    # LSimValu = CSng(CDbl(1))
    f.set('lsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(1)])]))
    return 215

def _namesimilarity_215(f, c):
    # If (LSimValu = CDbl(0)) Then GoTo L0AB8 Else GoTo L0B43
    return 216 if truth(c.binary('=', f.get('lsimvalu'), c.builtin('cdbl', [Integer(0)]))) else 226

def _namesimilarity_216(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # LSimValu = CSng(IsSimilar(DashNameL, TestL, tmp_FD30))
    f.set('lsimvalu', c.builtin('csng', [c.call('issimilar', [f.get('dashnamel'), f.get('testl'), f.ref('tmp_fd30')])]))
    # If (LSimValu < CSng(0.8)) Then GoTo L0AEB Else GoTo L0AF3
    return 219 if truth(c.binary('<', f.get('lsimvalu'), c.builtin('csng', [0.8]))) else 220

def _namesimilarity_219(f, c):
    # LSimValu = CSng(CDbl(0))
    f.set('lsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(0)])]))
    return 220

def _namesimilarity_220(f, c):
    # If (LSimValu = CDbl(0)) Then GoTo L0AFF Else GoTo L0B1F
    return 221 if truth(c.binary('=', f.get('lsimvalu'), c.builtin('cdbl', [Integer(0)]))) else 223

def _namesimilarity_221(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # LSimValu = CSng(IsSimilar(DashNameR, TestL, tmp_FD30))
    f.set('lsimvalu', c.builtin('csng', [c.call('issimilar', [f.get('dashnamer'), f.get('testl'), f.ref('tmp_fd30')])]))
    return 223

def _namesimilarity_223(f, c):
    # If (LSimValu < CSng(0.8)) Then GoTo L0B34 Else GoTo L0B41
    return 224 if truth(c.binary('<', f.get('lsimvalu'), c.builtin('csng', [0.8]))) else 226

def _namesimilarity_224(f, c):
    # SimScore = CSng(CDbl(0))
    f.set('simscore', c.builtin('csng', [c.builtin('cdbl', [Integer(0)])]))
    # GoTo L19F9
    return 557

def _namesimilarity_226(f, c):
    # GoTo L0D6D
    return 271

def _namesimilarity_227(f, c):
    # tmp_FE30 = (RefL Like "*-*")
    f.set('tmp_fe30', c.binary('like', f.get('refl'), '*-*'))
    # tmp_FE20 = (Not tmp_FE30)
    f.set('tmp_fe20', c.unary('not', f.get('tmp_fe30')))
    # tmp_FE08 = (TestL Like "*-*")
    f.set('tmp_fe08', c.binary('like', f.get('testl'), '*-*'))
    # tmp_FDC8 = (tmp_FE20 And tmp_FE08)
    f.set('tmp_fdc8', c.binary('and', f.get('tmp_fe20'), f.get('tmp_fe08')))
    # If tmp_FDC8 Then GoTo L0B6F Else GoTo L0D6D
    return 232 if truth(f.get('tmp_fdc8')) else 271

def _namesimilarity_232(f, c):
    # tmp_FE30 = InStr(1, TestL, "-", 2)
    f.set('tmp_fe30', c.builtin('instr', [Integer(1), f.get('testl'), '-', Integer(2)]))
    # tmp_FE20 = (tmp_FE30 + 1)
    f.set('tmp_fe20', c.binary('+', f.get('tmp_fe30'), Integer(1)))
    # tmp_FDC8 = Mid(TestL, CLng(tmp_FE20))
    f.set('tmp_fdc8', c.builtin('mid', [f.get('testl'), c.builtin('clng', [f.get('tmp_fe20')])]))
    # tmp_FDA8 = Trim(tmp_FDC8)
    f.set('tmp_fda8', c.builtin('trim', [f.get('tmp_fdc8')]))
    # DashNameR = tmp_FDA8
    f.set('dashnamer', f.get('tmp_fda8'))
    # tmp_FE30 = InStr(1, TestL, "-", 2)
    f.set('tmp_fe30', c.builtin('instr', [Integer(1), f.get('testl'), '-', Integer(2)]))
    # tmp_FE20 = (tmp_FE30 - 1)
    f.set('tmp_fe20', c.binary('-', f.get('tmp_fe30'), Integer(1)))
    # tmp_FE08 = Left(TestL, CLng(tmp_FE20))
    f.set('tmp_fe08', c.builtin('left', [f.get('testl'), c.builtin('clng', [f.get('tmp_fe20')])]))
    # tmp_FDC8 = Trim(tmp_FE08)
    f.set('tmp_fdc8', c.builtin('trim', [f.get('tmp_fe08')]))
    # DashNameL = tmp_FDC8
    f.set('dashnamel', f.get('tmp_fdc8'))
    # tmp_FE30 = (RefL Like "* *")
    f.set('tmp_fe30', c.binary('like', f.get('refl'), '* *'))
    # If tmp_FE30 Then GoTo L0C17 Else GoTo L0C95
    return 244 if truth(f.get('tmp_fe30')) else 254

def _namesimilarity_244(f, c):
    # tmp_FE18 = 0
    f.set('tmp_fe18', Integer(0))
    # tmp_FE1C = 1
    f.set('tmp_fe1c', Integer(1))
    # tmp_FE20 = " "
    f.set('tmp_fe20', ' ')
    # tmp_FE30 = "-"
    f.set('tmp_fe30', '-')
    # tmp_FE08 = StrReplace(TestL, tmp_FE30, tmp_FE20, tmp_FE1C, tmp_FE18)
    f.set('tmp_fe08', c.call('strreplace', [f.ref('testl'), f.ref('tmp_fe30'), f.ref('tmp_fe20'), f.ref('tmp_fe1c'), f.ref('tmp_fe18')]))
    # DashName = tmp_FE08
    f.set('dashname', f.get('tmp_fe08'))
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # LSimValu = CSng(IsSimilar(DashName, RefL, tmp_FD30))
    f.set('lsimvalu', c.builtin('csng', [c.call('issimilar', [f.get('dashname'), f.get('refl'), f.ref('tmp_fd30')])]))
    # If (LSimValu < CSng(0.8)) Then GoTo L0C8B Else GoTo L0C93
    return 253 if truth(c.binary('<', f.get('lsimvalu'), c.builtin('csng', [0.8]))) else 254

def _namesimilarity_253(f, c):
    # LSimValu = CSng(CDbl(0))
    f.set('lsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(0)])]))
    return 254

def _namesimilarity_254(f, c):
    # If (LSimValu = CDbl(0)) Then GoTo L0CA3 Else GoTo L0CD2
    return 255 if truth(c.binary('=', f.get('lsimvalu'), c.builtin('cdbl', [Integer(0)]))) else 260

def _namesimilarity_255(f, c):
    # If (DashNameR = RefL) Then GoTo L0CB0 Else GoTo L0CBB
    return 256 if truth(c.binary('=', f.get('dashnamer'), f.get('refl'))) else 258

def _namesimilarity_256(f, c):
    # LSimValu = CSng(CDbl(1))
    f.set('lsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(1)])]))
    # GoTo L0CD0
    return 260

def _namesimilarity_258(f, c):
    # If (DashNameL = RefL) Then GoTo L0CC8 Else GoTo L0CD0
    return 259 if truth(c.binary('=', f.get('dashnamel'), f.get('refl'))) else 260

def _namesimilarity_259(f, c):
    # LSimValu = CSng(CDbl(1))
    f.set('lsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(1)])]))
    return 260

def _namesimilarity_260(f, c):
    # If (LSimValu = CDbl(0)) Then GoTo L0CE0 Else GoTo L0D6B
    return 261 if truth(c.binary('=', f.get('lsimvalu'), c.builtin('cdbl', [Integer(0)]))) else 271

def _namesimilarity_261(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # LSimValu = CSng(IsSimilar(DashNameL, RefL, tmp_FD30))
    f.set('lsimvalu', c.builtin('csng', [c.call('issimilar', [f.get('dashnamel'), f.get('refl'), f.ref('tmp_fd30')])]))
    # If (LSimValu < CSng(0.8)) Then GoTo L0D13 Else GoTo L0D1B
    return 264 if truth(c.binary('<', f.get('lsimvalu'), c.builtin('csng', [0.8]))) else 265

def _namesimilarity_264(f, c):
    # LSimValu = CSng(CDbl(0))
    f.set('lsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(0)])]))
    return 265

def _namesimilarity_265(f, c):
    # If (LSimValu = CDbl(0)) Then GoTo L0D27 Else GoTo L0D47
    return 266 if truth(c.binary('=', f.get('lsimvalu'), c.builtin('cdbl', [Integer(0)]))) else 268

def _namesimilarity_266(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # LSimValu = CSng(IsSimilar(DashNameR, RefL, tmp_FD30))
    f.set('lsimvalu', c.builtin('csng', [c.call('issimilar', [f.get('dashnamer'), f.get('refl'), f.ref('tmp_fd30')])]))
    return 268

def _namesimilarity_268(f, c):
    # If (LSimValu < CSng(0.8)) Then GoTo L0D5C Else GoTo L0D69
    return 269 if truth(c.binary('<', f.get('lsimvalu'), c.builtin('csng', [0.8]))) else 271

def _namesimilarity_269(f, c):
    # SimScore = CSng(CDbl(0))
    f.set('simscore', c.builtin('csng', [c.builtin('cdbl', [Integer(0)])]))
    # GoTo L19F9
    return 557

def _namesimilarity_271(f, c):
    # If LastInMiddle Then GoTo L0D79 Else GoTo L0E88
    return 272 if truth(f.get('lastinmiddle')) else 296

def _namesimilarity_272(f, c):
    # If (RefF = TestF) Then GoTo L0D86 Else GoTo L0D91
    return 273 if truth(c.binary('=', f.get('reff'), f.get('testf'))) else 275

def _namesimilarity_273(f, c):
    # FSimValu = CSng(CDbl(1))
    f.set('fsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(1)])]))
    # GoTo L0E6D
    return 294

def _namesimilarity_275(f, c):
    # tmp_FE30 = (RefFLen > 1)
    f.set('tmp_fe30', c.binary('>', f.get('refflen'), Integer(1)))
    # tmp_FE20 = (TestFLen = 1)
    f.set('tmp_fe20', c.binary('=', f.get('testflen'), Integer(1)))
    # tmp_FE08 = (tmp_FE30 And tmp_FE20)
    f.set('tmp_fe08', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # tmp_FDC8 = (RefFLen = 1)
    f.set('tmp_fdc8', c.binary('=', f.get('refflen'), Integer(1)))
    # tmp_FDA8 = (TestFLen > 1)
    f.set('tmp_fda8', c.binary('>', f.get('testflen'), Integer(1)))
    # tmp_FD98 = (tmp_FDC8 And tmp_FDA8)
    f.set('tmp_fd98', c.binary('and', f.get('tmp_fdc8'), f.get('tmp_fda8')))
    # tmp_FD78 = (tmp_FE08 Or tmp_FD98)
    f.set('tmp_fd78', c.binary('or', f.get('tmp_fe08'), f.get('tmp_fd98')))
    # If tmp_FD78 Then GoTo L0DDA Else GoTo L0E12
    return 283 if truth(f.get('tmp_fd78')) else 287

def _namesimilarity_283(f, c):
    # tmp_FE30 = Left(RefF, 1)
    f.set('tmp_fe30', c.builtin('left', [f.get('reff'), Integer(1)]))
    # tmp_FE20 = Left(TestF, 1)
    f.set('tmp_fe20', c.builtin('left', [f.get('testf'), Integer(1)]))
    # tmp_FE08 = (tmp_FE30 = tmp_FE20)
    f.set('tmp_fe08', c.binary('=', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # FFirstSameLetter = CInt(CBool(tmp_FE08))
    f.set('ffirstsameletter', c.builtin('cint', [c.builtin('cbool', [f.get('tmp_fe08')])]))
    return 287

def _namesimilarity_287(f, c):
    # If (Not FFirstSameLetter) Then GoTo L0E1D Else GoTo L0E40
    return 288 if truth(c.unary('not', f.get('ffirstsameletter'))) else 291

def _namesimilarity_288(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # FSimValu = CSng(IsSimilar(RefF, TestF, tmp_FD30))
    f.set('fsimvalu', c.builtin('csng', [c.call('issimilar', [f.get('reff'), f.get('testf'), f.ref('tmp_fd30')])]))
    # GoTo L0E50
    return 292

def _namesimilarity_291(f, c):
    # FSimValu = CSng(0.8)
    f.set('fsimvalu', c.builtin('csng', [0.8]))
    return 292

def _namesimilarity_292(f, c):
    # If (FSimValu < CSng(0.7)) Then GoTo L0E65 Else GoTo L0E6D
    return 293 if truth(c.binary('<', f.get('fsimvalu'), c.builtin('csng', [0.7]))) else 294

def _namesimilarity_293(f, c):
    # FSimValu = CSng(CDbl(0))
    f.set('fsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(0)])]))
    return 294

def _namesimilarity_294(f, c):
    # SimScore = CSng((((LSimValu + FSimValu) + MSimValu) / CDbl(3)))
    f.set('simscore', c.builtin('csng', [c.binary('/', c.binary('+', c.binary('+', f.get('lsimvalu'), f.get('fsimvalu')), f.get('msimvalu')), c.builtin('cdbl', [Integer(3)]))]))
    # GoTo L19F9
    return 557

def _namesimilarity_296(f, c):
    # If (RefF = TestF) Then GoTo L0E97 Else GoTo L0E9F
    return 297 if truth(c.binary('=', f.get('reff'), f.get('testf'))) else 298

def _namesimilarity_297(f, c):
    # FSimValu = CSng(CDbl(1))
    f.set('fsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(1)])]))
    return 298

def _namesimilarity_298(f, c):
    # tmp_FE30 = (RefM = TestM)
    f.set('tmp_fe30', c.binary('=', f.get('refm'), f.get('testm')))
    # tmp_FE20 = (RefMLen > 0)
    f.set('tmp_fe20', c.binary('>', f.get('refmlen'), Integer(0)))
    # tmp_FE08 = (TestMLen > 0)
    f.set('tmp_fe08', c.binary('>', f.get('testmlen'), Integer(0)))
    # tmp_FDC8 = (tmp_FE20 And tmp_FE08)
    f.set('tmp_fdc8', c.binary('and', f.get('tmp_fe20'), f.get('tmp_fe08')))
    # tmp_FDA8 = (tmp_FE30 And tmp_FDC8)
    f.set('tmp_fda8', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fdc8')))
    # If tmp_FDA8 Then GoTo L0ED4 Else GoTo L0EDC
    return 304 if truth(f.get('tmp_fda8')) else 305

def _namesimilarity_304(f, c):
    # MSimValu = CSng(CDbl(1))
    f.set('msimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(1)])]))
    return 305

def _namesimilarity_305(f, c):
    # tmp_FE30 = (RefF = TestF)
    f.set('tmp_fe30', c.binary('=', f.get('reff'), f.get('testf')))
    # tmp_FE20 = (RefM = TestM)
    f.set('tmp_fe20', c.binary('=', f.get('refm'), f.get('testm')))
    # tmp_FE08 = (RefMLen > 0)
    f.set('tmp_fe08', c.binary('>', f.get('refmlen'), Integer(0)))
    # tmp_FDC8 = (TestMLen > 0)
    f.set('tmp_fdc8', c.binary('>', f.get('testmlen'), Integer(0)))
    # tmp_FDA8 = (tmp_FE08 And tmp_FDC8)
    f.set('tmp_fda8', c.binary('and', f.get('tmp_fe08'), f.get('tmp_fdc8')))
    # tmp_FD98 = (tmp_FE20 And tmp_FDA8)
    f.set('tmp_fd98', c.binary('and', f.get('tmp_fe20'), f.get('tmp_fda8')))
    # tmp_FD78 = (tmp_FE30 And tmp_FD98)
    f.set('tmp_fd78', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fd98')))
    # If tmp_FD78 Then GoTo L0F1D Else GoTo L0F4B
    return 313 if truth(f.get('tmp_fd78')) else 316

def _namesimilarity_313(f, c):
    # If (LSimValu > CSng(0.86)) Then GoTo L0F30 Else GoTo L0F49
    return 314 if truth(c.binary('>', f.get('lsimvalu'), c.builtin('csng', [0.86]))) else 316

def _namesimilarity_314(f, c):
    # SimScore = CSng((((LSimValu + FSimValu) + MSimValu) / CDbl(3)))
    f.set('simscore', c.builtin('csng', [c.binary('/', c.binary('+', c.binary('+', f.get('lsimvalu'), f.get('fsimvalu')), f.get('msimvalu')), c.builtin('cdbl', [Integer(3)]))]))
    # GoTo L19F9
    return 557

def _namesimilarity_316(f, c):
    # If (LSimValu > CSng(0.84)) Then GoTo L0F60 Else GoTo L14E1
    return 317 if truth(c.binary('>', f.get('lsimvalu'), c.builtin('csng', [0.84]))) else 445

def _namesimilarity_317(f, c):
    # tmp_FE30 = (RefMLen > 1)
    f.set('tmp_fe30', c.binary('>', f.get('refmlen'), Integer(1)))
    # tmp_FE20 = (TestMLen > 1)
    f.set('tmp_fe20', c.binary('>', f.get('testmlen'), Integer(1)))
    # tmp_FE08 = (tmp_FE30 Or tmp_FE20)
    f.set('tmp_fe08', c.binary('or', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # If tmp_FE08 Then GoTo L0F85 Else GoTo L1093
    return 321 if truth(f.get('tmp_fe08')) else 347

def _namesimilarity_321(f, c):
    # tmp_FE30 = (RefF = TestF)
    f.set('tmp_fe30', c.binary('=', f.get('reff'), f.get('testf')))
    # tmp_FE20 = (Not tmp_FE30)
    f.set('tmp_fe20', c.unary('not', f.get('tmp_fe30')))
    # tmp_FE08 = (RefM = TestM)
    f.set('tmp_fe08', c.binary('=', f.get('refm'), f.get('testm')))
    # tmp_FDC8 = (Not tmp_FE08)
    f.set('tmp_fdc8', c.unary('not', f.get('tmp_fe08')))
    # tmp_FDA8 = (tmp_FE20 And tmp_FDC8)
    f.set('tmp_fda8', c.binary('and', f.get('tmp_fe20'), f.get('tmp_fdc8')))
    # If tmp_FDA8 Then GoTo L0FAC Else GoTo L1091
    return 327 if truth(f.get('tmp_fda8')) else 347

def _namesimilarity_327(f, c):
    # tmp_FE30 = (RefF & RefM)
    f.set('tmp_fe30', c.binary('&', f.get('reff'), f.get('refm')))
    # tmp_FE20 = (tmp_FE30 = TestF)
    f.set('tmp_fe20', c.binary('=', f.get('tmp_fe30'), f.get('testf')))
    # tmp_FE08 = (TestF & TestM)
    f.set('tmp_fe08', c.binary('&', f.get('testf'), f.get('testm')))
    # tmp_FDC8 = (RefF = tmp_FE08)
    f.set('tmp_fdc8', c.binary('=', f.get('reff'), f.get('tmp_fe08')))
    # tmp_FDA8 = (tmp_FE20 Or tmp_FDC8)
    f.set('tmp_fda8', c.binary('or', f.get('tmp_fe20'), f.get('tmp_fdc8')))
    # If tmp_FDA8 Then GoTo L0FE0 Else GoTo L0FF6
    return 333 if truth(f.get('tmp_fda8')) else 336

def _namesimilarity_333(f, c):
    # SimScore = CSng(0.8)
    f.set('simscore', c.builtin('csng', [0.8]))
    # GoTo L19F9
    return 557

def _namesimilarity_335(f, c):
    # GoTo L108F
    return 347

def _namesimilarity_336(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # tmp_FE30 = (RefF & RefM)
    f.set('tmp_fe30', c.binary('&', f.get('reff'), f.get('refm')))
    # If (CSng(IsSimilar(tmp_FE30, TestF, tmp_FD30)) > CSng(0.85)) Then GoTo L102E Else GoTo L1044
    return 339 if truth(c.binary('>', c.builtin('csng', [c.call('issimilar', [f.get('tmp_fe30'), f.get('testf'), f.ref('tmp_fd30')])]), c.builtin('csng', [0.85]))) else 342

def _namesimilarity_339(f, c):
    # SimScore = CSng(0.8)
    f.set('simscore', c.builtin('csng', [0.8]))
    # GoTo L19F9
    return 557

def _namesimilarity_341(f, c):
    # GoTo L108D
    return 347

def _namesimilarity_342(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # tmp_FE30 = (TestF & TestF)
    f.set('tmp_fe30', c.binary('&', f.get('testf'), f.get('testf')))
    # If (CSng(IsSimilar(RefF, tmp_FE30, tmp_FD30)) > CSng(0.85)) Then GoTo L107A Else GoTo L108D
    return 345 if truth(c.binary('>', c.builtin('csng', [c.call('issimilar', [f.get('reff'), f.get('tmp_fe30'), f.ref('tmp_fd30')])]), c.builtin('csng', [0.85]))) else 347

def _namesimilarity_345(f, c):
    # SimScore = CSng(0.8)
    f.set('simscore', c.builtin('csng', [0.8]))
    # GoTo L19F9
    return 557

def _namesimilarity_347(f, c):
    # tmp_FE30 = (RefFLen > 1)
    f.set('tmp_fe30', c.binary('>', f.get('refflen'), Integer(1)))
    # tmp_FE20 = (TestMLen > 1)
    f.set('tmp_fe20', c.binary('>', f.get('testmlen'), Integer(1)))
    # tmp_FE08 = (tmp_FE30 And tmp_FE20)
    f.set('tmp_fe08', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # If tmp_FE08 Then GoTo L10BA Else GoTo L1106
    return 351 if truth(f.get('tmp_fe08')) else 357

def _namesimilarity_351(f, c):
    # If (RefF = TestM) Then GoTo L10C7 Else GoTo L10D1
    return 352 if truth(c.binary('=', f.get('reff'), f.get('testm'))) else 354

def _namesimilarity_352(f, c):
    # RF_in_TM = CInt(-1)
    f.set('rf_in_tm', c.builtin('cint', [c.unary('-', Integer(1))]))
    # GoTo L1104
    return 357

def _namesimilarity_354(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # If (CSng(IsSimilar(RefF, TestM, tmp_FD30)) > CSng(0.86)) Then GoTo L10FD Else GoTo L1104
    return 356 if truth(c.binary('>', c.builtin('csng', [c.call('issimilar', [f.get('reff'), f.get('testm'), f.ref('tmp_fd30')])]), c.builtin('csng', [0.86]))) else 357

def _namesimilarity_356(f, c):
    # RF_in_TM = CInt(-1)
    f.set('rf_in_tm', c.builtin('cint', [c.unary('-', Integer(1))]))
    return 357

def _namesimilarity_357(f, c):
    # tmp_FE30 = (RefMLen > 1)
    f.set('tmp_fe30', c.binary('>', f.get('refmlen'), Integer(1)))
    # tmp_FE20 = (TestFLen > 1)
    f.set('tmp_fe20', c.binary('>', f.get('testflen'), Integer(1)))
    # tmp_FE08 = (tmp_FE30 And tmp_FE20)
    f.set('tmp_fe08', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # If tmp_FE08 Then GoTo L112D Else GoTo L1179
    return 361 if truth(f.get('tmp_fe08')) else 367

def _namesimilarity_361(f, c):
    # If (RefM = TestF) Then GoTo L113A Else GoTo L1144
    return 362 if truth(c.binary('=', f.get('refm'), f.get('testf'))) else 364

def _namesimilarity_362(f, c):
    # RM_in_TF = CInt(-1)
    f.set('rm_in_tf', c.builtin('cint', [c.unary('-', Integer(1))]))
    # GoTo L1177
    return 367

def _namesimilarity_364(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # If (CSng(IsSimilar(RefM, TestF, tmp_FD30)) > CSng(0.86)) Then GoTo L1170 Else GoTo L1177
    return 366 if truth(c.binary('>', c.builtin('csng', [c.call('issimilar', [f.get('refm'), f.get('testf'), f.ref('tmp_fd30')])]), c.builtin('csng', [0.86]))) else 367

def _namesimilarity_366(f, c):
    # RM_in_TF = CInt(-1)
    f.set('rm_in_tf', c.builtin('cint', [c.unary('-', Integer(1))]))
    return 367

def _namesimilarity_367(f, c):
    # If (((RF_in_TM And RM_in_TF) Or (RF_in_TM And (Not RM_in_TF))) Or ((Not RF_in_TM) And RM_in_TF)) Then GoTo L1199 Else GoTo L11AC
    return 368 if truth(c.binary('or', c.binary('or', c.binary('and', f.get('rf_in_tm'), f.get('rm_in_tf')), c.binary('and', f.get('rf_in_tm'), c.unary('not', f.get('rm_in_tf')))), c.binary('and', c.unary('not', f.get('rf_in_tm')), f.get('rm_in_tf')))) else 370

def _namesimilarity_368(f, c):
    # SimScore = CSng(0.8)
    f.set('simscore', c.builtin('csng', [0.8]))
    # GoTo L19F9
    return 557

def _namesimilarity_370(f, c):
    # tmp_FE30 = (RefFLen > 1)
    f.set('tmp_fe30', c.binary('>', f.get('refflen'), Integer(1)))
    # tmp_FE20 = (TestFLen = 1)
    f.set('tmp_fe20', c.binary('=', f.get('testflen'), Integer(1)))
    # tmp_FE08 = (tmp_FE30 And tmp_FE20)
    f.set('tmp_fe08', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # tmp_FDC8 = (RefFLen = 1)
    f.set('tmp_fdc8', c.binary('=', f.get('refflen'), Integer(1)))
    # tmp_FDA8 = (TestFLen > 1)
    f.set('tmp_fda8', c.binary('>', f.get('testflen'), Integer(1)))
    # tmp_FD98 = (tmp_FDC8 And tmp_FDA8)
    f.set('tmp_fd98', c.binary('and', f.get('tmp_fdc8'), f.get('tmp_fda8')))
    # tmp_FD78 = (tmp_FE08 Or tmp_FD98)
    f.set('tmp_fd78', c.binary('or', f.get('tmp_fe08'), f.get('tmp_fd98')))
    # If tmp_FD78 Then GoTo L11F5 Else GoTo L122D
    return 378 if truth(f.get('tmp_fd78')) else 382

def _namesimilarity_378(f, c):
    # tmp_FE30 = Left(RefF, 1)
    f.set('tmp_fe30', c.builtin('left', [f.get('reff'), Integer(1)]))
    # tmp_FE20 = Left(TestF, 1)
    f.set('tmp_fe20', c.builtin('left', [f.get('testf'), Integer(1)]))
    # tmp_FE08 = (tmp_FE30 = tmp_FE20)
    f.set('tmp_fe08', c.binary('=', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # FFirstSameLetter = CInt(CBool(tmp_FE08))
    f.set('ffirstsameletter', c.builtin('cint', [c.builtin('cbool', [f.get('tmp_fe08')])]))
    return 382

def _namesimilarity_382(f, c):
    # tmp_FE30 = (RefMLen > 1)
    f.set('tmp_fe30', c.binary('>', f.get('refmlen'), Integer(1)))
    # tmp_FE20 = (TestMLen = 1)
    f.set('tmp_fe20', c.binary('=', f.get('testmlen'), Integer(1)))
    # tmp_FE08 = (tmp_FE30 And tmp_FE20)
    f.set('tmp_fe08', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # tmp_FDC8 = (RefMLen = 1)
    f.set('tmp_fdc8', c.binary('=', f.get('refmlen'), Integer(1)))
    # tmp_FDA8 = (TestMLen > 1)
    f.set('tmp_fda8', c.binary('>', f.get('testmlen'), Integer(1)))
    # tmp_FD98 = (tmp_FDC8 And tmp_FDA8)
    f.set('tmp_fd98', c.binary('and', f.get('tmp_fdc8'), f.get('tmp_fda8')))
    # tmp_FD78 = (tmp_FE08 Or tmp_FD98)
    f.set('tmp_fd78', c.binary('or', f.get('tmp_fe08'), f.get('tmp_fd98')))
    # If tmp_FD78 Then GoTo L1276 Else GoTo L12AE
    return 390 if truth(f.get('tmp_fd78')) else 394

def _namesimilarity_390(f, c):
    # tmp_FE30 = Left(RefM, 1)
    f.set('tmp_fe30', c.builtin('left', [f.get('refm'), Integer(1)]))
    # tmp_FE20 = Left(TestM, 1)
    f.set('tmp_fe20', c.builtin('left', [f.get('testm'), Integer(1)]))
    # tmp_FE08 = (tmp_FE30 = tmp_FE20)
    f.set('tmp_fe08', c.binary('=', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # MFirstSameLetter = CInt(CBool(tmp_FE08))
    f.set('mfirstsameletter', c.builtin('cint', [c.builtin('cbool', [f.get('tmp_fe08')])]))
    return 394

def _namesimilarity_394(f, c):
    # If FFirstSameLetter Then GoTo L12B8 Else GoTo L13DA
    return 395 if truth(f.get('ffirstsameletter')) else 423

def _namesimilarity_395(f, c):
    # FSimValu = CSng(0.8)
    f.set('fsimvalu', c.builtin('csng', [0.8]))
    # tmp_FE30 = (RefMLen = 0)
    f.set('tmp_fe30', c.binary('=', f.get('refmlen'), Integer(0)))
    # tmp_FE20 = (TestMLen = 0)
    f.set('tmp_fe20', c.binary('=', f.get('testmlen'), Integer(0)))
    # tmp_FE08 = (tmp_FE30 And tmp_FE20)
    f.set('tmp_fe08', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # If tmp_FE08 Then GoTo L12EB Else GoTo L1303
    return 400 if truth(f.get('tmp_fe08')) else 403

def _namesimilarity_400(f, c):
    # SimScore = CSng(((LSimValu + FSimValu) / CDbl(2)))
    f.set('simscore', c.builtin('csng', [c.binary('/', c.binary('+', f.get('lsimvalu'), f.get('fsimvalu')), c.builtin('cdbl', [Integer(2)]))]))
    # GoTo L19F9
    return 557

def _namesimilarity_402(f, c):
    # GoTo L13D8
    return 423

def _namesimilarity_403(f, c):
    # tmp_FE30 = (RefMLen > 1)
    f.set('tmp_fe30', c.binary('>', f.get('refmlen'), Integer(1)))
    # tmp_FE20 = (TestMLen = 0)
    f.set('tmp_fe20', c.binary('=', f.get('testmlen'), Integer(0)))
    # tmp_FE08 = (tmp_FE30 And tmp_FE20)
    f.set('tmp_fe08', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # tmp_FDC8 = (RefMLen = 0)
    f.set('tmp_fdc8', c.binary('=', f.get('refmlen'), Integer(0)))
    # tmp_FDA8 = (TestMLen > 1)
    f.set('tmp_fda8', c.binary('>', f.get('testmlen'), Integer(1)))
    # tmp_FD98 = (tmp_FDC8 And tmp_FDA8)
    f.set('tmp_fd98', c.binary('and', f.get('tmp_fdc8'), f.get('tmp_fda8')))
    # tmp_FD78 = (tmp_FE08 Or tmp_FD98)
    f.set('tmp_fd78', c.binary('or', f.get('tmp_fe08'), f.get('tmp_fd98')))
    # If tmp_FD78 Then GoTo L134A Else GoTo L136C
    return 411 if truth(f.get('tmp_fd78')) else 414

def _namesimilarity_411(f, c):
    # SimScore = CSng((((LSimValu + FSimValu) + 0.5) / CDbl(3)))
    f.set('simscore', c.builtin('csng', [c.binary('/', c.binary('+', c.binary('+', f.get('lsimvalu'), f.get('fsimvalu')), 0.5), c.builtin('cdbl', [Integer(3)]))]))
    # GoTo L19F9
    return 557

def _namesimilarity_413(f, c):
    # GoTo L13D8
    return 423

def _namesimilarity_414(f, c):
    # If (Not MFirstSameLetter) Then GoTo L1375 Else GoTo L13B1
    return 415 if truth(c.unary('not', f.get('mfirstsameletter'))) else 420

def _namesimilarity_415(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # MSimValu = CSng(IsSimilar(RefM, TestM, tmp_FD30))
    f.set('msimvalu', c.builtin('csng', [c.call('issimilar', [f.get('refm'), f.get('testm'), f.ref('tmp_fd30')])]))
    # SimScore = CSng((((LSimValu + FSimValu) + MSimValu) / CDbl(3)))
    f.set('simscore', c.builtin('csng', [c.binary('/', c.binary('+', c.binary('+', f.get('lsimvalu'), f.get('fsimvalu')), f.get('msimvalu')), c.builtin('cdbl', [Integer(3)]))]))
    # GoTo L19F9
    return 557

def _namesimilarity_419(f, c):
    # GoTo L13D8
    return 423

def _namesimilarity_420(f, c):
    # If MFirstSameLetter Then GoTo L13B9 Else GoTo L13D8
    return 421 if truth(f.get('mfirstsameletter')) else 423

def _namesimilarity_421(f, c):
    # SimScore = CSng((((LSimValu + FSimValu) + 0.8) / CDbl(3)))
    f.set('simscore', c.builtin('csng', [c.binary('/', c.binary('+', c.binary('+', f.get('lsimvalu'), f.get('fsimvalu')), 0.8), c.builtin('cdbl', [Integer(3)]))]))
    # GoTo L19F9
    return 557

def _namesimilarity_423(f, c):
    # tmp_FE30 = (RefF & RefM)
    f.set('tmp_fe30', c.binary('&', f.get('reff'), f.get('refm')))
    # tmp_FE20 = (tmp_FE30 = TestF)
    f.set('tmp_fe20', c.binary('=', f.get('tmp_fe30'), f.get('testf')))
    # tmp_FE08 = (TestF & TestM)
    f.set('tmp_fe08', c.binary('&', f.get('testf'), f.get('testm')))
    # tmp_FDC8 = (RefF = tmp_FE08)
    f.set('tmp_fdc8', c.binary('=', f.get('reff'), f.get('tmp_fe08')))
    # tmp_FDA8 = (tmp_FE20 Or tmp_FDC8)
    f.set('tmp_fda8', c.binary('or', f.get('tmp_fe20'), f.get('tmp_fdc8')))
    # If tmp_FDA8 Then GoTo L1410 Else GoTo L1426
    return 429 if truth(f.get('tmp_fda8')) else 432

def _namesimilarity_429(f, c):
    # SimScore = CSng(0.8)
    f.set('simscore', c.builtin('csng', [0.8]))
    # GoTo L19F9
    return 557

def _namesimilarity_431(f, c):
    # GoTo L14DF
    return 445

def _namesimilarity_432(f, c):
    # If (RefMLen > 1) Then GoTo L1436 Else GoTo L1484
    return 433 if truth(c.binary('>', f.get('refmlen'), Integer(1))) else 439

def _namesimilarity_433(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # tmp_FE30 = (RefF & RefM)
    f.set('tmp_fe30', c.binary('&', f.get('reff'), f.get('refm')))
    # If (CSng(IsSimilar(tmp_FE30, TestF, tmp_FD30)) > CSng(0.8)) Then GoTo L146C Else GoTo L147F
    return 436 if truth(c.binary('>', c.builtin('csng', [c.call('issimilar', [f.get('tmp_fe30'), f.get('testf'), f.ref('tmp_fd30')])]), c.builtin('csng', [0.8]))) else 438

def _namesimilarity_436(f, c):
    # SimScore = CSng(0.8)
    f.set('simscore', c.builtin('csng', [0.8]))
    # GoTo L19F9
    return 557

def _namesimilarity_438(f, c):
    # GoTo L14DF
    return 445

def _namesimilarity_439(f, c):
    # If (TestMLen > 1) Then GoTo L1494 Else GoTo L14DF
    return 440 if truth(c.binary('>', f.get('testmlen'), Integer(1))) else 445

def _namesimilarity_440(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # tmp_FE30 = (TestF & TestM)
    f.set('tmp_fe30', c.binary('&', f.get('testf'), f.get('testm')))
    # If (CSng(IsSimilar(RefF, tmp_FE30, tmp_FD30)) > CSng(0.8)) Then GoTo L14CA Else GoTo L14DD
    return 443 if truth(c.binary('>', c.builtin('csng', [c.call('issimilar', [f.get('reff'), f.get('tmp_fe30'), f.ref('tmp_fd30')])]), c.builtin('csng', [0.8]))) else 445

def _namesimilarity_443(f, c):
    # SimScore = CSng(0.8)
    f.set('simscore', c.builtin('csng', [0.8]))
    # GoTo L19F9
    return 557

def _namesimilarity_445(f, c):
    # If (RefF = TestF) Then GoTo L14F0 Else GoTo L14FB
    return 446 if truth(c.binary('=', f.get('reff'), f.get('testf'))) else 448

def _namesimilarity_446(f, c):
    # FSimValu = CSng(CDbl(1))
    f.set('fsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(1)])]))
    # GoTo L157B
    return 455

def _namesimilarity_448(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # FSimValu = CSng(IsSimilar(RefF, TestF, tmp_FD30))
    f.set('fsimvalu', c.builtin('csng', [c.call('issimilar', [f.get('reff'), f.get('testf'), f.ref('tmp_fd30')])]))
    # If (CSng(((LSimValu + FSimValu) / CDbl(2))) < CSng(0.8)) Then GoTo L1539 Else GoTo L1579
    return 451 if truth(c.binary('<', c.builtin('csng', [c.binary('/', c.binary('+', f.get('lsimvalu'), f.get('fsimvalu')), c.builtin('cdbl', [Integer(2)]))]), c.builtin('csng', [0.8]))) else 455

def _namesimilarity_451(f, c):
    # If (FSimValu < CSng(0.5)) Then GoTo L154C Else GoTo L1554
    return 452 if truth(c.binary('<', f.get('fsimvalu'), c.builtin('csng', [0.5]))) else 453

def _namesimilarity_452(f, c):
    # FSimValu = CSng(CDbl(0))
    f.set('fsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(0)])]))
    return 453

def _namesimilarity_453(f, c):
    # If ((MSimValu > CDbl(0)) And (MSimValu < CSng(0.45))) Then GoTo L156F Else GoTo L1577
    return 454 if truth(c.binary('and', c.binary('>', f.get('msimvalu'), c.builtin('cdbl', [Integer(0)])), c.binary('<', f.get('msimvalu'), c.builtin('csng', [0.45])))) else 455

def _namesimilarity_454(f, c):
    # MSimValu = CSng(CDbl(0))
    f.set('msimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(0)])]))
    return 455

def _namesimilarity_455(f, c):
    # If MFirstSameLetter Then GoTo L1585 Else GoTo L15CA
    return 456 if truth(f.get('mfirstsameletter')) else 460

def _namesimilarity_456(f, c):
    # If (CSng(((LSimValu + FSimValu) / CDbl(2))) > CSng(0.8)) Then GoTo L15A1 Else GoTo L15C8
    return 457 if truth(c.binary('>', c.builtin('csng', [c.binary('/', c.binary('+', f.get('lsimvalu'), f.get('fsimvalu')), c.builtin('cdbl', [Integer(2)]))]), c.builtin('csng', [0.8]))) else 460

def _namesimilarity_457(f, c):
    # MSimValu = CSng(0.8)
    f.set('msimvalu', c.builtin('csng', [0.8]))
    # SimScore = CSng((((LSimValu + FSimValu) + MSimValu) / CDbl(3)))
    f.set('simscore', c.builtin('csng', [c.binary('/', c.binary('+', c.binary('+', f.get('lsimvalu'), f.get('fsimvalu')), f.get('msimvalu')), c.builtin('cdbl', [Integer(3)]))]))
    # GoTo L19F9
    return 557

def _namesimilarity_460(f, c):
    # tmp_FE30 = (RefMLen > 0)
    f.set('tmp_fe30', c.binary('>', f.get('refmlen'), Integer(0)))
    # tmp_FE20 = (TestMLen = 0)
    f.set('tmp_fe20', c.binary('=', f.get('testmlen'), Integer(0)))
    # tmp_FE08 = (tmp_FE30 And tmp_FE20)
    f.set('tmp_fe08', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # If tmp_FE08 Then GoTo L15F1 Else GoTo L16B8
    return 464 if truth(f.get('tmp_fe08')) else 481

def _namesimilarity_464(f, c):
    # If (RefM = TestM) Then GoTo L15FE Else GoTo L161E
    return 465 if truth(c.binary('=', f.get('refm'), f.get('testm'))) else 468

def _namesimilarity_465(f, c):
    # If (FSimValu > CSng(0.8)) Then GoTo L1611 Else GoTo L1619
    return 466 if truth(c.binary('>', f.get('fsimvalu'), c.builtin('csng', [0.8]))) else 467

def _namesimilarity_466(f, c):
    # MSimValu = CSng(CDbl(1))
    f.set('msimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(1)])]))
    return 467

def _namesimilarity_467(f, c):
    # GoTo L16B6
    return 481

def _namesimilarity_468(f, c):
    # tmp_FE30 = (RefMLen > 0)
    f.set('tmp_fe30', c.binary('>', f.get('refmlen'), Integer(0)))
    # tmp_FE20 = (TestMLen = 0)
    f.set('tmp_fe20', c.binary('=', f.get('testmlen'), Integer(0)))
    # tmp_FE08 = (tmp_FE30 And tmp_FE20)
    f.set('tmp_fe08', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # tmp_FDC8 = (RefMLen = 0)
    f.set('tmp_fdc8', c.binary('=', f.get('refmlen'), Integer(0)))
    # tmp_FDA8 = (TestMLen > 0)
    f.set('tmp_fda8', c.binary('>', f.get('testmlen'), Integer(0)))
    # tmp_FD98 = (tmp_FDC8 And tmp_FDA8)
    f.set('tmp_fd98', c.binary('and', f.get('tmp_fdc8'), f.get('tmp_fda8')))
    # tmp_FD78 = (tmp_FE08 Or tmp_FD98)
    f.set('tmp_fd78', c.binary('or', f.get('tmp_fe08'), f.get('tmp_fd98')))
    # If tmp_FD78 Then GoTo L1665 Else GoTo L1694
    return 476 if truth(f.get('tmp_fd78')) else 479

def _namesimilarity_476(f, c):
    # If (CSng(((LSimValu + FSimValu) / CDbl(2))) > CSng(0.83)) Then GoTo L1681 Else GoTo L168F
    return 477 if truth(c.binary('>', c.builtin('csng', [c.binary('/', c.binary('+', f.get('lsimvalu'), f.get('fsimvalu')), c.builtin('cdbl', [Integer(2)]))]), c.builtin('csng', [0.83]))) else 478

def _namesimilarity_477(f, c):
    # MSimValu = CSng(0.5)
    f.set('msimvalu', c.builtin('csng', [0.5]))
    return 478

def _namesimilarity_478(f, c):
    # GoTo L16B6
    return 481

def _namesimilarity_479(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # MSimValu = CSng(IsSimilar(RefM, TestM, tmp_FD30))
    f.set('msimvalu', c.builtin('csng', [c.call('issimilar', [f.get('refm'), f.get('testm'), f.ref('tmp_fd30')])]))
    return 481

def _namesimilarity_481(f, c):
    # If (LSimValu < CSng(0.75)) Then GoTo L16CD Else GoTo L16D5
    return 482 if truth(c.binary('<', f.get('lsimvalu'), c.builtin('csng', [0.75]))) else 483

def _namesimilarity_482(f, c):
    # LSimValu = CSng(CDbl(0))
    f.set('lsimvalu', c.builtin('csng', [c.builtin('cdbl', [Integer(0)])]))
    return 483

def _namesimilarity_483(f, c):
    # tmp_FE30 = (RefMLen > 0)
    f.set('tmp_fe30', c.binary('>', f.get('refmlen'), Integer(0)))
    # tmp_FE20 = (TestMLen = 0)
    f.set('tmp_fe20', c.binary('=', f.get('testmlen'), Integer(0)))
    # tmp_FE08 = (tmp_FE30 And tmp_FE20)
    f.set('tmp_fe08', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # If tmp_FE08 Then GoTo L16FA Else GoTo L1746
    return 487 if truth(f.get('tmp_fe08')) else 494

def _namesimilarity_487(f, c):
    # tmp_FE30 = (RefF & RefM)
    f.set('tmp_fe30', c.binary('&', f.get('reff'), f.get('refm')))
    # tmp_FE20 = (TestF & TestM)
    f.set('tmp_fe20', c.binary('&', f.get('testf'), f.get('testm')))
    # tmp_FE08 = (tmp_FE30 = tmp_FE20)
    f.set('tmp_fe08', c.binary('=', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # tmp_FE50 = CBool((LSimValu > CSng(0.7)))
    f.set('tmp_fe50', c.builtin('cbool', [c.binary('>', f.get('lsimvalu'), c.builtin('csng', [0.7]))]))
    # tmp_FDC8 = (tmp_FE08 And tmp_FE50)
    f.set('tmp_fdc8', c.binary('and', f.get('tmp_fe08'), f.get('tmp_fe50')))
    # If tmp_FDC8 Then GoTo L1738 Else GoTo L1746
    return 493 if truth(f.get('tmp_fdc8')) else 494

def _namesimilarity_493(f, c):
    # LSimValu = CSng(0.8)
    f.set('lsimvalu', c.builtin('csng', [0.8]))
    return 494

def _namesimilarity_494(f, c):
    # If ((LSimValu = CDbl(1)) And (CSng(((LSimValu + FSimValu) / CDbl(2))) < CSng(0.84))) Then GoTo L176C Else GoTo L1839
    return 495 if truth(c.binary('and', c.binary('=', f.get('lsimvalu'), c.builtin('cdbl', [Integer(1)])), c.binary('<', c.builtin('csng', [c.binary('/', c.binary('+', f.get('lsimvalu'), f.get('fsimvalu')), c.builtin('cdbl', [Integer(2)]))]), c.builtin('csng', [0.84])))) else 516

def _namesimilarity_495(f, c):
    # tmp_FE30 = (RefMLen > 0)
    f.set('tmp_fe30', c.binary('>', f.get('refmlen'), Integer(0)))
    # tmp_FE20 = (TestMLen = 0)
    f.set('tmp_fe20', c.binary('=', f.get('testmlen'), Integer(0)))
    # tmp_FE08 = (tmp_FE30 And tmp_FE20)
    f.set('tmp_fe08', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # tmp_FDC8 = (RefMLen = 0)
    f.set('tmp_fdc8', c.binary('=', f.get('refmlen'), Integer(0)))
    # tmp_FDA8 = (TestMLen > 0)
    f.set('tmp_fda8', c.binary('>', f.get('testmlen'), Integer(0)))
    # tmp_FD98 = (tmp_FDC8 And tmp_FDA8)
    f.set('tmp_fd98', c.binary('and', f.get('tmp_fdc8'), f.get('tmp_fda8')))
    # tmp_FD78 = (tmp_FE08 Or tmp_FD98)
    f.set('tmp_fd78', c.binary('or', f.get('tmp_fe08'), f.get('tmp_fd98')))
    # If tmp_FD78 Then GoTo L17B3 Else GoTo L17C4
    return 503 if truth(f.get('tmp_fd78')) else 505

def _namesimilarity_503(f, c):
    # MSimValu = CSng(0.45)
    f.set('msimvalu', c.builtin('csng', [0.45]))
    # GoTo L1834
    return 515

def _namesimilarity_505(f, c):
    # tmp_FE30 = (RefMLen > 1)
    f.set('tmp_fe30', c.binary('>', f.get('refmlen'), Integer(1)))
    # tmp_FE20 = (TestMLen > 1)
    f.set('tmp_fe20', c.binary('>', f.get('testmlen'), Integer(1)))
    # tmp_FE08 = (tmp_FE30 And tmp_FE20)
    f.set('tmp_fe08', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # If tmp_FE08 Then GoTo L17EB Else GoTo L181C
    return 509 if truth(f.get('tmp_fe08')) else 513

def _namesimilarity_509(f, c):
    # If (MSimValu = CDbl(0)) Then GoTo L17F7 Else GoTo L1817
    return 510 if truth(c.binary('=', f.get('msimvalu'), c.builtin('cdbl', [Integer(0)]))) else 512

def _namesimilarity_510(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # MSimValu = CSng(IsSimilar(RefM, TestM, tmp_FD30))
    f.set('msimvalu', c.builtin('csng', [c.call('issimilar', [f.get('refm'), f.get('testm'), f.ref('tmp_fd30')])]))
    return 512

def _namesimilarity_512(f, c):
    # GoTo L1832
    return 515

def _namesimilarity_513(f, c):
    # If MFirstSameLetter Then GoTo L1824 Else GoTo L1832
    return 514 if truth(f.get('mfirstsameletter')) else 515

def _namesimilarity_514(f, c):
    # MSimValu = CSng(0.45)
    f.set('msimvalu', c.builtin('csng', [0.45]))
    return 515

def _namesimilarity_515(f, c):
    # GoTo L1977
    return 546

def _namesimilarity_516(f, c):
    # If (CSng(((LSimValu + FSimValu) / CDbl(2))) > CSng(0.85)) Then GoTo L1855 Else GoTo L1977
    return 517 if truth(c.binary('>', c.builtin('csng', [c.binary('/', c.binary('+', f.get('lsimvalu'), f.get('fsimvalu')), c.builtin('cdbl', [Integer(2)]))]), c.builtin('csng', [0.85]))) else 546

def _namesimilarity_517(f, c):
    # tmp_FE30 = (RefMLen > 0)
    f.set('tmp_fe30', c.binary('>', f.get('refmlen'), Integer(0)))
    # tmp_FE20 = (TestMLen = 0)
    f.set('tmp_fe20', c.binary('=', f.get('testmlen'), Integer(0)))
    # tmp_FE08 = (tmp_FE30 And tmp_FE20)
    f.set('tmp_fe08', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # tmp_FDC8 = (RefMLen = 0)
    f.set('tmp_fdc8', c.binary('=', f.get('refmlen'), Integer(0)))
    # tmp_FDA8 = (TestMLen > 0)
    f.set('tmp_fda8', c.binary('>', f.get('testmlen'), Integer(0)))
    # tmp_FD98 = (tmp_FDC8 And tmp_FDA8)
    f.set('tmp_fd98', c.binary('and', f.get('tmp_fdc8'), f.get('tmp_fda8')))
    # tmp_FD78 = (tmp_FE08 Or tmp_FD98)
    f.set('tmp_fd78', c.binary('or', f.get('tmp_fe08'), f.get('tmp_fd98')))
    # If tmp_FD78 Then GoTo L189C Else GoTo L18AD
    return 525 if truth(f.get('tmp_fd78')) else 527

def _namesimilarity_525(f, c):
    # MSimValu = CSng(0.5)
    f.set('msimvalu', c.builtin('csng', [0.5]))
    # GoTo L1975
    return 546

def _namesimilarity_527(f, c):
    # tmp_FE30 = (RefMLen > 1)
    f.set('tmp_fe30', c.binary('>', f.get('refmlen'), Integer(1)))
    # tmp_FE20 = (TestMLen > 1)
    f.set('tmp_fe20', c.binary('>', f.get('testmlen'), Integer(1)))
    # tmp_FE08 = (tmp_FE30 And tmp_FE20)
    f.set('tmp_fe08', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # If tmp_FE08 Then GoTo L18D4 Else GoTo L1905
    return 531 if truth(f.get('tmp_fe08')) else 535

def _namesimilarity_531(f, c):
    # If (MSimValu = CDbl(0)) Then GoTo L18E0 Else GoTo L1900
    return 532 if truth(c.binary('=', f.get('msimvalu'), c.builtin('cdbl', [Integer(0)]))) else 534

def _namesimilarity_532(f, c):
    # tmp_FD30 = CStr(0)
    f.set('tmp_fd30', c.builtin('cstr', [Integer(0)]))
    # MSimValu = CSng(IsSimilar(RefM, TestM, tmp_FD30))
    f.set('msimvalu', c.builtin('csng', [c.call('issimilar', [f.get('refm'), f.get('testm'), f.ref('tmp_fd30')])]))
    return 534

def _namesimilarity_534(f, c):
    # GoTo L1973
    return 546

def _namesimilarity_535(f, c):
    # If MFirstSameLetter Then GoTo L190D Else GoTo L191E
    return 536 if truth(f.get('mfirstsameletter')) else 538

def _namesimilarity_536(f, c):
    # MSimValu = CSng(0.5)
    f.set('msimvalu', c.builtin('csng', [0.5]))
    # GoTo L1973
    return 546

def _namesimilarity_538(f, c):
    # tmp_FE30 = (RefMLen = 1)
    f.set('tmp_fe30', c.binary('=', f.get('refmlen'), Integer(1)))
    # tmp_FE20 = (TestMLen = 1)
    f.set('tmp_fe20', c.binary('=', f.get('testmlen'), Integer(1)))
    # tmp_FE08 = (tmp_FE30 And tmp_FE20)
    f.set('tmp_fe08', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # If tmp_FE08 Then GoTo L1943 Else GoTo L1973
    return 542 if truth(f.get('tmp_fe08')) else 546

def _namesimilarity_542(f, c):
    # If (RefM = TestM) Then GoTo L1950 Else GoTo L1961
    return 543 if truth(c.binary('=', f.get('refm'), f.get('testm'))) else 545

def _namesimilarity_543(f, c):
    # MSimValu = CSng(0.75)
    f.set('msimvalu', c.builtin('csng', [0.75]))
    # GoTo L1971
    return 546

def _namesimilarity_545(f, c):
    # MSimValu = CSng(0.45)
    f.set('msimvalu', c.builtin('csng', [0.45]))
    return 546

def _namesimilarity_546(f, c):
    # tmp_FE30 = (RefL & RefF)
    f.set('tmp_fe30', c.binary('&', f.get('refl'), f.get('reff')))
    # tmp_FE20 = (TestL & TestF)
    f.set('tmp_fe20', c.binary('&', f.get('testl'), f.get('testf')))
    # If (tmp_FE30 = tmp_FE20) Then GoTo L199B Else GoTo L19A9
    return 549 if truth(c.binary('=', f.get('tmp_fe30'), f.get('tmp_fe20'))) else 550

def _namesimilarity_549(f, c):
    # MSimValu = CSng(0.55)
    f.set('msimvalu', c.builtin('csng', [0.55]))
    return 550

def _namesimilarity_550(f, c):
    # tmp_FE30 = (RefMLen = 0)
    f.set('tmp_fe30', c.binary('=', f.get('refmlen'), Integer(0)))
    # tmp_FE20 = (TestMLen = 0)
    f.set('tmp_fe20', c.binary('=', f.get('testmlen'), Integer(0)))
    # tmp_FE08 = (tmp_FE30 And tmp_FE20)
    f.set('tmp_fe08', c.binary('and', f.get('tmp_fe30'), f.get('tmp_fe20')))
    # If tmp_FE08 Then GoTo L19CE Else GoTo L19E1
    return 554 if truth(f.get('tmp_fe08')) else 556

def _namesimilarity_554(f, c):
    # SimScore = CSng(((LSimValu + FSimValu) / CDbl(2)))
    f.set('simscore', c.builtin('csng', [c.binary('/', c.binary('+', f.get('lsimvalu'), f.get('fsimvalu')), c.builtin('cdbl', [Integer(2)]))]))
    # GoTo L19F7
    return 557

def _namesimilarity_556(f, c):
    # SimScore = CSng((((LSimValu + FSimValu) + MSimValu) / CDbl(3)))
    f.set('simscore', c.builtin('csng', [c.binary('/', c.binary('+', c.binary('+', f.get('lsimvalu'), f.get('fsimvalu')), f.get('msimvalu')), c.builtin('cdbl', [Integer(3)]))]))
    return 557

def _namesimilarity_557(f, c):
    # If ((SimScore > CSng(0.77)) And (FullNameSimValu > CSng(0.78))) Then GoTo L1A1B Else GoTo L1A4F
    return 558 if truth(c.binary('and', c.binary('>', f.get('simscore'), c.builtin('csng', [0.77])), c.binary('>', f.get('fullnamesimvalu'), c.builtin('csng', [0.78])))) else 561

def _namesimilarity_558(f, c):
    # tmp_FE08 = Maximum(SimScore, FullNameSimValu)
    f.set('tmp_fe08', c.call('maximum', [f.ref('simscore'), f.ref('fullnamesimvalu')]))
    # NameSimilarity = CSng(CDbl(tmp_FE08))
    f.set('namesimilarity', c.builtin('csng', [c.builtin('cdbl', [f.get('tmp_fe08')])]))
    # GoTo L1A59
    return 562

def _namesimilarity_561(f, c):
    # NameSimilarity = CSng(SimScore)
    f.set('namesimilarity', c.builtin('csng', [f.get('simscore')]))
    return 562

def _namesimilarity_562(f, c):
    # Exit Function
    return None

def _namesimilarity_end(f, c):
    return None

_blocks_namesimilarity = {0: _namesimilarity_0, 2: _namesimilarity_2, 8: _namesimilarity_8, 10: _namesimilarity_10, 16: _namesimilarity_16, 18: _namesimilarity_18, 30: _namesimilarity_30, 32: _namesimilarity_32, 44: _namesimilarity_44, 101: _namesimilarity_101, 105: _namesimilarity_105, 112: _namesimilarity_112, 116: _namesimilarity_116, 120: _namesimilarity_120, 123: _namesimilarity_123, 125: _namesimilarity_125, 126: _namesimilarity_126, 129: _namesimilarity_129, 131: _namesimilarity_131, 132: _namesimilarity_132, 133: _namesimilarity_133, 135: _namesimilarity_135, 137: _namesimilarity_137, 138: _namesimilarity_138, 149: _namesimilarity_149, 151: _namesimilarity_151, 154: _namesimilarity_154, 155: _namesimilarity_155, 156: _namesimilarity_156, 160: _namesimilarity_160, 162: _namesimilarity_162, 166: _namesimilarity_166, 167: _namesimilarity_167, 168: _namesimilarity_168, 179: _namesimilarity_179, 181: _namesimilarity_181, 182: _namesimilarity_182, 187: _namesimilarity_187, 199: _namesimilarity_199, 208: _namesimilarity_208, 209: _namesimilarity_209, 210: _namesimilarity_210, 211: _namesimilarity_211, 213: _namesimilarity_213, 214: _namesimilarity_214, 215: _namesimilarity_215, 216: _namesimilarity_216, 219: _namesimilarity_219, 220: _namesimilarity_220, 221: _namesimilarity_221, 223: _namesimilarity_223, 224: _namesimilarity_224, 226: _namesimilarity_226, 227: _namesimilarity_227, 232: _namesimilarity_232, 244: _namesimilarity_244, 253: _namesimilarity_253, 254: _namesimilarity_254, 255: _namesimilarity_255, 256: _namesimilarity_256, 258: _namesimilarity_258, 259: _namesimilarity_259, 260: _namesimilarity_260, 261: _namesimilarity_261, 264: _namesimilarity_264, 265: _namesimilarity_265, 266: _namesimilarity_266, 268: _namesimilarity_268, 269: _namesimilarity_269, 271: _namesimilarity_271, 272: _namesimilarity_272, 273: _namesimilarity_273, 275: _namesimilarity_275, 283: _namesimilarity_283, 287: _namesimilarity_287, 288: _namesimilarity_288, 291: _namesimilarity_291, 292: _namesimilarity_292, 293: _namesimilarity_293, 294: _namesimilarity_294, 296: _namesimilarity_296, 297: _namesimilarity_297, 298: _namesimilarity_298, 304: _namesimilarity_304, 305: _namesimilarity_305, 313: _namesimilarity_313, 314: _namesimilarity_314, 316: _namesimilarity_316, 317: _namesimilarity_317, 321: _namesimilarity_321, 327: _namesimilarity_327, 333: _namesimilarity_333, 335: _namesimilarity_335, 336: _namesimilarity_336, 339: _namesimilarity_339, 341: _namesimilarity_341, 342: _namesimilarity_342, 345: _namesimilarity_345, 347: _namesimilarity_347, 351: _namesimilarity_351, 352: _namesimilarity_352, 354: _namesimilarity_354, 356: _namesimilarity_356, 357: _namesimilarity_357, 361: _namesimilarity_361, 362: _namesimilarity_362, 364: _namesimilarity_364, 366: _namesimilarity_366, 367: _namesimilarity_367, 368: _namesimilarity_368, 370: _namesimilarity_370, 378: _namesimilarity_378, 382: _namesimilarity_382, 390: _namesimilarity_390, 394: _namesimilarity_394, 395: _namesimilarity_395, 400: _namesimilarity_400, 402: _namesimilarity_402, 403: _namesimilarity_403, 411: _namesimilarity_411, 413: _namesimilarity_413, 414: _namesimilarity_414, 415: _namesimilarity_415, 419: _namesimilarity_419, 420: _namesimilarity_420, 421: _namesimilarity_421, 423: _namesimilarity_423, 429: _namesimilarity_429, 431: _namesimilarity_431, 432: _namesimilarity_432, 433: _namesimilarity_433, 436: _namesimilarity_436, 438: _namesimilarity_438, 439: _namesimilarity_439, 440: _namesimilarity_440, 443: _namesimilarity_443, 445: _namesimilarity_445, 446: _namesimilarity_446, 448: _namesimilarity_448, 451: _namesimilarity_451, 452: _namesimilarity_452, 453: _namesimilarity_453, 454: _namesimilarity_454, 455: _namesimilarity_455, 456: _namesimilarity_456, 457: _namesimilarity_457, 460: _namesimilarity_460, 464: _namesimilarity_464, 465: _namesimilarity_465, 466: _namesimilarity_466, 467: _namesimilarity_467, 468: _namesimilarity_468, 476: _namesimilarity_476, 477: _namesimilarity_477, 478: _namesimilarity_478, 479: _namesimilarity_479, 481: _namesimilarity_481, 482: _namesimilarity_482, 483: _namesimilarity_483, 487: _namesimilarity_487, 493: _namesimilarity_493, 494: _namesimilarity_494, 495: _namesimilarity_495, 503: _namesimilarity_503, 505: _namesimilarity_505, 509: _namesimilarity_509, 510: _namesimilarity_510, 512: _namesimilarity_512, 513: _namesimilarity_513, 514: _namesimilarity_514, 515: _namesimilarity_515, 516: _namesimilarity_516, 517: _namesimilarity_517, 525: _namesimilarity_525, 527: _namesimilarity_527, 531: _namesimilarity_531, 532: _namesimilarity_532, 534: _namesimilarity_534, 535: _namesimilarity_535, 536: _namesimilarity_536, 538: _namesimilarity_538, 542: _namesimilarity_542, 543: _namesimilarity_543, 545: _namesimilarity_545, 546: _namesimilarity_546, 549: _namesimilarity_549, 550: _namesimilarity_550, 554: _namesimilarity_554, 556: _namesimilarity_556, 557: _namesimilarity_557, 558: _namesimilarity_558, 561: _namesimilarity_561, 562: _namesimilarity_562, 563: _namesimilarity_end}
def vb_namesimilarity(c, arguments):
    return run(c, 'namesimilarity', [('refstr', 'variant', False, False, MISSING), ('teststr', 'variant', False, False, MISSING)], {'tmp_fd2c': 'string', 'tmp_fd30': 'string', 'tmp_fd36': 'integer', 'tmp_fd38': 'variant', 'tmp_fd48': 'variant', 'tmp_fd58': 'variant', 'tmp_fd78': 'variant', 'tmp_fd88': 'variant', 'tmp_fd98': 'variant', 'tmp_fda8': 'variant', 'tmp_fdc8': 'variant', 'tmp_fe08': 'variant', 'tmp_fe18': 'long', 'tmp_fe1c': 'long', 'tmp_fe20': 'variant', 'tmp_fe30': 'variant', 'tmp_fe50': 'variant', 'mfirstsameletter': 'boolean', 'ffirstsameletter': 'boolean', 'rf_in_tm': 'boolean', 'lastinmiddle': 'boolean', 'msimvalu': 'single', 'fsimvalu': 'single', 'lsimvalu': 'single', 'simscore': 'single', 'rm_in_tf': 'boolean', 'dashnamer': 'variant', 'dashnamel': 'variant', 'testmlen': 'variant', 'testflen': 'variant', 'testllen': 'variant', 'refmlen': 'variant', 'refflen': 'variant', 'refllen': 'variant', 'fullnamesimvalu': 'single', 'dashinboth': 'boolean', 'dashinone': 'boolean', 'dashname': 'variant', 'testm': 'variant', 'testf': 'variant', 'testl': 'variant', 'refm': 'variant', 'reff': 'variant', 'refl': 'variant'}, 'single', _blocks_namesimilarity, arguments)

def _lcs_0(f, c):
    # str1 = input_str1
    f.set('str1', f.get('input_str1'))
    # str2 = input_str2
    f.set('str2', f.get('input_str2'))
    # If IsMissing(AlgInUse) Then GoTo L001B Else GoTo L0026
    return 3 if truth(c.builtin('ismissing', [f.get('alginuse')])) else 4

def _lcs_3(f, c):
    # AlgInUse = ""
    f.set('alginuse', '')
    return 4

def _lcs_4(f, c):
    # Str1Len = CInt(CInt(UBound(str1, 1)))
    f.set('str1len', c.builtin('cint', [c.builtin('cint', [c.builtin('ubound', [f.get('str1'), Integer(1)])])]))
    # Str2Len = CInt(CInt(UBound(str2, 1)))
    f.set('str2len', c.builtin('cint', [c.builtin('cint', [c.builtin('ubound', [f.get('str2'), Integer(1)])])]))
    # tmp_FEC4 = Minimum(Str1Len, Str2Len)
    f.set('tmp_fec4', c.call('minimum', [f.ref('str1len'), f.ref('str2len')]))
    # n = CInt(CInt(tmp_FEC4))
    f.set('n', c.builtin('cint', [c.builtin('cint', [f.get('tmp_fec4')])]))
    # tmp_FEC4 = Maximum(Str1Len, Str2Len)
    f.set('tmp_fec4', c.call('maximum', [f.ref('str1len'), f.ref('str2len')]))
    # m = CInt(CInt(tmp_FEC4))
    f.set('m', c.builtin('cint', [c.builtin('cint', [f.get('tmp_fec4')])]))
    # ReDim X(0 To CLng(m))
    f.redim('x', [(Integer(0), c.builtin('clng', [f.get('m')]))], False, 'string')
    # ReDim Y(0 To CLng(m))
    f.redim('y', [(Integer(0), c.builtin('clng', [f.get('m')]))], False, 'string')
    # ReDim c(0 To CLng(m), 0 To CLng(m))
    f.redim('c', [(Integer(0), c.builtin('clng', [f.get('m')])), (Integer(0), c.builtin('clng', [f.get('m')]))], False, 'integer')
    # ReDim B(0 To CLng(m), 0 To CLng(m))
    f.redim('b', [(Integer(0), c.builtin('clng', [f.get('m')])), (Integer(0), c.builtin('clng', [f.get('m')]))], False, 'integer')
    # If (Str1Len > Str2Len) Then GoTo L0124 Else GoTo L01A9
    return 15 if truth(c.binary('>', f.get('str1len'), f.get('str2len'))) else 26

def _lcs_15(f, c):
    # For i = 0 To (Str1Len - 1)
    return 16 if f.begin_loop(15, 'i', Integer(0), c.binary('-', f.get('str1len'), Integer(1)), Integer(1)) else 20

def _lcs_16(f, c):
    # tmp_FEF4 = str1(i)
    f.set('tmp_fef4', f.index('str1', f.get('i')))
    # tmp_FEBC = CStr(CStr(tmp_FEF4))
    f.set('tmp_febc', c.builtin('cstr', [c.builtin('cstr', [f.get('tmp_fef4')])]))
    # X(CLng(i)) = tmp_FEBC
    f.put('x', [c.builtin('clng', [f.get('i')])], f.get('tmp_febc'))
    # Next i
    return 16 if f.next_loop(15) else 20

def _lcs_20(f, c):
    # For i = 0 To (Str2Len - 1)
    return 21 if f.begin_loop(20, 'i', Integer(0), c.binary('-', f.get('str2len'), Integer(1)), Integer(1)) else 25

def _lcs_21(f, c):
    # tmp_FEF4 = str2(i)
    f.set('tmp_fef4', f.index('str2', f.get('i')))
    # tmp_FEBC = CStr(CStr(tmp_FEF4))
    f.set('tmp_febc', c.builtin('cstr', [c.builtin('cstr', [f.get('tmp_fef4')])]))
    # Y(CLng(i)) = tmp_FEBC
    f.put('y', [c.builtin('clng', [f.get('i')])], f.get('tmp_febc'))
    # Next i
    return 21 if f.next_loop(20) else 25

def _lcs_25(f, c):
    # GoTo L022D
    return 36

def _lcs_26(f, c):
    # For i = 0 To (Str2Len - 1)
    return 27 if f.begin_loop(26, 'i', Integer(0), c.binary('-', f.get('str2len'), Integer(1)), Integer(1)) else 31

def _lcs_27(f, c):
    # tmp_FEF4 = str2(i)
    f.set('tmp_fef4', f.index('str2', f.get('i')))
    # tmp_FEBC = CStr(CStr(tmp_FEF4))
    f.set('tmp_febc', c.builtin('cstr', [c.builtin('cstr', [f.get('tmp_fef4')])]))
    # X(CLng(i)) = tmp_FEBC
    f.put('x', [c.builtin('clng', [f.get('i')])], f.get('tmp_febc'))
    # Next i
    return 27 if f.next_loop(26) else 31

def _lcs_31(f, c):
    # For i = 0 To (Str1Len - 1)
    return 32 if f.begin_loop(31, 'i', Integer(0), c.binary('-', f.get('str1len'), Integer(1)), Integer(1)) else 36

def _lcs_32(f, c):
    # tmp_FEF4 = str1(i)
    f.set('tmp_fef4', f.index('str1', f.get('i')))
    # tmp_FEBC = CStr(CStr(tmp_FEF4))
    f.set('tmp_febc', c.builtin('cstr', [c.builtin('cstr', [f.get('tmp_fef4')])]))
    # Y(CLng(i)) = tmp_FEBC
    f.put('y', [c.builtin('clng', [f.get('i')])], f.get('tmp_febc'))
    # Next i
    return 32 if f.next_loop(31) else 36

def _lcs_36(f, c):
    # For i = 1 To m
    return 37 if f.begin_loop(36, 'i', Integer(1), f.get('m'), Integer(1)) else 50

def _lcs_37(f, c):
    # For j = 1 To n
    return 38 if f.begin_loop(37, 'j', Integer(1), f.get('n'), Integer(1)) else 49

def _lcs_38(f, c):
    # If (X(CLng((i - 1))) = Y(CLng((j - 1)))) Then GoTo L026C Else GoTo L02B1
    return 39 if truth(c.binary('=', f.index('x', c.builtin('clng', [c.binary('-', f.get('i'), Integer(1))])), f.index('y', c.builtin('clng', [c.binary('-', f.get('j'), Integer(1))])))) else 42

def _lcs_39(f, c):
    # c(CLng(i), CLng(j)) = CInt((c(CLng((i - 1)), CLng((j - 1))) + 1))
    f.put('c', [c.builtin('clng', [f.get('i')]), c.builtin('clng', [f.get('j')])], c.builtin('cint', [c.binary('+', f.index('c', c.builtin('clng', [c.binary('-', f.get('i'), Integer(1))]), c.builtin('clng', [c.binary('-', f.get('j'), Integer(1))])), Integer(1))]))
    # B(CLng(i), CLng(j)) = CInt(1)
    f.put('b', [c.builtin('clng', [f.get('i')]), c.builtin('clng', [f.get('j')])], c.builtin('cint', [Integer(1)]))
    # GoTo L035C
    return 48

def _lcs_42(f, c):
    # If (c(CLng((i - 1)), CLng(j)) >= c(CLng(i), CLng((j - 1)))) Then GoTo L02DF Else GoTo L031E
    return 43 if truth(c.binary('>=', f.index('c', c.builtin('clng', [c.binary('-', f.get('i'), Integer(1))]), c.builtin('clng', [f.get('j')])), f.index('c', c.builtin('clng', [f.get('i')]), c.builtin('clng', [c.binary('-', f.get('j'), Integer(1))])))) else 46

def _lcs_43(f, c):
    # c(CLng(i), CLng(j)) = CInt(c(CLng((i - 1)), CLng(j)))
    f.put('c', [c.builtin('clng', [f.get('i')]), c.builtin('clng', [f.get('j')])], c.builtin('cint', [f.index('c', c.builtin('clng', [c.binary('-', f.get('i'), Integer(1))]), c.builtin('clng', [f.get('j')]))]))
    # B(CLng(i), CLng(j)) = CInt(2)
    f.put('b', [c.builtin('clng', [f.get('i')]), c.builtin('clng', [f.get('j')])], c.builtin('cint', [Integer(2)]))
    # GoTo L035C
    return 48

def _lcs_46(f, c):
    # c(CLng(i), CLng(j)) = CInt(c(CLng(i), CLng((j - 1))))
    f.put('c', [c.builtin('clng', [f.get('i')]), c.builtin('clng', [f.get('j')])], c.builtin('cint', [f.index('c', c.builtin('clng', [f.get('i')]), c.builtin('clng', [c.binary('-', f.get('j'), Integer(1))]))]))
    # B(CLng(i), CLng(j)) = CInt(3)
    f.put('b', [c.builtin('clng', [f.get('i')]), c.builtin('clng', [f.get('j')])], c.builtin('cint', [Integer(3)]))
    return 48

def _lcs_48(f, c):
    # Next j
    return 38 if f.next_loop(37) else 49

def _lcs_49(f, c):
    # Next i
    return 37 if f.next_loop(36) else 50

def _lcs_50(f, c):
    # If (c(CLng(m), CLng(n)) > 0) Then GoTo L038B Else GoTo L042C
    return 51 if truth(c.binary('>', f.index('c', c.builtin('clng', [f.get('m')]), c.builtin('clng', [f.get('n')])), Integer(0))) else 62

def _lcs_51(f, c):
    # tmp_FEF4 = (AlgInUse = "Dmph")
    f.set('tmp_fef4', c.binary('=', f.get('alginuse'), 'Dmph'))
    # tmp_FED4 = (AlgInUse = "SSLCS")
    f.set('tmp_fed4', c.binary('=', f.get('alginuse'), 'SSLCS'))
    # tmp_FEC4 = (tmp_FEF4 Or tmp_FED4)
    f.set('tmp_fec4', c.binary('or', f.get('tmp_fef4'), f.get('tmp_fed4')))
    # If tmp_FEC4 Then GoTo L03B6 Else GoTo L03D0
    return 55 if truth(f.get('tmp_fec4')) else 57

def _lcs_55(f, c):
    # LCS = CSng(CDbl(c(CLng(m), CLng(n))))
    f.set('lcs', c.builtin('csng', [c.builtin('cdbl', [f.index('c', c.builtin('clng', [f.get('m')]), c.builtin('clng', [f.get('n')]))])]))
    # GoTo L0427
    return 61

def _lcs_57(f, c):
    # tmp_FED4 = "#.##"
    f.set('tmp_fed4', '#.##')
    # tmp_FEF4 = CDbl((CDbl(c(CLng(m), CLng(n))) / (CDbl((Str1Len + Str2Len)) / CDbl(2))))
    f.set('tmp_fef4', c.builtin('cdbl', [c.binary('/', c.builtin('cdbl', [f.index('c', c.builtin('clng', [f.get('m')]), c.builtin('clng', [f.get('n')]))]), c.binary('/', c.builtin('cdbl', [c.binary('+', f.get('str1len'), f.get('str2len'))]), c.builtin('cdbl', [Integer(2)])))]))
    # tmp_FEC4 = Format(tmp_FEF4, tmp_FED4, 1, 1)
    f.set('tmp_fec4', c.builtin('format', [f.get('tmp_fef4'), f.get('tmp_fed4'), Integer(1), Integer(1)]))
    # LCS = CSng(CSng(tmp_FEC4))
    f.set('lcs', c.builtin('csng', [c.builtin('csng', [f.get('tmp_fec4')])]))
    return 61

def _lcs_61(f, c):
    # GoTo L0436
    return 63

def _lcs_62(f, c):
    # LCS = CSng(CDbl(0))
    f.set('lcs', c.builtin('csng', [c.builtin('cdbl', [Integer(0)])]))
    return 63

def _lcs_63(f, c):
    # Erase X
    f.ref('x').value = EMPTY
    # Erase Y
    f.ref('y').value = EMPTY
    # Erase c
    f.ref('c').value = EMPTY
    # Erase B
    f.ref('b').value = EMPTY
    # Exit Function
    return None

def _lcs_end(f, c):
    return None

_blocks_lcs = {0: _lcs_0, 3: _lcs_3, 4: _lcs_4, 15: _lcs_15, 16: _lcs_16, 20: _lcs_20, 21: _lcs_21, 25: _lcs_25, 26: _lcs_26, 27: _lcs_27, 31: _lcs_31, 32: _lcs_32, 36: _lcs_36, 37: _lcs_37, 38: _lcs_38, 39: _lcs_39, 42: _lcs_42, 43: _lcs_43, 46: _lcs_46, 48: _lcs_48, 49: _lcs_49, 50: _lcs_50, 51: _lcs_51, 55: _lcs_55, 57: _lcs_57, 61: _lcs_61, 62: _lcs_62, 63: _lcs_63, 68: _lcs_end}
def vb_lcs(c, arguments):
    return run(c, 'lcs', [('input_str1', 'variant', True, False, MISSING), ('input_str2', 'variant', True, False, MISSING), ('alginuse', 'variant', False, True, MISSING)], {'tmp_febc': 'string', 'tmp_fec4': 'variant', 'tmp_fed4': 'variant', 'tmp_fef4': 'variant', 'str2len': 'integer', 'str1len': 'integer', 'y': 'variant', 'x': 'variant', 'b': 'variant', 'c': 'variant', 'n': 'integer', 'm': 'integer', 'j': 'integer', 'i': 'integer', 'str2': 'variant', 'str1': 'variant'}, 'single', _blocks_lcs, arguments)

def _doublemetaphone_0(f, c):
    # pWord = input_pWord
    f.set('pword', f.get('input_pword'))
    # cache_m8_0004 = ""
    f.set('cache_m8_0004', '')
    # cache_m8_0014 = ""
    f.set('cache_m8_0014', '')
    # SIGNIFICANTCHARS = CInt(4)
    f.set('significantchars', c.builtin('cint', [Integer(4)]))
    # nLength = CInt(CInt(UBound(pWord, 1)))
    f.set('nlength', c.builtin('cint', [c.builtin('cint', [c.builtin('ubound', [f.get('pword'), Integer(1)])])]))
    # nLast = CInt(nLength)
    f.set('nlast', c.builtin('cint', [f.get('nlength')]))
    # tmp_FF28 = " "
    f.set('tmp_ff28', ' ')
    # tmp_FF3A = 5
    f.set('tmp_ff3a', Integer(5))
    # Call RApad(pWord, tmp_FF3A, tmp_FF28)
    c.call('rapad', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')])
    # ReDim tmp_FF24(0 To 4)
    f.redim('tmp_ff24', [(Integer(0), Integer(4))], False, 'variant')
    # tmp_FF24(0) = "GN"
    f.put('tmp_ff24', [Integer(0)], 'GN')
    # tmp_FF24(1) = "KN"
    f.put('tmp_ff24', [Integer(1)], 'KN')
    # tmp_FF24(2) = "PN"
    f.put('tmp_ff24', [Integer(2)], 'PN')
    # tmp_FF24(3) = "WR"
    f.put('tmp_ff24', [Integer(3)], 'WR')
    # tmp_FF24(4) = "PS"
    f.put('tmp_ff24', [Integer(4)], 'PS')
    # tmp_FF28 = VBA.Array("GN", "KN", "PN", "WR", "PS")
    f.set('tmp_ff28', c.builtin('vba.array', ['GN', 'KN', 'PN', 'WR', 'PS']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = 0
    f.set('tmp_ff3a', Integer(0))
    # If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L00E7 Else GoTo L00F2
    return 19 if truth(c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')])) else 20

def _doublemetaphone_19(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 20

def _doublemetaphone_20(f, c):
    # tmp_FF28 = pWord(0)
    f.set('tmp_ff28', f.index('pword', Integer(0)))
    # If (tmp_FF28 = "X") Then GoTo L0113 Else GoTo L013A
    return 22 if truth(c.binary('=', f.get('tmp_ff28'), 'X')) else 25

def _doublemetaphone_22(f, c):
    # tmp_FF28 = "S"
    f.set('tmp_ff28', 'S')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 25

def _doublemetaphone_25(f, c):
    # tmp_FF28 = Len(cache_m8_0004)
    f.set('tmp_ff28', c.builtin('len', [f.get('cache_m8_0004')]))
    # tmp_FED4 = (tmp_FF28 < 4)
    f.set('tmp_fed4', c.binary('<', f.get('tmp_ff28'), Integer(4)))
    # tmp_FEC4 = (True Or tmp_FED4)
    f.set('tmp_fec4', c.binary('or', True, f.get('tmp_fed4')))
    # tmp_FEB4 = Len(cache_m8_0014)
    f.set('tmp_feb4', c.builtin('len', [f.get('cache_m8_0014')]))
    # tmp_FEA4 = (tmp_FEB4 < 4)
    f.set('tmp_fea4', c.binary('<', f.get('tmp_feb4'), Integer(4)))
    # tmp_FE94 = (tmp_FEC4 Or tmp_FEA4)
    f.set('tmp_fe94', c.binary('or', f.get('tmp_fec4'), f.get('tmp_fea4')))
    # If tmp_FE94 Then GoTo L0174 Else GoTo L3CD8
    return 32 if truth(f.get('tmp_fe94')) else 1321

def _doublemetaphone_32(f, c):
    # PreviousFlag = CInt(0)
    f.set('previousflag', c.builtin('cint', [Integer(0)]))
    # PreviousFlag2 = CInt(0)
    f.set('previousflag2', c.builtin('cint', [Integer(0)]))
    # If (nCurrent > nLength) Then GoTo L018E Else GoTo L0193
    return 35 if truth(c.binary('>', f.get('ncurrent'), f.get('nlength'))) else 36

def _doublemetaphone_35(f, c):
    # GoTo L3CD8
    return 1321

def _doublemetaphone_36(f, c):
    # tmp_FF28 = pWord(nCurrent)
    f.set('tmp_ff28', f.index('pword', f.get('ncurrent')))
    # sLetter = tmp_FF28
    f.set('sletter', f.get('tmp_ff28'))
    # tmp_FE84 = sLetter
    f.set('tmp_fe84', f.get('sletter'))
    # If (tmp_FE84 = "A") Then GoTo L020A Else GoTo L01C4
    return 45 if truth(c.binary('=', f.get('tmp_fe84'), 'A')) else 40

def _doublemetaphone_40(f, c):
    # If (tmp_FE84 = "E") Then GoTo L020A Else GoTo L01D2
    return 45 if truth(c.binary('=', f.get('tmp_fe84'), 'E')) else 41

def _doublemetaphone_41(f, c):
    # If (tmp_FE84 = "I") Then GoTo L020A Else GoTo L01E0
    return 45 if truth(c.binary('=', f.get('tmp_fe84'), 'I')) else 42

def _doublemetaphone_42(f, c):
    # If (tmp_FE84 = "O") Then GoTo L020A Else GoTo L01EE
    return 45 if truth(c.binary('=', f.get('tmp_fe84'), 'O')) else 43

def _doublemetaphone_43(f, c):
    # If (tmp_FE84 = "U") Then GoTo L020A Else GoTo L01FC
    return 45 if truth(c.binary('=', f.get('tmp_fe84'), 'U')) else 44

def _doublemetaphone_44(f, c):
    # If (tmp_FE84 = "Y") Then GoTo L020A Else GoTo L0241
    return 45 if truth(c.binary('=', f.get('tmp_fe84'), 'Y')) else 50

def _doublemetaphone_45(f, c):
    # If (nCurrent = 0) Then GoTo L0215 Else GoTo L0231
    return 46 if truth(c.binary('=', f.get('ncurrent'), Integer(0))) else 48

def _doublemetaphone_46(f, c):
    # tmp_FF28 = "A"
    f.set('tmp_ff28', 'A')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 48

def _doublemetaphone_48(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # GoTo L3CD1
    return 1320

def _doublemetaphone_50(f, c):
    # If (tmp_FE84 = "B") Then GoTo L0251 Else GoTo L02F4
    return 51 if truth(c.binary('=', f.get('tmp_fe84'), 'B')) else 67

def _doublemetaphone_51(f, c):
    # If (nCurrent > 0) Then GoTo L025C Else GoTo L0283
    return 52 if truth(c.binary('>', f.get('ncurrent'), Integer(0))) else 56

def _doublemetaphone_52(f, c):
    # tmp_FF3C = CInt((nCurrent - 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('-', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 = "M")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'M'))
    # PreviousFlag = CInt(CBool(tmp_FED4))
    f.set('previousflag', c.builtin('cint', [c.builtin('cbool', [f.get('tmp_fed4')])]))
    return 56

def _doublemetaphone_56(f, c):
    # tmp_FF04 = CBool(PreviousFlag)
    f.set('tmp_ff04', c.builtin('cbool', [f.get('previousflag')]))
    # tmp_FF28 = pWord(nCurrent)
    f.set('tmp_ff28', f.index('pword', f.get('ncurrent')))
    # tmp_FED4 = (tmp_FF28 = "B")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'B'))
    # tmp_FEC4 = (tmp_FF04 And tmp_FED4)
    f.set('tmp_fec4', c.binary('and', f.get('tmp_ff04'), f.get('tmp_fed4')))
    # If tmp_FEC4 Then GoTo L02B8 Else GoTo L02C6
    return 61 if truth(f.get('tmp_fec4')) else 63

def _doublemetaphone_61(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L02EF
    return 66

def _doublemetaphone_63(f, c):
    # tmp_FF28 = "B"
    f.set('tmp_ff28', 'B')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 66

def _doublemetaphone_66(f, c):
    # GoTo L3CD1
    return 1320

def _doublemetaphone_67(f, c):
    # If (tmp_FE84 = "Ç") Then GoTo L0304 Else GoTo L032E
    return 68 if truth(c.binary('=', f.get('tmp_fe84'), 'Ç')) else 72

def _doublemetaphone_68(f, c):
    # tmp_FF28 = "S"
    f.set('tmp_ff28', 'S')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # GoTo L3CD1
    return 1320

def _doublemetaphone_72(f, c):
    # If (tmp_FE84 = "C") Then GoTo L033E Else GoTo L1208
    return 73 if truth(c.binary('=', f.get('tmp_fe84'), 'C')) else 367

def _doublemetaphone_73(f, c):
    # tmp_FF04 = CBool((nCurrent > 0))
    f.set('tmp_ff04', c.builtin('cbool', [c.binary('>', f.get('ncurrent'), Integer(0))]))
    # tmp_FF28 = pWord(nCurrent)
    f.set('tmp_ff28', f.index('pword', f.get('ncurrent')))
    # tmp_FED4 = (tmp_FF28 Like "[aeiouy]")
    f.set('tmp_fed4', c.binary('like', f.get('tmp_ff28'), '[aeiouy]'))
    # tmp_FEC4 = (Not tmp_FED4)
    f.set('tmp_fec4', c.unary('not', f.get('tmp_fed4')))
    # tmp_FEB4 = (tmp_FF04 And tmp_FEC4)
    f.set('tmp_feb4', c.binary('and', f.get('tmp_ff04'), f.get('tmp_fec4')))
    # ReDim tmp_FF24(0 To 0)
    f.redim('tmp_ff24', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FF24(0) = "ACH"
    f.put('tmp_ff24', [Integer(0)], 'ACH')
    # tmp_FEA4 = VBA.Array("ACH")
    f.set('tmp_fea4', c.builtin('vba.array', ['ACH']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FEE4 = CBool(IsInArry(pWord, nCurrent, tmp_FEA4))
    f.set('tmp_fee4', c.builtin('cbool', [c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_fea4')])]))
    # tmp_FE94 = (tmp_FEB4 And tmp_FEE4)
    f.set('tmp_fe94', c.binary('and', f.get('tmp_feb4'), f.get('tmp_fee4')))
    # tmp_FE54 = pWord(nCurrent)
    f.set('tmp_fe54', f.index('pword', f.get('ncurrent')))
    # tmp_FE44 = (tmp_FE54 <> "I")
    f.set('tmp_fe44', c.binary('<>', f.get('tmp_fe54'), 'I'))
    # tmp_FE34 = (tmp_FE94 And tmp_FE44)
    f.set('tmp_fe34', c.binary('and', f.get('tmp_fe94'), f.get('tmp_fe44')))
    # tmp_FE24 = CInt((nCurrent + 2))
    f.set('tmp_fe24', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # tmp_FDF4 = pWord(tmp_FE24)
    f.set('tmp_fdf4', f.index('pword', f.get('tmp_fe24')))
    # tmp_FDE4 = (tmp_FDF4 <> "E")
    f.set('tmp_fde4', c.binary('<>', f.get('tmp_fdf4'), 'E'))
    # ReDim tmp_FDE0(0 To 1)
    f.redim('tmp_fde0', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FDE0(0) = "BACHER"
    f.put('tmp_fde0', [Integer(0)], 'BACHER')
    # tmp_FDE0(1) = "MACHER"
    f.put('tmp_fde0', [Integer(1)], 'MACHER')
    # tmp_FDB0 = VBA.Array("BACHER", "MACHER")
    f.set('tmp_fdb0', c.builtin('vba.array', ['BACHER', 'MACHER']))
    # Erase tmp_FDE0
    f.ref('tmp_fde0').value = EMPTY
    # tmp_FDA0 = CBool(IsInArry(pWord, nCurrent, tmp_FDB0))
    f.set('tmp_fda0', c.builtin('cbool', [c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_fdb0')])]))
    # tmp_FD90 = (tmp_FDE4 Or tmp_FDA0)
    f.set('tmp_fd90', c.binary('or', f.get('tmp_fde4'), f.get('tmp_fda0')))
    # tmp_FD80 = (tmp_FE34 And tmp_FD90)
    f.set('tmp_fd80', c.binary('and', f.get('tmp_fe34'), f.get('tmp_fd90')))
    # If tmp_FD80 Then GoTo L0467 Else GoTo L0493
    return 99 if truth(f.get('tmp_fd80')) else 103

def _doublemetaphone_99(f, c):
    # tmp_FF28 = "K"
    f.set('tmp_ff28', 'K')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_103(f, c):
    # ReDim tmp_FF24(0 To 0)
    f.redim('tmp_ff24', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FF24(0) = "CAESAR"
    f.put('tmp_ff24', [Integer(0)], 'CAESAR')
    # tmp_FF28 = VBA.Array("CAESAR")
    f.set('tmp_ff28', c.builtin('vba.array', ['CAESAR']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # If ((nCurrent = 0) And IsInArry(pWord, nCurrent, tmp_FF28)) Then GoTo L04E7 Else GoTo L0513
    return 108 if truth(c.binary('and', c.binary('=', f.get('ncurrent'), Integer(0)), c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')]))) else 112

def _doublemetaphone_108(f, c):
    # tmp_FF28 = "S"
    f.set('tmp_ff28', 'S')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_112(f, c):
    # ReDim tmp_FF24(0 To 0)
    f.redim('tmp_ff24', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FF24(0) = "CHIA"
    f.put('tmp_ff24', [Integer(0)], 'CHIA')
    # tmp_FF28 = VBA.Array("CHIA")
    f.set('tmp_ff28', c.builtin('vba.array', ['CHIA']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # If IsInArry(pWord, nCurrent, tmp_FF28) Then GoTo L0560 Else GoTo L058C
    return 117 if truth(c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')])) else 121

def _doublemetaphone_117(f, c):
    # tmp_FF28 = "K"
    f.set('tmp_ff28', 'K')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_121(f, c):
    # tmp_FF28 = pWord(nCurrent)
    f.set('tmp_ff28', f.index('pword', f.get('ncurrent')))
    # tmp_FED4 = (tmp_FF28 = "C")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'C'))
    # tmp_FF04 = CInt((nCurrent + 1))
    f.set('tmp_ff04', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FEC4 = pWord(tmp_FF04)
    f.set('tmp_fec4', f.index('pword', f.get('tmp_ff04')))
    # tmp_FEB4 = (tmp_FEC4 = "H")
    f.set('tmp_feb4', c.binary('=', f.get('tmp_fec4'), 'H'))
    # tmp_FEA4 = (tmp_FED4 And tmp_FEB4)
    f.set('tmp_fea4', c.binary('and', f.get('tmp_fed4'), f.get('tmp_feb4')))
    # If tmp_FEA4 Then GoTo L05D7 Else GoTo L0B60
    return 128 if truth(f.get('tmp_fea4')) else 228

def _doublemetaphone_128(f, c):
    # ReDim tmp_FF24(0 To 0)
    f.redim('tmp_ff24', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FF24(0) = "CHAE"
    f.put('tmp_ff24', [Integer(0)], 'CHAE')
    # tmp_FF28 = VBA.Array("CHAE")
    f.set('tmp_ff28', c.builtin('vba.array', ['CHAE']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # If ((nCurrent > 0) And IsInArry(pWord, nCurrent, tmp_FF28)) Then GoTo L0629 Else GoTo L065D
    return 133 if truth(c.binary('and', c.binary('>', f.get('ncurrent'), Integer(0)), c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')]))) else 138

def _doublemetaphone_133(f, c):
    # tmp_FED4 = "X"
    f.set('tmp_fed4', 'X')
    # tmp_FF28 = "K"
    f.set('tmp_ff28', 'K')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_138(f, c):
    # ReDim tmp_FF24(0 To 1)
    f.redim('tmp_ff24', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FF24(0) = "HARAC"
    f.put('tmp_ff24', [Integer(0)], 'HARAC')
    # tmp_FF24(1) = "HARIS"
    f.put('tmp_ff24', [Integer(1)], 'HARIS')
    # tmp_FF28 = VBA.Array("HARAC", "HARIS")
    f.set('tmp_ff28', c.builtin('vba.array', ['HARAC', 'HARIS']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # ReDim tmp_FDE0(0 To 3)
    f.redim('tmp_fde0', [(Integer(0), Integer(3))], False, 'variant')
    # tmp_FDE0(0) = "HOR"
    f.put('tmp_fde0', [Integer(0)], 'HOR')
    # tmp_FDE0(1) = "HYM"
    f.put('tmp_fde0', [Integer(1)], 'HYM')
    # tmp_FDE0(2) = "HIA"
    f.put('tmp_fde0', [Integer(2)], 'HIA')
    # tmp_FDE0(3) = "HEM"
    f.put('tmp_fde0', [Integer(3)], 'HEM')
    # tmp_FED4 = VBA.Array("HOR", "HYM", "HIA", "HEM")
    f.set('tmp_fed4', c.builtin('vba.array', ['HOR', 'HYM', 'HIA', 'HEM']))
    # Erase tmp_FDE0
    f.ref('tmp_fde0').value = EMPTY
    # ReDim tmp_FD7C(0 To 0)
    f.redim('tmp_fd7c', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FD7C(0) = "CHORE"
    f.put('tmp_fd7c', [Integer(0)], 'CHORE')
    # tmp_FEC4 = VBA.Array("CHORE")
    f.set('tmp_fec4', c.builtin('vba.array', ['CHORE']))
    # Erase tmp_FD7C
    f.ref('tmp_fd7c').value = EMPTY
    # tmp_FF3A = 0
    f.set('tmp_ff3a', Integer(0))
    # If (((nCurrent = 0) And (IsInArry(pWord, nCurrent, tmp_FF28) Or IsInArry(pWord, nCurrent, tmp_FED4))) And (Not IsInArry(pWord, tmp_FF3A, tmp_FEC4))) Then GoTo L077E Else GoTo L07AA
    return 156 if truth(c.binary('and', c.binary('and', c.binary('=', f.get('ncurrent'), Integer(0)), c.binary('or', c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')]), c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_fed4')]))), c.unary('not', c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_fec4')])))) else 160

def _doublemetaphone_156(f, c):
    # tmp_FF28 = "K"
    f.set('tmp_ff28', 'K')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_160(f, c):
    # If (nCurrent > 0) Then GoTo L07B7 Else GoTo L0835
    return 161 if truth(c.binary('>', f.get('ncurrent'), Integer(0))) else 170

def _doublemetaphone_161(f, c):
    # ReDim tmp_FF24(0 To 3)
    f.redim('tmp_ff24', [(Integer(0), Integer(3))], False, 'variant')
    # tmp_FF24(0) = "A"
    f.put('tmp_ff24', [Integer(0)], 'A')
    # tmp_FF24(1) = "O"
    f.put('tmp_ff24', [Integer(1)], 'O')
    # tmp_FF24(2) = "U"
    f.put('tmp_ff24', [Integer(2)], 'U')
    # tmp_FF24(3) = "E"
    f.put('tmp_ff24', [Integer(3)], 'E')
    # tmp_FF28 = VBA.Array("A", "O", "U", "E")
    f.set('tmp_ff28', c.builtin('vba.array', ['A', 'O', 'U', 'E']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = (nCurrent - 1)
    f.set('tmp_ff3a', c.binary('-', f.get('ncurrent'), Integer(1)))
    # PreviousFlag = CInt(IsInArry(pWord, tmp_FF3A, tmp_FF28))
    f.set('previousflag', c.builtin('cint', [c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')])]))
    return 170

def _doublemetaphone_170(f, c):
    # ReDim tmp_FF24(0 To 1)
    f.redim('tmp_ff24', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FF24(0) = "VAN "
    f.put('tmp_ff24', [Integer(0)], 'VAN ')
    # tmp_FF24(1) = "VON "
    f.put('tmp_ff24', [Integer(1)], 'VON ')
    # tmp_FF28 = VBA.Array("VAN ", "VON ")
    f.set('tmp_ff28', c.builtin('vba.array', ['VAN ', 'VON ']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = 0
    f.set('tmp_ff3a', Integer(0))
    # ReDim tmp_FDE0(0 To 0)
    f.redim('tmp_fde0', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FDE0(0) = "SCH"
    f.put('tmp_fde0', [Integer(0)], 'SCH')
    # tmp_FED4 = VBA.Array("SCH")
    f.set('tmp_fed4', c.builtin('vba.array', ['SCH']))
    # Erase tmp_FDE0
    f.ref('tmp_fde0').value = EMPTY
    # tmp_FD7A = 0
    f.set('tmp_fd7a', Integer(0))
    # ReDim tmp_FD7C(0 To 2)
    f.redim('tmp_fd7c', [(Integer(0), Integer(2))], False, 'variant')
    # tmp_FD7C(0) = "ORCHES"
    f.put('tmp_fd7c', [Integer(0)], 'ORCHES')
    # tmp_FD7C(1) = "ARCHIT"
    f.put('tmp_fd7c', [Integer(1)], 'ARCHIT')
    # tmp_FD7C(2) = "ORCHID"
    f.put('tmp_fd7c', [Integer(2)], 'ORCHID')
    # tmp_FEC4 = VBA.Array("ORCHES", "ARCHIT", "ORCHID")
    f.set('tmp_fec4', c.builtin('vba.array', ['ORCHES', 'ARCHIT', 'ORCHID']))
    # Erase tmp_FD7C
    f.ref('tmp_fd7c').value = EMPTY
    # ReDim tmp_FD74(0 To 1)
    f.redim('tmp_fd74', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FD74(0) = "T"
    f.put('tmp_fd74', [Integer(0)], 'T')
    # tmp_FD74(1) = "S"
    f.put('tmp_fd74', [Integer(1)], 'S')
    # tmp_FEB4 = VBA.Array("T", "S")
    f.set('tmp_feb4', c.builtin('vba.array', ['T', 'S']))
    # Erase tmp_FD74
    f.ref('tmp_fd74').value = EMPTY
    # tmp_FD72 = (nCurrent + 1)
    f.set('tmp_fd72', c.binary('+', f.get('ncurrent'), Integer(1)))
    # ReDim tmp_FD6C(0 To 8)
    f.redim('tmp_fd6c', [(Integer(0), Integer(8))], False, 'variant')
    # tmp_FD6C(0) = "L"
    f.put('tmp_fd6c', [Integer(0)], 'L')
    # tmp_FD6C(1) = "R"
    f.put('tmp_fd6c', [Integer(1)], 'R')
    # tmp_FD6C(2) = "N"
    f.put('tmp_fd6c', [Integer(2)], 'N')
    # tmp_FD6C(3) = "M"
    f.put('tmp_fd6c', [Integer(3)], 'M')
    # tmp_FD6C(4) = "B"
    f.put('tmp_fd6c', [Integer(4)], 'B')
    # tmp_FD6C(5) = "H"
    f.put('tmp_fd6c', [Integer(5)], 'H')
    # tmp_FD6C(6) = "F"
    f.put('tmp_fd6c', [Integer(6)], 'F')
    # tmp_FD6C(7) = "V"
    f.put('tmp_fd6c', [Integer(7)], 'V')
    # tmp_FD6C(8) = "W"
    f.put('tmp_fd6c', [Integer(8)], 'W')
    # tmp_FEA4 = VBA.Array("L", "R", "N", "M", "B", "H", "F", "V", "W")
    f.set('tmp_fea4', c.builtin('vba.array', ['L', 'R', 'N', 'M', 'B', 'H', 'F', 'V', 'W']))
    # Erase tmp_FD6C
    f.ref('tmp_fd6c').value = EMPTY
    # tmp_FD2A = (nCurrent + 1)
    f.set('tmp_fd2a', c.binary('+', f.get('ncurrent'), Integer(1)))
    # If ((((IsInArry(pWord, tmp_FF3A, tmp_FF28) Or IsInArry(pWord, tmp_FD7A, tmp_FED4)) Or IsInArry(pWord, nCurrent, tmp_FEC4)) Or IsInArry(pWord, tmp_FD72, tmp_FEB4)) Or ((PreviousFlag Or (nCurrent = 0)) And IsInArry(pWord, tmp_FD2A, tmp_FEA4))) Then GoTo L0A6B Else GoTo L0A8A
    return 207 if truth(c.binary('or', c.binary('or', c.binary('or', c.binary('or', c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')]), c.call('isinarry', [f.ref('pword'), f.ref('tmp_fd7a'), f.ref('tmp_fed4')])), c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_fec4')])), c.call('isinarry', [f.ref('pword'), f.ref('tmp_fd72'), f.ref('tmp_feb4')])), c.binary('and', c.binary('or', f.get('previousflag'), c.binary('=', f.get('ncurrent'), Integer(0))), c.call('isinarry', [f.ref('pword'), f.ref('tmp_fd2a'), f.ref('tmp_fea4')])))) else 210

def _doublemetaphone_207(f, c):
    # tmp_FF28 = "K"
    f.set('tmp_ff28', 'K')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # GoTo L0B4E
    return 226

def _doublemetaphone_210(f, c):
    # If (nCurrent > 0) Then GoTo L0A97 Else GoTo L0B2E
    return 211 if truth(c.binary('>', f.get('ncurrent'), Integer(0))) else 224

def _doublemetaphone_211(f, c):
    # ReDim tmp_FF24(0 To 0)
    f.redim('tmp_ff24', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FF24(0) = "MC"
    f.put('tmp_ff24', [Integer(0)], 'MC')
    # tmp_FF28 = VBA.Array("MC")
    f.set('tmp_ff28', c.builtin('vba.array', ['MC']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = 0
    f.set('tmp_ff3a', Integer(0))
    # If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L0AE4 Else GoTo L0B03
    return 217 if truth(c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')])) else 220

def _doublemetaphone_217(f, c):
    # tmp_FF28 = "K"
    f.set('tmp_ff28', 'K')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # GoTo L0B29
    return 223

def _doublemetaphone_220(f, c):
    # tmp_FED4 = "K"
    f.set('tmp_fed4', 'K')
    # tmp_FF28 = "X"
    f.set('tmp_ff28', 'X')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    return 223

def _doublemetaphone_223(f, c):
    # GoTo L0B4C
    return 226

def _doublemetaphone_224(f, c):
    # tmp_FF28 = "X"
    f.set('tmp_ff28', 'X')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 226

def _doublemetaphone_226(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_228(f, c):
    # ReDim tmp_FF24(0 To 0)
    f.redim('tmp_ff24', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FF24(0) = "CZ"
    f.put('tmp_ff24', [Integer(0)], 'CZ')
    # tmp_FF28 = VBA.Array("CZ")
    f.set('tmp_ff28', c.builtin('vba.array', ['CZ']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # ReDim tmp_FDE0(0 To 0)
    f.redim('tmp_fde0', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FDE0(0) = "WICZ"
    f.put('tmp_fde0', [Integer(0)], 'WICZ')
    # tmp_FED4 = VBA.Array("WICZ")
    f.set('tmp_fed4', c.builtin('vba.array', ['WICZ']))
    # Erase tmp_FDE0
    f.ref('tmp_fde0').value = EMPTY
    # If (IsInArry(pWord, nCurrent, tmp_FF28) And (Not IsInArry(pWord, nCurrent, tmp_FED4))) Then GoTo L0BF6 Else GoTo L0C2A
    return 237 if truth(c.binary('and', c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')]), c.unary('not', c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_fed4')])))) else 242

def _doublemetaphone_237(f, c):
    # tmp_FED4 = "X"
    f.set('tmp_fed4', 'X')
    # tmp_FF28 = "S"
    f.set('tmp_ff28', 'S')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_242(f, c):
    # ReDim tmp_FF24(0 To 0)
    f.redim('tmp_ff24', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FF24(0) = "CIA"
    f.put('tmp_ff24', [Integer(0)], 'CIA')
    # tmp_FF28 = VBA.Array("CIA")
    f.set('tmp_ff28', c.builtin('vba.array', ['CIA']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = (nCurrent + 1)
    f.set('tmp_ff3a', c.binary('+', f.get('ncurrent'), Integer(1)))
    # If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L0C7D Else GoTo L0CA9
    return 248 if truth(c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')])) else 252

def _doublemetaphone_248(f, c):
    # tmp_FF28 = "X"
    f.set('tmp_ff28', 'X')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 3))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(3))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_252(f, c):
    # tmp_FF28 = pWord(nCurrent)
    f.set('tmp_ff28', f.index('pword', f.get('ncurrent')))
    # tmp_FED4 = (tmp_FF28 = "C")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'C'))
    # tmp_FF04 = CInt((nCurrent + 1))
    f.set('tmp_ff04', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FEC4 = pWord(tmp_FF04)
    f.set('tmp_fec4', f.index('pword', f.get('tmp_ff04')))
    # tmp_FEB4 = (tmp_FEC4 = "C")
    f.set('tmp_feb4', c.binary('=', f.get('tmp_fec4'), 'C'))
    # tmp_FEA4 = (tmp_FED4 And tmp_FEB4)
    f.set('tmp_fea4', c.binary('and', f.get('tmp_fed4'), f.get('tmp_feb4')))
    # tmp_FE14 = CBool((nCurrent = 0))
    f.set('tmp_fe14', c.builtin('cbool', [c.binary('=', f.get('ncurrent'), Integer(0))]))
    # tmp_FE94 = pWord(0)
    f.set('tmp_fe94', f.index('pword', Integer(0)))
    # tmp_FE54 = (tmp_FE94 = "M")
    f.set('tmp_fe54', c.binary('=', f.get('tmp_fe94'), 'M'))
    # tmp_FE44 = (tmp_FE14 And tmp_FE54)
    f.set('tmp_fe44', c.binary('and', f.get('tmp_fe14'), f.get('tmp_fe54')))
    # tmp_FE34 = (Not tmp_FE44)
    f.set('tmp_fe34', c.unary('not', f.get('tmp_fe44')))
    # tmp_FDF4 = (tmp_FEA4 And tmp_FE34)
    f.set('tmp_fdf4', c.binary('and', f.get('tmp_fea4'), f.get('tmp_fe34')))
    # If tmp_FDF4 Then GoTo L0D27 Else GoTo L0EFB
    return 265 if truth(f.get('tmp_fdf4')) else 306

def _doublemetaphone_265(f, c):
    # ReDim tmp_FF24(0 To 2)
    f.redim('tmp_ff24', [(Integer(0), Integer(2))], False, 'variant')
    # tmp_FF24(0) = "I"
    f.put('tmp_ff24', [Integer(0)], 'I')
    # tmp_FF24(1) = "E"
    f.put('tmp_ff24', [Integer(1)], 'E')
    # tmp_FF24(2) = "H"
    f.put('tmp_ff24', [Integer(2)], 'H')
    # tmp_FF28 = VBA.Array("I", "E", "H")
    f.set('tmp_ff28', c.builtin('vba.array', ['I', 'E', 'H']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = (nCurrent + 2)
    f.set('tmp_ff3a', c.binary('+', f.get('ncurrent'), Integer(2)))
    # tmp_FE04 = CBool(IsInArry(pWord, tmp_FF3A, tmp_FF28))
    f.set('tmp_fe04', c.builtin('cbool', [c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')])]))
    # tmp_FEF4 = CInt((nCurrent + 2))
    f.set('tmp_fef4', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # tmp_FED4 = pWord(tmp_FEF4)
    f.set('tmp_fed4', f.index('pword', f.get('tmp_fef4')))
    # tmp_FEC4 = (tmp_FED4 <> "H")
    f.set('tmp_fec4', c.binary('<>', f.get('tmp_fed4'), 'H'))
    # tmp_FE64 = CInt((nCurrent + 3))
    f.set('tmp_fe64', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(3))]))
    # tmp_FEB4 = pWord(tmp_FE64)
    f.set('tmp_feb4', f.index('pword', f.get('tmp_fe64')))
    # tmp_FEA4 = (tmp_FEB4 <> "U")
    f.set('tmp_fea4', c.binary('<>', f.get('tmp_feb4'), 'U'))
    # tmp_FE94 = (tmp_FEC4 And tmp_FEA4)
    f.set('tmp_fe94', c.binary('and', f.get('tmp_fec4'), f.get('tmp_fea4')))
    # tmp_FE54 = (tmp_FE04 And tmp_FE94)
    f.set('tmp_fe54', c.binary('and', f.get('tmp_fe04'), f.get('tmp_fe94')))
    # If tmp_FE54 Then GoTo L0DE6 Else GoTo L0ECB
    return 282 if truth(f.get('tmp_fe54')) else 302

def _doublemetaphone_282(f, c):
    # tmp_FEF4 = CBool((nCurrent = 0))
    f.set('tmp_fef4', c.builtin('cbool', [c.binary('=', f.get('ncurrent'), Integer(0))]))
    # tmp_FF28 = pWord(0)
    f.set('tmp_ff28', f.index('pword', Integer(0)))
    # tmp_FED4 = (tmp_FF28 = "A")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'A'))
    # tmp_FEC4 = (tmp_FEF4 And tmp_FED4)
    f.set('tmp_fec4', c.binary('and', f.get('tmp_fef4'), f.get('tmp_fed4')))
    # ReDim tmp_FF24(0 To 1)
    f.redim('tmp_ff24', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FF24(0) = "UCCEE"
    f.put('tmp_ff24', [Integer(0)], 'UCCEE')
    # tmp_FF24(1) = "UCCES"
    f.put('tmp_ff24', [Integer(1)], 'UCCES')
    # tmp_FEB4 = VBA.Array("UCCEE", "UCCES")
    f.set('tmp_feb4', c.builtin('vba.array', ['UCCEE', 'UCCES']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FE64 = CBool(IsInArry(pWord, nCurrent, tmp_FEB4))
    f.set('tmp_fe64', c.builtin('cbool', [c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_feb4')])]))
    # tmp_FEA4 = (tmp_FEC4 Or tmp_FE64)
    f.set('tmp_fea4', c.binary('or', f.get('tmp_fec4'), f.get('tmp_fe64')))
    # If tmp_FEA4 Then GoTo L0E79 Else GoTo L0E98
    return 294 if truth(f.get('tmp_fea4')) else 297

def _doublemetaphone_294(f, c):
    # tmp_FF28 = "KS"
    f.set('tmp_ff28', 'KS')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # GoTo L0EB6
    return 299

def _doublemetaphone_297(f, c):
    # tmp_FF28 = "X"
    f.set('tmp_ff28', 'X')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 299

def _doublemetaphone_299(f, c):
    # nCurrent = CInt((nCurrent + 3))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(3))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_301(f, c):
    # GoTo L0EF9
    return 306

def _doublemetaphone_302(f, c):
    # tmp_FF28 = "K"
    f.set('tmp_ff28', 'K')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_306(f, c):
    # ReDim tmp_FF24(0 To 2)
    f.redim('tmp_ff24', [(Integer(0), Integer(2))], False, 'variant')
    # tmp_FF24(0) = "CK"
    f.put('tmp_ff24', [Integer(0)], 'CK')
    # tmp_FF24(1) = "CG"
    f.put('tmp_ff24', [Integer(1)], 'CG')
    # tmp_FF24(2) = "CQ"
    f.put('tmp_ff24', [Integer(2)], 'CQ')
    # tmp_FF28 = VBA.Array("CK", "CG", "CQ")
    f.set('tmp_ff28', c.builtin('vba.array', ['CK', 'CG', 'CQ']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # If IsInArry(pWord, nCurrent, tmp_FF28) Then GoTo L0F66 Else GoTo L0F92
    return 313 if truth(c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')])) else 317

def _doublemetaphone_313(f, c):
    # tmp_FF28 = "K"
    f.set('tmp_ff28', 'K')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_317(f, c):
    # ReDim tmp_FF24(0 To 2)
    f.redim('tmp_ff24', [(Integer(0), Integer(2))], False, 'variant')
    # tmp_FF24(0) = "CI"
    f.put('tmp_ff24', [Integer(0)], 'CI')
    # tmp_FF24(1) = "CE"
    f.put('tmp_ff24', [Integer(1)], 'CE')
    # tmp_FF24(2) = "CY"
    f.put('tmp_ff24', [Integer(2)], 'CY')
    # tmp_FF28 = VBA.Array("CI", "CE", "CY")
    f.set('tmp_ff28', c.builtin('vba.array', ['CI', 'CE', 'CY']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # If IsInArry(pWord, nCurrent, tmp_FF28) Then GoTo L0FFD Else GoTo L10BD
    return 324 if truth(c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')])) else 339

def _doublemetaphone_324(f, c):
    # ReDim tmp_FF24(0 To 2)
    f.redim('tmp_ff24', [(Integer(0), Integer(2))], False, 'variant')
    # tmp_FF24(0) = "CIO"
    f.put('tmp_ff24', [Integer(0)], 'CIO')
    # tmp_FF24(1) = "CIE"
    f.put('tmp_ff24', [Integer(1)], 'CIE')
    # tmp_FF24(2) = "CIA"
    f.put('tmp_ff24', [Integer(2)], 'CIA')
    # tmp_FF28 = VBA.Array("CIO", "CIE", "CIA")
    f.set('tmp_ff28', c.builtin('vba.array', ['CIO', 'CIE', 'CIA']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # If IsInArry(pWord, nCurrent, tmp_FF28) Then GoTo L1066 Else GoTo L108D
    return 331 if truth(c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')])) else 335

def _doublemetaphone_331(f, c):
    # tmp_FED4 = "X"
    f.set('tmp_fed4', 'X')
    # tmp_FF28 = "S"
    f.set('tmp_ff28', 'S')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # GoTo L10AB
    return 337

def _doublemetaphone_335(f, c):
    # tmp_FF28 = "S"
    f.set('tmp_ff28', 'S')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 337

def _doublemetaphone_337(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_339(f, c):
    # tmp_FF28 = "K"
    f.set('tmp_ff28', 'K')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # ReDim tmp_FF24(0 To 2)
    f.redim('tmp_ff24', [(Integer(0), Integer(2))], False, 'variant')
    # tmp_FF24(0) = " C"
    f.put('tmp_ff24', [Integer(0)], ' C')
    # tmp_FF24(1) = " Q"
    f.put('tmp_ff24', [Integer(1)], ' Q')
    # tmp_FF24(2) = " G"
    f.put('tmp_ff24', [Integer(2)], ' G')
    # tmp_FF28 = VBA.Array(" C", " Q", " G")
    f.set('tmp_ff28', c.builtin('vba.array', [' C', ' Q', ' G']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = (nCurrent + 1)
    f.set('tmp_ff3a', c.binary('+', f.get('ncurrent'), Integer(1)))
    # If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L114A Else GoTo L1158
    return 349 if truth(c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')])) else 351

def _doublemetaphone_349(f, c):
    # nCurrent = CInt((nCurrent + 3))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(3))]))
    # GoTo L1203
    return 366

def _doublemetaphone_351(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 Like "[CKQ]")
    f.set('tmp_fed4', c.binary('like', f.get('tmp_ff28'), '[CKQ]'))
    # ReDim tmp_FF24(0 To 1)
    f.redim('tmp_ff24', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FF24(0) = "CE"
    f.put('tmp_ff24', [Integer(0)], 'CE')
    # tmp_FF24(1) = "CI"
    f.put('tmp_ff24', [Integer(1)], 'CI')
    # tmp_FEC4 = VBA.Array("CE", "CI")
    f.set('tmp_fec4', c.builtin('vba.array', ['CE', 'CI']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = (nCurrent + 1)
    f.set('tmp_ff3a', c.binary('+', f.get('ncurrent'), Integer(1)))
    # tmp_FE74 = CBool(IsInArry(pWord, tmp_FF3A, tmp_FEC4))
    f.set('tmp_fe74', c.builtin('cbool', [c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_fec4')])]))
    # tmp_FEB4 = (tmp_FED4 And tmp_FE74)
    f.set('tmp_feb4', c.binary('and', f.get('tmp_fed4'), f.get('tmp_fe74')))
    # If tmp_FEB4 Then GoTo L11E6 Else GoTo L11F4
    return 363 if truth(f.get('tmp_feb4')) else 365

def _doublemetaphone_363(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L1201
    return 366

def _doublemetaphone_365(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 366

def _doublemetaphone_366(f, c):
    # GoTo L3CD1
    return 1320

def _doublemetaphone_367(f, c):
    # If (tmp_FE84 = "D") Then GoTo L1218 Else GoTo L1395
    return 368 if truth(c.binary('=', f.get('tmp_fe84'), 'D')) else 401

def _doublemetaphone_368(f, c):
    # tmp_FF28 = pWord(nCurrent)
    f.set('tmp_ff28', f.index('pword', f.get('ncurrent')))
    # tmp_FED4 = (tmp_FF28 = "D")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'D'))
    # tmp_FF04 = CInt((nCurrent + 1))
    f.set('tmp_ff04', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FEC4 = pWord(tmp_FF04)
    f.set('tmp_fec4', f.index('pword', f.get('tmp_ff04')))
    # tmp_FEB4 = (tmp_FEC4 = "G")
    f.set('tmp_feb4', c.binary('=', f.get('tmp_fec4'), 'G'))
    # tmp_FEA4 = (tmp_FED4 And tmp_FEB4)
    f.set('tmp_fea4', c.binary('and', f.get('tmp_fed4'), f.get('tmp_feb4')))
    # If tmp_FEA4 Then GoTo L1261 Else GoTo L12E1
    return 375 if truth(f.get('tmp_fea4')) else 387

def _doublemetaphone_375(f, c):
    # tmp_FF3C = CInt((nCurrent + 2))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 Like "[IEY]")
    f.set('tmp_fed4', c.binary('like', f.get('tmp_ff28'), '[IEY]'))
    # If tmp_FED4 Then GoTo L1287 Else GoTo L12B1
    return 379 if truth(f.get('tmp_fed4')) else 383

def _doublemetaphone_379(f, c):
    # tmp_FF28 = "J"
    f.set('tmp_ff28', 'J')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 3))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(3))]))
    # GoTo L12DA
    return 386

def _doublemetaphone_383(f, c):
    # tmp_FF28 = "TK"
    f.set('tmp_ff28', 'TK')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    return 386

def _doublemetaphone_386(f, c):
    # GoTo L3CD3
    return 1320

def _doublemetaphone_387(f, c):
    # ReDim tmp_FF24(0 To 1)
    f.redim('tmp_ff24', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FF24(0) = "DT"
    f.put('tmp_ff24', [Integer(0)], 'DT')
    # tmp_FF24(1) = "DD"
    f.put('tmp_ff24', [Integer(1)], 'DD')
    # tmp_FF28 = VBA.Array("DT", "DD")
    f.set('tmp_ff28', c.builtin('vba.array', ['DT', 'DD']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # If IsInArry(pWord, nCurrent, tmp_FF28) Then GoTo L133D Else GoTo L1369
    return 393 if truth(c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')])) else 397

def _doublemetaphone_393(f, c):
    # tmp_FF28 = "T"
    f.set('tmp_ff28', 'T')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_397(f, c):
    # tmp_FF28 = "T"
    f.set('tmp_ff28', 'T')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # GoTo L3CD1
    return 1320

def _doublemetaphone_401(f, c):
    # If (tmp_FE84 = "F") Then GoTo L13A5 Else GoTo L1404
    return 402 if truth(c.binary('=', f.get('tmp_fe84'), 'F')) else 411

def _doublemetaphone_402(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # If (tmp_FF28 = "F") Then GoTo L13C8 Else GoTo L13D6
    return 405 if truth(c.binary('=', f.get('tmp_ff28'), 'F')) else 407

def _doublemetaphone_405(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L13E3
    return 408

def _doublemetaphone_407(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 408

def _doublemetaphone_408(f, c):
    # tmp_FF28 = "F"
    f.set('tmp_ff28', 'F')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # GoTo L3CD1
    return 1320

def _doublemetaphone_411(f, c):
    # If (tmp_FE84 = "G") Then GoTo L1414 Else GoTo L1E93
    return 412 if truth(c.binary('=', f.get('tmp_fe84'), 'G')) else 655

def _doublemetaphone_412(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # If (tmp_FF28 = "H") Then GoTo L1437 Else GoTo L16B9
    return 415 if truth(c.binary('=', f.get('tmp_ff28'), 'H')) else 478

def _doublemetaphone_415(f, c):
    # tmp_FF04 = CBool((nCurrent > 0))
    f.set('tmp_ff04', c.builtin('cbool', [c.binary('>', f.get('ncurrent'), Integer(0))]))
    # tmp_FF28 = pWord(nCurrent)
    f.set('tmp_ff28', f.index('pword', f.get('ncurrent')))
    # tmp_FED4 = (tmp_FF28 Like "[aeiouy]")
    f.set('tmp_fed4', c.binary('like', f.get('tmp_ff28'), '[aeiouy]'))
    # tmp_FEC4 = (Not tmp_FED4)
    f.set('tmp_fec4', c.unary('not', f.get('tmp_fed4')))
    # tmp_FEB4 = (tmp_FF04 And tmp_FEC4)
    f.set('tmp_feb4', c.binary('and', f.get('tmp_ff04'), f.get('tmp_fec4')))
    # If tmp_FEB4 Then GoTo L1470 Else GoTo L149C
    return 421 if truth(f.get('tmp_feb4')) else 425

def _doublemetaphone_421(f, c):
    # tmp_FF28 = "K"
    f.set('tmp_ff28', 'K')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_425(f, c):
    # If (nCurrent < 2) Then GoTo L14A9 Else GoTo L1528
    return 426 if truth(c.binary('<', f.get('ncurrent'), Integer(2))) else 437

def _doublemetaphone_426(f, c):
    # If (nCurrent = 0) Then GoTo L14B4 Else GoTo L1526
    return 427 if truth(c.binary('=', f.get('ncurrent'), Integer(0))) else 437

def _doublemetaphone_427(f, c):
    # tmp_FF3C = CInt((nCurrent + 2))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # If (tmp_FF28 = "I") Then GoTo L14D7 Else GoTo L14F6
    return 430 if truth(c.binary('=', f.get('tmp_ff28'), 'I')) else 433

def _doublemetaphone_430(f, c):
    # tmp_FF28 = "J"
    f.set('tmp_ff28', 'J')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # GoTo L1514
    return 435

def _doublemetaphone_433(f, c):
    # tmp_FF28 = "K"
    f.set('tmp_ff28', 'K')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 435

def _doublemetaphone_435(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_437(f, c):
    # tmp_FF04 = CBool((nCurrent > 0))
    f.set('tmp_ff04', c.builtin('cbool', [c.binary('>', f.get('ncurrent'), Integer(0))]))
    # tmp_FF28 = pWord(nCurrent)
    f.set('tmp_ff28', f.index('pword', f.get('ncurrent')))
    # tmp_FED4 = (tmp_FF28 Like "[BHD]")
    f.set('tmp_fed4', c.binary('like', f.get('tmp_ff28'), '[BHD]'))
    # tmp_FEC4 = (tmp_FF04 And tmp_FED4)
    f.set('tmp_fec4', c.binary('and', f.get('tmp_ff04'), f.get('tmp_fed4')))
    # tmp_FE64 = CBool((nCurrent > 1))
    f.set('tmp_fe64', c.builtin('cbool', [c.binary('>', f.get('ncurrent'), Integer(1))]))
    # tmp_FEF4 = CInt((nCurrent - 1))
    f.set('tmp_fef4', c.builtin('cint', [c.binary('-', f.get('ncurrent'), Integer(1))]))
    # tmp_FEB4 = pWord(tmp_FEF4)
    f.set('tmp_feb4', f.index('pword', f.get('tmp_fef4')))
    # tmp_FEA4 = (tmp_FEB4 Like "[BHD]")
    f.set('tmp_fea4', c.binary('like', f.get('tmp_feb4'), '[BHD]'))
    # tmp_FE94 = (tmp_FE64 And tmp_FEA4)
    f.set('tmp_fe94', c.binary('and', f.get('tmp_fe64'), f.get('tmp_fea4')))
    # tmp_FE54 = (tmp_FEC4 Or tmp_FE94)
    f.set('tmp_fe54', c.binary('or', f.get('tmp_fec4'), f.get('tmp_fe94')))
    # tmp_FDD0 = CBool((nCurrent > 2))
    f.set('tmp_fdd0', c.builtin('cbool', [c.binary('>', f.get('ncurrent'), Integer(2))]))
    # tmp_FE24 = CInt((nCurrent - 2))
    f.set('tmp_fe24', c.builtin('cint', [c.binary('-', f.get('ncurrent'), Integer(2))]))
    # tmp_FE44 = pWord(tmp_FE24)
    f.set('tmp_fe44', f.index('pword', f.get('tmp_fe24')))
    # tmp_FE34 = (tmp_FE44 Like "[BH]")
    f.set('tmp_fe34', c.binary('like', f.get('tmp_fe44'), '[BH]'))
    # tmp_FDF4 = (tmp_FDD0 And tmp_FE34)
    f.set('tmp_fdf4', c.binary('and', f.get('tmp_fdd0'), f.get('tmp_fe34')))
    # tmp_FDE4 = (tmp_FE54 Or tmp_FDF4)
    f.set('tmp_fde4', c.binary('or', f.get('tmp_fe54'), f.get('tmp_fdf4')))
    # If tmp_FDE4 Then GoTo L15C3 Else GoTo L15D6
    return 454 if truth(f.get('tmp_fde4')) else 457

def _doublemetaphone_454(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_456(f, c):
    # GoTo L16B7
    return 478

def _doublemetaphone_457(f, c):
    # tmp_FF04 = CBool((nCurrent > 1))
    f.set('tmp_ff04', c.builtin('cbool', [c.binary('>', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(nCurrent)
    f.set('tmp_ff28', f.index('pword', f.get('ncurrent')))
    # tmp_FED4 = (tmp_FF28 = "U")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'U'))
    # tmp_FEC4 = (tmp_FF04 And tmp_FED4)
    f.set('tmp_fec4', c.binary('and', f.get('tmp_ff04'), f.get('tmp_fed4')))
    # tmp_FEF4 = CInt((nCurrent - 1))
    f.set('tmp_fef4', c.builtin('cint', [c.binary('-', f.get('ncurrent'), Integer(1))]))
    # tmp_FEB4 = pWord(tmp_FEF4)
    f.set('tmp_feb4', f.index('pword', f.get('tmp_fef4')))
    # tmp_FEA4 = (tmp_FEB4 Like "[CGLRT]")
    f.set('tmp_fea4', c.binary('like', f.get('tmp_feb4'), '[CGLRT]'))
    # tmp_FE94 = (tmp_FEC4 And tmp_FEA4)
    f.set('tmp_fe94', c.binary('and', f.get('tmp_fec4'), f.get('tmp_fea4')))
    # If tmp_FE94 Then GoTo L1630 Else GoTo L164F
    return 466 if truth(f.get('tmp_fe94')) else 469

def _doublemetaphone_466(f, c):
    # tmp_FF28 = "F"
    f.set('tmp_ff28', 'F')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # GoTo L16A5
    return 476

def _doublemetaphone_469(f, c):
    # tmp_FF04 = CBool((nCurrent > 0))
    f.set('tmp_ff04', c.builtin('cbool', [c.binary('>', f.get('ncurrent'), Integer(0))]))
    # tmp_FF28 = pWord(nCurrent)
    f.set('tmp_ff28', f.index('pword', f.get('ncurrent')))
    # tmp_FED4 = (tmp_FF28 <> "I")
    f.set('tmp_fed4', c.binary('<>', f.get('tmp_ff28'), 'I'))
    # tmp_FEC4 = (tmp_FF04 And tmp_FED4)
    f.set('tmp_fec4', c.binary('and', f.get('tmp_ff04'), f.get('tmp_fed4')))
    # If tmp_FEC4 Then GoTo L1687 Else GoTo L16A3
    return 474 if truth(f.get('tmp_fec4')) else 476

def _doublemetaphone_474(f, c):
    # tmp_FF28 = "K"
    f.set('tmp_ff28', 'K')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 476

def _doublemetaphone_476(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_478(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # If (tmp_FF28 = "N") Then GoTo L16DE Else GoTo L1829
    return 481 if truth(c.binary('=', f.get('tmp_ff28'), 'N')) else 514

def _doublemetaphone_481(f, c):
    # tmp_FEF4 = CBool((nCurrent = 0))
    f.set('tmp_fef4', c.builtin('cbool', [c.binary('=', f.get('ncurrent'), Integer(0))]))
    # tmp_FF28 = pWord(0)
    f.set('tmp_ff28', f.index('pword', Integer(0)))
    # tmp_FED4 = (tmp_FF28 Like "[aeiouy]")
    f.set('tmp_fed4', c.binary('like', f.get('tmp_ff28'), '[aeiouy]'))
    # tmp_FEC4 = (tmp_FEF4 And tmp_FED4)
    f.set('tmp_fec4', c.binary('and', f.get('tmp_fef4'), f.get('tmp_fed4')))
    # tmp_FEE4 = CBool((Not SlavoGermanic(pWord)))
    f.set('tmp_fee4', c.builtin('cbool', [c.unary('not', c.call('slavogermanic', [f.ref('pword')]))]))
    # tmp_FEB4 = (tmp_FEC4 And tmp_FEE4)
    f.set('tmp_feb4', c.binary('and', f.get('tmp_fec4'), f.get('tmp_fee4')))
    # If tmp_FEB4 Then GoTo L1725 Else GoTo L174C
    return 488 if truth(f.get('tmp_feb4')) else 492

def _doublemetaphone_488(f, c):
    # tmp_FED4 = "N"
    f.set('tmp_fed4', 'N')
    # tmp_FF28 = "KN"
    f.set('tmp_ff28', 'KN')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # GoTo L1817
    return 512

def _doublemetaphone_492(f, c):
    # tmp_FF3C = CInt((nCurrent + 2))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 <> "E")
    f.set('tmp_fed4', c.binary('<>', f.get('tmp_ff28'), 'E'))
    # tmp_FEF4 = CInt((nCurrent + 3))
    f.set('tmp_fef4', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(3))]))
    # tmp_FEC4 = pWord(tmp_FEF4)
    f.set('tmp_fec4', f.index('pword', f.get('tmp_fef4')))
    # tmp_FEB4 = (tmp_FEC4 <> "Y")
    f.set('tmp_feb4', c.binary('<>', f.get('tmp_fec4'), 'Y'))
    # tmp_FEA4 = (tmp_FED4 And tmp_FEB4)
    f.set('tmp_fea4', c.binary('and', f.get('tmp_fed4'), f.get('tmp_feb4')))
    # tmp_FE64 = CInt((nCurrent + 1))
    f.set('tmp_fe64', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FE94 = pWord(tmp_FE64)
    f.set('tmp_fe94', f.index('pword', f.get('tmp_fe64')))
    # tmp_FE54 = (tmp_FE94 <> "Y")
    f.set('tmp_fe54', c.binary('<>', f.get('tmp_fe94'), 'Y'))
    # tmp_FE44 = (tmp_FEA4 And tmp_FE54)
    f.set('tmp_fe44', c.binary('and', f.get('tmp_fea4'), f.get('tmp_fe54')))
    # tmp_FE04 = CBool((Not SlavoGermanic(pWord)))
    f.set('tmp_fe04', c.builtin('cbool', [c.unary('not', c.call('slavogermanic', [f.ref('pword')]))]))
    # tmp_FE34 = (tmp_FE44 And tmp_FE04)
    f.set('tmp_fe34', c.binary('and', f.get('tmp_fe44'), f.get('tmp_fe04')))
    # If tmp_FE34 Then GoTo L17D0 Else GoTo L17F7
    return 506 if truth(f.get('tmp_fe34')) else 510

def _doublemetaphone_506(f, c):
    # tmp_FED4 = "KN"
    f.set('tmp_fed4', 'KN')
    # tmp_FF28 = "N"
    f.set('tmp_ff28', 'N')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # GoTo L1815
    return 512

def _doublemetaphone_510(f, c):
    # tmp_FF28 = "KN"
    f.set('tmp_ff28', 'KN')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 512

def _doublemetaphone_512(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_514(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 = "L")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'L'))
    # tmp_FEF4 = CInt((nCurrent + 2))
    f.set('tmp_fef4', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # tmp_FEC4 = pWord(tmp_FEF4)
    f.set('tmp_fec4', f.index('pword', f.get('tmp_fef4')))
    # tmp_FEB4 = (tmp_FEC4 = "I")
    f.set('tmp_feb4', c.binary('=', f.get('tmp_fec4'), 'I'))
    # tmp_FEA4 = (tmp_FED4 And tmp_FEB4)
    f.set('tmp_fea4', c.binary('and', f.get('tmp_fed4'), f.get('tmp_feb4')))
    # tmp_FE64 = CBool((Not SlavoGermanic(pWord)))
    f.set('tmp_fe64', c.builtin('cbool', [c.unary('not', c.call('slavogermanic', [f.ref('pword')]))]))
    # tmp_FE94 = (tmp_FEA4 And tmp_FE64)
    f.set('tmp_fe94', c.binary('and', f.get('tmp_fea4'), f.get('tmp_fe64')))
    # If tmp_FE94 Then GoTo L188A Else GoTo L18BE
    return 524 if truth(f.get('tmp_fe94')) else 529

def _doublemetaphone_524(f, c):
    # tmp_FED4 = "L"
    f.set('tmp_fed4', 'L')
    # tmp_FF28 = "KL"
    f.set('tmp_ff28', 'KL')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_529(f, c):
    # tmp_FD3C = CBool((nCurrent = 0))
    f.set('tmp_fd3c', c.builtin('cbool', [c.binary('=', f.get('ncurrent'), Integer(0))]))
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 = "Y")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'Y'))
    # ReDim tmp_FF24(0 To 10)
    f.redim('tmp_ff24', [(Integer(0), Integer(10))], False, 'variant')
    # tmp_FF24(0) = "ES"
    f.put('tmp_ff24', [Integer(0)], 'ES')
    # tmp_FF24(1) = "EP"
    f.put('tmp_ff24', [Integer(1)], 'EP')
    # tmp_FF24(2) = "EB"
    f.put('tmp_ff24', [Integer(2)], 'EB')
    # tmp_FF24(3) = "EL"
    f.put('tmp_ff24', [Integer(3)], 'EL')
    # tmp_FF24(4) = "EY"
    f.put('tmp_ff24', [Integer(4)], 'EY')
    # tmp_FF24(5) = "IB"
    f.put('tmp_ff24', [Integer(5)], 'IB')
    # tmp_FF24(6) = "IL"
    f.put('tmp_ff24', [Integer(6)], 'IL')
    # tmp_FF24(7) = "IN"
    f.put('tmp_ff24', [Integer(7)], 'IN')
    # tmp_FF24(8) = "IE"
    f.put('tmp_ff24', [Integer(8)], 'IE')
    # tmp_FF24(9) = "EI"
    f.put('tmp_ff24', [Integer(9)], 'EI')
    # tmp_FF24(10) = "ER"
    f.put('tmp_ff24', [Integer(10)], 'ER')
    # tmp_FEC4 = VBA.Array("ES", "EP", "EB", "EL", "EY", "IB", "IL", "IN", "IE", "EI", "ER")
    f.set('tmp_fec4', c.builtin('vba.array', ['ES', 'EP', 'EB', 'EL', 'EY', 'IB', 'IL', 'IN', 'IE', 'EI', 'ER']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = (nCurrent + 1)
    f.set('tmp_ff3a', c.binary('+', f.get('ncurrent'), Integer(1)))
    # tmp_FD4C = CBool(IsInArry(pWord, tmp_FF3A, tmp_FEC4))
    f.set('tmp_fd4c', c.builtin('cbool', [c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_fec4')])]))
    # tmp_FEB4 = (tmp_FED4 Or tmp_FD4C)
    f.set('tmp_feb4', c.binary('or', f.get('tmp_fed4'), f.get('tmp_fd4c')))
    # tmp_FEA4 = (tmp_FD3C And tmp_FEB4)
    f.set('tmp_fea4', c.binary('and', f.get('tmp_fd3c'), f.get('tmp_feb4')))
    # If tmp_FEA4 Then GoTo L19E4 Else GoTo L1A18
    return 552 if truth(f.get('tmp_fea4')) else 557

def _doublemetaphone_552(f, c):
    # tmp_FED4 = "J"
    f.set('tmp_fed4', 'J')
    # tmp_FF28 = "K"
    f.set('tmp_ff28', 'K')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_557(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 = "E")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'E'))
    # tmp_FEF4 = CInt((nCurrent + 2))
    f.set('tmp_fef4', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # tmp_FEC4 = pWord(tmp_FEF4)
    f.set('tmp_fec4', f.index('pword', f.get('tmp_fef4')))
    # tmp_FEB4 = (tmp_FEC4 = "R")
    f.set('tmp_feb4', c.binary('=', f.get('tmp_fec4'), 'R'))
    # tmp_FEA4 = (tmp_FED4 And tmp_FEB4)
    f.set('tmp_fea4', c.binary('and', f.get('tmp_fed4'), f.get('tmp_feb4')))
    # tmp_FE64 = CInt((nCurrent + 1))
    f.set('tmp_fe64', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FE94 = pWord(tmp_FE64)
    f.set('tmp_fe94', f.index('pword', f.get('tmp_fe64')))
    # tmp_FE54 = (tmp_FE94 = "Y")
    f.set('tmp_fe54', c.binary('=', f.get('tmp_fe94'), 'Y'))
    # tmp_FE44 = (tmp_FEA4 Or tmp_FE54)
    f.set('tmp_fe44', c.binary('or', f.get('tmp_fea4'), f.get('tmp_fe54')))
    # ReDim tmp_FF24(0 To 2)
    f.redim('tmp_ff24', [(Integer(0), Integer(2))], False, 'variant')
    # tmp_FF24(0) = "DANGER"
    f.put('tmp_ff24', [Integer(0)], 'DANGER')
    # tmp_FF24(1) = "RANGER"
    f.put('tmp_ff24', [Integer(1)], 'RANGER')
    # tmp_FF24(2) = "MANGER"
    f.put('tmp_ff24', [Integer(2)], 'MANGER')
    # tmp_FE34 = VBA.Array("DANGER", "RANGER", "MANGER")
    f.set('tmp_fe34', c.builtin('vba.array', ['DANGER', 'RANGER', 'MANGER']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = 1
    f.set('tmp_ff3a', Integer(1))
    # tmp_FDA0 = CBool((Not IsInArry(pWord, tmp_FF3A, tmp_FE34)))
    f.set('tmp_fda0', c.builtin('cbool', [c.unary('not', c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_fe34')]))]))
    # tmp_FDF4 = (tmp_FE44 And tmp_FDA0)
    f.set('tmp_fdf4', c.binary('and', f.get('tmp_fe44'), f.get('tmp_fda0')))
    # ReDim tmp_FDE0(0 To 1)
    f.redim('tmp_fde0', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FDE0(0) = "E"
    f.put('tmp_fde0', [Integer(0)], 'E')
    # tmp_FDE0(1) = "I"
    f.put('tmp_fde0', [Integer(1)], 'I')
    # tmp_FDE4 = VBA.Array("E", "I")
    f.set('tmp_fde4', c.builtin('vba.array', ['E', 'I']))
    # Erase tmp_FDE0
    f.ref('tmp_fde0').value = EMPTY
    # tmp_FD3C = CBool((Not IsInArry(pWord, nCurrent, tmp_FDE4)))
    f.set('tmp_fd3c', c.builtin('cbool', [c.unary('not', c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_fde4')]))]))
    # tmp_FDB0 = (tmp_FDF4 And tmp_FD3C)
    f.set('tmp_fdb0', c.binary('and', f.get('tmp_fdf4'), f.get('tmp_fd3c')))
    # ReDim tmp_FD7C(0 To 1)
    f.redim('tmp_fd7c', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FD7C(0) = "RGY"
    f.put('tmp_fd7c', [Integer(0)], 'RGY')
    # tmp_FD7C(1) = "OGY"
    f.put('tmp_fd7c', [Integer(1)], 'OGY')
    # tmp_FD90 = VBA.Array("RGY", "OGY")
    f.set('tmp_fd90', c.builtin('vba.array', ['RGY', 'OGY']))
    # Erase tmp_FD7C
    f.ref('tmp_fd7c').value = EMPTY
    # tmp_FD08 = CBool((Not IsInArry(pWord, nCurrent, tmp_FD90)))
    f.set('tmp_fd08', c.builtin('cbool', [c.unary('not', c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_fd90')]))]))
    # tmp_FD80 = (tmp_FDB0 And tmp_FD08)
    f.set('tmp_fd80', c.binary('and', f.get('tmp_fdb0'), f.get('tmp_fd08')))
    # If tmp_FD80 Then GoTo L1BB7 Else GoTo L1BEB
    return 592 if truth(f.get('tmp_fd80')) else 597

def _doublemetaphone_592(f, c):
    # tmp_FED4 = "J"
    f.set('tmp_fed4', 'J')
    # tmp_FF28 = "K"
    f.set('tmp_ff28', 'K')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_597(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 Like "[EIY]")
    f.set('tmp_fed4', c.binary('like', f.get('tmp_ff28'), '[EIY]'))
    # ReDim tmp_FF24(0 To 1)
    f.redim('tmp_ff24', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FF24(0) = "AGGI"
    f.put('tmp_ff24', [Integer(0)], 'AGGI')
    # tmp_FF24(1) = "OGGI"
    f.put('tmp_ff24', [Integer(1)], 'OGGI')
    # tmp_FEC4 = VBA.Array("AGGI", "OGGI")
    f.set('tmp_fec4', c.builtin('vba.array', ['AGGI', 'OGGI']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FE74 = CBool(IsInArry(pWord, nCurrent, tmp_FEC4))
    f.set('tmp_fe74', c.builtin('cbool', [c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_fec4')])]))
    # tmp_FEB4 = (tmp_FED4 Or tmp_FE74)
    f.set('tmp_feb4', c.binary('or', f.get('tmp_fed4'), f.get('tmp_fe74')))
    # If tmp_FEB4 Then GoTo L1C73 Else GoTo L1E32
    return 608 if truth(f.get('tmp_feb4')) else 646

def _doublemetaphone_608(f, c):
    # ReDim tmp_FF24(0 To 1)
    f.redim('tmp_ff24', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FF24(0) = "VAN "
    f.put('tmp_ff24', [Integer(0)], 'VAN ')
    # tmp_FF24(1) = "VON "
    f.put('tmp_ff24', [Integer(1)], 'VON ')
    # tmp_FF28 = VBA.Array("VAN ", "VON ")
    f.set('tmp_ff28', c.builtin('vba.array', ['VAN ', 'VON ']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = 0
    f.set('tmp_ff3a', Integer(0))
    # ReDim tmp_FDE0(0 To 0)
    f.redim('tmp_fde0', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FDE0(0) = "SCH"
    f.put('tmp_fde0', [Integer(0)], 'SCH')
    # tmp_FED4 = VBA.Array("SCH")
    f.set('tmp_fed4', c.builtin('vba.array', ['SCH']))
    # Erase tmp_FDE0
    f.ref('tmp_fde0').value = EMPTY
    # tmp_FD7A = 0
    f.set('tmp_fd7a', Integer(0))
    # tmp_FE04 = CBool((IsInArry(pWord, tmp_FF3A, tmp_FF28) Or IsInArry(pWord, tmp_FD7A, tmp_FED4)))
    f.set('tmp_fe04', c.builtin('cbool', [c.binary('or', c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')]), c.call('isinarry', [f.ref('pword'), f.ref('tmp_fd7a'), f.ref('tmp_fed4')]))]))
    # tmp_FEF4 = CInt((nCurrent + 1))
    f.set('tmp_fef4', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FEC4 = pWord(tmp_FEF4)
    f.set('tmp_fec4', f.index('pword', f.get('tmp_fef4')))
    # tmp_FEB4 = (tmp_FEC4 = "E")
    f.set('tmp_feb4', c.binary('=', f.get('tmp_fec4'), 'E'))
    # tmp_FE64 = CInt((nCurrent + 2))
    f.set('tmp_fe64', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # tmp_FEA4 = pWord(tmp_FE64)
    f.set('tmp_fea4', f.index('pword', f.get('tmp_fe64')))
    # tmp_FE94 = (tmp_FEA4 = "T")
    f.set('tmp_fe94', c.binary('=', f.get('tmp_fea4'), 'T'))
    # tmp_FE54 = (tmp_FEB4 And tmp_FE94)
    f.set('tmp_fe54', c.binary('and', f.get('tmp_feb4'), f.get('tmp_fe94')))
    # tmp_FE44 = (tmp_FE04 Or tmp_FE54)
    f.set('tmp_fe44', c.binary('or', f.get('tmp_fe04'), f.get('tmp_fe54')))
    # If tmp_FE44 Then GoTo L1D67 Else GoTo L1D86
    return 629 if truth(f.get('tmp_fe44')) else 632

def _doublemetaphone_629(f, c):
    # tmp_FF28 = "K"
    f.set('tmp_ff28', 'K')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # GoTo L1E20
    return 644

def _doublemetaphone_632(f, c):
    # ReDim tmp_FF24(0 To 0)
    f.redim('tmp_ff24', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FF24(0) = "IER "
    f.put('tmp_ff24', [Integer(0)], 'IER ')
    # tmp_FF28 = VBA.Array("IER ")
    f.set('tmp_ff28', c.builtin('vba.array', ['IER ']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = (nCurrent + 1)
    f.set('tmp_ff3a', c.binary('+', f.get('ncurrent'), Integer(1)))
    # If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L1DD9 Else GoTo L1DF8
    return 638 if truth(c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')])) else 641

def _doublemetaphone_638(f, c):
    # tmp_FF28 = "J"
    f.set('tmp_ff28', 'J')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # GoTo L1E1E
    return 644

def _doublemetaphone_641(f, c):
    # tmp_FED4 = "K"
    f.set('tmp_fed4', 'K')
    # tmp_FF28 = "J"
    f.set('tmp_ff28', 'J')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    return 644

def _doublemetaphone_644(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_646(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # If (tmp_FF28 = "G") Then GoTo L1E57 Else GoTo L1E65
    return 649 if truth(c.binary('=', f.get('tmp_ff28'), 'G')) else 651

def _doublemetaphone_649(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L1E72
    return 652

def _doublemetaphone_651(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 652

def _doublemetaphone_652(f, c):
    # tmp_FF28 = "K"
    f.set('tmp_ff28', 'K')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # GoTo L3CD1
    return 1320

def _doublemetaphone_655(f, c):
    # If (tmp_FE84 = "H") Then GoTo L1EA3 Else GoTo L1F57
    return 656 if truth(c.binary('=', f.get('tmp_fe84'), 'H')) else 675

def _doublemetaphone_656(f, c):
    # If (nCurrent > 0) Then GoTo L1EAE Else GoTo L1ED4
    return 657 if truth(c.binary('>', f.get('ncurrent'), Integer(0))) else 661

def _doublemetaphone_657(f, c):
    # tmp_FF3C = CInt((nCurrent - 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('-', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 Like "[aeiouy]")
    f.set('tmp_fed4', c.binary('like', f.get('tmp_ff28'), '[aeiouy]'))
    # PreviousFlag = CInt(CBool(tmp_FED4))
    f.set('previousflag', c.builtin('cint', [c.builtin('cbool', [f.get('tmp_fed4')])]))
    return 661

def _doublemetaphone_661(f, c):
    # tmp_FEE4 = CBool((nCurrent = 0))
    f.set('tmp_fee4', c.builtin('cbool', [c.binary('=', f.get('ncurrent'), Integer(0))]))
    # tmp_FEF4 = CBool(PreviousFlag)
    f.set('tmp_fef4', c.builtin('cbool', [f.get('previousflag')]))
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 Like "[aeiouy]")
    f.set('tmp_fed4', c.binary('like', f.get('tmp_ff28'), '[aeiouy]'))
    # tmp_FEC4 = (tmp_FEF4 And tmp_FED4)
    f.set('tmp_fec4', c.binary('and', f.get('tmp_fef4'), f.get('tmp_fed4')))
    # tmp_FEB4 = (tmp_FEE4 Or tmp_FEC4)
    f.set('tmp_feb4', c.binary('or', f.get('tmp_fee4'), f.get('tmp_fec4')))
    # If tmp_FEB4 Then GoTo L1F1B Else GoTo L1F45
    return 669 if truth(f.get('tmp_feb4')) else 673

def _doublemetaphone_669(f, c):
    # tmp_FF28 = "H"
    f.set('tmp_ff28', 'H')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L1F52
    return 674

def _doublemetaphone_673(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 674

def _doublemetaphone_674(f, c):
    # GoTo L3CD1
    return 1320

def _doublemetaphone_675(f, c):
    # If (tmp_FE84 = "J") Then GoTo L1F67 Else GoTo L22F2
    return 676 if truth(c.binary('=', f.get('tmp_fe84'), 'J')) else 757

def _doublemetaphone_676(f, c):
    # ReDim tmp_FF24(0 To 0)
    f.redim('tmp_ff24', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FF24(0) = "JOSE"
    f.put('tmp_ff24', [Integer(0)], 'JOSE')
    # tmp_FF28 = VBA.Array("JOSE")
    f.set('tmp_ff28', c.builtin('vba.array', ['JOSE']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # ReDim tmp_FDE0(0 To 0)
    f.redim('tmp_fde0', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FDE0(0) = "SAN "
    f.put('tmp_fde0', [Integer(0)], 'SAN ')
    # tmp_FED4 = VBA.Array("SAN ")
    f.set('tmp_fed4', c.builtin('vba.array', ['SAN ']))
    # Erase tmp_FDE0
    f.ref('tmp_fde0').value = EMPTY
    # tmp_FF3A = 0
    f.set('tmp_ff3a', Integer(0))
    # If (IsInArry(pWord, nCurrent, tmp_FF28) Or IsInArry(pWord, tmp_FF3A, tmp_FED4)) Then GoTo L1FFC Else GoTo L20DD
    return 686 if truth(c.binary('or', c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')]), c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_fed4')]))) else 707

def _doublemetaphone_686(f, c):
    # tmp_FEF4 = CBool((nCurrent = 0))
    f.set('tmp_fef4', c.builtin('cbool', [c.binary('=', f.get('ncurrent'), Integer(0))]))
    # tmp_FF3C = CInt((nCurrent + 3))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(3))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 = " ")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), ' '))
    # tmp_FEC4 = (tmp_FEF4 And tmp_FED4)
    f.set('tmp_fec4', c.binary('and', f.get('tmp_fef4'), f.get('tmp_fed4')))
    # ReDim tmp_FF24(0 To 0)
    f.redim('tmp_ff24', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FF24(0) = "SAN "
    f.put('tmp_ff24', [Integer(0)], 'SAN ')
    # tmp_FEB4 = VBA.Array("SAN ")
    f.set('tmp_feb4', c.builtin('vba.array', ['SAN ']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = 1
    f.set('tmp_ff3a', Integer(1))
    # tmp_FE74 = CBool(IsInArry(pWord, tmp_FF3A, tmp_FEB4))
    f.set('tmp_fe74', c.builtin('cbool', [c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_feb4')])]))
    # tmp_FEA4 = (tmp_FEC4 Or tmp_FE74)
    f.set('tmp_fea4', c.binary('or', f.get('tmp_fec4'), f.get('tmp_fe74')))
    # If tmp_FEA4 Then GoTo L2086 Else GoTo L20A5
    return 699 if truth(f.get('tmp_fea4')) else 702

def _doublemetaphone_699(f, c):
    # tmp_FF28 = "H"
    f.set('tmp_ff28', 'H')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # GoTo L20CB
    return 705

def _doublemetaphone_702(f, c):
    # tmp_FED4 = "H"
    f.set('tmp_fed4', 'H')
    # tmp_FF28 = "J"
    f.set('tmp_ff28', 'J')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    return 705

def _doublemetaphone_705(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_707(f, c):
    # ReDim tmp_FF24(0 To 0)
    f.redim('tmp_ff24', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FF24(0) = "JOSE"
    f.put('tmp_ff24', [Integer(0)], 'JOSE')
    # tmp_FF28 = VBA.Array("JOSE")
    f.set('tmp_ff28', c.builtin('vba.array', ['JOSE']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = 0
    f.set('tmp_ff3a', Integer(0))
    # If ((nCurrent = 0) And (Not IsInArry(pWord, tmp_FF3A, tmp_FF28))) Then GoTo L2134 Else GoTo L215B
    return 713 if truth(c.binary('and', c.binary('=', f.get('ncurrent'), Integer(0)), c.unary('not', c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')])))) else 717

def _doublemetaphone_713(f, c):
    # tmp_FED4 = "A"
    f.set('tmp_fed4', 'A')
    # tmp_FF28 = "J"
    f.set('tmp_ff28', 'J')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # GoTo L22AD
    return 750

def _doublemetaphone_717(f, c):
    # tmp_FF28 = pWord(nCurrent)
    f.set('tmp_ff28', f.index('pword', f.get('ncurrent')))
    # tmp_FED4 = (tmp_FF28 Like "[aeiouy]")
    f.set('tmp_fed4', c.binary('like', f.get('tmp_ff28'), '[aeiouy]'))
    # tmp_FF04 = CBool((Not SlavoGermanic(pWord)))
    f.set('tmp_ff04', c.builtin('cbool', [c.unary('not', c.call('slavogermanic', [f.ref('pword')]))]))
    # tmp_FEC4 = (tmp_FED4 And tmp_FF04)
    f.set('tmp_fec4', c.binary('and', f.get('tmp_fed4'), f.get('tmp_ff04')))
    # tmp_FEF4 = CInt((nCurrent + 1))
    f.set('tmp_fef4', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FEB4 = pWord(tmp_FEF4)
    f.set('tmp_feb4', f.index('pword', f.get('tmp_fef4')))
    # tmp_FEA4 = (tmp_FEB4 = "A")
    f.set('tmp_fea4', c.binary('=', f.get('tmp_feb4'), 'A'))
    # tmp_FE64 = CInt((nCurrent + 2))
    f.set('tmp_fe64', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # tmp_FE94 = pWord(tmp_FE64)
    f.set('tmp_fe94', f.index('pword', f.get('tmp_fe64')))
    # tmp_FE54 = (tmp_FE94 = "O")
    f.set('tmp_fe54', c.binary('=', f.get('tmp_fe94'), 'O'))
    # tmp_FE44 = (tmp_FEA4 And tmp_FE54)
    f.set('tmp_fe44', c.binary('and', f.get('tmp_fea4'), f.get('tmp_fe54')))
    # tmp_FE34 = (tmp_FEC4 And tmp_FE44)
    f.set('tmp_fe34', c.binary('and', f.get('tmp_fec4'), f.get('tmp_fe44')))
    # If tmp_FE34 Then GoTo L21DB Else GoTo L2202
    return 730 if truth(f.get('tmp_fe34')) else 734

def _doublemetaphone_730(f, c):
    # tmp_FED4 = "H"
    f.set('tmp_fed4', 'H')
    # tmp_FF28 = "J"
    f.set('tmp_ff28', 'J')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # GoTo L22AB
    return 750

def _doublemetaphone_734(f, c):
    # If (nCurrent = (nLast - 1)) Then GoTo L2213 Else GoTo L223A
    return 735 if truth(c.binary('=', f.get('ncurrent'), c.binary('-', f.get('nlast'), Integer(1)))) else 739

def _doublemetaphone_735(f, c):
    # tmp_FED4 = " "
    f.set('tmp_fed4', ' ')
    # tmp_FF28 = "J"
    f.set('tmp_ff28', 'J')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # GoTo L22A9
    return 750

def _doublemetaphone_739(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 Like "[LTKSNMBZ]")
    f.set('tmp_fed4', c.binary('like', f.get('tmp_ff28'), '[LTKSNMBZ]'))
    # tmp_FEC4 = (Not tmp_FED4)
    f.set('tmp_fec4', c.unary('not', f.get('tmp_fed4')))
    # tmp_FEB4 = pWord(nCurrent)
    f.set('tmp_feb4', f.index('pword', f.get('ncurrent')))
    # tmp_FEA4 = (tmp_FEB4 Like "[SKL]")
    f.set('tmp_fea4', c.binary('like', f.get('tmp_feb4'), '[SKL]'))
    # tmp_FE94 = (Not tmp_FEA4)
    f.set('tmp_fe94', c.unary('not', f.get('tmp_fea4')))
    # tmp_FE54 = (tmp_FEC4 And tmp_FE94)
    f.set('tmp_fe54', c.binary('and', f.get('tmp_fec4'), f.get('tmp_fe94')))
    # If tmp_FE54 Then GoTo L228B Else GoTo L22A7
    return 748 if truth(f.get('tmp_fe54')) else 750

def _doublemetaphone_748(f, c):
    # tmp_FF28 = "J"
    f.set('tmp_ff28', 'J')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 750

def _doublemetaphone_750(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # If (tmp_FF28 = "J") Then GoTo L22D2 Else GoTo L22E0
    return 753 if truth(c.binary('=', f.get('tmp_ff28'), 'J')) else 755

def _doublemetaphone_753(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L22ED
    return 756

def _doublemetaphone_755(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 756

def _doublemetaphone_756(f, c):
    # GoTo L3CD1
    return 1320

def _doublemetaphone_757(f, c):
    # If (tmp_FE84 = "K") Then GoTo L2302 Else GoTo L2361
    return 758 if truth(c.binary('=', f.get('tmp_fe84'), 'K')) else 767

def _doublemetaphone_758(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # If (tmp_FF28 = "K") Then GoTo L2325 Else GoTo L2333
    return 761 if truth(c.binary('=', f.get('tmp_ff28'), 'K')) else 763

def _doublemetaphone_761(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L2340
    return 764

def _doublemetaphone_763(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 764

def _doublemetaphone_764(f, c):
    # tmp_FF28 = "K"
    f.set('tmp_ff28', 'K')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # GoTo L3CD1
    return 1320

def _doublemetaphone_767(f, c):
    # If (tmp_FE84 = "L") Then GoTo L2371 Else GoTo L255F
    return 768 if truth(c.binary('=', f.get('tmp_fe84'), 'L')) else 808

def _doublemetaphone_768(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # If (tmp_FF28 = "L") Then GoTo L2394 Else GoTo L2531
    return 771 if truth(c.binary('=', f.get('tmp_ff28'), 'L')) else 804

def _doublemetaphone_771(f, c):
    # If (nCurrent = ((nLength - 3) - 1)) Then GoTo L23A6 Else GoTo L2521
    return 772 if truth(c.binary('=', f.get('ncurrent'), c.binary('-', c.binary('-', f.get('nlength'), Integer(3)), Integer(1)))) else 802

def _doublemetaphone_772(f, c):
    # ReDim tmp_FF24(0 To 2)
    f.redim('tmp_ff24', [(Integer(0), Integer(2))], False, 'variant')
    # tmp_FF24(0) = "ILLO"
    f.put('tmp_ff24', [Integer(0)], 'ILLO')
    # tmp_FF24(1) = "ILLA"
    f.put('tmp_ff24', [Integer(1)], 'ILLA')
    # tmp_FF24(2) = "ALLE"
    f.put('tmp_ff24', [Integer(2)], 'ALLE')
    # tmp_FF28 = VBA.Array("ILLO", "ILLA", "ALLE")
    f.set('tmp_ff28', c.builtin('vba.array', ['ILLO', 'ILLA', 'ALLE']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FDD0 = CBool(IsInArry(pWord, nCurrent, tmp_FF28))
    f.set('tmp_fdd0', c.builtin('cbool', [c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')])]))
    # ReDim tmp_FDE0(0 To 1)
    f.redim('tmp_fde0', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FDE0(0) = "AS"
    f.put('tmp_fde0', [Integer(0)], 'AS')
    # tmp_FDE0(1) = "OS"
    f.put('tmp_fde0', [Integer(1)], 'OS')
    # tmp_FED4 = VBA.Array("AS", "OS")
    f.set('tmp_fed4', c.builtin('vba.array', ['AS', 'OS']))
    # Erase tmp_FDE0
    f.ref('tmp_fde0').value = EMPTY
    # tmp_FF3A = (nLast - 1)
    f.set('tmp_ff3a', c.binary('-', f.get('nlast'), Integer(1)))
    # tmp_FE24 = CBool(IsInArry(pWord, tmp_FF3A, tmp_FED4))
    f.set('tmp_fe24', c.builtin('cbool', [c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_fed4')])]))
    # tmp_FEC4 = pWord(nLast)
    f.set('tmp_fec4', f.index('pword', f.get('nlast')))
    # tmp_FEB4 = (tmp_FEC4 Like "[AO]")
    f.set('tmp_feb4', c.binary('like', f.get('tmp_fec4'), '[AO]'))
    # tmp_FEA4 = (tmp_FE24 Or tmp_FEB4)
    f.set('tmp_fea4', c.binary('or', f.get('tmp_fe24'), f.get('tmp_feb4')))
    # ReDim tmp_FD7C(0 To 0)
    f.redim('tmp_fd7c', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FD7C(0) = "ALLE"
    f.put('tmp_fd7c', [Integer(0)], 'ALLE')
    # tmp_FE94 = VBA.Array("ALLE")
    f.set('tmp_fe94', c.builtin('vba.array', ['ALLE']))
    # Erase tmp_FD7C
    f.ref('tmp_fd7c').value = EMPTY
    # tmp_FE04 = CBool(IsInArry(pWord, nCurrent, tmp_FE94))
    f.set('tmp_fe04', c.builtin('cbool', [c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_fe94')])]))
    # tmp_FE54 = (tmp_FEA4 And tmp_FE04)
    f.set('tmp_fe54', c.binary('and', f.get('tmp_fea4'), f.get('tmp_fe04')))
    # tmp_FE44 = (tmp_FDD0 Or tmp_FE54)
    f.set('tmp_fe44', c.binary('or', f.get('tmp_fdd0'), f.get('tmp_fe54')))
    # If tmp_FE44 Then GoTo L24EB Else GoTo L251F
    return 797 if truth(f.get('tmp_fe44')) else 802

def _doublemetaphone_797(f, c):
    # tmp_FED4 = " "
    f.set('tmp_fed4', ' ')
    # tmp_FF28 = "L"
    f.set('tmp_ff28', 'L')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_802(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L253E
    return 805

def _doublemetaphone_804(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 805

def _doublemetaphone_805(f, c):
    # tmp_FF28 = "L"
    f.set('tmp_ff28', 'L')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # GoTo L3CD1
    return 1320

def _doublemetaphone_808(f, c):
    # If (tmp_FE84 = "M") Then GoTo L256F Else GoTo L267D
    return 809 if truth(c.binary('=', f.get('tmp_fe84'), 'M')) else 835

def _doublemetaphone_809(f, c):
    # ReDim tmp_FF24(0 To 0)
    f.redim('tmp_ff24', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FF24(0) = "UMB"
    f.put('tmp_ff24', [Integer(0)], 'UMB')
    # tmp_FF28 = VBA.Array("UMB")
    f.set('tmp_ff28', c.builtin('vba.array', ['UMB']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FE14 = CBool(IsInArry(pWord, nCurrent, tmp_FF28))
    f.set('tmp_fe14', c.builtin('cbool', [c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')])]))
    # tmp_FE24 = CInt((((nCurrent + 1) = nLast) - 1))
    f.set('tmp_fe24', c.builtin('cint', [c.binary('-', c.binary('=', c.binary('+', f.get('ncurrent'), Integer(1)), f.get('nlast')), Integer(1))]))
    # tmp_FF14 = CInt((nCurrent + 2))
    f.set('tmp_ff14', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # tmp_FED4 = pWord(tmp_FF14)
    f.set('tmp_fed4', f.index('pword', f.get('tmp_ff14')))
    # tmp_FEC4 = (tmp_FED4 = "E")
    f.set('tmp_fec4', c.binary('=', f.get('tmp_fed4'), 'E'))
    # tmp_FEE4 = CInt((nCurrent + 3))
    f.set('tmp_fee4', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(3))]))
    # tmp_FEB4 = pWord(tmp_FEE4)
    f.set('tmp_feb4', f.index('pword', f.get('tmp_fee4')))
    # tmp_FEA4 = (tmp_FEB4 = "R")
    f.set('tmp_fea4', c.binary('=', f.get('tmp_feb4'), 'R'))
    # tmp_FE94 = (tmp_FEC4 And tmp_FEA4)
    f.set('tmp_fe94', c.binary('and', f.get('tmp_fec4'), f.get('tmp_fea4')))
    # tmp_FE54 = (tmp_FE24 Or tmp_FE94)
    f.set('tmp_fe54', c.binary('or', f.get('tmp_fe24'), f.get('tmp_fe94')))
    # tmp_FE44 = (tmp_FE14 And tmp_FE54)
    f.set('tmp_fe44', c.binary('and', f.get('tmp_fe14'), f.get('tmp_fe54')))
    # tmp_FE04 = CInt((nCurrent + 1))
    f.set('tmp_fe04', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FE34 = pWord(tmp_FE04)
    f.set('tmp_fe34', f.index('pword', f.get('tmp_fe04')))
    # tmp_FDF4 = (tmp_FE34 = "M")
    f.set('tmp_fdf4', c.binary('=', f.get('tmp_fe34'), 'M'))
    # tmp_FDE4 = (tmp_FE44 Or tmp_FDF4)
    f.set('tmp_fde4', c.binary('or', f.get('tmp_fe44'), f.get('tmp_fdf4')))
    # If tmp_FDE4 Then GoTo L2641 Else GoTo L264F
    return 829 if truth(f.get('tmp_fde4')) else 831

def _doublemetaphone_829(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L265C
    return 832

def _doublemetaphone_831(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 832

def _doublemetaphone_832(f, c):
    # tmp_FF28 = "M"
    f.set('tmp_ff28', 'M')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # GoTo L3CD1
    return 1320

def _doublemetaphone_835(f, c):
    # If (tmp_FE84 = "N") Then GoTo L268D Else GoTo L26EC
    return 836 if truth(c.binary('=', f.get('tmp_fe84'), 'N')) else 845

def _doublemetaphone_836(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # If (tmp_FF28 = "N") Then GoTo L26B0 Else GoTo L26BE
    return 839 if truth(c.binary('=', f.get('tmp_ff28'), 'N')) else 841

def _doublemetaphone_839(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L26CB
    return 842

def _doublemetaphone_841(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 842

def _doublemetaphone_842(f, c):
    # tmp_FF28 = "N"
    f.set('tmp_ff28', 'N')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # GoTo L3CD1
    return 1320

def _doublemetaphone_845(f, c):
    # If (tmp_FE84 = "Ñ") Then GoTo L26FC Else GoTo L2726
    return 846 if truth(c.binary('=', f.get('tmp_fe84'), 'Ñ')) else 850

def _doublemetaphone_846(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = "N"
    f.set('tmp_ff28', 'N')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # GoTo L3CD1
    return 1320

def _doublemetaphone_850(f, c):
    # If (tmp_FE84 = "P") Then GoTo L2736 Else GoTo L280F
    return 851 if truth(c.binary('=', f.get('tmp_fe84'), 'P')) else 872

def _doublemetaphone_851(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # If (tmp_FF28 = "H") Then GoTo L2759 Else GoTo L2785
    return 854 if truth(c.binary('=', f.get('tmp_ff28'), 'H')) else 858

def _doublemetaphone_854(f, c):
    # tmp_FF28 = "F"
    f.set('tmp_ff28', 'F')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_858(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 = "P")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'P'))
    # tmp_FEF4 = CInt((nCurrent + 2))
    f.set('tmp_fef4', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # tmp_FEC4 = pWord(tmp_FEF4)
    f.set('tmp_fec4', f.index('pword', f.get('tmp_fef4')))
    # tmp_FEB4 = (tmp_FEC4 = "B")
    f.set('tmp_feb4', c.binary('=', f.get('tmp_fec4'), 'B'))
    # tmp_FEA4 = (tmp_FED4 And tmp_FEB4)
    f.set('tmp_fea4', c.binary('and', f.get('tmp_fed4'), f.get('tmp_feb4')))
    # If tmp_FEA4 Then GoTo L27D3 Else GoTo L27E1
    return 866 if truth(f.get('tmp_fea4')) else 868

def _doublemetaphone_866(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L280A
    return 871

def _doublemetaphone_868(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = "P"
    f.set('tmp_ff28', 'P')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 871

def _doublemetaphone_871(f, c):
    # GoTo L3CD1
    return 1320

def _doublemetaphone_872(f, c):
    # If (tmp_FE84 = "Q") Then GoTo L281F Else GoTo L287E
    return 873 if truth(c.binary('=', f.get('tmp_fe84'), 'Q')) else 882

def _doublemetaphone_873(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # If (tmp_FF28 = "Q") Then GoTo L2842 Else GoTo L2850
    return 876 if truth(c.binary('=', f.get('tmp_ff28'), 'Q')) else 878

def _doublemetaphone_876(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L285D
    return 879

def _doublemetaphone_878(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 879

def _doublemetaphone_879(f, c):
    # tmp_FF28 = "K"
    f.set('tmp_ff28', 'K')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # GoTo L3CD1
    return 1320

def _doublemetaphone_882(f, c):
    # If (tmp_FE84 = "R") Then GoTo L288E Else GoTo L29F2
    return 883 if truth(c.binary('=', f.get('tmp_fe84'), 'R')) else 915

def _doublemetaphone_883(f, c):
    # If ((nCurrent = (nLast - 1)) And (Not SlavoGermanic(pWord))) Then GoTo L28A7 Else GoTo L298F
    return 884 if truth(c.binary('and', c.binary('=', f.get('ncurrent'), c.binary('-', f.get('nlast'), Integer(1))), c.unary('not', c.call('slavogermanic', [f.ref('pword')])))) else 906

def _doublemetaphone_884(f, c):
    # tmp_FF28 = pWord(nCurrent)
    f.set('tmp_ff28', f.index('pword', f.get('ncurrent')))
    # tmp_FED4 = (tmp_FF28 = "I")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'I'))
    # tmp_FF04 = CInt((nCurrent + 1))
    f.set('tmp_ff04', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FEC4 = pWord(tmp_FF04)
    f.set('tmp_fec4', f.index('pword', f.get('tmp_ff04')))
    # tmp_FEB4 = (tmp_FEC4 = "E")
    f.set('tmp_feb4', c.binary('=', f.get('tmp_fec4'), 'E'))
    # tmp_FEA4 = (tmp_FED4 And tmp_FEB4)
    f.set('tmp_fea4', c.binary('and', f.get('tmp_fed4'), f.get('tmp_feb4')))
    # If tmp_FEA4 Then GoTo L28F0 Else GoTo L2983
    return 891 if truth(f.get('tmp_fea4')) else 904

def _doublemetaphone_891(f, c):
    # ReDim tmp_FF24(0 To 1)
    f.redim('tmp_ff24', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FF24(0) = "ME"
    f.put('tmp_ff24', [Integer(0)], 'ME')
    # tmp_FF24(1) = "MA"
    f.put('tmp_ff24', [Integer(1)], 'MA')
    # tmp_FF28 = VBA.Array("ME", "MA")
    f.set('tmp_ff28', c.builtin('vba.array', ['ME', 'MA']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = (nCurrent - 2)
    f.set('tmp_ff3a', c.binary('-', f.get('ncurrent'), Integer(2)))
    # If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L2950 Else GoTo L2977
    return 898 if truth(c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')])) else 902

def _doublemetaphone_898(f, c):
    # tmp_FED4 = "R"
    f.set('tmp_fed4', 'R')
    # tmp_FF28 = ""
    f.set('tmp_ff28', '')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # GoTo L297E
    return 903

def _doublemetaphone_902(f, c):
    # GoTo L2991
    return 906

def _doublemetaphone_903(f, c):
    # GoTo L298A
    return 905

def _doublemetaphone_904(f, c):
    # GoTo L2991
    return 906

def _doublemetaphone_905(f, c):
    # GoTo L29AD
    return 908

def _doublemetaphone_906(f, c):
    # tmp_FF28 = "R"
    f.set('tmp_ff28', 'R')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 908

def _doublemetaphone_908(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # If (tmp_FF28 = "R") Then GoTo L29D2 Else GoTo L29E0
    return 911 if truth(c.binary('=', f.get('tmp_ff28'), 'R')) else 913

def _doublemetaphone_911(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L29ED
    return 914

def _doublemetaphone_913(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 914

def _doublemetaphone_914(f, c):
    # GoTo L3CD1
    return 1320

def _doublemetaphone_915(f, c):
    # If (tmp_FE84 = "S") Then GoTo L2A02 Else GoTo L31ED
    return 916 if truth(c.binary('=', f.get('tmp_fe84'), 'S')) else 1086

def _doublemetaphone_916(f, c):
    # ReDim tmp_FF24(0 To 1)
    f.redim('tmp_ff24', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FF24(0) = "ISL"
    f.put('tmp_ff24', [Integer(0)], 'ISL')
    # tmp_FF24(1) = "YSL"
    f.put('tmp_ff24', [Integer(1)], 'YSL')
    # tmp_FF28 = VBA.Array("ISL", "YSL")
    f.set('tmp_ff28', c.builtin('vba.array', ['ISL', 'YSL']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # If IsInArry(pWord, nCurrent, tmp_FF28) Then GoTo L2A5C Else GoTo L2A6C
    return 922 if truth(c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')])) else 924

def _doublemetaphone_922(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_924(f, c):
    # ReDim tmp_FF24(0 To 0)
    f.redim('tmp_ff24', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FF24(0) = "SUGAR"
    f.put('tmp_ff24', [Integer(0)], 'SUGAR')
    # tmp_FF28 = VBA.Array("SUGAR")
    f.set('tmp_ff28', c.builtin('vba.array', ['SUGAR']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # If ((nCurrent = 0) And IsInArry(pWord, nCurrent, tmp_FF28)) Then GoTo L2AC0 Else GoTo L2AF4
    return 929 if truth(c.binary('and', c.binary('=', f.get('ncurrent'), Integer(0)), c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')]))) else 934

def _doublemetaphone_929(f, c):
    # tmp_FED4 = "S"
    f.set('tmp_fed4', 'S')
    # tmp_FF28 = "X"
    f.set('tmp_ff28', 'X')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_934(f, c):
    # tmp_FF28 = pWord(nCurrent)
    f.set('tmp_ff28', f.index('pword', f.get('ncurrent')))
    # tmp_FED4 = (tmp_FF28 = "S")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'S'))
    # tmp_FF04 = CInt((nCurrent + 1))
    f.set('tmp_ff04', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FEC4 = pWord(tmp_FF04)
    f.set('tmp_fec4', f.index('pword', f.get('tmp_ff04')))
    # tmp_FEB4 = (tmp_FEC4 = "H")
    f.set('tmp_feb4', c.binary('=', f.get('tmp_fec4'), 'H'))
    # tmp_FEA4 = (tmp_FED4 And tmp_FEB4)
    f.set('tmp_fea4', c.binary('and', f.get('tmp_fed4'), f.get('tmp_feb4')))
    # If tmp_FEA4 Then GoTo L2B3F Else GoTo L2C0C
    return 941 if truth(f.get('tmp_fea4')) else 957

def _doublemetaphone_941(f, c):
    # ReDim tmp_FF24(0 To 3)
    f.redim('tmp_ff24', [(Integer(0), Integer(3))], False, 'variant')
    # tmp_FF24(0) = "HEIM"
    f.put('tmp_ff24', [Integer(0)], 'HEIM')
    # tmp_FF24(1) = "HOEK"
    f.put('tmp_ff24', [Integer(1)], 'HOEK')
    # tmp_FF24(2) = "HOLM"
    f.put('tmp_ff24', [Integer(2)], 'HOLM')
    # tmp_FF24(3) = "HOLZ"
    f.put('tmp_ff24', [Integer(3)], 'HOLZ')
    # tmp_FF28 = VBA.Array("HEIM", "HOEK", "HOLM", "HOLZ")
    f.set('tmp_ff28', c.builtin('vba.array', ['HEIM', 'HOEK', 'HOLM', 'HOLZ']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = (nCurrent + 1)
    f.set('tmp_ff3a', c.binary('+', f.get('ncurrent'), Integer(1)))
    # If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L2BBD Else GoTo L2BDC
    return 950 if truth(c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')])) else 953

def _doublemetaphone_950(f, c):
    # tmp_FF28 = "S"
    f.set('tmp_ff28', 'S')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # GoTo L2BFA
    return 955

def _doublemetaphone_953(f, c):
    # tmp_FF28 = "X"
    f.set('tmp_ff28', 'X')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 955

def _doublemetaphone_955(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_957(f, c):
    # ReDim tmp_FF24(0 To 1)
    f.redim('tmp_ff24', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FF24(0) = "SIO"
    f.put('tmp_ff24', [Integer(0)], 'SIO')
    # tmp_FF24(1) = "SIA"
    f.put('tmp_ff24', [Integer(1)], 'SIA')
    # tmp_FF28 = VBA.Array("SIO", "SIA")
    f.set('tmp_ff28', c.builtin('vba.array', ['SIO', 'SIA']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # ReDim tmp_FDE0(0 To 0)
    f.redim('tmp_fde0', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FDE0(0) = "SIAN"
    f.put('tmp_fde0', [Integer(0)], 'SIAN')
    # tmp_FED4 = VBA.Array("SIAN")
    f.set('tmp_fed4', c.builtin('vba.array', ['SIAN']))
    # Erase tmp_FDE0
    f.ref('tmp_fde0').value = EMPTY
    # If (IsInArry(pWord, nCurrent, tmp_FF28) Or IsInArry(pWord, nCurrent, tmp_FED4)) Then GoTo L2CB0 Else GoTo L2D15
    return 967 if truth(c.binary('or', c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')]), c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_fed4')]))) else 976

def _doublemetaphone_967(f, c):
    # If (Not SlavoGermanic(pWord)) Then GoTo L2CBE Else GoTo L2CE5
    return 968 if truth(c.unary('not', c.call('slavogermanic', [f.ref('pword')]))) else 972

def _doublemetaphone_968(f, c):
    # tmp_FED4 = "X"
    f.set('tmp_fed4', 'X')
    # tmp_FF28 = "S"
    f.set('tmp_ff28', 'S')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # GoTo L2D03
    return 974

def _doublemetaphone_972(f, c):
    # tmp_FF28 = "S"
    f.set('tmp_ff28', 'S')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 974

def _doublemetaphone_974(f, c):
    # nCurrent = CInt((nCurrent + 3))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(3))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_976(f, c):
    # tmp_FEF4 = CBool((nCurrent = 0))
    f.set('tmp_fef4', c.builtin('cbool', [c.binary('=', f.get('ncurrent'), Integer(0))]))
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 Like "[MNLW]")
    f.set('tmp_fed4', c.binary('like', f.get('tmp_ff28'), '[MNLW]'))
    # tmp_FEC4 = (tmp_FEF4 And tmp_FED4)
    f.set('tmp_fec4', c.binary('and', f.get('tmp_fef4'), f.get('tmp_fed4')))
    # tmp_FEE4 = CInt((nCurrent + 1))
    f.set('tmp_fee4', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FEB4 = pWord(tmp_FEE4)
    f.set('tmp_feb4', f.index('pword', f.get('tmp_fee4')))
    # tmp_FEA4 = (tmp_FEB4 = "Z")
    f.set('tmp_fea4', c.binary('=', f.get('tmp_feb4'), 'Z'))
    # tmp_FE94 = (tmp_FEC4 Or tmp_FEA4)
    f.set('tmp_fe94', c.binary('or', f.get('tmp_fec4'), f.get('tmp_fea4')))
    # If tmp_FE94 Then GoTo L2D72 Else GoTo L2DDB
    return 986 if truth(f.get('tmp_fe94')) else 996

def _doublemetaphone_986(f, c):
    # tmp_FED4 = "X"
    f.set('tmp_fed4', 'X')
    # tmp_FF28 = "S"
    f.set('tmp_ff28', 'S')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # If (tmp_FF28 = "Z") Then GoTo L2DB9 Else GoTo L2DC7
    return 992 if truth(c.binary('=', f.get('tmp_ff28'), 'Z')) else 994

def _doublemetaphone_992(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L2DD4
    return 995

def _doublemetaphone_994(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 995

def _doublemetaphone_995(f, c):
    # GoTo L3CD3
    return 1320

def _doublemetaphone_996(f, c):
    # tmp_FF28 = pWord(nCurrent)
    f.set('tmp_ff28', f.index('pword', f.get('ncurrent')))
    # tmp_FED4 = (tmp_FF28 = "S")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'S'))
    # tmp_FF04 = CInt((nCurrent + 1))
    f.set('tmp_ff04', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FEC4 = pWord(tmp_FF04)
    f.set('tmp_fec4', f.index('pword', f.get('tmp_ff04')))
    # tmp_FEB4 = (tmp_FEC4 = "C")
    f.set('tmp_feb4', c.binary('=', f.get('tmp_fec4'), 'C'))
    # tmp_FEA4 = (tmp_FED4 And tmp_FEB4)
    f.set('tmp_fea4', c.binary('and', f.get('tmp_fed4'), f.get('tmp_feb4')))
    # If tmp_FEA4 Then GoTo L2E26 Else GoTo L30D3
    return 1003 if truth(f.get('tmp_fea4')) else 1062

def _doublemetaphone_1003(f, c):
    # tmp_FF3C = CInt((nCurrent + 2))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # If (tmp_FF28 = "H") Then GoTo L2E49 Else GoTo L3051
    return 1006 if truth(c.binary('=', f.get('tmp_ff28'), 'H')) else 1050

def _doublemetaphone_1006(f, c):
    # ReDim tmp_FF24(0 To 5)
    f.redim('tmp_ff24', [(Integer(0), Integer(5))], False, 'variant')
    # tmp_FF24(0) = "OO"
    f.put('tmp_ff24', [Integer(0)], 'OO')
    # tmp_FF24(1) = "ER"
    f.put('tmp_ff24', [Integer(1)], 'ER')
    # tmp_FF24(2) = "EN"
    f.put('tmp_ff24', [Integer(2)], 'EN')
    # tmp_FF24(3) = "UY"
    f.put('tmp_ff24', [Integer(3)], 'UY')
    # tmp_FF24(4) = "ED"
    f.put('tmp_ff24', [Integer(4)], 'ED')
    # tmp_FF24(5) = "EM"
    f.put('tmp_ff24', [Integer(5)], 'EM')
    # tmp_FF28 = VBA.Array("OO", "ER", "EN", "UY", "ED", "EM")
    f.set('tmp_ff28', c.builtin('vba.array', ['OO', 'ER', 'EN', 'UY', 'ED', 'EM']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = (nCurrent + 3)
    f.set('tmp_ff3a', c.binary('+', f.get('ncurrent'), Integer(3)))
    # If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L2EE5 Else GoTo L2F9F
    return 1017 if truth(c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')])) else 1033

def _doublemetaphone_1017(f, c):
    # ReDim tmp_FF24(0 To 1)
    f.redim('tmp_ff24', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FF24(0) = "ER"
    f.put('tmp_ff24', [Integer(0)], 'ER')
    # tmp_FF24(1) = "EN"
    f.put('tmp_ff24', [Integer(1)], 'EN')
    # tmp_FF28 = VBA.Array("ER", "EN")
    f.set('tmp_ff28', c.builtin('vba.array', ['ER', 'EN']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = (nCurrent + 3)
    f.set('tmp_ff3a', c.binary('+', f.get('ncurrent'), Integer(3)))
    # If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L2F45 Else GoTo L2F6C
    return 1024 if truth(c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')])) else 1028

def _doublemetaphone_1024(f, c):
    # tmp_FED4 = "SK"
    f.set('tmp_fed4', 'SK')
    # tmp_FF28 = "X"
    f.set('tmp_ff28', 'X')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # GoTo L2F8A
    return 1030

def _doublemetaphone_1028(f, c):
    # tmp_FF28 = "SK"
    f.set('tmp_ff28', 'SK')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 1030

def _doublemetaphone_1030(f, c):
    # nCurrent = CInt((nCurrent + 3))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(3))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_1032(f, c):
    # GoTo L304F
    return 1050

def _doublemetaphone_1033(f, c):
    # tmp_FEF4 = CBool((nCurrent = 0))
    f.set('tmp_fef4', c.builtin('cbool', [c.binary('=', f.get('ncurrent'), Integer(0))]))
    # tmp_FF28 = pWord(2)
    f.set('tmp_ff28', f.index('pword', Integer(2)))
    # tmp_FED4 = (tmp_FF28 Like "[aeiouy]")
    f.set('tmp_fed4', c.binary('like', f.get('tmp_ff28'), '[aeiouy]'))
    # tmp_FEC4 = (Not tmp_FED4)
    f.set('tmp_fec4', c.unary('not', f.get('tmp_fed4')))
    # tmp_FEB4 = (tmp_FEF4 And tmp_FEC4)
    f.set('tmp_feb4', c.binary('and', f.get('tmp_fef4'), f.get('tmp_fec4')))
    # tmp_FEA4 = pWord(2)
    f.set('tmp_fea4', f.index('pword', Integer(2)))
    # tmp_FE94 = (tmp_FEA4 <> "W")
    f.set('tmp_fe94', c.binary('<>', f.get('tmp_fea4'), 'W'))
    # tmp_FE54 = (tmp_FEB4 And tmp_FE94)
    f.set('tmp_fe54', c.binary('and', f.get('tmp_feb4'), f.get('tmp_fe94')))
    # If tmp_FE54 Then GoTo L2FF8 Else GoTo L301F
    return 1042 if truth(f.get('tmp_fe54')) else 1046

def _doublemetaphone_1042(f, c):
    # tmp_FED4 = "S"
    f.set('tmp_fed4', 'S')
    # tmp_FF28 = "X"
    f.set('tmp_ff28', 'X')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # GoTo L303D
    return 1048

def _doublemetaphone_1046(f, c):
    # tmp_FF28 = "X"
    f.set('tmp_ff28', 'X')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 1048

def _doublemetaphone_1048(f, c):
    # nCurrent = CInt((nCurrent + 3))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(3))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_1050(f, c):
    # tmp_FF3C = CInt((nCurrent + 2))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 Like "[IEY]")
    f.set('tmp_fed4', c.binary('like', f.get('tmp_ff28'), '[IEY]'))
    # If tmp_FED4 Then GoTo L3079 Else GoTo L30A5
    return 1054 if truth(f.get('tmp_fed4')) else 1058

def _doublemetaphone_1054(f, c):
    # tmp_FF28 = "S"
    f.set('tmp_ff28', 'S')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 3))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(3))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_1058(f, c):
    # tmp_FF28 = "SK"
    f.set('tmp_ff28', 'SK')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 3))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(3))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_1062(f, c):
    # ReDim tmp_FF24(0 To 1)
    f.redim('tmp_ff24', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FF24(0) = "AI"
    f.put('tmp_ff24', [Integer(0)], 'AI')
    # tmp_FF24(1) = "OI"
    f.put('tmp_ff24', [Integer(1)], 'OI')
    # tmp_FF28 = VBA.Array("AI", "OI")
    f.set('tmp_ff28', c.builtin('vba.array', ['AI', 'OI']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # If ((nCurrent = (nLast - 1)) And IsInArry(pWord, nCurrent, tmp_FF28)) Then GoTo L313A Else GoTo L3161
    return 1068 if truth(c.binary('and', c.binary('=', f.get('ncurrent'), c.binary('-', f.get('nlast'), Integer(1))), c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')]))) else 1072

def _doublemetaphone_1068(f, c):
    # tmp_FED4 = "S"
    f.set('tmp_fed4', 'S')
    # tmp_FF28 = ""
    f.set('tmp_ff28', '')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # GoTo L317F
    return 1074

def _doublemetaphone_1072(f, c):
    # tmp_FF28 = "S"
    f.set('tmp_ff28', 'S')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 1074

def _doublemetaphone_1074(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 = "S")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'S'))
    # tmp_FEF4 = CInt((nCurrent + 2))
    f.set('tmp_fef4', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # tmp_FEC4 = pWord(tmp_FEF4)
    f.set('tmp_fec4', f.index('pword', f.get('tmp_fef4')))
    # tmp_FEB4 = (tmp_FEC4 = "Z")
    f.set('tmp_feb4', c.binary('=', f.get('tmp_fec4'), 'Z'))
    # tmp_FEA4 = (tmp_FED4 And tmp_FEB4)
    f.set('tmp_fea4', c.binary('and', f.get('tmp_fed4'), f.get('tmp_feb4')))
    # If tmp_FEA4 Then GoTo L31CD Else GoTo L31DB
    return 1082 if truth(f.get('tmp_fea4')) else 1084

def _doublemetaphone_1082(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L31E8
    return 1085

def _doublemetaphone_1084(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 1085

def _doublemetaphone_1085(f, c):
    # GoTo L3CD1
    return 1320

def _doublemetaphone_1086(f, c):
    # If (tmp_FE84 = "T") Then GoTo L31FD Else GoTo L3578
    return 1087 if truth(c.binary('=', f.get('tmp_fe84'), 'T')) else 1159

def _doublemetaphone_1087(f, c):
    # ReDim tmp_FF24(0 To 0)
    f.redim('tmp_ff24', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FF24(0) = "TION"
    f.put('tmp_ff24', [Integer(0)], 'TION')
    # tmp_FF28 = VBA.Array("TION")
    f.set('tmp_ff28', c.builtin('vba.array', ['TION']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # If IsInArry(pWord, nCurrent, tmp_FF28) Then GoTo L3248 Else GoTo L3274
    return 1092 if truth(c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')])) else 1096

def _doublemetaphone_1092(f, c):
    # tmp_FF28 = "X"
    f.set('tmp_ff28', 'X')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 3))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(3))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_1096(f, c):
    # ReDim tmp_FF24(0 To 1)
    f.redim('tmp_ff24', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FF24(0) = "TIA"
    f.put('tmp_ff24', [Integer(0)], 'TIA')
    # tmp_FF24(1) = "TCH"
    f.put('tmp_ff24', [Integer(1)], 'TCH')
    # tmp_FF28 = VBA.Array("TIA", "TCH")
    f.set('tmp_ff28', c.builtin('vba.array', ['TIA', 'TCH']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # If IsInArry(pWord, nCurrent, tmp_FF28) Then GoTo L32D0 Else GoTo L32FC
    return 1102 if truth(c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')])) else 1106

def _doublemetaphone_1102(f, c):
    # tmp_FF28 = "X"
    f.set('tmp_ff28', 'X')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 3))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(3))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_1106(f, c):
    # tmp_FF28 = pWord(nCurrent)
    f.set('tmp_ff28', f.index('pword', f.get('ncurrent')))
    # tmp_FED4 = (tmp_FF28 = "T")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'T'))
    # tmp_FF04 = CInt((nCurrent + 1))
    f.set('tmp_ff04', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FEC4 = pWord(tmp_FF04)
    f.set('tmp_fec4', f.index('pword', f.get('tmp_ff04')))
    # tmp_FEB4 = (tmp_FEC4 = "H")
    f.set('tmp_feb4', c.binary('=', f.get('tmp_fec4'), 'H'))
    # tmp_FEA4 = (tmp_FED4 And tmp_FEB4)
    f.set('tmp_fea4', c.binary('and', f.get('tmp_fed4'), f.get('tmp_feb4')))
    # ReDim tmp_FF24(0 To 0)
    f.redim('tmp_ff24', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FF24(0) = "TTH"
    f.put('tmp_ff24', [Integer(0)], 'TTH')
    # tmp_FE94 = VBA.Array("TTH")
    f.set('tmp_fe94', c.builtin('vba.array', ['TTH']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FE64 = CBool(IsInArry(pWord, nCurrent, tmp_FE94))
    f.set('tmp_fe64', c.builtin('cbool', [c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_fe94')])]))
    # tmp_FE54 = (tmp_FEA4 Or tmp_FE64)
    f.set('tmp_fe54', c.binary('or', f.get('tmp_fea4'), f.get('tmp_fe64')))
    # If tmp_FE54 Then GoTo L3396 Else GoTo L34EE
    return 1119 if truth(f.get('tmp_fe54')) else 1145

def _doublemetaphone_1119(f, c):
    # ReDim tmp_FF24(0 To 1)
    f.redim('tmp_ff24', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FF24(0) = "OM"
    f.put('tmp_ff24', [Integer(0)], 'OM')
    # tmp_FF24(1) = "AM"
    f.put('tmp_ff24', [Integer(1)], 'AM')
    # tmp_FF28 = VBA.Array("OM", "AM")
    f.set('tmp_ff28', c.builtin('vba.array', ['OM', 'AM']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = (nCurrent + 2)
    f.set('tmp_ff3a', c.binary('+', f.get('ncurrent'), Integer(2)))
    # ReDim tmp_FDE0(0 To 1)
    f.redim('tmp_fde0', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FDE0(0) = "VAN "
    f.put('tmp_fde0', [Integer(0)], 'VAN ')
    # tmp_FDE0(1) = "VON "
    f.put('tmp_fde0', [Integer(1)], 'VON ')
    # tmp_FED4 = VBA.Array("VAN ", "VON ")
    f.set('tmp_fed4', c.builtin('vba.array', ['VAN ', 'VON ']))
    # Erase tmp_FDE0
    f.ref('tmp_fde0').value = EMPTY
    # tmp_FD7A = 1
    f.set('tmp_fd7a', Integer(1))
    # ReDim tmp_FD7C(0 To 0)
    f.redim('tmp_fd7c', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FD7C(0) = "SCH"
    f.put('tmp_fd7c', [Integer(0)], 'SCH')
    # tmp_FEC4 = VBA.Array("SCH")
    f.set('tmp_fec4', c.builtin('vba.array', ['SCH']))
    # Erase tmp_FD7C
    f.ref('tmp_fd7c').value = EMPTY
    # tmp_FD72 = 0
    f.set('tmp_fd72', Integer(0))
    # If ((IsInArry(pWord, tmp_FF3A, tmp_FF28) Or IsInArry(pWord, tmp_FD7A, tmp_FED4)) Or IsInArry(pWord, tmp_FD72, tmp_FEC4)) Then GoTo L3497 Else GoTo L34B6
    return 1137 if truth(c.binary('or', c.binary('or', c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')]), c.call('isinarry', [f.ref('pword'), f.ref('tmp_fd7a'), f.ref('tmp_fed4')])), c.call('isinarry', [f.ref('pword'), f.ref('tmp_fd72'), f.ref('tmp_fec4')]))) else 1140

def _doublemetaphone_1137(f, c):
    # tmp_FF28 = "T"
    f.set('tmp_ff28', 'T')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # GoTo L34DC
    return 1143

def _doublemetaphone_1140(f, c):
    # tmp_FED4 = "T"
    f.set('tmp_fed4', 'T')
    # tmp_FF28 = "0"
    f.set('tmp_ff28', '0')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    return 1143

def _doublemetaphone_1143(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_1145(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 = "T")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'T'))
    # tmp_FEF4 = CInt((nCurrent + 2))
    f.set('tmp_fef4', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # tmp_FEC4 = pWord(tmp_FEF4)
    f.set('tmp_fec4', f.index('pword', f.get('tmp_fef4')))
    # tmp_FEB4 = (tmp_FEC4 = "D")
    f.set('tmp_feb4', c.binary('=', f.get('tmp_fec4'), 'D'))
    # tmp_FEA4 = (tmp_FED4 And tmp_FEB4)
    f.set('tmp_fea4', c.binary('and', f.get('tmp_fed4'), f.get('tmp_feb4')))
    # If tmp_FEA4 Then GoTo L353C Else GoTo L354A
    return 1153 if truth(f.get('tmp_fea4')) else 1155

def _doublemetaphone_1153(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3573
    return 1158

def _doublemetaphone_1155(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = "T"
    f.set('tmp_ff28', 'T')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 1158

def _doublemetaphone_1158(f, c):
    # GoTo L3CD1
    return 1320

def _doublemetaphone_1159(f, c):
    # If (tmp_FE84 = "V") Then GoTo L3588 Else GoTo L35E7
    return 1160 if truth(c.binary('=', f.get('tmp_fe84'), 'V')) else 1169

def _doublemetaphone_1160(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # If (tmp_FF28 = "V") Then GoTo L35AB Else GoTo L35B9
    return 1163 if truth(c.binary('=', f.get('tmp_ff28'), 'V')) else 1165

def _doublemetaphone_1163(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L35E2
    return 1168

def _doublemetaphone_1165(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = "F"
    f.set('tmp_ff28', 'F')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 1168

def _doublemetaphone_1168(f, c):
    # GoTo L3CD1
    return 1320

def _doublemetaphone_1169(f, c):
    # If (tmp_FE84 = "W") Then GoTo L35F7 Else GoTo L3932
    return 1170 if truth(c.binary('=', f.get('tmp_fe84'), 'W')) else 1243

def _doublemetaphone_1170(f, c):
    # tmp_FF28 = pWord(nCurrent)
    f.set('tmp_ff28', f.index('pword', f.get('ncurrent')))
    # tmp_FED4 = (tmp_FF28 = "W")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'W'))
    # tmp_FF04 = CInt((nCurrent + 1))
    f.set('tmp_ff04', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FEC4 = pWord(tmp_FF04)
    f.set('tmp_fec4', f.index('pword', f.get('tmp_ff04')))
    # tmp_FEB4 = (tmp_FEC4 = "R")
    f.set('tmp_feb4', c.binary('=', f.get('tmp_fec4'), 'R'))
    # tmp_FEA4 = (tmp_FED4 And tmp_FEB4)
    f.set('tmp_fea4', c.binary('and', f.get('tmp_fed4'), f.get('tmp_feb4')))
    # If tmp_FEA4 Then GoTo L3640 Else GoTo L366C
    return 1177 if truth(f.get('tmp_fea4')) else 1181

def _doublemetaphone_1177(f, c):
    # tmp_FF28 = "R"
    f.set('tmp_ff28', 'R')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_1181(f, c):
    # tmp_FEF4 = CBool((nCurrent = 0))
    f.set('tmp_fef4', c.builtin('cbool', [c.binary('=', f.get('ncurrent'), Integer(0))]))
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 Like "[aeiouy]")
    f.set('tmp_fed4', c.binary('like', f.get('tmp_ff28'), '[aeiouy]'))
    # tmp_FEC4 = (tmp_FEF4 And tmp_FED4)
    f.set('tmp_fec4', c.binary('and', f.get('tmp_fef4'), f.get('tmp_fed4')))
    # tmp_FEB4 = pWord(nCurrent)
    f.set('tmp_feb4', f.index('pword', f.get('ncurrent')))
    # tmp_FEA4 = (tmp_FEB4 = "W")
    f.set('tmp_fea4', c.binary('=', f.get('tmp_feb4'), 'W'))
    # tmp_FE64 = CInt((nCurrent + 1))
    f.set('tmp_fe64', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FE94 = pWord(tmp_FE64)
    f.set('tmp_fe94', f.index('pword', f.get('tmp_fe64')))
    # tmp_FE54 = (tmp_FE94 = "H")
    f.set('tmp_fe54', c.binary('=', f.get('tmp_fe94'), 'H'))
    # tmp_FE44 = (tmp_FEA4 And tmp_FE54)
    f.set('tmp_fe44', c.binary('and', f.get('tmp_fea4'), f.get('tmp_fe54')))
    # tmp_FE34 = (tmp_FEC4 Or tmp_FE44)
    f.set('tmp_fe34', c.binary('or', f.get('tmp_fec4'), f.get('tmp_fe44')))
    # If tmp_FE34 Then GoTo L36E9 Else GoTo L3756
    return 1194 if truth(f.get('tmp_fe34')) else 1204

def _doublemetaphone_1194(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 Like "[aeiouy]")
    f.set('tmp_fed4', c.binary('like', f.get('tmp_ff28'), '[aeiouy]'))
    # If tmp_FED4 Then GoTo L370F Else GoTo L3736
    return 1198 if truth(f.get('tmp_fed4')) else 1202

def _doublemetaphone_1198(f, c):
    # tmp_FED4 = "F"
    f.set('tmp_fed4', 'F')
    # tmp_FF28 = "A"
    f.set('tmp_ff28', 'A')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # GoTo L3754
    return 1204

def _doublemetaphone_1202(f, c):
    # tmp_FF28 = "R"
    f.set('tmp_ff28', 'R')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 1204

def _doublemetaphone_1204(f, c):
    # tmp_FF04 = CBool((nCurrent = (nLast - 1)))
    f.set('tmp_ff04', c.builtin('cbool', [c.binary('=', f.get('ncurrent'), c.binary('-', f.get('nlast'), Integer(1)))]))
    # tmp_FF28 = pWord(nCurrent)
    f.set('tmp_ff28', f.index('pword', f.get('ncurrent')))
    # tmp_FED4 = (tmp_FF28 Like "[aeiouy]")
    f.set('tmp_fed4', c.binary('like', f.get('tmp_ff28'), '[aeiouy]'))
    # tmp_FEC4 = (tmp_FF04 And tmp_FED4)
    f.set('tmp_fec4', c.binary('and', f.get('tmp_ff04'), f.get('tmp_fed4')))
    # ReDim tmp_FF24(0 To 3)
    f.redim('tmp_ff24', [(Integer(0), Integer(3))], False, 'variant')
    # tmp_FF24(0) = "EWSKI"
    f.put('tmp_ff24', [Integer(0)], 'EWSKI')
    # tmp_FF24(1) = "EWSKY"
    f.put('tmp_ff24', [Integer(1)], 'EWSKY')
    # tmp_FF24(2) = "OWSKI"
    f.put('tmp_ff24', [Integer(2)], 'OWSKI')
    # tmp_FF24(3) = "OWSKY"
    f.put('tmp_ff24', [Integer(3)], 'OWSKY')
    # tmp_FEB4 = VBA.Array("EWSKI", "EWSKY", "OWSKI", "OWSKY")
    f.set('tmp_feb4', c.builtin('vba.array', ['EWSKI', 'EWSKY', 'OWSKI', 'OWSKY']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FE24 = CBool(IsInArry(pWord, nCurrent, tmp_FEB4))
    f.set('tmp_fe24', c.builtin('cbool', [c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_feb4')])]))
    # tmp_FEA4 = (tmp_FEC4 Or tmp_FE24)
    f.set('tmp_fea4', c.binary('or', f.get('tmp_fec4'), f.get('tmp_fe24')))
    # ReDim tmp_FDE0(0 To 0)
    f.redim('tmp_fde0', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FDE0(0) = "SCH"
    f.put('tmp_fde0', [Integer(0)], 'SCH')
    # tmp_FE94 = VBA.Array("SCH")
    f.set('tmp_fe94', c.builtin('vba.array', ['SCH']))
    # Erase tmp_FDE0
    f.ref('tmp_fde0').value = EMPTY
    # tmp_FF3A = 1
    f.set('tmp_ff3a', Integer(1))
    # tmp_FE04 = CBool(IsInArry(pWord, tmp_FF3A, tmp_FE94))
    f.set('tmp_fe04', c.builtin('cbool', [c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_fe94')])]))
    # tmp_FE54 = (tmp_FEA4 Or tmp_FE04)
    f.set('tmp_fe54', c.binary('or', f.get('tmp_fea4'), f.get('tmp_fe04')))
    # If tmp_FE54 Then GoTo L385E Else GoTo L3892
    return 1225 if truth(f.get('tmp_fe54')) else 1230

def _doublemetaphone_1225(f, c):
    # tmp_FED4 = "F"
    f.set('tmp_fed4', 'F')
    # tmp_FF28 = ""
    f.set('tmp_ff28', '')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_1230(f, c):
    # ReDim tmp_FF24(0 To 1)
    f.redim('tmp_ff24', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FF24(0) = "WICZ"
    f.put('tmp_ff24', [Integer(0)], 'WICZ')
    # tmp_FF24(1) = "WITZ"
    f.put('tmp_ff24', [Integer(1)], 'WITZ')
    # tmp_FF28 = VBA.Array("WICZ", "WITZ")
    f.set('tmp_ff28', c.builtin('vba.array', ['WICZ', 'WITZ']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # If IsInArry(pWord, nCurrent, tmp_FF28) Then GoTo L38EE Else GoTo L3922
    return 1236 if truth(c.call('isinarry', [f.ref('pword'), f.ref('ncurrent'), f.ref('tmp_ff28')])) else 1241

def _doublemetaphone_1236(f, c):
    # tmp_FED4 = "FX"
    f.set('tmp_fed4', 'FX')
    # tmp_FF28 = "TS"
    f.set('tmp_ff28', 'TS')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # nCurrent = CInt((nCurrent + 4))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(4))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_1241(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # GoTo L3CD1
    return 1320

def _doublemetaphone_1243(f, c):
    # If (tmp_FE84 = "X") Then GoTo L3942 Else GoTo L3B29
    return 1244 if truth(c.binary('=', f.get('tmp_fe84'), 'X')) else 1283

def _doublemetaphone_1244(f, c):
    # If (nCurrent > 2) Then GoTo L394D Else GoTo L39AD
    return 1245 if truth(c.binary('>', f.get('ncurrent'), Integer(2))) else 1252

def _doublemetaphone_1245(f, c):
    # ReDim tmp_FF24(0 To 1)
    f.redim('tmp_ff24', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FF24(0) = "IAU"
    f.put('tmp_ff24', [Integer(0)], 'IAU')
    # tmp_FF24(1) = "EAU"
    f.put('tmp_ff24', [Integer(1)], 'EAU')
    # tmp_FF28 = VBA.Array("IAU", "EAU")
    f.set('tmp_ff28', c.builtin('vba.array', ['IAU', 'EAU']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = (nCurrent - 3)
    f.set('tmp_ff3a', c.binary('-', f.get('ncurrent'), Integer(3)))
    # PreviousFlag = CInt(IsInArry(pWord, tmp_FF3A, tmp_FF28))
    f.set('previousflag', c.builtin('cint', [c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')])]))
    return 1252

def _doublemetaphone_1252(f, c):
    # If (nCurrent > 1) Then GoTo L39BA Else GoTo L3A1A
    return 1253 if truth(c.binary('>', f.get('ncurrent'), Integer(1))) else 1260

def _doublemetaphone_1253(f, c):
    # ReDim tmp_FF24(0 To 1)
    f.redim('tmp_ff24', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FF24(0) = "AU"
    f.put('tmp_ff24', [Integer(0)], 'AU')
    # tmp_FF24(1) = "OU"
    f.put('tmp_ff24', [Integer(1)], 'OU')
    # tmp_FF28 = VBA.Array("AU", "OU")
    f.set('tmp_ff28', c.builtin('vba.array', ['AU', 'OU']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = (nCurrent - 2)
    f.set('tmp_ff3a', c.binary('-', f.get('ncurrent'), Integer(2)))
    # PreviousFlag2 = CInt(IsInArry(pWord, tmp_FF3A, tmp_FF28))
    f.set('previousflag2', c.builtin('cint', [c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')])]))
    return 1260

def _doublemetaphone_1260(f, c):
    # If (Not ((nCurrent = (nLast - 1)) And (PreviousFlag Or PreviousFlag2))) Then GoTo L3A34 Else GoTo L3A50
    return 1261 if truth(c.unary('not', c.binary('and', c.binary('=', f.get('ncurrent'), c.binary('-', f.get('nlast'), Integer(1))), c.binary('or', f.get('previousflag'), f.get('previousflag2'))))) else 1263

def _doublemetaphone_1261(f, c):
    # tmp_FF28 = "KS"
    f.set('tmp_ff28', 'KS')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 1263

def _doublemetaphone_1263(f, c):
    # ReDim tmp_FF24(0 To 0)
    f.redim('tmp_ff24', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FF24(0) = "AUX"
    f.put('tmp_ff24', [Integer(0)], 'AUX')
    # tmp_FF28 = VBA.Array("AUX")
    f.set('tmp_ff28', c.builtin('vba.array', ['AUX']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = 0
    f.set('tmp_ff3a', Integer(0))
    # If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L3A9F Else GoTo L3ABB
    return 1269 if truth(c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')])) else 1271

def _doublemetaphone_1269(f, c):
    # tmp_FF28 = "KS"
    f.set('tmp_ff28', 'KS')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 1271

def _doublemetaphone_1271(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # tmp_FED4 = (tmp_FF28 = "C")
    f.set('tmp_fed4', c.binary('=', f.get('tmp_ff28'), 'C'))
    # tmp_FEF4 = CInt((nCurrent + 2))
    f.set('tmp_fef4', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # tmp_FEC4 = pWord(tmp_FEF4)
    f.set('tmp_fec4', f.index('pword', f.get('tmp_fef4')))
    # tmp_FEB4 = (tmp_FEC4 = "X")
    f.set('tmp_feb4', c.binary('=', f.get('tmp_fec4'), 'X'))
    # tmp_FEA4 = (tmp_FED4 And tmp_FEB4)
    f.set('tmp_fea4', c.binary('and', f.get('tmp_fed4'), f.get('tmp_feb4')))
    # If tmp_FEA4 Then GoTo L3B09 Else GoTo L3B17
    return 1279 if truth(f.get('tmp_fea4')) else 1281

def _doublemetaphone_1279(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3B24
    return 1282

def _doublemetaphone_1281(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 1282

def _doublemetaphone_1282(f, c):
    # GoTo L3CD1
    return 1320

def _doublemetaphone_1283(f, c):
    # If (tmp_FE84 = "Z") Then GoTo L3B39 Else GoTo L3CC4
    return 1284 if truth(c.binary('=', f.get('tmp_fe84'), 'Z')) else 1319

def _doublemetaphone_1284(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # If (tmp_FF28 = "H") Then GoTo L3B5C Else GoTo L3B8B
    return 1287 if truth(c.binary('=', f.get('tmp_ff28'), 'H')) else 1292

def _doublemetaphone_1287(f, c):
    # tmp_FF28 = "J"
    f.set('tmp_ff28', 'J')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CD3
    return 1320

def _doublemetaphone_1291(f, c):
    # GoTo L3CBF
    return 1318

def _doublemetaphone_1292(f, c):
    # ReDim tmp_FF24(0 To 2)
    f.redim('tmp_ff24', [(Integer(0), Integer(2))], False, 'variant')
    # tmp_FF24(0) = "ZO"
    f.put('tmp_ff24', [Integer(0)], 'ZO')
    # tmp_FF24(1) = "ZI"
    f.put('tmp_ff24', [Integer(1)], 'ZI')
    # tmp_FF24(2) = "ZA"
    f.put('tmp_ff24', [Integer(2)], 'ZA')
    # tmp_FF28 = VBA.Array("ZO", "ZI", "ZA")
    f.set('tmp_ff28', c.builtin('vba.array', ['ZO', 'ZI', 'ZA']))
    # Erase tmp_FF24
    f.ref('tmp_ff24').value = EMPTY
    # tmp_FF3A = (nCurrent + 1)
    f.set('tmp_ff3a', c.binary('+', f.get('ncurrent'), Integer(1)))
    # tmp_FE64 = CBool(IsInArry(pWord, tmp_FF3A, tmp_FF28))
    f.set('tmp_fe64', c.builtin('cbool', [c.call('isinarry', [f.ref('pword'), f.ref('tmp_ff3a'), f.ref('tmp_ff28')])]))
    # tmp_FE74 = CBool(SlavoGermanic(pWord))
    f.set('tmp_fe74', c.builtin('cbool', [c.call('slavogermanic', [f.ref('pword')])]))
    # tmp_FED4 = pWord(nCurrent)
    f.set('tmp_fed4', f.index('pword', f.get('ncurrent')))
    # tmp_FEC4 = (tmp_FED4 <> "T")
    f.set('tmp_fec4', c.binary('<>', f.get('tmp_fed4'), 'T'))
    # tmp_FEB4 = (tmp_FE74 And tmp_FEC4)
    f.set('tmp_feb4', c.binary('and', f.get('tmp_fe74'), f.get('tmp_fec4')))
    # tmp_FEA4 = (tmp_FE64 Or tmp_FEB4)
    f.set('tmp_fea4', c.binary('or', f.get('tmp_fe64'), f.get('tmp_feb4')))
    # If tmp_FEA4 Then GoTo L3C38 Else GoTo L3C5F
    return 1306 if truth(f.get('tmp_fea4')) else 1310

def _doublemetaphone_1306(f, c):
    # tmp_FED4 = "TS"
    f.set('tmp_fed4', 'TS')
    # tmp_FF28 = "S"
    f.set('tmp_ff28', 'S')
    # Call MetaphAdd(tmp_FF28, tmp_FED4)
    c.call('metaphadd', [f.ref('tmp_ff28'), f.ref('tmp_fed4')])
    # GoTo L3C7D
    return 1312

def _doublemetaphone_1310(f, c):
    # tmp_FF28 = "S"
    f.set('tmp_ff28', 'S')
    # Call MetaphAdd(tmp_FF28)
    c.call('metaphadd', [f.ref('tmp_ff28')])
    return 1312

def _doublemetaphone_1312(f, c):
    # tmp_FF3C = CInt((nCurrent + 1))
    f.set('tmp_ff3c', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    # tmp_FF28 = pWord(tmp_FF3C)
    f.set('tmp_ff28', f.index('pword', f.get('tmp_ff3c')))
    # If (tmp_FF28 = "Z") Then GoTo L3CA2 Else GoTo L3CB0
    return 1315 if truth(c.binary('=', f.get('tmp_ff28'), 'Z')) else 1317

def _doublemetaphone_1315(f, c):
    # nCurrent = CInt((nCurrent + 2))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(2))]))
    # GoTo L3CBD
    return 1318

def _doublemetaphone_1317(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 1318

def _doublemetaphone_1318(f, c):
    # GoTo L3CD1
    return 1320

def _doublemetaphone_1319(f, c):
    # nCurrent = CInt((nCurrent + 1))
    f.set('ncurrent', c.builtin('cint', [c.binary('+', f.get('ncurrent'), Integer(1))]))
    return 1320

def _doublemetaphone_1320(f, c):
    # GoTo L013C
    return 25

def _doublemetaphone_1321(f, c):
    # MetaPh = cache_m8_0004
    f.set('metaph', f.get('cache_m8_0004'))
    # If cache_m8_0000 Then GoTo L3CED Else GoTo L3CF8
    return 1323 if truth(f.get('cache_m8_0000')) else 1324

def _doublemetaphone_1323(f, c):
    # MetaPh2 = cache_m8_0014
    f.set('metaph2', f.get('cache_m8_0014'))
    return 1324

def _doublemetaphone_1324(f, c):
    # DoubleMetaphone = CInt(-1)
    f.set('doublemetaphone', c.builtin('cint', [c.unary('-', Integer(1))]))
    # Exit Function
    return None

def _doublemetaphone_end(f, c):
    return None

_blocks_doublemetaphone = {0: _doublemetaphone_0, 19: _doublemetaphone_19, 20: _doublemetaphone_20, 22: _doublemetaphone_22, 25: _doublemetaphone_25, 32: _doublemetaphone_32, 35: _doublemetaphone_35, 36: _doublemetaphone_36, 40: _doublemetaphone_40, 41: _doublemetaphone_41, 42: _doublemetaphone_42, 43: _doublemetaphone_43, 44: _doublemetaphone_44, 45: _doublemetaphone_45, 46: _doublemetaphone_46, 48: _doublemetaphone_48, 50: _doublemetaphone_50, 51: _doublemetaphone_51, 52: _doublemetaphone_52, 56: _doublemetaphone_56, 61: _doublemetaphone_61, 63: _doublemetaphone_63, 66: _doublemetaphone_66, 67: _doublemetaphone_67, 68: _doublemetaphone_68, 72: _doublemetaphone_72, 73: _doublemetaphone_73, 99: _doublemetaphone_99, 103: _doublemetaphone_103, 108: _doublemetaphone_108, 112: _doublemetaphone_112, 117: _doublemetaphone_117, 121: _doublemetaphone_121, 128: _doublemetaphone_128, 133: _doublemetaphone_133, 138: _doublemetaphone_138, 156: _doublemetaphone_156, 160: _doublemetaphone_160, 161: _doublemetaphone_161, 170: _doublemetaphone_170, 207: _doublemetaphone_207, 210: _doublemetaphone_210, 211: _doublemetaphone_211, 217: _doublemetaphone_217, 220: _doublemetaphone_220, 223: _doublemetaphone_223, 224: _doublemetaphone_224, 226: _doublemetaphone_226, 228: _doublemetaphone_228, 237: _doublemetaphone_237, 242: _doublemetaphone_242, 248: _doublemetaphone_248, 252: _doublemetaphone_252, 265: _doublemetaphone_265, 282: _doublemetaphone_282, 294: _doublemetaphone_294, 297: _doublemetaphone_297, 299: _doublemetaphone_299, 301: _doublemetaphone_301, 302: _doublemetaphone_302, 306: _doublemetaphone_306, 313: _doublemetaphone_313, 317: _doublemetaphone_317, 324: _doublemetaphone_324, 331: _doublemetaphone_331, 335: _doublemetaphone_335, 337: _doublemetaphone_337, 339: _doublemetaphone_339, 349: _doublemetaphone_349, 351: _doublemetaphone_351, 363: _doublemetaphone_363, 365: _doublemetaphone_365, 366: _doublemetaphone_366, 367: _doublemetaphone_367, 368: _doublemetaphone_368, 375: _doublemetaphone_375, 379: _doublemetaphone_379, 383: _doublemetaphone_383, 386: _doublemetaphone_386, 387: _doublemetaphone_387, 393: _doublemetaphone_393, 397: _doublemetaphone_397, 401: _doublemetaphone_401, 402: _doublemetaphone_402, 405: _doublemetaphone_405, 407: _doublemetaphone_407, 408: _doublemetaphone_408, 411: _doublemetaphone_411, 412: _doublemetaphone_412, 415: _doublemetaphone_415, 421: _doublemetaphone_421, 425: _doublemetaphone_425, 426: _doublemetaphone_426, 427: _doublemetaphone_427, 430: _doublemetaphone_430, 433: _doublemetaphone_433, 435: _doublemetaphone_435, 437: _doublemetaphone_437, 454: _doublemetaphone_454, 456: _doublemetaphone_456, 457: _doublemetaphone_457, 466: _doublemetaphone_466, 469: _doublemetaphone_469, 474: _doublemetaphone_474, 476: _doublemetaphone_476, 478: _doublemetaphone_478, 481: _doublemetaphone_481, 488: _doublemetaphone_488, 492: _doublemetaphone_492, 506: _doublemetaphone_506, 510: _doublemetaphone_510, 512: _doublemetaphone_512, 514: _doublemetaphone_514, 524: _doublemetaphone_524, 529: _doublemetaphone_529, 552: _doublemetaphone_552, 557: _doublemetaphone_557, 592: _doublemetaphone_592, 597: _doublemetaphone_597, 608: _doublemetaphone_608, 629: _doublemetaphone_629, 632: _doublemetaphone_632, 638: _doublemetaphone_638, 641: _doublemetaphone_641, 644: _doublemetaphone_644, 646: _doublemetaphone_646, 649: _doublemetaphone_649, 651: _doublemetaphone_651, 652: _doublemetaphone_652, 655: _doublemetaphone_655, 656: _doublemetaphone_656, 657: _doublemetaphone_657, 661: _doublemetaphone_661, 669: _doublemetaphone_669, 673: _doublemetaphone_673, 674: _doublemetaphone_674, 675: _doublemetaphone_675, 676: _doublemetaphone_676, 686: _doublemetaphone_686, 699: _doublemetaphone_699, 702: _doublemetaphone_702, 705: _doublemetaphone_705, 707: _doublemetaphone_707, 713: _doublemetaphone_713, 717: _doublemetaphone_717, 730: _doublemetaphone_730, 734: _doublemetaphone_734, 735: _doublemetaphone_735, 739: _doublemetaphone_739, 748: _doublemetaphone_748, 750: _doublemetaphone_750, 753: _doublemetaphone_753, 755: _doublemetaphone_755, 756: _doublemetaphone_756, 757: _doublemetaphone_757, 758: _doublemetaphone_758, 761: _doublemetaphone_761, 763: _doublemetaphone_763, 764: _doublemetaphone_764, 767: _doublemetaphone_767, 768: _doublemetaphone_768, 771: _doublemetaphone_771, 772: _doublemetaphone_772, 797: _doublemetaphone_797, 802: _doublemetaphone_802, 804: _doublemetaphone_804, 805: _doublemetaphone_805, 808: _doublemetaphone_808, 809: _doublemetaphone_809, 829: _doublemetaphone_829, 831: _doublemetaphone_831, 832: _doublemetaphone_832, 835: _doublemetaphone_835, 836: _doublemetaphone_836, 839: _doublemetaphone_839, 841: _doublemetaphone_841, 842: _doublemetaphone_842, 845: _doublemetaphone_845, 846: _doublemetaphone_846, 850: _doublemetaphone_850, 851: _doublemetaphone_851, 854: _doublemetaphone_854, 858: _doublemetaphone_858, 866: _doublemetaphone_866, 868: _doublemetaphone_868, 871: _doublemetaphone_871, 872: _doublemetaphone_872, 873: _doublemetaphone_873, 876: _doublemetaphone_876, 878: _doublemetaphone_878, 879: _doublemetaphone_879, 882: _doublemetaphone_882, 883: _doublemetaphone_883, 884: _doublemetaphone_884, 891: _doublemetaphone_891, 898: _doublemetaphone_898, 902: _doublemetaphone_902, 903: _doublemetaphone_903, 904: _doublemetaphone_904, 905: _doublemetaphone_905, 906: _doublemetaphone_906, 908: _doublemetaphone_908, 911: _doublemetaphone_911, 913: _doublemetaphone_913, 914: _doublemetaphone_914, 915: _doublemetaphone_915, 916: _doublemetaphone_916, 922: _doublemetaphone_922, 924: _doublemetaphone_924, 929: _doublemetaphone_929, 934: _doublemetaphone_934, 941: _doublemetaphone_941, 950: _doublemetaphone_950, 953: _doublemetaphone_953, 955: _doublemetaphone_955, 957: _doublemetaphone_957, 967: _doublemetaphone_967, 968: _doublemetaphone_968, 972: _doublemetaphone_972, 974: _doublemetaphone_974, 976: _doublemetaphone_976, 986: _doublemetaphone_986, 992: _doublemetaphone_992, 994: _doublemetaphone_994, 995: _doublemetaphone_995, 996: _doublemetaphone_996, 1003: _doublemetaphone_1003, 1006: _doublemetaphone_1006, 1017: _doublemetaphone_1017, 1024: _doublemetaphone_1024, 1028: _doublemetaphone_1028, 1030: _doublemetaphone_1030, 1032: _doublemetaphone_1032, 1033: _doublemetaphone_1033, 1042: _doublemetaphone_1042, 1046: _doublemetaphone_1046, 1048: _doublemetaphone_1048, 1050: _doublemetaphone_1050, 1054: _doublemetaphone_1054, 1058: _doublemetaphone_1058, 1062: _doublemetaphone_1062, 1068: _doublemetaphone_1068, 1072: _doublemetaphone_1072, 1074: _doublemetaphone_1074, 1082: _doublemetaphone_1082, 1084: _doublemetaphone_1084, 1085: _doublemetaphone_1085, 1086: _doublemetaphone_1086, 1087: _doublemetaphone_1087, 1092: _doublemetaphone_1092, 1096: _doublemetaphone_1096, 1102: _doublemetaphone_1102, 1106: _doublemetaphone_1106, 1119: _doublemetaphone_1119, 1137: _doublemetaphone_1137, 1140: _doublemetaphone_1140, 1143: _doublemetaphone_1143, 1145: _doublemetaphone_1145, 1153: _doublemetaphone_1153, 1155: _doublemetaphone_1155, 1158: _doublemetaphone_1158, 1159: _doublemetaphone_1159, 1160: _doublemetaphone_1160, 1163: _doublemetaphone_1163, 1165: _doublemetaphone_1165, 1168: _doublemetaphone_1168, 1169: _doublemetaphone_1169, 1170: _doublemetaphone_1170, 1177: _doublemetaphone_1177, 1181: _doublemetaphone_1181, 1194: _doublemetaphone_1194, 1198: _doublemetaphone_1198, 1202: _doublemetaphone_1202, 1204: _doublemetaphone_1204, 1225: _doublemetaphone_1225, 1230: _doublemetaphone_1230, 1236: _doublemetaphone_1236, 1241: _doublemetaphone_1241, 1243: _doublemetaphone_1243, 1244: _doublemetaphone_1244, 1245: _doublemetaphone_1245, 1252: _doublemetaphone_1252, 1253: _doublemetaphone_1253, 1260: _doublemetaphone_1260, 1261: _doublemetaphone_1261, 1263: _doublemetaphone_1263, 1269: _doublemetaphone_1269, 1271: _doublemetaphone_1271, 1279: _doublemetaphone_1279, 1281: _doublemetaphone_1281, 1282: _doublemetaphone_1282, 1283: _doublemetaphone_1283, 1284: _doublemetaphone_1284, 1287: _doublemetaphone_1287, 1291: _doublemetaphone_1291, 1292: _doublemetaphone_1292, 1306: _doublemetaphone_1306, 1310: _doublemetaphone_1310, 1312: _doublemetaphone_1312, 1315: _doublemetaphone_1315, 1317: _doublemetaphone_1317, 1318: _doublemetaphone_1318, 1319: _doublemetaphone_1319, 1320: _doublemetaphone_1320, 1321: _doublemetaphone_1321, 1323: _doublemetaphone_1323, 1324: _doublemetaphone_1324, 1326: _doublemetaphone_end}
def vb_doublemetaphone(c, arguments):
    return run(c, 'doublemetaphone', [('input_pword', 'variant', True, False, MISSING), ('metaph', 'variant', False, False, MISSING), ('metaph2', 'variant', False, False, MISSING)], {'tmp_fd08': 'variant', 'tmp_fd2a': 'integer', 'tmp_fd3c': 'variant', 'tmp_fd4c': 'variant', 'tmp_fd6c': 'variant', 'tmp_fd72': 'integer', 'tmp_fd74': 'variant', 'tmp_fd7a': 'integer', 'tmp_fd7c': 'variant', 'tmp_fd80': 'variant', 'tmp_fd90': 'variant', 'tmp_fda0': 'variant', 'tmp_fdb0': 'variant', 'tmp_fdd0': 'variant', 'tmp_fde0': 'variant', 'tmp_fde4': 'variant', 'tmp_fdf4': 'variant', 'tmp_fe04': 'variant', 'tmp_fe14': 'variant', 'tmp_fe24': 'variant', 'tmp_fe34': 'variant', 'tmp_fe44': 'variant', 'tmp_fe54': 'variant', 'tmp_fe64': 'variant', 'tmp_fe74': 'variant', 'tmp_fe84': 'variant', 'tmp_fe94': 'variant', 'tmp_fea4': 'variant', 'tmp_feb4': 'variant', 'tmp_fec4': 'variant', 'tmp_fed4': 'variant', 'tmp_fee4': 'variant', 'tmp_fef4': 'variant', 'tmp_ff04': 'variant', 'tmp_ff14': 'variant', 'tmp_ff24': 'variant', 'tmp_ff28': 'variant', 'tmp_ff3a': 'integer', 'tmp_ff3c': 'variant', 'previousflag2': 'boolean', 'previousflag': 'boolean', 'nlast': 'integer', 'ncurrent': 'integer', 'sletter': 'variant', 'nlength': 'integer', 'significantchars': 'integer', 'pword': 'variant'}, 'boolean', _blocks_doublemetaphone, arguments)

def _metaphadd_0(f, c):
    # tmp_FF5C = (cache_m8_0004 & pChr)
    f.set('tmp_ff5c', c.binary('&', f.get('cache_m8_0004'), f.get('pchr')))
    # cache_m8_0004 = tmp_FF5C
    f.set('cache_m8_0004', f.get('tmp_ff5c'))
    # If (Not IsMissing(pChr2)) Then GoTo L0027 Else GoTo L0090
    return 3 if truth(c.unary('not', c.builtin('ismissing', [f.get('pchr2')]))) else 12

def _metaphadd_3(f, c):
    # cache_m8_0000 = CInt(-1)
    f.set('cache_m8_0000', c.builtin('cint', [c.unary('-', Integer(1))]))
    # If (pChr2 <> " ") Then GoTo L0043 Else GoTo L005D
    return 5 if truth(c.binary('<>', f.get('pchr2'), ' ')) else 8

def _metaphadd_5(f, c):
    # tmp_FF5C = (cache_m8_0014 & pChr2)
    f.set('tmp_ff5c', c.binary('&', f.get('cache_m8_0014'), f.get('pchr2')))
    # cache_m8_0014 = tmp_FF5C
    f.set('cache_m8_0014', f.get('tmp_ff5c'))
    # GoTo L008B
    return 11

def _metaphadd_8(f, c):
    # If (pChr <> " ") Then GoTo L0072 Else GoTo L0089
    return 9 if truth(c.binary('<>', f.get('pchr'), ' ')) else 11

def _metaphadd_9(f, c):
    # tmp_FF5C = (cache_m8_0014 & pChr)
    f.set('tmp_ff5c', c.binary('&', f.get('cache_m8_0014'), f.get('pchr')))
    # cache_m8_0014 = tmp_FF5C
    f.set('cache_m8_0014', f.get('tmp_ff5c'))
    return 11

def _metaphadd_11(f, c):
    # GoTo L00A9
    return 14

def _metaphadd_12(f, c):
    # tmp_FF5C = (cache_m8_0014 & pChr)
    f.set('tmp_ff5c', c.binary('&', f.get('cache_m8_0014'), f.get('pchr')))
    # cache_m8_0014 = tmp_FF5C
    f.set('cache_m8_0014', f.get('tmp_ff5c'))
    return 14

def _metaphadd_14(f, c):
    # Exit Sub
    return None

def _metaphadd_end(f, c):
    return None

_blocks_metaphadd = {0: _metaphadd_0, 3: _metaphadd_3, 5: _metaphadd_5, 8: _metaphadd_8, 9: _metaphadd_9, 11: _metaphadd_11, 12: _metaphadd_12, 14: _metaphadd_14, 15: _metaphadd_end}
def vb_metaphadd(c, arguments):
    return run(c, 'metaphadd', [('pchr', 'variant', False, False, MISSING), ('pchr2', 'variant', False, True, MISSING)], {'tmp_ff5c': 'variant'}, None, _blocks_metaphadd, arguments)

def _isvowel_0(f, c):
    # tmp_FF48 = Mid(pChr, CLng(pos), 1)
    f.set('tmp_ff48', c.builtin('mid', [f.get('pchr'), c.builtin('clng', [f.get('pos')]), Integer(1)]))
    # tmp_FF28 = (tmp_FF48 Like "[aeiouy]")
    f.set('tmp_ff28', c.binary('like', f.get('tmp_ff48'), '[aeiouy]'))
    # IsVowel = CInt(CBool(tmp_FF28))
    f.set('isvowel', c.builtin('cint', [c.builtin('cbool', [f.get('tmp_ff28')])]))
    # Exit Function
    return None

def _isvowel_end(f, c):
    return None

_blocks_isvowel = {0: _isvowel_0, 4: _isvowel_end}
def vb_isvowel(c, arguments):
    return run(c, 'isvowel', [('pchr', 'variant', False, False, MISSING), ('pos', 'integer', False, False, MISSING)], {'tmp_ff28': 'variant', 'tmp_ff48': 'variant'}, 'boolean', _blocks_isvowel, arguments)

def _slavogermanic_0(f, c):
    # ReDim tmp_FF74(0 To 1)
    f.redim('tmp_ff74', [(Integer(0), Integer(1))], False, 'variant')
    # tmp_FF74(0) = "WK"
    f.put('tmp_ff74', [Integer(0)], 'WK')
    # tmp_FF74(1) = "CZ"
    f.put('tmp_ff74', [Integer(1)], 'CZ')
    # tmp_FF44 = VBA.Array("WK", "CZ")
    f.set('tmp_ff44', c.builtin('vba.array', ['WK', 'CZ']))
    # Erase tmp_FF74
    f.ref('tmp_ff74').value = EMPTY
    # tmp_FF42 = 0
    f.set('tmp_ff42', Integer(0))
    # SlavoGermanic = CInt(IsInArry(pArry, tmp_FF42, tmp_FF44))
    f.set('slavogermanic', c.builtin('cint', [c.call('isinarry', [f.ref('parry'), f.ref('tmp_ff42'), f.ref('tmp_ff44')])]))
    # If (Not SlavoGermanic) Then GoTo L0067 Else GoTo L00B4
    return 8 if truth(c.unary('not', f.get('slavogermanic'))) else 14

def _slavogermanic_8(f, c):
    # ReDim tmp_FF74(0 To 0)
    f.redim('tmp_ff74', [(Integer(0), Integer(0))], False, 'variant')
    # tmp_FF74(0) = "WITZ"
    f.put('tmp_ff74', [Integer(0)], 'WITZ')
    # tmp_FF44 = VBA.Array("WITZ")
    f.set('tmp_ff44', c.builtin('vba.array', ['WITZ']))
    # Erase tmp_FF74
    f.ref('tmp_ff74').value = EMPTY
    # tmp_FF42 = 0
    f.set('tmp_ff42', Integer(0))
    # SlavoGermanic = CInt(IsInArry(pArry, tmp_FF42, tmp_FF44))
    f.set('slavogermanic', c.builtin('cint', [c.call('isinarry', [f.ref('parry'), f.ref('tmp_ff42'), f.ref('tmp_ff44')])]))
    return 14

def _slavogermanic_14(f, c):
    # Exit Function
    return None

def _slavogermanic_end(f, c):
    return None

_blocks_slavogermanic = {0: _slavogermanic_0, 8: _slavogermanic_8, 14: _slavogermanic_14, 15: _slavogermanic_end}
def vb_slavogermanic(c, arguments):
    return run(c, 'slavogermanic', [('parry', 'variant', False, False, MISSING)], {'tmp_ff42': 'integer', 'tmp_ff44': 'variant', 'tmp_ff74': 'variant'}, 'boolean', _blocks_slavogermanic, arguments)

def _isinstr_0(f, c):
    # tmp_FF44 = Len(pStr)
    f.set('tmp_ff44', c.builtin('len', [f.get('pstr')]))
    # If (pLen > tmp_FF44) Then GoTo L0019 Else GoTo L001C
    return 2 if truth(c.binary('>', f.get('plen'), f.get('tmp_ff44'))) else 3

def _isinstr_2(f, c):
    # Exit Function
    return None

def _isinstr_3(f, c):
    # If (StartDX < 1) Then GoTo L0029 Else GoTo L002C
    return 4 if truth(c.binary('<', f.get('startdx'), Integer(1))) else 5

def _isinstr_4(f, c):
    # Exit Function
    return None

def _isinstr_5(f, c):
    # tmp_FF44 = Mid(pStr, CLng(StartDX), pLen)
    f.set('tmp_ff44', c.builtin('mid', [f.get('pstr'), c.builtin('clng', [f.get('startdx')]), f.get('plen')]))
    # Str2Check = tmp_FF44
    f.set('str2check', f.get('tmp_ff44'))
    # tmp_FF44 = InStr(1, pList, ",", 2)
    f.set('tmp_ff44', c.builtin('instr', [Integer(1), f.get('plist'), ',', Integer(2)]))
    # Increment = CInt(CInt(tmp_FF44))
    f.set('increment', c.builtin('cint', [c.builtin('cint', [f.get('tmp_ff44')])]))
    # tmp_FF44 = (pList & ",")
    f.set('tmp_ff44', c.binary('&', f.get('plist'), ','))
    # pList = tmp_FF44
    f.set('plist', f.get('tmp_ff44'))
    # tmp_FF44 = Len(pList)
    f.set('tmp_ff44', c.builtin('len', [f.get('plist')]))
    # tmp_FF24 = (tmp_FF44 - 1)
    f.set('tmp_ff24', c.binary('-', f.get('tmp_ff44'), Integer(1)))
    # For X = 1 To CInt(tmp_FF24) Step Increment
    return 14 if f.begin_loop(13, 'x', Integer(1), c.builtin('cint', [f.get('tmp_ff24')]), f.get('increment')) else 24

def _isinstr_14(f, c):
    # tmp_FF24 = Mid(pList, CLng(X))
    f.set('tmp_ff24', c.builtin('mid', [f.get('plist'), c.builtin('clng', [f.get('x')])]))
    # tmp_FF10 = InStr(1, tmp_FF24, ",", 2)
    f.set('tmp_ff10', c.builtin('instr', [Integer(1), f.get('tmp_ff24'), ',', Integer(2)]))
    # tmp_FEF0 = (tmp_FF10 - 1)
    f.set('tmp_fef0', c.binary('-', f.get('tmp_ff10'), Integer(1)))
    # tmp_FEE0 = tmp_FEF0
    f.set('tmp_fee0', f.get('tmp_fef0'))
    # tmp_FED0 = Mid(pList, CLng(X), tmp_FEE0)
    f.set('tmp_fed0', c.builtin('mid', [f.get('plist'), c.builtin('clng', [f.get('x')]), f.get('tmp_fee0')]))
    # tmp_FEC0 = InStr(1, Str2Check, tmp_FED0, 2)
    f.set('tmp_fec0', c.builtin('instr', [Integer(1), f.get('str2check'), f.get('tmp_fed0'), Integer(2)]))
    # If (tmp_FEC0 > 0) Then GoTo L011A Else GoTo L0126
    return 21 if truth(c.binary('>', f.get('tmp_fec0'), Integer(0))) else 23

def _isinstr_21(f, c):
    # IsInStr = CInt(-1)
    f.set('isinstr', c.builtin('cint', [c.unary('-', Integer(1))]))
    # GoTo L0132
    return 24

def _isinstr_23(f, c):
    # Next X
    return 14 if f.next_loop(13) else 24

def _isinstr_24(f, c):
    # Exit Function
    return None

def _isinstr_end(f, c):
    return None

_blocks_isinstr = {0: _isinstr_0, 2: _isinstr_2, 3: _isinstr_3, 4: _isinstr_4, 5: _isinstr_5, 14: _isinstr_14, 21: _isinstr_21, 23: _isinstr_23, 24: _isinstr_24, 25: _isinstr_end}
def vb_isinstr(c, arguments):
    return run(c, 'isinstr', [('pstr', 'variant', False, False, MISSING), ('startdx', 'integer', False, False, MISSING), ('plen', 'variant', False, False, MISSING), ('plist', 'variant', False, False, MISSING)], {'tmp_fec0': 'variant', 'tmp_fed0': 'variant', 'tmp_fee0': 'variant', 'tmp_fef0': 'variant', 'tmp_ff10': 'variant', 'tmp_ff24': 'variant', 'tmp_ff44': 'variant', 'str2check': 'variant', 'increment': 'integer', 'x': 'integer'}, 'boolean', _blocks_isinstr, arguments)

def _rapad_0(f, c):
    # ALen = CInt(CInt((UBound(pArry, 1) + CLng(NumChrs))))
    f.set('alen', c.builtin('cint', [c.builtin('cint', [c.binary('+', c.builtin('ubound', [f.get('parry'), Integer(1)]), c.builtin('clng', [f.get('numchrs')]))])]))
    # ReDim Preserve pArry(0 To CLng((ALen - 1)))
    f.redim('parry', [(Integer(0), c.builtin('clng', [c.binary('-', f.get('alen'), Integer(1))]))], True, None)
    # For X = (ALen - NumChrs) To (ALen - 1)
    return 3 if f.begin_loop(2, 'x', c.binary('-', f.get('alen'), f.get('numchrs')), c.binary('-', f.get('alen'), Integer(1)), Integer(1)) else 5

def _rapad_3(f, c):
    # pArry(X) = pChr
    f.put('parry', [f.get('x')], f.get('pchr'))
    # Next X
    return 3 if f.next_loop(2) else 5

def _rapad_5(f, c):
    # Exit Sub
    return None

def _rapad_end(f, c):
    return None

_blocks_rapad = {0: _rapad_0, 3: _rapad_3, 5: _rapad_5, 6: _rapad_end}
def vb_rapad(c, arguments):
    return run(c, 'rapad', [('parry', 'variant', False, False, MISSING), ('numchrs', 'integer', False, False, MISSING), ('pchr', 'variant', False, False, MISSING)], {'alen': 'integer', 'x': 'integer'}, None, _blocks_rapad, arguments)

def _isinarry_0(f, c):
    # On Error GoTo L0130
    f.handler = 28
    # ArryLen = CInt(CInt(UBound(pArry, 1)))
    f.set('arrylen', c.builtin('cint', [c.builtin('cint', [c.builtin('ubound', [f.get('parry'), Integer(1)])])]))
    # tmp_FF0C = CInt(ArryLen)
    f.set('tmp_ff0c', c.builtin('cint', [f.get('arrylen')]))
    # tmp_FF2C = pListArry(0)
    f.set('tmp_ff2c', f.index('plistarry', Integer(0)))
    # tmp_FF1C = Len(tmp_FF2C)
    f.set('tmp_ff1c', c.builtin('len', [f.get('tmp_ff2c')]))
    # If (tmp_FF0C < tmp_FF1C) Then GoTo L003B Else GoTo L003E
    return 6 if truth(c.binary('<', f.get('tmp_ff0c'), f.get('tmp_ff1c'))) else 7

def _isinarry_6(f, c):
    # Exit Function
    return None

def _isinarry_7(f, c):
    # ListArryLen = CInt(CInt(UBound(pListArry, 1)))
    f.set('listarrylen', c.builtin('cint', [c.builtin('cint', [c.builtin('ubound', [f.get('plistarry'), Integer(1)])])]))
    # tmp_FF2C = pListArry(0)
    f.set('tmp_ff2c', f.index('plistarry', Integer(0)))
    # tmp_FF1C = Len(tmp_FF2C)
    f.set('tmp_ff1c', c.builtin('len', [f.get('tmp_ff2c')]))
    # tmp_FEFC = (tmp_FF1C - 1)
    f.set('tmp_fefc', c.binary('-', f.get('tmp_ff1c'), Integer(1)))
    # StrLen = CInt(CInt(tmp_FEFC))
    f.set('strlen', c.builtin('cint', [c.builtin('cint', [f.get('tmp_fefc')])]))
    # For X = 0 To ListArryLen
    return 13 if f.begin_loop(12, 'x', Integer(0), f.get('listarrylen'), Integer(1)) else 27

def _isinarry_13(f, c):
    # For Y = StartDX To ArryLen
    return 14 if f.begin_loop(13, 'y', f.get('startdx'), f.get('arrylen'), Integer(1)) else 26

def _isinarry_14(f, c):
    # TmpStr = ""
    f.set('tmpstr', '')
    # If ((Y + StrLen) <= ArryLen) Then GoTo L00AF Else GoTo L00EE
    return 16 if truth(c.binary('<=', c.binary('+', f.get('y'), f.get('strlen')), f.get('arrylen'))) else 21

def _isinarry_16(f, c):
    # For z = Y To (Y + StrLen)
    return 17 if f.begin_loop(16, 'z', f.get('y'), c.binary('+', f.get('y'), f.get('strlen')), Integer(1)) else 21

def _isinarry_17(f, c):
    # tmp_FF2C = pArry(z)
    f.set('tmp_ff2c', f.index('parry', f.get('z')))
    # tmp_FF1C = (TmpStr & tmp_FF2C)
    f.set('tmp_ff1c', c.binary('&', f.get('tmpstr'), f.get('tmp_ff2c')))
    # TmpStr = tmp_FF1C
    f.set('tmpstr', f.get('tmp_ff1c'))
    # Next z
    return 17 if f.next_loop(16) else 21

def _isinarry_21(f, c):
    # tmp_FF2C = pListArry(X)
    f.set('tmp_ff2c', f.index('plistarry', f.get('x')))
    # If (TmpStr = tmp_FF2C) Then GoTo L010D Else GoTo L0117
    return 23 if truth(c.binary('=', f.get('tmpstr'), f.get('tmp_ff2c'))) else 25

def _isinarry_23(f, c):
    # IsInArry = CInt(-1)
    f.set('isinarry', c.builtin('cint', [c.unary('-', Integer(1))]))
    # Exit Function
    return None

def _isinarry_25(f, c):
    # Next Y
    return 14 if f.next_loop(13) else 26

def _isinarry_26(f, c):
    # Next X
    return 13 if f.next_loop(12) else 27

def _isinarry_27(f, c):
    # Exit Function
    return None

def _isinarry_28(f, c):
    # Resume L012D
    f.handling_error = False
    return 27

def _isinarry_29(f, c):
    # Exit Function
    return None

def _isinarry_end(f, c):
    return None

_blocks_isinarry = {0: _isinarry_0, 6: _isinarry_6, 7: _isinarry_7, 13: _isinarry_13, 14: _isinarry_14, 16: _isinarry_16, 17: _isinarry_17, 21: _isinarry_21, 23: _isinarry_23, 25: _isinarry_25, 26: _isinarry_26, 27: _isinarry_27, 28: _isinarry_28, 29: _isinarry_29, 30: _isinarry_end}
def vb_isinarry(c, arguments):
    return run(c, 'isinarry', [('parry', 'variant', False, False, MISSING), ('startdx', 'integer', False, False, MISSING), ('plistarry', 'variant', False, False, MISSING)], {'tmp_fefc': 'variant', 'tmp_ff0c': 'variant', 'tmp_ff1c': 'variant', 'tmp_ff2c': 'variant', 'y': 'integer', 'strlen': 'integer', 'listarrylen': 'integer', 'tmpstr': 'variant', 'z': 'integer', 'arrylen': 'integer', 'x': 'integer'}, 'boolean', _blocks_isinarry, arguments)

def _minimum_0(f, c):
    # Minimum = pVal1
    f.set('minimum', f.get('pval1'))
    # TopVal = CInt(2)
    f.set('topval', c.builtin('cint', [Integer(2)]))
    # If (Not IsMissing(pVal3)) Then GoTo L0023 Else GoTo L0041
    return 3 if truth(c.unary('not', c.builtin('ismissing', [f.get('pval3')]))) else 6

def _minimum_3(f, c):
    # TopVal = CInt(3)
    f.set('topval', c.builtin('cint', [Integer(3)]))
    # If (Not IsMissing(pVal4)) Then GoTo L0038 Else GoTo L003F
    return 5 if truth(c.unary('not', c.builtin('ismissing', [f.get('pval4')]))) else 6

def _minimum_5(f, c):
    # TopVal = CInt(4)
    f.set('topval', c.builtin('cint', [Integer(4)]))
    return 6

def _minimum_6(f, c):
    # tmp_FF56 = CInt(TopVal)
    f.set('tmp_ff56', c.builtin('cint', [f.get('topval')]))
    # If (tmp_FF56 = 2) Then GoTo L0056 Else GoTo L0075
    return 8 if truth(c.binary('=', f.get('tmp_ff56'), Integer(2))) else 11

def _minimum_8(f, c):
    # If (pVal2 < Minimum) Then GoTo L0066 Else GoTo L0072
    return 9 if truth(c.binary('<', f.get('pval2'), f.get('minimum'))) else 10

def _minimum_9(f, c):
    # Minimum = pVal2
    f.set('minimum', f.get('pval2'))
    return 10

def _minimum_10(f, c):
    # GoTo L011A
    return 24

def _minimum_11(f, c):
    # If (tmp_FF56 = 3) Then GoTo L0080 Else GoTo L00BB
    return 12 if truth(c.binary('=', f.get('tmp_ff56'), Integer(3))) else 17

def _minimum_12(f, c):
    # If (pVal2 < Minimum) Then GoTo L0090 Else GoTo L009C
    return 13 if truth(c.binary('<', f.get('pval2'), f.get('minimum'))) else 14

def _minimum_13(f, c):
    # Minimum = pVal2
    f.set('minimum', f.get('pval2'))
    return 14

def _minimum_14(f, c):
    # If (pVal3 < Minimum) Then GoTo L00AC Else GoTo L00B8
    return 15 if truth(c.binary('<', f.get('pval3'), f.get('minimum'))) else 16

def _minimum_15(f, c):
    # Minimum = pVal3
    f.set('minimum', f.get('pval3'))
    return 16

def _minimum_16(f, c):
    # GoTo L011A
    return 24

def _minimum_17(f, c):
    # If (tmp_FF56 = 4) Then GoTo L00C6 Else GoTo L011A
    return 18 if truth(c.binary('=', f.get('tmp_ff56'), Integer(4))) else 24

def _minimum_18(f, c):
    # If (pVal2 < Minimum) Then GoTo L00D6 Else GoTo L00E2
    return 19 if truth(c.binary('<', f.get('pval2'), f.get('minimum'))) else 20

def _minimum_19(f, c):
    # Minimum = pVal2
    f.set('minimum', f.get('pval2'))
    return 20

def _minimum_20(f, c):
    # If (pVal3 < Minimum) Then GoTo L00F2 Else GoTo L00FE
    return 21 if truth(c.binary('<', f.get('pval3'), f.get('minimum'))) else 22

def _minimum_21(f, c):
    # Minimum = pVal3
    f.set('minimum', f.get('pval3'))
    return 22

def _minimum_22(f, c):
    # If (pVal4 < Minimum) Then GoTo L010E Else GoTo L011A
    return 23 if truth(c.binary('<', f.get('pval4'), f.get('minimum'))) else 24

def _minimum_23(f, c):
    # Minimum = pVal4
    f.set('minimum', f.get('pval4'))
    return 24

def _minimum_24(f, c):
    # Exit Function
    return None

def _minimum_end(f, c):
    return None

_blocks_minimum = {0: _minimum_0, 3: _minimum_3, 5: _minimum_5, 6: _minimum_6, 8: _minimum_8, 9: _minimum_9, 10: _minimum_10, 11: _minimum_11, 12: _minimum_12, 13: _minimum_13, 14: _minimum_14, 15: _minimum_15, 16: _minimum_16, 17: _minimum_17, 18: _minimum_18, 19: _minimum_19, 20: _minimum_20, 21: _minimum_21, 22: _minimum_22, 23: _minimum_23, 24: _minimum_24, 25: _minimum_end}
def vb_minimum(c, arguments):
    return run(c, 'minimum', [('pval1', 'variant', False, False, MISSING), ('pval2', 'variant', False, False, MISSING), ('pval3', 'variant', False, True, MISSING), ('pval4', 'variant', False, True, MISSING)], {'tmp_ff56': 'variant', 'topval': 'integer'}, 'variant', _blocks_minimum, arguments)

def _maximum_0(f, c):
    # Maximum = pVal1
    f.set('maximum', f.get('pval1'))
    # TopVal = CInt(2)
    f.set('topval', c.builtin('cint', [Integer(2)]))
    # If (Not IsMissing(pVal3)) Then GoTo L0023 Else GoTo L0041
    return 3 if truth(c.unary('not', c.builtin('ismissing', [f.get('pval3')]))) else 6

def _maximum_3(f, c):
    # TopVal = CInt(3)
    f.set('topval', c.builtin('cint', [Integer(3)]))
    # If (Not IsMissing(pVal4)) Then GoTo L0038 Else GoTo L003F
    return 5 if truth(c.unary('not', c.builtin('ismissing', [f.get('pval4')]))) else 6

def _maximum_5(f, c):
    # TopVal = CInt(4)
    f.set('topval', c.builtin('cint', [Integer(4)]))
    return 6

def _maximum_6(f, c):
    # tmp_FF56 = CInt(TopVal)
    f.set('tmp_ff56', c.builtin('cint', [f.get('topval')]))
    # If (tmp_FF56 = 2) Then GoTo L0056 Else GoTo L0075
    return 8 if truth(c.binary('=', f.get('tmp_ff56'), Integer(2))) else 11

def _maximum_8(f, c):
    # If (pVal2 > Maximum) Then GoTo L0066 Else GoTo L0072
    return 9 if truth(c.binary('>', f.get('pval2'), f.get('maximum'))) else 10

def _maximum_9(f, c):
    # Maximum = pVal2
    f.set('maximum', f.get('pval2'))
    return 10

def _maximum_10(f, c):
    # GoTo L011A
    return 24

def _maximum_11(f, c):
    # If (tmp_FF56 = 3) Then GoTo L0080 Else GoTo L00BB
    return 12 if truth(c.binary('=', f.get('tmp_ff56'), Integer(3))) else 17

def _maximum_12(f, c):
    # If (pVal2 > Maximum) Then GoTo L0090 Else GoTo L009C
    return 13 if truth(c.binary('>', f.get('pval2'), f.get('maximum'))) else 14

def _maximum_13(f, c):
    # Maximum = pVal2
    f.set('maximum', f.get('pval2'))
    return 14

def _maximum_14(f, c):
    # If (pVal3 > Maximum) Then GoTo L00AC Else GoTo L00B8
    return 15 if truth(c.binary('>', f.get('pval3'), f.get('maximum'))) else 16

def _maximum_15(f, c):
    # Maximum = pVal3
    f.set('maximum', f.get('pval3'))
    return 16

def _maximum_16(f, c):
    # GoTo L011A
    return 24

def _maximum_17(f, c):
    # If (tmp_FF56 = 4) Then GoTo L00C6 Else GoTo L011A
    return 18 if truth(c.binary('=', f.get('tmp_ff56'), Integer(4))) else 24

def _maximum_18(f, c):
    # If (pVal2 > Maximum) Then GoTo L00D6 Else GoTo L00E2
    return 19 if truth(c.binary('>', f.get('pval2'), f.get('maximum'))) else 20

def _maximum_19(f, c):
    # Maximum = pVal2
    f.set('maximum', f.get('pval2'))
    return 20

def _maximum_20(f, c):
    # If (pVal3 > Maximum) Then GoTo L00F2 Else GoTo L00FE
    return 21 if truth(c.binary('>', f.get('pval3'), f.get('maximum'))) else 22

def _maximum_21(f, c):
    # Maximum = pVal3
    f.set('maximum', f.get('pval3'))
    return 22

def _maximum_22(f, c):
    # If (pVal4 > Maximum) Then GoTo L010E Else GoTo L011A
    return 23 if truth(c.binary('>', f.get('pval4'), f.get('maximum'))) else 24

def _maximum_23(f, c):
    # Maximum = pVal4
    f.set('maximum', f.get('pval4'))
    return 24

def _maximum_24(f, c):
    # Exit Function
    return None

def _maximum_end(f, c):
    return None

_blocks_maximum = {0: _maximum_0, 3: _maximum_3, 5: _maximum_5, 6: _maximum_6, 8: _maximum_8, 9: _maximum_9, 10: _maximum_10, 11: _maximum_11, 12: _maximum_12, 13: _maximum_13, 14: _maximum_14, 15: _maximum_15, 16: _maximum_16, 17: _maximum_17, 18: _maximum_18, 19: _maximum_19, 20: _maximum_20, 21: _maximum_21, 22: _maximum_22, 23: _maximum_23, 24: _maximum_24, 25: _maximum_end}
def vb_maximum(c, arguments):
    return run(c, 'maximum', [('pval1', 'variant', False, False, MISSING), ('pval2', 'variant', False, False, MISSING), ('pval3', 'variant', False, True, MISSING), ('pval4', 'variant', False, True, MISSING)], {'tmp_ff56': 'variant', 'topval': 'integer'}, 'variant', _blocks_maximum, arguments)

def _strreplace_0(f, c):
    # If IsNull(cString) Then GoTo L000F Else GoTo L001F
    return 1 if truth(c.builtin('isnull', [f.get('cstring')])) else 3

def _strreplace_1(f, c):
    # StrReplace = Null
    f.set('strreplace', None)
    # Exit Function
    return None

def _strreplace_3(f, c):
    # If (cString = "") Then GoTo L0034 Else GoTo L0045
    return 4 if truth(c.binary('=', f.get('cstring'), '')) else 6

def _strreplace_4(f, c):
    # StrReplace = ""
    f.set('strreplace', '')
    # Exit Function
    return None

def _strreplace_6(f, c):
    # If IsNull(cSearch) Then GoTo L0054 Else GoTo L0066
    return 7 if truth(c.builtin('isnull', [f.get('csearch')])) else 9

def _strreplace_7(f, c):
    # StrReplace = cString
    f.set('strreplace', f.get('cstring'))
    # Exit Function
    return None

def _strreplace_9(f, c):
    # If (Not (nCount > 0)) Then GoTo L0077 Else GoTo L0088
    return 10 if truth(c.unary('not', c.binary('>', f.get('ncount'), Integer(0)))) else 12

def _strreplace_10(f, c):
    # tmp_FF24 = Len(cString)
    f.set('tmp_ff24', c.builtin('len', [f.get('cstring')]))
    # nCount = CLng(CLng(tmp_FF24))
    f.set('ncount', c.builtin('clng', [c.builtin('clng', [f.get('tmp_ff24')])]))
    return 12

def _strreplace_12(f, c):
    # tmp_FF24 = Len(cString)
    f.set('tmp_ff24', c.builtin('len', [f.get('cstring')]))
    # cStringLen = CLng(CLng(tmp_FF24))
    f.set('cstringlen', c.builtin('clng', [c.builtin('clng', [f.get('tmp_ff24')])]))
    # tmp_FF24 = Len(cReplace)
    f.set('tmp_ff24', c.builtin('len', [f.get('creplace')]))
    # cReplLen = CLng(CLng(tmp_FF24))
    f.set('crepllen', c.builtin('clng', [c.builtin('clng', [f.get('tmp_ff24')])]))
    # tmp_FF24 = Len(cSearch)
    f.set('tmp_ff24', c.builtin('len', [f.get('csearch')]))
    # cSrchLen = CLng(CLng(tmp_FF24))
    f.set('csrchlen', c.builtin('clng', [c.builtin('clng', [f.get('tmp_ff24')])]))
    # For X = 1 To cStringLen
    return 19 if f.begin_loop(18, 'x', Integer(1), f.get('cstringlen'), Integer(1)) else 52

def _strreplace_19(f, c):
    # If (X >= nStart) Then GoTo L00DC Else GoTo L0205
    return 20 if truth(c.binary('>=', f.get('x'), f.get('nstart'))) else 47

def _strreplace_20(f, c):
    # tmp_FF24 = Mid(cString, X, cSrchLen)
    f.set('tmp_ff24', c.builtin('mid', [f.get('cstring'), f.get('x'), f.get('csrchlen')]))
    # tmp_FF0C = (tmp_FF24 = cSearch)
    f.set('tmp_ff0c', c.binary('=', f.get('tmp_ff24'), f.get('csearch')))
    # tmp_FEFC = CBool((ReplCount < nCount))
    f.set('tmp_fefc', c.builtin('cbool', [c.binary('<', f.get('replcount'), f.get('ncount'))]))
    # tmp_FEEC = (tmp_FF0C And tmp_FEFC)
    f.set('tmp_feec', c.binary('and', f.get('tmp_ff0c'), f.get('tmp_fefc')))
    # If tmp_FEEC Then GoTo L011C Else GoTo L018A
    return 25 if truth(f.get('tmp_feec')) else 35

def _strreplace_25(f, c):
    # If (X > 1) Then GoTo L012A Else GoTo L0146
    return 26 if truth(c.binary('>', f.get('x'), Integer(1))) else 30

def _strreplace_26(f, c):
    # tmp_FF44 = CStr(NewString)
    f.set('tmp_ff44', c.builtin('cstr', [f.get('newstring')]))
    # tmp_FF24 = (tmp_FF44 & cReplace)
    f.set('tmp_ff24', c.binary('&', f.get('tmp_ff44'), f.get('creplace')))
    # NewString = CStr(CStr(tmp_FF24))
    f.set('newstring', c.builtin('cstr', [c.builtin('cstr', [f.get('tmp_ff24')])]))
    # GoTo L0155
    return 31

def _strreplace_30(f, c):
    # NewString = CStr(CStr(cReplace))
    f.set('newstring', c.builtin('cstr', [c.builtin('cstr', [f.get('creplace')])]))
    return 31

def _strreplace_31(f, c):
    # If (cSrchLen > 1) Then GoTo L0165 Else GoTo L0177
    return 32 if truth(c.binary('>', f.get('csrchlen'), Integer(1))) else 33

def _strreplace_32(f, c):
    # X = CLng((X + (cSrchLen - 1)))
    f.set('x', c.builtin('clng', [c.binary('+', f.get('x'), c.binary('-', f.get('csrchlen'), Integer(1)))]))
    return 33

def _strreplace_33(f, c):
    # ReplCount = CLng((ReplCount + 1))
    f.set('replcount', c.builtin('clng', [c.binary('+', f.get('replcount'), Integer(1))]))
    # GoTo L0200
    return 46

def _strreplace_35(f, c):
    # If (ReplCount < nCount) Then GoTo L0198 Else GoTo L01CA
    return 36 if truth(c.binary('<', f.get('replcount'), f.get('ncount'))) else 41

def _strreplace_36(f, c):
    # tmp_FF34 = CStr(NewString)
    f.set('tmp_ff34', c.builtin('cstr', [f.get('newstring')]))
    # tmp_FF0C = Mid(cString, X, 1)
    f.set('tmp_ff0c', c.builtin('mid', [f.get('cstring'), f.get('x'), Integer(1)]))
    # tmp_FEEC = (tmp_FF34 & tmp_FF0C)
    f.set('tmp_feec', c.binary('&', f.get('tmp_ff34'), f.get('tmp_ff0c')))
    # NewString = CStr(CStr(tmp_FEEC))
    f.set('newstring', c.builtin('cstr', [c.builtin('cstr', [f.get('tmp_feec')])]))
    # GoTo L01FE
    return 46

def _strreplace_41(f, c):
    # tmp_FF34 = CStr(NewString)
    f.set('tmp_ff34', c.builtin('cstr', [f.get('newstring')]))
    # tmp_FF0C = Mid(cString, X)
    f.set('tmp_ff0c', c.builtin('mid', [f.get('cstring'), f.get('x')]))
    # tmp_FEEC = (tmp_FF34 & tmp_FF0C)
    f.set('tmp_feec', c.binary('&', f.get('tmp_ff34'), f.get('tmp_ff0c')))
    # NewString = CStr(CStr(tmp_FEEC))
    f.set('newstring', c.builtin('cstr', [c.builtin('cstr', [f.get('tmp_feec')])]))
    # GoTo L0242
    return 52

def _strreplace_46(f, c):
    # GoTo L0236
    return 51

def _strreplace_47(f, c):
    # tmp_FF34 = CStr(NewString)
    f.set('tmp_ff34', c.builtin('cstr', [f.get('newstring')]))
    # tmp_FF0C = Mid(cString, X, 1)
    f.set('tmp_ff0c', c.builtin('mid', [f.get('cstring'), f.get('x'), Integer(1)]))
    # tmp_FEEC = (tmp_FF34 & tmp_FF0C)
    f.set('tmp_feec', c.binary('&', f.get('tmp_ff34'), f.get('tmp_ff0c')))
    # NewString = CStr(CStr(tmp_FEEC))
    f.set('newstring', c.builtin('cstr', [c.builtin('cstr', [f.get('tmp_feec')])]))
    return 51

def _strreplace_51(f, c):
    # Next X
    return 19 if f.next_loop(18) else 52

def _strreplace_52(f, c):
    # tmp_FF44 = CStr(NewString)
    f.set('tmp_ff44', c.builtin('cstr', [f.get('newstring')]))
    # StrReplace = tmp_FF44
    f.set('strreplace', f.get('tmp_ff44'))
    # Exit Function
    return None

def _strreplace_end(f, c):
    return None

_blocks_strreplace = {0: _strreplace_0, 1: _strreplace_1, 3: _strreplace_3, 4: _strreplace_4, 6: _strreplace_6, 7: _strreplace_7, 9: _strreplace_9, 10: _strreplace_10, 12: _strreplace_12, 19: _strreplace_19, 20: _strreplace_20, 25: _strreplace_25, 26: _strreplace_26, 30: _strreplace_30, 31: _strreplace_31, 32: _strreplace_32, 33: _strreplace_33, 35: _strreplace_35, 36: _strreplace_36, 41: _strreplace_41, 46: _strreplace_46, 47: _strreplace_47, 51: _strreplace_51, 52: _strreplace_52, 55: _strreplace_end}
def vb_strreplace(c, arguments):
    return run(c, 'strreplace', [('cstring', 'variant', False, False, MISSING), ('csearch', 'variant', False, False, MISSING), ('creplace', 'variant', False, False, MISSING), ('nstart', 'long', False, True, MISSING), ('ncount', 'long', False, True, MISSING)], {'tmp_feec': 'variant', 'tmp_fefc': 'variant', 'tmp_ff0c': 'variant', 'tmp_ff24': 'variant', 'tmp_ff34': 'variant', 'tmp_ff44': 'variant', 'csrchlen': 'long', 'cstringlen': 'long', 'replcount': 'long', 'newstring': 'string', 'crepllen': 'long', 'x': 'long'}, 'variant', _blocks_strreplace, arguments)

def _getlastchrpos_0(f, c):
    # If (Not IsNull(pStr)) Then GoTo L0010 Else GoTo L00A3
    return 1 if truth(c.unary('not', c.builtin('isnull', [f.get('pstr')]))) else 11

def _getlastchrpos_1(f, c):
    # tmp_FF38 = InStr(1, pStr, pChr, 2)
    f.set('tmp_ff38', c.builtin('instr', [Integer(1), f.get('pstr'), f.get('pchr'), Integer(2)]))
    # If (tmp_FF38 > 0) Then GoTo L003A Else GoTo L00A1
    return 3 if truth(c.binary('>', f.get('tmp_ff38'), Integer(0))) else 11

def _getlastchrpos_3(f, c):
    # tmp_FF38 = Len(pStr)
    f.set('tmp_ff38', c.builtin('len', [f.get('pstr')]))
    # pLen = tmp_FF38
    f.set('plen', f.get('tmp_ff38'))
    # For X = CInt(pLen) To 1 Step -1
    return 6 if f.begin_loop(5, 'x', c.builtin('cint', [f.get('plen')]), Integer(1), c.unary('-', Integer(1))) else 10

def _getlastchrpos_6(f, c):
    # tmp_FF18 = Mid(pStr, CLng(X), 1)
    f.set('tmp_ff18', c.builtin('mid', [f.get('pstr'), c.builtin('clng', [f.get('x')]), Integer(1)]))
    # If (tmp_FF18 = pChr) Then GoTo L0088 Else GoTo L008D
    return 8 if truth(c.binary('=', f.get('tmp_ff18'), f.get('pchr'))) else 9

def _getlastchrpos_8(f, c):
    # GoTo L0099
    return 10

def _getlastchrpos_9(f, c):
    # Next X
    return 6 if f.next_loop(5) else 10

def _getlastchrpos_10(f, c):
    # GetLastChrPos = CInt(X)
    f.set('getlastchrpos', c.builtin('cint', [f.get('x')]))
    return 11

def _getlastchrpos_11(f, c):
    # Exit Function
    return None

def _getlastchrpos_end(f, c):
    return None

_blocks_getlastchrpos = {0: _getlastchrpos_0, 1: _getlastchrpos_1, 3: _getlastchrpos_3, 6: _getlastchrpos_6, 8: _getlastchrpos_8, 9: _getlastchrpos_9, 10: _getlastchrpos_10, 11: _getlastchrpos_11, 12: _getlastchrpos_end}
def vb_getlastchrpos(c, arguments):
    return run(c, 'getlastchrpos', [('pstr', 'variant', False, False, MISSING), ('pchr', 'variant', False, False, MISSING)], {'tmp_ff18': 'variant', 'tmp_ff38': 'variant', 'plen': 'variant', 'x': 'integer'}, 'integer', _blocks_getlastchrpos, arguments)

def _str2arry_0(f, c):
    # tmp_FF48 = Len(pStr)
    f.set('tmp_ff48', c.builtin('len', [f.get('pstr')]))
    # StrLen = tmp_FF48
    f.set('strlen', f.get('tmp_ff48'))
    # tmp_FF48 = (StrLen - 1)
    f.set('tmp_ff48', c.binary('-', f.get('strlen'), Integer(1)))
    # ReDim Arry(0 To CLng(tmp_FF48))
    f.redim('arry', [(Integer(0), c.builtin('clng', [f.get('tmp_ff48')]))], False, None)
    # For X = 1 To CInt(StrLen)
    return 5 if f.begin_loop(4, 'x', Integer(1), c.builtin('cint', [f.get('strlen')]), Integer(1)) else 9

def _str2arry_5(f, c):
    # tmp_FF24 = CInt((X - 1))
    f.set('tmp_ff24', c.builtin('cint', [c.binary('-', f.get('x'), Integer(1))]))
    # tmp_FF34 = Mid(pStr, CLng(X), 1)
    f.set('tmp_ff34', c.builtin('mid', [f.get('pstr'), c.builtin('clng', [f.get('x')]), Integer(1)]))
    # Arry(tmp_FF24) = tmp_FF34
    f.put('arry', [f.get('tmp_ff24')], f.get('tmp_ff34'))
    # Next X
    return 5 if f.next_loop(4) else 9

def _str2arry_9(f, c):
    # Exit Sub
    return None

def _str2arry_end(f, c):
    return None

_blocks_str2arry = {0: _str2arry_0, 5: _str2arry_5, 9: _str2arry_9, 10: _str2arry_end}
def vb_str2arry(c, arguments):
    return run(c, 'str2arry', [('pstr', 'variant', False, False, MISSING), ('arry', 'variant', False, False, MISSING)], {'tmp_ff24': 'variant', 'tmp_ff34': 'variant', 'tmp_ff48': 'variant', 'x': 'integer', 'strlen': 'variant'}, None, _blocks_str2arry, arguments)

FUNCTIONS = {'bigram': vb_bigram, 'levdist': vb_levdist, 'issimilar': vb_issimilar, 'dice': vb_dice, 'namesimilarity': vb_namesimilarity, 'lcs': vb_lcs, 'doublemetaphone': vb_doublemetaphone, 'metaphadd': vb_metaphadd, 'isvowel': vb_isvowel, 'slavogermanic': vb_slavogermanic, 'isinstr': vb_isinstr, 'rapad': vb_rapad, 'isinarry': vb_isinarry, 'minimum': vb_minimum, 'maximum': vb_maximum, 'strreplace': vb_strreplace, 'getlastchrpos': vb_getlastchrpos, 'str2arry': vb_str2arry}
