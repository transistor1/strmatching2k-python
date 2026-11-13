Attribute VB_Name = "Recovered_DblMetaPhone"
' EXPERIMENTAL reconstruction: not compiled or runtime verified.
' Instructions fully traversed; this does not prove semantic equivalence.
Option Compare Database
Option Explicit

Public cache_m8_0000 As Integer
Public cache_m8_0004 As Variant
Public cache_m8_0014 As Variant

Public Function DoubleMetaphone(ByVal input_pWord As Variant, ByRef MetaPh As Variant, ByRef MetaPh2 As Variant) As Boolean
    Dim tmp_FD08 As Variant
    Dim tmp_FD2A As Integer
    Dim tmp_FD3C As Variant
    Dim tmp_FD4C As Variant
    Dim tmp_FD6C() As Variant
    Dim tmp_FD72 As Integer
    Dim tmp_FD74() As Variant
    Dim tmp_FD7A As Integer
    Dim tmp_FD7C() As Variant
    Dim tmp_FD80 As Variant
    Dim tmp_FD90 As Variant
    Dim tmp_FDA0 As Variant
    Dim tmp_FDB0 As Variant
    Dim tmp_FDD0 As Variant
    Dim tmp_FDE0() As Variant
    Dim tmp_FDE4 As Variant
    Dim tmp_FDF4 As Variant
    Dim tmp_FE04 As Variant
    Dim tmp_FE14 As Variant
    Dim tmp_FE24 As Variant
    Dim tmp_FE34 As Variant
    Dim tmp_FE44 As Variant
    Dim tmp_FE54 As Variant
    Dim tmp_FE64 As Variant
    Dim tmp_FE74 As Variant
    Dim tmp_FE84 As Variant
    Dim tmp_FE94 As Variant
    Dim tmp_FEA4 As Variant
    Dim tmp_FEB4 As Variant
    Dim tmp_FEC4 As Variant
    Dim tmp_FED4 As Variant
    Dim tmp_FEE4 As Variant
    Dim tmp_FEF4 As Variant
    Dim tmp_FF04 As Variant
    Dim tmp_FF14 As Variant
    Dim tmp_FF24() As Variant
    Dim tmp_FF28 As Variant
    Dim tmp_FF3A As Integer
    Dim tmp_FF3C As Variant
    Dim PreviousFlag2 As Boolean
    Dim PreviousFlag As Boolean
    Dim nLast As Integer
    Dim nCurrent As Integer
    Dim sLetter As Variant
    Dim nLength As Integer
    Dim SIGNIFICANTCHARS As Integer
    Dim pWord As Variant

    pWord = input_pWord  ' pc=0002
    cache_m8_0004 = ""  ' pc=000F
    cache_m8_0014 = ""  ' pc=001C
    SIGNIFICANTCHARS = CInt(4)  ' pc=0026
    nLength = CInt(CInt(UBound(pWord, 1)))  ' pc=0036
    nLast = CInt(nLength)  ' pc=003E
    tmp_FF28 = " "  ' pc=0048
    tmp_FF3A = 5  ' pc=0050
    Call RApad(pWord, tmp_FF3A, tmp_FF28)  ' pc=0056
    ReDim tmp_FF24(0 To 4)  ' pc=006D
    tmp_FF24(0) = "GN"  ' pc=0084
    tmp_FF24(1) = "KN"  ' pc=0093
    tmp_FF24(2) = "PN"  ' pc=00A2
    tmp_FF24(3) = "WR"  ' pc=00B1
    tmp_FF24(4) = "PS"  ' pc=00C0
    tmp_FF28 = VBA.Array("GN", "KN", "PN", "WR", "PS")  ' pc=00C8
    Erase tmp_FF24  ' pc=00D0
    tmp_FF3A = 0  ' pc=00D6
    If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L00E7 Else GoTo L00F2  ' pc=00E4
L00E7:
    nCurrent = CInt((nCurrent + 1))  ' pc=00EF
L00F2:
    tmp_FF28 = pWord(0)  ' pc=00FF
    If (tmp_FF28 = "X") Then GoTo L0113 Else GoTo L013A  ' pc=0110
L0113:
    tmp_FF28 = "S"  ' pc=011D
    Call MetaphAdd(tmp_FF28)  ' pc=0123
    nCurrent = CInt((nCurrent + 1))  ' pc=0137
L013A:
L013C:
    tmp_FF28 = Len(cache_m8_0004)  ' pc=0146
    tmp_FED4 = (tmp_FF28 < 4)  ' pc=0150
    tmp_FEC4 = (True Or tmp_FED4)  ' pc=0154
    tmp_FEB4 = Len(cache_m8_0014)  ' pc=015D
    tmp_FEA4 = (tmp_FEB4 < 4)  ' pc=0167
    tmp_FE94 = (tmp_FEC4 Or tmp_FEA4)  ' pc=016B
    If tmp_FE94 Then GoTo L0174 Else GoTo L3CD8  ' pc=0171
L0174:
    PreviousFlag = CInt(0)  ' pc=0178
    PreviousFlag2 = CInt(0)  ' pc=017F
    If (nCurrent > nLength) Then GoTo L018E Else GoTo L0193  ' pc=018B
L018E:
    GoTo L3CD8  ' pc=0190
L0193:
    tmp_FF28 = pWord(nCurrent)  ' pc=01A1
    sLetter = tmp_FF28  ' pc=01A7
    tmp_FE84 = sLetter  ' pc=01B0
    If (tmp_FE84 = "A") Then GoTo L020A Else GoTo L01C4  ' pc=01C1
L01C4:
    If (tmp_FE84 = "E") Then GoTo L020A Else GoTo L01D2  ' pc=01CF
L01D2:
    If (tmp_FE84 = "I") Then GoTo L020A Else GoTo L01E0  ' pc=01DD
L01E0:
    If (tmp_FE84 = "O") Then GoTo L020A Else GoTo L01EE  ' pc=01EB
L01EE:
    If (tmp_FE84 = "U") Then GoTo L020A Else GoTo L01FC  ' pc=01F9
L01FC:
    If (tmp_FE84 = "Y") Then GoTo L020A Else GoTo L0241  ' pc=0207
L020A:
    If (nCurrent = 0) Then GoTo L0215 Else GoTo L0231  ' pc=0212
L0215:
    tmp_FF28 = "A"  ' pc=021F
    Call MetaphAdd(tmp_FF28)  ' pc=0225
L0231:
    nCurrent = CInt((nCurrent + 1))  ' pc=023B
    GoTo L3CD1  ' pc=023E
L0241:
    If (tmp_FE84 = "B") Then GoTo L0251 Else GoTo L02F4  ' pc=024E
L0251:
    If (nCurrent > 0) Then GoTo L025C Else GoTo L0283  ' pc=0259
L025C:
    tmp_FF3C = CInt((nCurrent - 1))  ' pc=0264
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=026B
    tmp_FED4 = (tmp_FF28 = "M")  ' pc=0277
    PreviousFlag = CInt(CBool(tmp_FED4))  ' pc=027D
L0283:
    tmp_FF04 = CBool(PreviousFlag)  ' pc=028A
    tmp_FF28 = pWord(nCurrent)  ' pc=0298
    tmp_FED4 = (tmp_FF28 = "B")  ' pc=02A4
    tmp_FEC4 = (tmp_FF04 And tmp_FED4)  ' pc=02A8
    If tmp_FEC4 Then GoTo L02B8 Else GoTo L02C6  ' pc=02B5
L02B8:
    nCurrent = CInt((nCurrent + 2))  ' pc=02C0
    GoTo L02EF  ' pc=02C3
L02C6:
    tmp_FF28 = "B"  ' pc=02D2
    Call MetaphAdd(tmp_FF28)  ' pc=02D8
    nCurrent = CInt((nCurrent + 1))  ' pc=02EC
L02EF:
    GoTo L3CD1  ' pc=02F1
L02F4:
    If (tmp_FE84 = "Ç") Then GoTo L0304 Else GoTo L032E  ' pc=0301
L0304:
    tmp_FF28 = "S"  ' pc=030E
    Call MetaphAdd(tmp_FF28)  ' pc=0314
    nCurrent = CInt((nCurrent + 1))  ' pc=0328
    GoTo L3CD1  ' pc=032B
L032E:
    If (tmp_FE84 = "C") Then GoTo L033E Else GoTo L1208  ' pc=033B
L033E:
    tmp_FF04 = CBool((nCurrent > 0))  ' pc=0346
    tmp_FF28 = pWord(nCurrent)  ' pc=0354
    tmp_FED4 = (tmp_FF28 Like "[aeiouy]")  ' pc=035F
    tmp_FEC4 = (Not tmp_FED4)  ' pc=0363
    tmp_FEB4 = (tmp_FF04 And tmp_FEC4)  ' pc=0367
    ReDim tmp_FF24(0 To 0)  ' pc=0378
    tmp_FF24(0) = "ACH"  ' pc=038F
    tmp_FEA4 = VBA.Array("ACH")  ' pc=0397
    Erase tmp_FF24  ' pc=039F
    tmp_FEE4 = CBool(IsInArry(pWord, nCurrent, tmp_FEA4))  ' pc=03AE
    tmp_FE94 = (tmp_FEB4 And tmp_FEE4)  ' pc=03B2
    tmp_FE54 = pWord(nCurrent)  ' pc=03C0
    tmp_FE44 = (tmp_FE54 <> "I")  ' pc=03CC
    tmp_FE34 = (tmp_FE94 And tmp_FE44)  ' pc=03D0
    tmp_FE24 = CInt((nCurrent + 2))  ' pc=03DA
    tmp_FDF4 = pWord(tmp_FE24)  ' pc=03E1
    tmp_FDE4 = (tmp_FDF4 <> "E")  ' pc=03ED
    ReDim tmp_FDE0(0 To 1)  ' pc=03FE
    tmp_FDE0(0) = "BACHER"  ' pc=0415
    tmp_FDE0(1) = "MACHER"  ' pc=0424
    tmp_FDB0 = VBA.Array("BACHER", "MACHER")  ' pc=042C
    Erase tmp_FDE0  ' pc=0434
    tmp_FDA0 = CBool(IsInArry(pWord, nCurrent, tmp_FDB0))  ' pc=0443
    tmp_FD90 = (tmp_FDE4 Or tmp_FDA0)  ' pc=0447
    tmp_FD80 = (tmp_FE34 And tmp_FD90)  ' pc=044B
    If tmp_FD80 Then GoTo L0467 Else GoTo L0493  ' pc=0464
L0467:
    tmp_FF28 = "K"  ' pc=0471
    Call MetaphAdd(tmp_FF28)  ' pc=0477
    nCurrent = CInt((nCurrent + 2))  ' pc=048B
    GoTo L3CD3  ' pc=0490
L0493:
    ReDim tmp_FF24(0 To 0)  ' pc=04AA
    tmp_FF24(0) = "CAESAR"  ' pc=04C1
    tmp_FF28 = VBA.Array("CAESAR")  ' pc=04C9
    Erase tmp_FF24  ' pc=04D1
    If ((nCurrent = 0) And IsInArry(pWord, nCurrent, tmp_FF28)) Then GoTo L04E7 Else GoTo L0513  ' pc=04E4
L04E7:
    tmp_FF28 = "S"  ' pc=04F1
    Call MetaphAdd(tmp_FF28)  ' pc=04F7
    nCurrent = CInt((nCurrent + 2))  ' pc=050B
    GoTo L3CD3  ' pc=0510
L0513:
    ReDim tmp_FF24(0 To 0)  ' pc=0524
    tmp_FF24(0) = "CHIA"  ' pc=053B
    tmp_FF28 = VBA.Array("CHIA")  ' pc=0543
    Erase tmp_FF24  ' pc=054B
    If IsInArry(pWord, nCurrent, tmp_FF28) Then GoTo L0560 Else GoTo L058C  ' pc=055D
L0560:
    tmp_FF28 = "K"  ' pc=056A
    Call MetaphAdd(tmp_FF28)  ' pc=0570
    nCurrent = CInt((nCurrent + 2))  ' pc=0584
    GoTo L3CD3  ' pc=0589
L058C:
    tmp_FF28 = pWord(nCurrent)  ' pc=059A
    tmp_FED4 = (tmp_FF28 = "C")  ' pc=05A6
    tmp_FF04 = CInt((nCurrent + 1))  ' pc=05B0
    tmp_FEC4 = pWord(tmp_FF04)  ' pc=05B7
    tmp_FEB4 = (tmp_FEC4 = "H")  ' pc=05C3
    tmp_FEA4 = (tmp_FED4 And tmp_FEB4)  ' pc=05C7
    If tmp_FEA4 Then GoTo L05D7 Else GoTo L0B60  ' pc=05D4
L05D7:
    ReDim tmp_FF24(0 To 0)  ' pc=05EC
    tmp_FF24(0) = "CHAE"  ' pc=0603
    tmp_FF28 = VBA.Array("CHAE")  ' pc=060B
    Erase tmp_FF24  ' pc=0613
    If ((nCurrent > 0) And IsInArry(pWord, nCurrent, tmp_FF28)) Then GoTo L0629 Else GoTo L065D  ' pc=0626
L0629:
    tmp_FED4 = "X"  ' pc=0630
    tmp_FF28 = "K"  ' pc=063B
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=0641
    nCurrent = CInt((nCurrent + 2))  ' pc=0655
    GoTo L3CD3  ' pc=065A
L065D:
    ReDim tmp_FF24(0 To 1)  ' pc=0674
    tmp_FF24(0) = "HARAC"  ' pc=068B
    tmp_FF24(1) = "HARIS"  ' pc=069A
    tmp_FF28 = VBA.Array("HARAC", "HARIS")  ' pc=06A2
    Erase tmp_FF24  ' pc=06AA
    ReDim tmp_FDE0(0 To 3)  ' pc=06C6
    tmp_FDE0(0) = "HOR"  ' pc=06DD
    tmp_FDE0(1) = "HYM"  ' pc=06EC
    tmp_FDE0(2) = "HIA"  ' pc=06FB
    tmp_FDE0(3) = "HEM"  ' pc=070A
    tmp_FED4 = VBA.Array("HOR", "HYM", "HIA", "HEM")  ' pc=0712
    Erase tmp_FDE0  ' pc=071A
    ReDim tmp_FD7C(0 To 0)  ' pc=0738
    tmp_FD7C(0) = "CHORE"  ' pc=074F
    tmp_FEC4 = VBA.Array("CHORE")  ' pc=0757
    Erase tmp_FD7C  ' pc=075F
    tmp_FF3A = 0  ' pc=0765
    If (((nCurrent = 0) And (IsInArry(pWord, nCurrent, tmp_FF28) Or IsInArry(pWord, nCurrent, tmp_FED4))) And (Not IsInArry(pWord, tmp_FF3A, tmp_FEC4))) Then GoTo L077E Else GoTo L07AA  ' pc=077B
L077E:
    tmp_FF28 = "K"  ' pc=0788
    Call MetaphAdd(tmp_FF28)  ' pc=078E
    nCurrent = CInt((nCurrent + 2))  ' pc=07A2
    GoTo L3CD3  ' pc=07A7
L07AA:
    If (nCurrent > 0) Then GoTo L07B7 Else GoTo L0835  ' pc=07B4
L07B7:
    ReDim tmp_FF24(0 To 3)  ' pc=07C6
    tmp_FF24(0) = "A"  ' pc=07DD
    tmp_FF24(1) = "O"  ' pc=07EC
    tmp_FF24(2) = "U"  ' pc=07FB
    tmp_FF24(3) = "E"  ' pc=080A
    tmp_FF28 = VBA.Array("A", "O", "U", "E")  ' pc=0812
    Erase tmp_FF24  ' pc=081A
    tmp_FF3A = (nCurrent - 1)  ' pc=0824
    PreviousFlag = CInt(IsInArry(pWord, tmp_FF3A, tmp_FF28))  ' pc=082F
L0835:
    ReDim tmp_FF24(0 To 1)  ' pc=0846
    tmp_FF24(0) = "VAN "  ' pc=085D
    tmp_FF24(1) = "VON "  ' pc=086C
    tmp_FF28 = VBA.Array("VAN ", "VON ")  ' pc=0874
    Erase tmp_FF24  ' pc=087C
    tmp_FF3A = 0  ' pc=0882
    ReDim tmp_FDE0(0 To 0)  ' pc=089A
    tmp_FDE0(0) = "SCH"  ' pc=08B1
    tmp_FED4 = VBA.Array("SCH")  ' pc=08B9
    Erase tmp_FDE0  ' pc=08C1
    tmp_FD7A = 0  ' pc=08C7
    ReDim tmp_FD7C(0 To 2)  ' pc=08E0
    tmp_FD7C(0) = "ORCHES"  ' pc=08F7
    tmp_FD7C(1) = "ARCHIT"  ' pc=0906
    tmp_FD7C(2) = "ORCHID"  ' pc=0915
    tmp_FEC4 = VBA.Array("ORCHES", "ARCHIT", "ORCHID")  ' pc=091D
    Erase tmp_FD7C  ' pc=0925
    ReDim tmp_FD74(0 To 1)  ' pc=0942
    tmp_FD74(0) = "T"  ' pc=0959
    tmp_FD74(1) = "S"  ' pc=0968
    tmp_FEB4 = VBA.Array("T", "S")  ' pc=0970
    Erase tmp_FD74  ' pc=0978
    tmp_FD72 = (nCurrent + 1)  ' pc=0982
    ReDim tmp_FD6C(0 To 8)  ' pc=09A5
    tmp_FD6C(0) = "L"  ' pc=09BC
    tmp_FD6C(1) = "R"  ' pc=09CB
    tmp_FD6C(2) = "N"  ' pc=09DA
    tmp_FD6C(3) = "M"  ' pc=09E9
    tmp_FD6C(4) = "B"  ' pc=09F8
    tmp_FD6C(5) = "H"  ' pc=0A07
    tmp_FD6C(6) = "F"  ' pc=0A16
    tmp_FD6C(7) = "V"  ' pc=0A25
    tmp_FD6C(8) = "W"  ' pc=0A34
    tmp_FEA4 = VBA.Array("L", "R", "N", "M", "B", "H", "F", "V", "W")  ' pc=0A3C
    Erase tmp_FD6C  ' pc=0A44
    tmp_FD2A = (nCurrent + 1)  ' pc=0A4E
    If ((((IsInArry(pWord, tmp_FF3A, tmp_FF28) Or IsInArry(pWord, tmp_FD7A, tmp_FED4)) Or IsInArry(pWord, nCurrent, tmp_FEC4)) Or IsInArry(pWord, tmp_FD72, tmp_FEB4)) Or ((PreviousFlag Or (nCurrent = 0)) And IsInArry(pWord, tmp_FD2A, tmp_FEA4))) Then GoTo L0A6B Else GoTo L0A8A  ' pc=0A68
L0A6B:
    tmp_FF28 = "K"  ' pc=0A75
    Call MetaphAdd(tmp_FF28)  ' pc=0A7B
    GoTo L0B4E  ' pc=0A87
L0A8A:
    If (nCurrent > 0) Then GoTo L0A97 Else GoTo L0B2E  ' pc=0A94
L0A97:
    ReDim tmp_FF24(0 To 0)  ' pc=0AA6
    tmp_FF24(0) = "MC"  ' pc=0ABD
    tmp_FF28 = VBA.Array("MC")  ' pc=0AC5
    Erase tmp_FF24  ' pc=0ACD
    tmp_FF3A = 0  ' pc=0AD3
    If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L0AE4 Else GoTo L0B03  ' pc=0AE1
L0AE4:
    tmp_FF28 = "K"  ' pc=0AEE
    Call MetaphAdd(tmp_FF28)  ' pc=0AF4
    GoTo L0B29  ' pc=0B00
L0B03:
    tmp_FED4 = "K"  ' pc=0B0C
    tmp_FF28 = "X"  ' pc=0B17
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=0B1D
L0B29:
    GoTo L0B4C  ' pc=0B2B
L0B2E:
    tmp_FF28 = "X"  ' pc=0B3A
    Call MetaphAdd(tmp_FF28)  ' pc=0B40
L0B4C:
L0B4E:
    nCurrent = CInt((nCurrent + 2))  ' pc=0B58
    GoTo L3CD3  ' pc=0B5D
L0B60:
    ReDim tmp_FF24(0 To 0)  ' pc=0B71
    tmp_FF24(0) = "CZ"  ' pc=0B88
    tmp_FF28 = VBA.Array("CZ")  ' pc=0B90
    Erase tmp_FF24  ' pc=0B98
    ReDim tmp_FDE0(0 To 0)  ' pc=0BB4
    tmp_FDE0(0) = "WICZ"  ' pc=0BCB
    tmp_FED4 = VBA.Array("WICZ")  ' pc=0BD3
    Erase tmp_FDE0  ' pc=0BDB
    If (IsInArry(pWord, nCurrent, tmp_FF28) And (Not IsInArry(pWord, nCurrent, tmp_FED4))) Then GoTo L0BF6 Else GoTo L0C2A  ' pc=0BF3
L0BF6:
    tmp_FED4 = "X"  ' pc=0BFD
    tmp_FF28 = "S"  ' pc=0C08
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=0C0E
    nCurrent = CInt((nCurrent + 2))  ' pc=0C22
    GoTo L3CD3  ' pc=0C27
L0C2A:
    ReDim tmp_FF24(0 To 0)  ' pc=0C3B
    tmp_FF24(0) = "CIA"  ' pc=0C52
    tmp_FF28 = VBA.Array("CIA")  ' pc=0C5A
    Erase tmp_FF24  ' pc=0C62
    tmp_FF3A = (nCurrent + 1)  ' pc=0C6C
    If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L0C7D Else GoTo L0CA9  ' pc=0C7A
L0C7D:
    tmp_FF28 = "X"  ' pc=0C87
    Call MetaphAdd(tmp_FF28)  ' pc=0C8D
    nCurrent = CInt((nCurrent + 3))  ' pc=0CA1
    GoTo L3CD3  ' pc=0CA6
L0CA9:
    tmp_FF28 = pWord(nCurrent)  ' pc=0CB7
    tmp_FED4 = (tmp_FF28 = "C")  ' pc=0CC3
    tmp_FF04 = CInt((nCurrent + 1))  ' pc=0CCD
    tmp_FEC4 = pWord(tmp_FF04)  ' pc=0CD4
    tmp_FEB4 = (tmp_FEC4 = "C")  ' pc=0CE0
    tmp_FEA4 = (tmp_FED4 And tmp_FEB4)  ' pc=0CE4
    tmp_FE14 = CBool((nCurrent = 0))  ' pc=0CEE
    tmp_FE94 = pWord(0)  ' pc=0CFB
    tmp_FE54 = (tmp_FE94 = "M")  ' pc=0D07
    tmp_FE44 = (tmp_FE14 And tmp_FE54)  ' pc=0D0B
    tmp_FE34 = (Not tmp_FE44)  ' pc=0D0F
    tmp_FDF4 = (tmp_FEA4 And tmp_FE34)  ' pc=0D13
    If tmp_FDF4 Then GoTo L0D27 Else GoTo L0EFB  ' pc=0D24
L0D27:
    ReDim tmp_FF24(0 To 2)  ' pc=0D36
    tmp_FF24(0) = "I"  ' pc=0D4D
    tmp_FF24(1) = "E"  ' pc=0D5C
    tmp_FF24(2) = "H"  ' pc=0D6B
    tmp_FF28 = VBA.Array("I", "E", "H")  ' pc=0D73
    Erase tmp_FF24  ' pc=0D7B
    tmp_FF3A = (nCurrent + 2)  ' pc=0D85
    tmp_FE04 = CBool(IsInArry(pWord, tmp_FF3A, tmp_FF28))  ' pc=0D90
    tmp_FEF4 = CInt((nCurrent + 2))  ' pc=0D9A
    tmp_FED4 = pWord(tmp_FEF4)  ' pc=0DA1
    tmp_FEC4 = (tmp_FED4 <> "H")  ' pc=0DAD
    tmp_FE64 = CInt((nCurrent + 3))  ' pc=0DB7
    tmp_FEB4 = pWord(tmp_FE64)  ' pc=0DBE
    tmp_FEA4 = (tmp_FEB4 <> "U")  ' pc=0DCA
    tmp_FE94 = (tmp_FEC4 And tmp_FEA4)  ' pc=0DCE
    tmp_FE54 = (tmp_FE04 And tmp_FE94)  ' pc=0DD2
    If tmp_FE54 Then GoTo L0DE6 Else GoTo L0ECB  ' pc=0DE3
L0DE6:
    tmp_FEF4 = CBool((nCurrent = 0))  ' pc=0DEE
    tmp_FF28 = pWord(0)  ' pc=0DFB
    tmp_FED4 = (tmp_FF28 = "A")  ' pc=0E07
    tmp_FEC4 = (tmp_FEF4 And tmp_FED4)  ' pc=0E0B
    ReDim tmp_FF24(0 To 1)  ' pc=0E1C
    tmp_FF24(0) = "UCCEE"  ' pc=0E33
    tmp_FF24(1) = "UCCES"  ' pc=0E42
    tmp_FEB4 = VBA.Array("UCCEE", "UCCES")  ' pc=0E4A
    Erase tmp_FF24  ' pc=0E52
    tmp_FE64 = CBool(IsInArry(pWord, nCurrent, tmp_FEB4))  ' pc=0E61
    tmp_FEA4 = (tmp_FEC4 Or tmp_FE64)  ' pc=0E65
    If tmp_FEA4 Then GoTo L0E79 Else GoTo L0E98  ' pc=0E76
L0E79:
    tmp_FF28 = "KS"  ' pc=0E83
    Call MetaphAdd(tmp_FF28)  ' pc=0E89
    GoTo L0EB6  ' pc=0E95
L0E98:
    tmp_FF28 = "X"  ' pc=0EA4
    Call MetaphAdd(tmp_FF28)  ' pc=0EAA
L0EB6:
    nCurrent = CInt((nCurrent + 3))  ' pc=0EC0
    GoTo L3CD3  ' pc=0EC5
    GoTo L0EF9  ' pc=0EC8
L0ECB:
    tmp_FF28 = "K"  ' pc=0ED7
    Call MetaphAdd(tmp_FF28)  ' pc=0EDD
    nCurrent = CInt((nCurrent + 2))  ' pc=0EF1
    GoTo L3CD3  ' pc=0EF6
L0EF9:
L0EFB:
    ReDim tmp_FF24(0 To 2)  ' pc=0F0C
    tmp_FF24(0) = "CK"  ' pc=0F23
    tmp_FF24(1) = "CG"  ' pc=0F32
    tmp_FF24(2) = "CQ"  ' pc=0F41
    tmp_FF28 = VBA.Array("CK", "CG", "CQ")  ' pc=0F49
    Erase tmp_FF24  ' pc=0F51
    If IsInArry(pWord, nCurrent, tmp_FF28) Then GoTo L0F66 Else GoTo L0F92  ' pc=0F63
L0F66:
    tmp_FF28 = "K"  ' pc=0F70
    Call MetaphAdd(tmp_FF28)  ' pc=0F76
    nCurrent = CInt((nCurrent + 2))  ' pc=0F8A
    GoTo L3CD3  ' pc=0F8F
L0F92:
    ReDim tmp_FF24(0 To 2)  ' pc=0FA3
    tmp_FF24(0) = "CI"  ' pc=0FBA
    tmp_FF24(1) = "CE"  ' pc=0FC9
    tmp_FF24(2) = "CY"  ' pc=0FD8
    tmp_FF28 = VBA.Array("CI", "CE", "CY")  ' pc=0FE0
    Erase tmp_FF24  ' pc=0FE8
    If IsInArry(pWord, nCurrent, tmp_FF28) Then GoTo L0FFD Else GoTo L10BD  ' pc=0FFA
L0FFD:
    ReDim tmp_FF24(0 To 2)  ' pc=100C
    tmp_FF24(0) = "CIO"  ' pc=1023
    tmp_FF24(1) = "CIE"  ' pc=1032
    tmp_FF24(2) = "CIA"  ' pc=1041
    tmp_FF28 = VBA.Array("CIO", "CIE", "CIA")  ' pc=1049
    Erase tmp_FF24  ' pc=1051
    If IsInArry(pWord, nCurrent, tmp_FF28) Then GoTo L1066 Else GoTo L108D  ' pc=1063
L1066:
    tmp_FED4 = "X"  ' pc=106D
    tmp_FF28 = "S"  ' pc=1078
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=107E
    GoTo L10AB  ' pc=108A
L108D:
    tmp_FF28 = "S"  ' pc=1099
    Call MetaphAdd(tmp_FF28)  ' pc=109F
L10AB:
    nCurrent = CInt((nCurrent + 2))  ' pc=10B5
    GoTo L3CD3  ' pc=10BA
L10BD:
    tmp_FF28 = "K"  ' pc=10C9
    Call MetaphAdd(tmp_FF28)  ' pc=10CF
    ReDim tmp_FF24(0 To 2)  ' pc=10EA
    tmp_FF24(0) = " C"  ' pc=1101
    tmp_FF24(1) = " Q"  ' pc=1110
    tmp_FF24(2) = " G"  ' pc=111F
    tmp_FF28 = VBA.Array(" C", " Q", " G")  ' pc=1127
    Erase tmp_FF24  ' pc=112F
    tmp_FF3A = (nCurrent + 1)  ' pc=1139
    If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L114A Else GoTo L1158  ' pc=1147
L114A:
    nCurrent = CInt((nCurrent + 3))  ' pc=1152
    GoTo L1203  ' pc=1155
L1158:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=1162
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=1169
    tmp_FED4 = (tmp_FF28 Like "[CKQ]")  ' pc=1174
    ReDim tmp_FF24(0 To 1)  ' pc=1185
    tmp_FF24(0) = "CE"  ' pc=119C
    tmp_FF24(1) = "CI"  ' pc=11AB
    tmp_FEC4 = VBA.Array("CE", "CI")  ' pc=11B3
    Erase tmp_FF24  ' pc=11BB
    tmp_FF3A = (nCurrent + 1)  ' pc=11C5
    tmp_FE74 = CBool(IsInArry(pWord, tmp_FF3A, tmp_FEC4))  ' pc=11D0
    tmp_FEB4 = (tmp_FED4 And tmp_FE74)  ' pc=11D4
    If tmp_FEB4 Then GoTo L11E6 Else GoTo L11F4  ' pc=11E3
L11E6:
    nCurrent = CInt((nCurrent + 2))  ' pc=11EE
    GoTo L1201  ' pc=11F1
L11F4:
    nCurrent = CInt((nCurrent + 1))  ' pc=11FE
L1201:
L1203:
    GoTo L3CD1  ' pc=1205
L1208:
    If (tmp_FE84 = "D") Then GoTo L1218 Else GoTo L1395  ' pc=1215
L1218:
    tmp_FF28 = pWord(nCurrent)  ' pc=1224
    tmp_FED4 = (tmp_FF28 = "D")  ' pc=1230
    tmp_FF04 = CInt((nCurrent + 1))  ' pc=123A
    tmp_FEC4 = pWord(tmp_FF04)  ' pc=1241
    tmp_FEB4 = (tmp_FEC4 = "G")  ' pc=124D
    tmp_FEA4 = (tmp_FED4 And tmp_FEB4)  ' pc=1251
    If tmp_FEA4 Then GoTo L1261 Else GoTo L12E1  ' pc=125E
L1261:
    tmp_FF3C = CInt((nCurrent + 2))  ' pc=1269
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=1270
    tmp_FED4 = (tmp_FF28 Like "[IEY]")  ' pc=127B
    If tmp_FED4 Then GoTo L1287 Else GoTo L12B1  ' pc=1284
L1287:
    tmp_FF28 = "J"  ' pc=1291
    Call MetaphAdd(tmp_FF28)  ' pc=1297
    nCurrent = CInt((nCurrent + 3))  ' pc=12AB
    GoTo L12DA  ' pc=12AE
L12B1:
    tmp_FF28 = "TK"  ' pc=12BD
    Call MetaphAdd(tmp_FF28)  ' pc=12C3
    nCurrent = CInt((nCurrent + 2))  ' pc=12D7
L12DA:
    GoTo L3CD3  ' pc=12DE
L12E1:
    ReDim tmp_FF24(0 To 1)  ' pc=12F2
    tmp_FF24(0) = "DT"  ' pc=1309
    tmp_FF24(1) = "DD"  ' pc=1318
    tmp_FF28 = VBA.Array("DT", "DD")  ' pc=1320
    Erase tmp_FF24  ' pc=1328
    If IsInArry(pWord, nCurrent, tmp_FF28) Then GoTo L133D Else GoTo L1369  ' pc=133A
L133D:
    tmp_FF28 = "T"  ' pc=1347
    Call MetaphAdd(tmp_FF28)  ' pc=134D
    nCurrent = CInt((nCurrent + 2))  ' pc=1361
    GoTo L3CD3  ' pc=1366
L1369:
    tmp_FF28 = "T"  ' pc=1375
    Call MetaphAdd(tmp_FF28)  ' pc=137B
    nCurrent = CInt((nCurrent + 1))  ' pc=138F
    GoTo L3CD1  ' pc=1392
L1395:
    If (tmp_FE84 = "F") Then GoTo L13A5 Else GoTo L1404  ' pc=13A2
L13A5:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=13AD
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=13B4
    If (tmp_FF28 = "F") Then GoTo L13C8 Else GoTo L13D6  ' pc=13C5
L13C8:
    nCurrent = CInt((nCurrent + 2))  ' pc=13D0
    GoTo L13E3  ' pc=13D3
L13D6:
    nCurrent = CInt((nCurrent + 1))  ' pc=13E0
L13E3:
    tmp_FF28 = "F"  ' pc=13EF
    Call MetaphAdd(tmp_FF28)  ' pc=13F5
    GoTo L3CD1  ' pc=1401
L1404:
    If (tmp_FE84 = "G") Then GoTo L1414 Else GoTo L1E93  ' pc=1411
L1414:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=141C
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=1423
    If (tmp_FF28 = "H") Then GoTo L1437 Else GoTo L16B9  ' pc=1434
L1437:
    tmp_FF04 = CBool((nCurrent > 0))  ' pc=143F
    tmp_FF28 = pWord(nCurrent)  ' pc=144D
    tmp_FED4 = (tmp_FF28 Like "[aeiouy]")  ' pc=1458
    tmp_FEC4 = (Not tmp_FED4)  ' pc=145C
    tmp_FEB4 = (tmp_FF04 And tmp_FEC4)  ' pc=1460
    If tmp_FEB4 Then GoTo L1470 Else GoTo L149C  ' pc=146D
L1470:
    tmp_FF28 = "K"  ' pc=147A
    Call MetaphAdd(tmp_FF28)  ' pc=1480
    nCurrent = CInt((nCurrent + 2))  ' pc=1494
    GoTo L3CD3  ' pc=1499
L149C:
    If (nCurrent < 2) Then GoTo L14A9 Else GoTo L1528  ' pc=14A6
L14A9:
    If (nCurrent = 0) Then GoTo L14B4 Else GoTo L1526  ' pc=14B1
L14B4:
    tmp_FF3C = CInt((nCurrent + 2))  ' pc=14BC
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=14C3
    If (tmp_FF28 = "I") Then GoTo L14D7 Else GoTo L14F6  ' pc=14D4
L14D7:
    tmp_FF28 = "J"  ' pc=14E1
    Call MetaphAdd(tmp_FF28)  ' pc=14E7
    GoTo L1514  ' pc=14F3
L14F6:
    tmp_FF28 = "K"  ' pc=1502
    Call MetaphAdd(tmp_FF28)  ' pc=1508
L1514:
    nCurrent = CInt((nCurrent + 2))  ' pc=151E
    GoTo L3CD3  ' pc=1523
L1526:
L1528:
    tmp_FF04 = CBool((nCurrent > 0))  ' pc=1532
    tmp_FF28 = pWord(nCurrent)  ' pc=1540
    tmp_FED4 = (tmp_FF28 Like "[BHD]")  ' pc=154B
    tmp_FEC4 = (tmp_FF04 And tmp_FED4)  ' pc=154F
    tmp_FE64 = CBool((nCurrent > 1))  ' pc=1559
    tmp_FEF4 = CInt((nCurrent - 1))  ' pc=1563
    tmp_FEB4 = pWord(tmp_FEF4)  ' pc=156A
    tmp_FEA4 = (tmp_FEB4 Like "[BHD]")  ' pc=1575
    tmp_FE94 = (tmp_FE64 And tmp_FEA4)  ' pc=1579
    tmp_FE54 = (tmp_FEC4 Or tmp_FE94)  ' pc=157D
    tmp_FDD0 = CBool((nCurrent > 2))  ' pc=1587
    tmp_FE24 = CInt((nCurrent - 2))  ' pc=1591
    tmp_FE44 = pWord(tmp_FE24)  ' pc=1598
    tmp_FE34 = (tmp_FE44 Like "[BH]")  ' pc=15A3
    tmp_FDF4 = (tmp_FDD0 And tmp_FE34)  ' pc=15A7
    tmp_FDE4 = (tmp_FE54 Or tmp_FDF4)  ' pc=15AB
    If tmp_FDE4 Then GoTo L15C3 Else GoTo L15D6  ' pc=15C0
L15C3:
    nCurrent = CInt((nCurrent + 2))  ' pc=15CB
    GoTo L3CD3  ' pc=15D0
    GoTo L16B7  ' pc=15D3
L15D6:
    tmp_FF04 = CBool((nCurrent > 1))  ' pc=15E0
    tmp_FF28 = pWord(nCurrent)  ' pc=15EE
    tmp_FED4 = (tmp_FF28 = "U")  ' pc=15FA
    tmp_FEC4 = (tmp_FF04 And tmp_FED4)  ' pc=15FE
    tmp_FEF4 = CInt((nCurrent - 1))  ' pc=1608
    tmp_FEB4 = pWord(tmp_FEF4)  ' pc=160F
    tmp_FEA4 = (tmp_FEB4 Like "[CGLRT]")  ' pc=161A
    tmp_FE94 = (tmp_FEC4 And tmp_FEA4)  ' pc=161E
    If tmp_FE94 Then GoTo L1630 Else GoTo L164F  ' pc=162D
L1630:
    tmp_FF28 = "F"  ' pc=163A
    Call MetaphAdd(tmp_FF28)  ' pc=1640
    GoTo L16A5  ' pc=164C
L164F:
    tmp_FF04 = CBool((nCurrent > 0))  ' pc=1659
    tmp_FF28 = pWord(nCurrent)  ' pc=1667
    tmp_FED4 = (tmp_FF28 <> "I")  ' pc=1673
    tmp_FEC4 = (tmp_FF04 And tmp_FED4)  ' pc=1677
    If tmp_FEC4 Then GoTo L1687 Else GoTo L16A3  ' pc=1684
L1687:
    tmp_FF28 = "K"  ' pc=1691
    Call MetaphAdd(tmp_FF28)  ' pc=1697
L16A3:
L16A5:
    nCurrent = CInt((nCurrent + 2))  ' pc=16AF
    GoTo L3CD3  ' pc=16B4
L16B7:
L16B9:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=16C3
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=16CA
    If (tmp_FF28 = "N") Then GoTo L16DE Else GoTo L1829  ' pc=16DB
L16DE:
    tmp_FEF4 = CBool((nCurrent = 0))  ' pc=16E6
    tmp_FF28 = pWord(0)  ' pc=16F3
    tmp_FED4 = (tmp_FF28 Like "[aeiouy]")  ' pc=16FE
    tmp_FEC4 = (tmp_FEF4 And tmp_FED4)  ' pc=1702
    tmp_FEE4 = CBool((Not SlavoGermanic(pWord)))  ' pc=170F
    tmp_FEB4 = (tmp_FEC4 And tmp_FEE4)  ' pc=1713
    If tmp_FEB4 Then GoTo L1725 Else GoTo L174C  ' pc=1722
L1725:
    tmp_FED4 = "N"  ' pc=172C
    tmp_FF28 = "KN"  ' pc=1737
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=173D
    GoTo L1817  ' pc=1749
L174C:
    tmp_FF3C = CInt((nCurrent + 2))  ' pc=1756
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=175D
    tmp_FED4 = (tmp_FF28 <> "E")  ' pc=1769
    tmp_FEF4 = CInt((nCurrent + 3))  ' pc=1773
    tmp_FEC4 = pWord(tmp_FEF4)  ' pc=177A
    tmp_FEB4 = (tmp_FEC4 <> "Y")  ' pc=1786
    tmp_FEA4 = (tmp_FED4 And tmp_FEB4)  ' pc=178A
    tmp_FE64 = CInt((nCurrent + 1))  ' pc=1794
    tmp_FE94 = pWord(tmp_FE64)  ' pc=179B
    tmp_FE54 = (tmp_FE94 <> "Y")  ' pc=17A7
    tmp_FE44 = (tmp_FEA4 And tmp_FE54)  ' pc=17AB
    tmp_FE04 = CBool((Not SlavoGermanic(pWord)))  ' pc=17B8
    tmp_FE34 = (tmp_FE44 And tmp_FE04)  ' pc=17BC
    If tmp_FE34 Then GoTo L17D0 Else GoTo L17F7  ' pc=17CD
L17D0:
    tmp_FED4 = "KN"  ' pc=17D7
    tmp_FF28 = "N"  ' pc=17E2
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=17E8
    GoTo L1815  ' pc=17F4
L17F7:
    tmp_FF28 = "KN"  ' pc=1803
    Call MetaphAdd(tmp_FF28)  ' pc=1809
L1815:
L1817:
    nCurrent = CInt((nCurrent + 2))  ' pc=1821
    GoTo L3CD3  ' pc=1826
L1829:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=1833
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=183A
    tmp_FED4 = (tmp_FF28 = "L")  ' pc=1846
    tmp_FEF4 = CInt((nCurrent + 2))  ' pc=1850
    tmp_FEC4 = pWord(tmp_FEF4)  ' pc=1857
    tmp_FEB4 = (tmp_FEC4 = "I")  ' pc=1863
    tmp_FEA4 = (tmp_FED4 And tmp_FEB4)  ' pc=1867
    tmp_FE64 = CBool((Not SlavoGermanic(pWord)))  ' pc=1874
    tmp_FE94 = (tmp_FEA4 And tmp_FE64)  ' pc=1878
    If tmp_FE94 Then GoTo L188A Else GoTo L18BE  ' pc=1887
L188A:
    tmp_FED4 = "L"  ' pc=1891
    tmp_FF28 = "KL"  ' pc=189C
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=18A2
    nCurrent = CInt((nCurrent + 2))  ' pc=18B6
    GoTo L3CD3  ' pc=18BB
L18BE:
    tmp_FD3C = CBool((nCurrent = 0))  ' pc=18C8
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=18D2
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=18D9
    tmp_FED4 = (tmp_FF28 = "Y")  ' pc=18E5
    ReDim tmp_FF24(0 To 10)  ' pc=18F6
    tmp_FF24(0) = "ES"  ' pc=190D
    tmp_FF24(1) = "EP"  ' pc=191C
    tmp_FF24(2) = "EB"  ' pc=192B
    tmp_FF24(3) = "EL"  ' pc=193A
    tmp_FF24(4) = "EY"  ' pc=1949
    tmp_FF24(5) = "IB"  ' pc=1958
    tmp_FF24(6) = "IL"  ' pc=1967
    tmp_FF24(7) = "IN"  ' pc=1976
    tmp_FF24(8) = "IE"  ' pc=1985
    tmp_FF24(9) = "EI"  ' pc=1994
    tmp_FF24(10) = "ER"  ' pc=19A3
    tmp_FEC4 = VBA.Array("ES", "EP", "EB", "EL", "EY", "IB", "IL", "IN", "IE", "EI", "ER")  ' pc=19AB
    Erase tmp_FF24  ' pc=19B3
    tmp_FF3A = (nCurrent + 1)  ' pc=19BD
    tmp_FD4C = CBool(IsInArry(pWord, tmp_FF3A, tmp_FEC4))  ' pc=19C8
    tmp_FEB4 = (tmp_FED4 Or tmp_FD4C)  ' pc=19CC
    tmp_FEA4 = (tmp_FD3C And tmp_FEB4)  ' pc=19D0
    If tmp_FEA4 Then GoTo L19E4 Else GoTo L1A18  ' pc=19E1
L19E4:
    tmp_FED4 = "J"  ' pc=19EB
    tmp_FF28 = "K"  ' pc=19F6
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=19FC
    nCurrent = CInt((nCurrent + 2))  ' pc=1A10
    GoTo L3CD3  ' pc=1A15
L1A18:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=1A22
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=1A29
    tmp_FED4 = (tmp_FF28 = "E")  ' pc=1A35
    tmp_FEF4 = CInt((nCurrent + 2))  ' pc=1A3F
    tmp_FEC4 = pWord(tmp_FEF4)  ' pc=1A46
    tmp_FEB4 = (tmp_FEC4 = "R")  ' pc=1A52
    tmp_FEA4 = (tmp_FED4 And tmp_FEB4)  ' pc=1A56
    tmp_FE64 = CInt((nCurrent + 1))  ' pc=1A60
    tmp_FE94 = pWord(tmp_FE64)  ' pc=1A67
    tmp_FE54 = (tmp_FE94 = "Y")  ' pc=1A73
    tmp_FE44 = (tmp_FEA4 Or tmp_FE54)  ' pc=1A77
    ReDim tmp_FF24(0 To 2)  ' pc=1A88
    tmp_FF24(0) = "DANGER"  ' pc=1A9F
    tmp_FF24(1) = "RANGER"  ' pc=1AAE
    tmp_FF24(2) = "MANGER"  ' pc=1ABD
    tmp_FE34 = VBA.Array("DANGER", "RANGER", "MANGER")  ' pc=1AC5
    Erase tmp_FF24  ' pc=1ACD
    tmp_FF3A = 1  ' pc=1AD3
    tmp_FDA0 = CBool((Not IsInArry(pWord, tmp_FF3A, tmp_FE34)))  ' pc=1ADF
    tmp_FDF4 = (tmp_FE44 And tmp_FDA0)  ' pc=1AE3
    ReDim tmp_FDE0(0 To 1)  ' pc=1AF4
    tmp_FDE0(0) = "E"  ' pc=1B0B
    tmp_FDE0(1) = "I"  ' pc=1B1A
    tmp_FDE4 = VBA.Array("E", "I")  ' pc=1B22
    Erase tmp_FDE0  ' pc=1B2A
    tmp_FD3C = CBool((Not IsInArry(pWord, nCurrent, tmp_FDE4)))  ' pc=1B3A
    tmp_FDB0 = (tmp_FDF4 And tmp_FD3C)  ' pc=1B3E
    ReDim tmp_FD7C(0 To 1)  ' pc=1B4F
    tmp_FD7C(0) = "RGY"  ' pc=1B66
    tmp_FD7C(1) = "OGY"  ' pc=1B75
    tmp_FD90 = VBA.Array("RGY", "OGY")  ' pc=1B7D
    Erase tmp_FD7C  ' pc=1B85
    tmp_FD08 = CBool((Not IsInArry(pWord, nCurrent, tmp_FD90)))  ' pc=1B95
    tmp_FD80 = (tmp_FDB0 And tmp_FD08)  ' pc=1B99
    If tmp_FD80 Then GoTo L1BB7 Else GoTo L1BEB  ' pc=1BB4
L1BB7:
    tmp_FED4 = "J"  ' pc=1BBE
    tmp_FF28 = "K"  ' pc=1BC9
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=1BCF
    nCurrent = CInt((nCurrent + 2))  ' pc=1BE3
    GoTo L3CD3  ' pc=1BE8
L1BEB:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=1BF5
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=1BFC
    tmp_FED4 = (tmp_FF28 Like "[EIY]")  ' pc=1C07
    ReDim tmp_FF24(0 To 1)  ' pc=1C18
    tmp_FF24(0) = "AGGI"  ' pc=1C2F
    tmp_FF24(1) = "OGGI"  ' pc=1C3E
    tmp_FEC4 = VBA.Array("AGGI", "OGGI")  ' pc=1C46
    Erase tmp_FF24  ' pc=1C4E
    tmp_FE74 = CBool(IsInArry(pWord, nCurrent, tmp_FEC4))  ' pc=1C5D
    tmp_FEB4 = (tmp_FED4 Or tmp_FE74)  ' pc=1C61
    If tmp_FEB4 Then GoTo L1C73 Else GoTo L1E32  ' pc=1C70
L1C73:
    ReDim tmp_FF24(0 To 1)  ' pc=1C82
    tmp_FF24(0) = "VAN "  ' pc=1C99
    tmp_FF24(1) = "VON "  ' pc=1CA8
    tmp_FF28 = VBA.Array("VAN ", "VON ")  ' pc=1CB0
    Erase tmp_FF24  ' pc=1CB8
    tmp_FF3A = 0  ' pc=1CBE
    ReDim tmp_FDE0(0 To 0)  ' pc=1CD6
    tmp_FDE0(0) = "SCH"  ' pc=1CED
    tmp_FED4 = VBA.Array("SCH")  ' pc=1CF5
    Erase tmp_FDE0  ' pc=1CFD
    tmp_FD7A = 0  ' pc=1D03
    tmp_FE04 = CBool((IsInArry(pWord, tmp_FF3A, tmp_FF28) Or IsInArry(pWord, tmp_FD7A, tmp_FED4)))  ' pc=1D0F
    tmp_FEF4 = CInt((nCurrent + 1))  ' pc=1D19
    tmp_FEC4 = pWord(tmp_FEF4)  ' pc=1D20
    tmp_FEB4 = (tmp_FEC4 = "E")  ' pc=1D2C
    tmp_FE64 = CInt((nCurrent + 2))  ' pc=1D36
    tmp_FEA4 = pWord(tmp_FE64)  ' pc=1D3D
    tmp_FE94 = (tmp_FEA4 = "T")  ' pc=1D49
    tmp_FE54 = (tmp_FEB4 And tmp_FE94)  ' pc=1D4D
    tmp_FE44 = (tmp_FE04 Or tmp_FE54)  ' pc=1D51
    If tmp_FE44 Then GoTo L1D67 Else GoTo L1D86  ' pc=1D64
L1D67:
    tmp_FF28 = "K"  ' pc=1D71
    Call MetaphAdd(tmp_FF28)  ' pc=1D77
    GoTo L1E20  ' pc=1D83
L1D86:
    ReDim tmp_FF24(0 To 0)  ' pc=1D97
    tmp_FF24(0) = "IER "  ' pc=1DAE
    tmp_FF28 = VBA.Array("IER ")  ' pc=1DB6
    Erase tmp_FF24  ' pc=1DBE
    tmp_FF3A = (nCurrent + 1)  ' pc=1DC8
    If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L1DD9 Else GoTo L1DF8  ' pc=1DD6
L1DD9:
    tmp_FF28 = "J"  ' pc=1DE3
    Call MetaphAdd(tmp_FF28)  ' pc=1DE9
    GoTo L1E1E  ' pc=1DF5
L1DF8:
    tmp_FED4 = "K"  ' pc=1E01
    tmp_FF28 = "J"  ' pc=1E0C
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=1E12
L1E1E:
L1E20:
    nCurrent = CInt((nCurrent + 2))  ' pc=1E2A
    GoTo L3CD3  ' pc=1E2F
L1E32:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=1E3C
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=1E43
    If (tmp_FF28 = "G") Then GoTo L1E57 Else GoTo L1E65  ' pc=1E54
L1E57:
    nCurrent = CInt((nCurrent + 2))  ' pc=1E5F
    GoTo L1E72  ' pc=1E62
L1E65:
    nCurrent = CInt((nCurrent + 1))  ' pc=1E6F
L1E72:
    tmp_FF28 = "K"  ' pc=1E7E
    Call MetaphAdd(tmp_FF28)  ' pc=1E84
    GoTo L3CD1  ' pc=1E90
L1E93:
    If (tmp_FE84 = "H") Then GoTo L1EA3 Else GoTo L1F57  ' pc=1EA0
L1EA3:
    If (nCurrent > 0) Then GoTo L1EAE Else GoTo L1ED4  ' pc=1EAB
L1EAE:
    tmp_FF3C = CInt((nCurrent - 1))  ' pc=1EB6
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=1EBD
    tmp_FED4 = (tmp_FF28 Like "[aeiouy]")  ' pc=1EC8
    PreviousFlag = CInt(CBool(tmp_FED4))  ' pc=1ECE
L1ED4:
    tmp_FEE4 = CBool((nCurrent = 0))  ' pc=1EDE
    tmp_FEF4 = CBool(PreviousFlag)  ' pc=1EE5
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=1EEF
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=1EF6
    tmp_FED4 = (tmp_FF28 Like "[aeiouy]")  ' pc=1F01
    tmp_FEC4 = (tmp_FEF4 And tmp_FED4)  ' pc=1F05
    tmp_FEB4 = (tmp_FEE4 Or tmp_FEC4)  ' pc=1F09
    If tmp_FEB4 Then GoTo L1F1B Else GoTo L1F45  ' pc=1F18
L1F1B:
    tmp_FF28 = "H"  ' pc=1F25
    Call MetaphAdd(tmp_FF28)  ' pc=1F2B
    nCurrent = CInt((nCurrent + 2))  ' pc=1F3F
    GoTo L1F52  ' pc=1F42
L1F45:
    nCurrent = CInt((nCurrent + 1))  ' pc=1F4F
L1F52:
    GoTo L3CD1  ' pc=1F54
L1F57:
    If (tmp_FE84 = "J") Then GoTo L1F67 Else GoTo L22F2  ' pc=1F64
L1F67:
    ReDim tmp_FF24(0 To 0)  ' pc=1F76
    tmp_FF24(0) = "JOSE"  ' pc=1F8D
    tmp_FF28 = VBA.Array("JOSE")  ' pc=1F95
    Erase tmp_FF24  ' pc=1F9D
    ReDim tmp_FDE0(0 To 0)  ' pc=1FB9
    tmp_FDE0(0) = "SAN "  ' pc=1FD0
    tmp_FED4 = VBA.Array("SAN ")  ' pc=1FD8
    Erase tmp_FDE0  ' pc=1FE0
    tmp_FF3A = 0  ' pc=1FE6
    If (IsInArry(pWord, nCurrent, tmp_FF28) Or IsInArry(pWord, tmp_FF3A, tmp_FED4)) Then GoTo L1FFC Else GoTo L20DD  ' pc=1FF9
L1FFC:
    tmp_FEF4 = CBool((nCurrent = 0))  ' pc=2004
    tmp_FF3C = CInt((nCurrent + 3))  ' pc=200E
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=2015
    tmp_FED4 = (tmp_FF28 = " ")  ' pc=2021
    tmp_FEC4 = (tmp_FEF4 And tmp_FED4)  ' pc=2025
    ReDim tmp_FF24(0 To 0)  ' pc=2036
    tmp_FF24(0) = "SAN "  ' pc=204D
    tmp_FEB4 = VBA.Array("SAN ")  ' pc=2055
    Erase tmp_FF24  ' pc=205D
    tmp_FF3A = 1  ' pc=2063
    tmp_FE74 = CBool(IsInArry(pWord, tmp_FF3A, tmp_FEB4))  ' pc=206E
    tmp_FEA4 = (tmp_FEC4 Or tmp_FE74)  ' pc=2072
    If tmp_FEA4 Then GoTo L2086 Else GoTo L20A5  ' pc=2083
L2086:
    tmp_FF28 = "H"  ' pc=2090
    Call MetaphAdd(tmp_FF28)  ' pc=2096
    GoTo L20CB  ' pc=20A2
L20A5:
    tmp_FED4 = "H"  ' pc=20AE
    tmp_FF28 = "J"  ' pc=20B9
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=20BF
L20CB:
    nCurrent = CInt((nCurrent + 1))  ' pc=20D5
    GoTo L3CD3  ' pc=20DA
L20DD:
    ReDim tmp_FF24(0 To 0)  ' pc=20F4
    tmp_FF24(0) = "JOSE"  ' pc=210B
    tmp_FF28 = VBA.Array("JOSE")  ' pc=2113
    Erase tmp_FF24  ' pc=211B
    tmp_FF3A = 0  ' pc=2121
    If ((nCurrent = 0) And (Not IsInArry(pWord, tmp_FF3A, tmp_FF28))) Then GoTo L2134 Else GoTo L215B  ' pc=2131
L2134:
    tmp_FED4 = "A"  ' pc=213B
    tmp_FF28 = "J"  ' pc=2146
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=214C
    GoTo L22AD  ' pc=2158
L215B:
    tmp_FF28 = pWord(nCurrent)  ' pc=2169
    tmp_FED4 = (tmp_FF28 Like "[aeiouy]")  ' pc=2174
    tmp_FF04 = CBool((Not SlavoGermanic(pWord)))  ' pc=2181
    tmp_FEC4 = (tmp_FED4 And tmp_FF04)  ' pc=2185
    tmp_FEF4 = CInt((nCurrent + 1))  ' pc=218F
    tmp_FEB4 = pWord(tmp_FEF4)  ' pc=2196
    tmp_FEA4 = (tmp_FEB4 = "A")  ' pc=21A2
    tmp_FE64 = CInt((nCurrent + 2))  ' pc=21AC
    tmp_FE94 = pWord(tmp_FE64)  ' pc=21B3
    tmp_FE54 = (tmp_FE94 = "O")  ' pc=21BF
    tmp_FE44 = (tmp_FEA4 And tmp_FE54)  ' pc=21C3
    tmp_FE34 = (tmp_FEC4 And tmp_FE44)  ' pc=21C7
    If tmp_FE34 Then GoTo L21DB Else GoTo L2202  ' pc=21D8
L21DB:
    tmp_FED4 = "H"  ' pc=21E2
    tmp_FF28 = "J"  ' pc=21ED
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=21F3
    GoTo L22AB  ' pc=21FF
L2202:
    If (nCurrent = (nLast - 1)) Then GoTo L2213 Else GoTo L223A  ' pc=2210
L2213:
    tmp_FED4 = " "  ' pc=221A
    tmp_FF28 = "J"  ' pc=2225
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=222B
    GoTo L22A9  ' pc=2237
L223A:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=2244
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=224B
    tmp_FED4 = (tmp_FF28 Like "[LTKSNMBZ]")  ' pc=2256
    tmp_FEC4 = (Not tmp_FED4)  ' pc=225A
    tmp_FEB4 = pWord(nCurrent)  ' pc=2268
    tmp_FEA4 = (tmp_FEB4 Like "[SKL]")  ' pc=2273
    tmp_FE94 = (Not tmp_FEA4)  ' pc=2277
    tmp_FE54 = (tmp_FEC4 And tmp_FE94)  ' pc=227B
    If tmp_FE54 Then GoTo L228B Else GoTo L22A7  ' pc=2288
L228B:
    tmp_FF28 = "J"  ' pc=2295
    Call MetaphAdd(tmp_FF28)  ' pc=229B
L22A7:
L22A9:
L22AB:
L22AD:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=22B7
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=22BE
    If (tmp_FF28 = "J") Then GoTo L22D2 Else GoTo L22E0  ' pc=22CF
L22D2:
    nCurrent = CInt((nCurrent + 2))  ' pc=22DA
    GoTo L22ED  ' pc=22DD
L22E0:
    nCurrent = CInt((nCurrent + 1))  ' pc=22EA
L22ED:
    GoTo L3CD1  ' pc=22EF
L22F2:
    If (tmp_FE84 = "K") Then GoTo L2302 Else GoTo L2361  ' pc=22FF
L2302:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=230A
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=2311
    If (tmp_FF28 = "K") Then GoTo L2325 Else GoTo L2333  ' pc=2322
L2325:
    nCurrent = CInt((nCurrent + 2))  ' pc=232D
    GoTo L2340  ' pc=2330
L2333:
    nCurrent = CInt((nCurrent + 1))  ' pc=233D
L2340:
    tmp_FF28 = "K"  ' pc=234C
    Call MetaphAdd(tmp_FF28)  ' pc=2352
    GoTo L3CD1  ' pc=235E
L2361:
    If (tmp_FE84 = "L") Then GoTo L2371 Else GoTo L255F  ' pc=236E
L2371:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=2379
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=2380
    If (tmp_FF28 = "L") Then GoTo L2394 Else GoTo L2531  ' pc=2391
L2394:
    If (nCurrent = ((nLength - 3) - 1)) Then GoTo L23A6 Else GoTo L2521  ' pc=23A3
L23A6:
    ReDim tmp_FF24(0 To 2)  ' pc=23B5
    tmp_FF24(0) = "ILLO"  ' pc=23CC
    tmp_FF24(1) = "ILLA"  ' pc=23DB
    tmp_FF24(2) = "ALLE"  ' pc=23EA
    tmp_FF28 = VBA.Array("ILLO", "ILLA", "ALLE")  ' pc=23F2
    Erase tmp_FF24  ' pc=23FA
    tmp_FDD0 = CBool(IsInArry(pWord, nCurrent, tmp_FF28))  ' pc=2409
    ReDim tmp_FDE0(0 To 1)  ' pc=241A
    tmp_FDE0(0) = "AS"  ' pc=2431
    tmp_FDE0(1) = "OS"  ' pc=2440
    tmp_FED4 = VBA.Array("AS", "OS")  ' pc=2448
    Erase tmp_FDE0  ' pc=2450
    tmp_FF3A = (nLast - 1)  ' pc=245A
    tmp_FE24 = CBool(IsInArry(pWord, tmp_FF3A, tmp_FED4))  ' pc=2465
    tmp_FEC4 = pWord(nLast)  ' pc=2473
    tmp_FEB4 = (tmp_FEC4 Like "[AO]")  ' pc=247E
    tmp_FEA4 = (tmp_FE24 Or tmp_FEB4)  ' pc=2482
    ReDim tmp_FD7C(0 To 0)  ' pc=2493
    tmp_FD7C(0) = "ALLE"  ' pc=24AA
    tmp_FE94 = VBA.Array("ALLE")  ' pc=24B2
    Erase tmp_FD7C  ' pc=24BA
    tmp_FE04 = CBool(IsInArry(pWord, nCurrent, tmp_FE94))  ' pc=24C9
    tmp_FE54 = (tmp_FEA4 And tmp_FE04)  ' pc=24CD
    tmp_FE44 = (tmp_FDD0 Or tmp_FE54)  ' pc=24D1
    If tmp_FE44 Then GoTo L24EB Else GoTo L251F  ' pc=24E8
L24EB:
    tmp_FED4 = " "  ' pc=24F2
    tmp_FF28 = "L"  ' pc=24FD
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=2503
    nCurrent = CInt((nCurrent + 2))  ' pc=2517
    GoTo L3CD3  ' pc=251C
L251F:
L2521:
    nCurrent = CInt((nCurrent + 2))  ' pc=252B
    GoTo L253E  ' pc=252E
L2531:
    nCurrent = CInt((nCurrent + 1))  ' pc=253B
L253E:
    tmp_FF28 = "L"  ' pc=254A
    Call MetaphAdd(tmp_FF28)  ' pc=2550
    GoTo L3CD1  ' pc=255C
L255F:
    If (tmp_FE84 = "M") Then GoTo L256F Else GoTo L267D  ' pc=256C
L256F:
    ReDim tmp_FF24(0 To 0)  ' pc=257E
    tmp_FF24(0) = "UMB"  ' pc=2595
    tmp_FF28 = VBA.Array("UMB")  ' pc=259D
    Erase tmp_FF24  ' pc=25A5
    tmp_FE14 = CBool(IsInArry(pWord, nCurrent, tmp_FF28))  ' pc=25B4
    tmp_FE24 = CInt((((nCurrent + 1) = nLast) - 1))  ' pc=25C5
    tmp_FF14 = CInt((nCurrent + 2))  ' pc=25CE
    tmp_FED4 = pWord(tmp_FF14)  ' pc=25D5
    tmp_FEC4 = (tmp_FED4 = "E")  ' pc=25E1
    tmp_FEE4 = CInt((nCurrent + 3))  ' pc=25EB
    tmp_FEB4 = pWord(tmp_FEE4)  ' pc=25F2
    tmp_FEA4 = (tmp_FEB4 = "R")  ' pc=25FE
    tmp_FE94 = (tmp_FEC4 And tmp_FEA4)  ' pc=2602
    tmp_FE54 = (tmp_FE24 Or tmp_FE94)  ' pc=2606
    tmp_FE44 = (tmp_FE14 And tmp_FE54)  ' pc=260A
    tmp_FE04 = CInt((nCurrent + 1))  ' pc=2614
    tmp_FE34 = pWord(tmp_FE04)  ' pc=261B
    tmp_FDF4 = (tmp_FE34 = "M")  ' pc=2627
    tmp_FDE4 = (tmp_FE44 Or tmp_FDF4)  ' pc=262B
    If tmp_FDE4 Then GoTo L2641 Else GoTo L264F  ' pc=263E
L2641:
    nCurrent = CInt((nCurrent + 2))  ' pc=2649
    GoTo L265C  ' pc=264C
L264F:
    nCurrent = CInt((nCurrent + 1))  ' pc=2659
L265C:
    tmp_FF28 = "M"  ' pc=2668
    Call MetaphAdd(tmp_FF28)  ' pc=266E
    GoTo L3CD1  ' pc=267A
L267D:
    If (tmp_FE84 = "N") Then GoTo L268D Else GoTo L26EC  ' pc=268A
L268D:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=2695
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=269C
    If (tmp_FF28 = "N") Then GoTo L26B0 Else GoTo L26BE  ' pc=26AD
L26B0:
    nCurrent = CInt((nCurrent + 2))  ' pc=26B8
    GoTo L26CB  ' pc=26BB
L26BE:
    nCurrent = CInt((nCurrent + 1))  ' pc=26C8
L26CB:
    tmp_FF28 = "N"  ' pc=26D7
    Call MetaphAdd(tmp_FF28)  ' pc=26DD
    GoTo L3CD1  ' pc=26E9
L26EC:
    If (tmp_FE84 = "Ñ") Then GoTo L26FC Else GoTo L2726  ' pc=26F9
L26FC:
    nCurrent = CInt((nCurrent + 1))  ' pc=2704
    tmp_FF28 = "N"  ' pc=2711
    Call MetaphAdd(tmp_FF28)  ' pc=2717
    GoTo L3CD1  ' pc=2723
L2726:
    If (tmp_FE84 = "P") Then GoTo L2736 Else GoTo L280F  ' pc=2733
L2736:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=273E
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=2745
    If (tmp_FF28 = "H") Then GoTo L2759 Else GoTo L2785  ' pc=2756
L2759:
    tmp_FF28 = "F"  ' pc=2763
    Call MetaphAdd(tmp_FF28)  ' pc=2769
    nCurrent = CInt((nCurrent + 2))  ' pc=277D
    GoTo L3CD3  ' pc=2782
L2785:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=278F
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=2796
    tmp_FED4 = (tmp_FF28 = "P")  ' pc=27A2
    tmp_FEF4 = CInt((nCurrent + 2))  ' pc=27AC
    tmp_FEC4 = pWord(tmp_FEF4)  ' pc=27B3
    tmp_FEB4 = (tmp_FEC4 = "B")  ' pc=27BF
    tmp_FEA4 = (tmp_FED4 And tmp_FEB4)  ' pc=27C3
    If tmp_FEA4 Then GoTo L27D3 Else GoTo L27E1  ' pc=27D0
L27D3:
    nCurrent = CInt((nCurrent + 2))  ' pc=27DB
    GoTo L280A  ' pc=27DE
L27E1:
    nCurrent = CInt((nCurrent + 1))  ' pc=27EB
    tmp_FF28 = "P"  ' pc=27F8
    Call MetaphAdd(tmp_FF28)  ' pc=27FE
L280A:
    GoTo L3CD1  ' pc=280C
L280F:
    If (tmp_FE84 = "Q") Then GoTo L281F Else GoTo L287E  ' pc=281C
L281F:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=2827
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=282E
    If (tmp_FF28 = "Q") Then GoTo L2842 Else GoTo L2850  ' pc=283F
L2842:
    nCurrent = CInt((nCurrent + 2))  ' pc=284A
    GoTo L285D  ' pc=284D
L2850:
    nCurrent = CInt((nCurrent + 1))  ' pc=285A
L285D:
    tmp_FF28 = "K"  ' pc=2869
    Call MetaphAdd(tmp_FF28)  ' pc=286F
    GoTo L3CD1  ' pc=287B
L287E:
    If (tmp_FE84 = "R") Then GoTo L288E Else GoTo L29F2  ' pc=288B
L288E:
    If ((nCurrent = (nLast - 1)) And (Not SlavoGermanic(pWord))) Then GoTo L28A7 Else GoTo L298F  ' pc=28A4
L28A7:
    tmp_FF28 = pWord(nCurrent)  ' pc=28B3
    tmp_FED4 = (tmp_FF28 = "I")  ' pc=28BF
    tmp_FF04 = CInt((nCurrent + 1))  ' pc=28C9
    tmp_FEC4 = pWord(tmp_FF04)  ' pc=28D0
    tmp_FEB4 = (tmp_FEC4 = "E")  ' pc=28DC
    tmp_FEA4 = (tmp_FED4 And tmp_FEB4)  ' pc=28E0
    If tmp_FEA4 Then GoTo L28F0 Else GoTo L2983  ' pc=28ED
L28F0:
    ReDim tmp_FF24(0 To 1)  ' pc=28FF
    tmp_FF24(0) = "ME"  ' pc=2916
    tmp_FF24(1) = "MA"  ' pc=2925
    tmp_FF28 = VBA.Array("ME", "MA")  ' pc=292D
    Erase tmp_FF24  ' pc=2935
    tmp_FF3A = (nCurrent - 2)  ' pc=293F
    If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L2950 Else GoTo L2977  ' pc=294D
L2950:
    tmp_FED4 = "R"  ' pc=2957
    tmp_FF28 = ""  ' pc=2962
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=2968
    GoTo L297E  ' pc=2974
L2977:
    GoTo L2991  ' pc=297B
L297E:
    GoTo L298A  ' pc=2980
L2983:
    GoTo L2991  ' pc=2987
L298A:
    GoTo L29AD  ' pc=298C
L298F:
L2991:
    tmp_FF28 = "R"  ' pc=299B
    Call MetaphAdd(tmp_FF28)  ' pc=29A1
L29AD:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=29B7
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=29BE
    If (tmp_FF28 = "R") Then GoTo L29D2 Else GoTo L29E0  ' pc=29CF
L29D2:
    nCurrent = CInt((nCurrent + 2))  ' pc=29DA
    GoTo L29ED  ' pc=29DD
L29E0:
    nCurrent = CInt((nCurrent + 1))  ' pc=29EA
L29ED:
    GoTo L3CD1  ' pc=29EF
L29F2:
    If (tmp_FE84 = "S") Then GoTo L2A02 Else GoTo L31ED  ' pc=29FF
L2A02:
    ReDim tmp_FF24(0 To 1)  ' pc=2A11
    tmp_FF24(0) = "ISL"  ' pc=2A28
    tmp_FF24(1) = "YSL"  ' pc=2A37
    tmp_FF28 = VBA.Array("ISL", "YSL")  ' pc=2A3F
    Erase tmp_FF24  ' pc=2A47
    If IsInArry(pWord, nCurrent, tmp_FF28) Then GoTo L2A5C Else GoTo L2A6C  ' pc=2A59
L2A5C:
    nCurrent = CInt((nCurrent + 1))  ' pc=2A64
    GoTo L3CD3  ' pc=2A69
L2A6C:
    ReDim tmp_FF24(0 To 0)  ' pc=2A83
    tmp_FF24(0) = "SUGAR"  ' pc=2A9A
    tmp_FF28 = VBA.Array("SUGAR")  ' pc=2AA2
    Erase tmp_FF24  ' pc=2AAA
    If ((nCurrent = 0) And IsInArry(pWord, nCurrent, tmp_FF28)) Then GoTo L2AC0 Else GoTo L2AF4  ' pc=2ABD
L2AC0:
    tmp_FED4 = "S"  ' pc=2AC7
    tmp_FF28 = "X"  ' pc=2AD2
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=2AD8
    nCurrent = CInt((nCurrent + 1))  ' pc=2AEC
    GoTo L3CD3  ' pc=2AF1
L2AF4:
    tmp_FF28 = pWord(nCurrent)  ' pc=2B02
    tmp_FED4 = (tmp_FF28 = "S")  ' pc=2B0E
    tmp_FF04 = CInt((nCurrent + 1))  ' pc=2B18
    tmp_FEC4 = pWord(tmp_FF04)  ' pc=2B1F
    tmp_FEB4 = (tmp_FEC4 = "H")  ' pc=2B2B
    tmp_FEA4 = (tmp_FED4 And tmp_FEB4)  ' pc=2B2F
    If tmp_FEA4 Then GoTo L2B3F Else GoTo L2C0C  ' pc=2B3C
L2B3F:
    ReDim tmp_FF24(0 To 3)  ' pc=2B4E
    tmp_FF24(0) = "HEIM"  ' pc=2B65
    tmp_FF24(1) = "HOEK"  ' pc=2B74
    tmp_FF24(2) = "HOLM"  ' pc=2B83
    tmp_FF24(3) = "HOLZ"  ' pc=2B92
    tmp_FF28 = VBA.Array("HEIM", "HOEK", "HOLM", "HOLZ")  ' pc=2B9A
    Erase tmp_FF24  ' pc=2BA2
    tmp_FF3A = (nCurrent + 1)  ' pc=2BAC
    If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L2BBD Else GoTo L2BDC  ' pc=2BBA
L2BBD:
    tmp_FF28 = "S"  ' pc=2BC7
    Call MetaphAdd(tmp_FF28)  ' pc=2BCD
    GoTo L2BFA  ' pc=2BD9
L2BDC:
    tmp_FF28 = "X"  ' pc=2BE8
    Call MetaphAdd(tmp_FF28)  ' pc=2BEE
L2BFA:
    nCurrent = CInt((nCurrent + 2))  ' pc=2C04
    GoTo L3CD3  ' pc=2C09
L2C0C:
    ReDim tmp_FF24(0 To 1)  ' pc=2C1D
    tmp_FF24(0) = "SIO"  ' pc=2C34
    tmp_FF24(1) = "SIA"  ' pc=2C43
    tmp_FF28 = VBA.Array("SIO", "SIA")  ' pc=2C4B
    Erase tmp_FF24  ' pc=2C53
    ReDim tmp_FDE0(0 To 0)  ' pc=2C6F
    tmp_FDE0(0) = "SIAN"  ' pc=2C86
    tmp_FED4 = VBA.Array("SIAN")  ' pc=2C8E
    Erase tmp_FDE0  ' pc=2C96
    If (IsInArry(pWord, nCurrent, tmp_FF28) Or IsInArry(pWord, nCurrent, tmp_FED4)) Then GoTo L2CB0 Else GoTo L2D15  ' pc=2CAD
L2CB0:
    If (Not SlavoGermanic(pWord)) Then GoTo L2CBE Else GoTo L2CE5  ' pc=2CBB
L2CBE:
    tmp_FED4 = "X"  ' pc=2CC5
    tmp_FF28 = "S"  ' pc=2CD0
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=2CD6
    GoTo L2D03  ' pc=2CE2
L2CE5:
    tmp_FF28 = "S"  ' pc=2CF1
    Call MetaphAdd(tmp_FF28)  ' pc=2CF7
L2D03:
    nCurrent = CInt((nCurrent + 3))  ' pc=2D0D
    GoTo L3CD3  ' pc=2D12
L2D15:
    tmp_FEF4 = CBool((nCurrent = 0))  ' pc=2D1F
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=2D29
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=2D30
    tmp_FED4 = (tmp_FF28 Like "[MNLW]")  ' pc=2D3B
    tmp_FEC4 = (tmp_FEF4 And tmp_FED4)  ' pc=2D3F
    tmp_FEE4 = CInt((nCurrent + 1))  ' pc=2D49
    tmp_FEB4 = pWord(tmp_FEE4)  ' pc=2D50
    tmp_FEA4 = (tmp_FEB4 = "Z")  ' pc=2D5C
    tmp_FE94 = (tmp_FEC4 Or tmp_FEA4)  ' pc=2D60
    If tmp_FE94 Then GoTo L2D72 Else GoTo L2DDB  ' pc=2D6F
L2D72:
    tmp_FED4 = "X"  ' pc=2D79
    tmp_FF28 = "S"  ' pc=2D84
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=2D8A
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=2D9E
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=2DA5
    If (tmp_FF28 = "Z") Then GoTo L2DB9 Else GoTo L2DC7  ' pc=2DB6
L2DB9:
    nCurrent = CInt((nCurrent + 2))  ' pc=2DC1
    GoTo L2DD4  ' pc=2DC4
L2DC7:
    nCurrent = CInt((nCurrent + 1))  ' pc=2DD1
L2DD4:
    GoTo L3CD3  ' pc=2DD8
L2DDB:
    tmp_FF28 = pWord(nCurrent)  ' pc=2DE9
    tmp_FED4 = (tmp_FF28 = "S")  ' pc=2DF5
    tmp_FF04 = CInt((nCurrent + 1))  ' pc=2DFF
    tmp_FEC4 = pWord(tmp_FF04)  ' pc=2E06
    tmp_FEB4 = (tmp_FEC4 = "C")  ' pc=2E12
    tmp_FEA4 = (tmp_FED4 And tmp_FEB4)  ' pc=2E16
    If tmp_FEA4 Then GoTo L2E26 Else GoTo L30D3  ' pc=2E23
L2E26:
    tmp_FF3C = CInt((nCurrent + 2))  ' pc=2E2E
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=2E35
    If (tmp_FF28 = "H") Then GoTo L2E49 Else GoTo L3051  ' pc=2E46
L2E49:
    ReDim tmp_FF24(0 To 5)  ' pc=2E58
    tmp_FF24(0) = "OO"  ' pc=2E6F
    tmp_FF24(1) = "ER"  ' pc=2E7E
    tmp_FF24(2) = "EN"  ' pc=2E8D
    tmp_FF24(3) = "UY"  ' pc=2E9C
    tmp_FF24(4) = "ED"  ' pc=2EAB
    tmp_FF24(5) = "EM"  ' pc=2EBA
    tmp_FF28 = VBA.Array("OO", "ER", "EN", "UY", "ED", "EM")  ' pc=2EC2
    Erase tmp_FF24  ' pc=2ECA
    tmp_FF3A = (nCurrent + 3)  ' pc=2ED4
    If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L2EE5 Else GoTo L2F9F  ' pc=2EE2
L2EE5:
    ReDim tmp_FF24(0 To 1)  ' pc=2EF4
    tmp_FF24(0) = "ER"  ' pc=2F0B
    tmp_FF24(1) = "EN"  ' pc=2F1A
    tmp_FF28 = VBA.Array("ER", "EN")  ' pc=2F22
    Erase tmp_FF24  ' pc=2F2A
    tmp_FF3A = (nCurrent + 3)  ' pc=2F34
    If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L2F45 Else GoTo L2F6C  ' pc=2F42
L2F45:
    tmp_FED4 = "SK"  ' pc=2F4C
    tmp_FF28 = "X"  ' pc=2F57
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=2F5D
    GoTo L2F8A  ' pc=2F69
L2F6C:
    tmp_FF28 = "SK"  ' pc=2F78
    Call MetaphAdd(tmp_FF28)  ' pc=2F7E
L2F8A:
    nCurrent = CInt((nCurrent + 3))  ' pc=2F94
    GoTo L3CD3  ' pc=2F99
    GoTo L304F  ' pc=2F9C
L2F9F:
    tmp_FEF4 = CBool((nCurrent = 0))  ' pc=2FA9
    tmp_FF28 = pWord(2)  ' pc=2FB6
    tmp_FED4 = (tmp_FF28 Like "[aeiouy]")  ' pc=2FC1
    tmp_FEC4 = (Not tmp_FED4)  ' pc=2FC5
    tmp_FEB4 = (tmp_FEF4 And tmp_FEC4)  ' pc=2FC9
    tmp_FEA4 = pWord(2)  ' pc=2FD6
    tmp_FE94 = (tmp_FEA4 <> "W")  ' pc=2FE2
    tmp_FE54 = (tmp_FEB4 And tmp_FE94)  ' pc=2FE6
    If tmp_FE54 Then GoTo L2FF8 Else GoTo L301F  ' pc=2FF5
L2FF8:
    tmp_FED4 = "S"  ' pc=2FFF
    tmp_FF28 = "X"  ' pc=300A
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=3010
    GoTo L303D  ' pc=301C
L301F:
    tmp_FF28 = "X"  ' pc=302B
    Call MetaphAdd(tmp_FF28)  ' pc=3031
L303D:
    nCurrent = CInt((nCurrent + 3))  ' pc=3047
    GoTo L3CD3  ' pc=304C
L304F:
L3051:
    tmp_FF3C = CInt((nCurrent + 2))  ' pc=305B
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=3062
    tmp_FED4 = (tmp_FF28 Like "[IEY]")  ' pc=306D
    If tmp_FED4 Then GoTo L3079 Else GoTo L30A5  ' pc=3076
L3079:
    tmp_FF28 = "S"  ' pc=3083
    Call MetaphAdd(tmp_FF28)  ' pc=3089
    nCurrent = CInt((nCurrent + 3))  ' pc=309D
    GoTo L3CD3  ' pc=30A2
L30A5:
    tmp_FF28 = "SK"  ' pc=30B1
    Call MetaphAdd(tmp_FF28)  ' pc=30B7
    nCurrent = CInt((nCurrent + 3))  ' pc=30CB
    GoTo L3CD3  ' pc=30D0
L30D3:
    ReDim tmp_FF24(0 To 1)  ' pc=30EE
    tmp_FF24(0) = "AI"  ' pc=3105
    tmp_FF24(1) = "OI"  ' pc=3114
    tmp_FF28 = VBA.Array("AI", "OI")  ' pc=311C
    Erase tmp_FF24  ' pc=3124
    If ((nCurrent = (nLast - 1)) And IsInArry(pWord, nCurrent, tmp_FF28)) Then GoTo L313A Else GoTo L3161  ' pc=3137
L313A:
    tmp_FED4 = "S"  ' pc=3141
    tmp_FF28 = ""  ' pc=314C
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=3152
    GoTo L317F  ' pc=315E
L3161:
    tmp_FF28 = "S"  ' pc=316D
    Call MetaphAdd(tmp_FF28)  ' pc=3173
L317F:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=3189
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=3190
    tmp_FED4 = (tmp_FF28 = "S")  ' pc=319C
    tmp_FEF4 = CInt((nCurrent + 2))  ' pc=31A6
    tmp_FEC4 = pWord(tmp_FEF4)  ' pc=31AD
    tmp_FEB4 = (tmp_FEC4 = "Z")  ' pc=31B9
    tmp_FEA4 = (tmp_FED4 And tmp_FEB4)  ' pc=31BD
    If tmp_FEA4 Then GoTo L31CD Else GoTo L31DB  ' pc=31CA
L31CD:
    nCurrent = CInt((nCurrent + 2))  ' pc=31D5
    GoTo L31E8  ' pc=31D8
L31DB:
    nCurrent = CInt((nCurrent + 1))  ' pc=31E5
L31E8:
    GoTo L3CD1  ' pc=31EA
L31ED:
    If (tmp_FE84 = "T") Then GoTo L31FD Else GoTo L3578  ' pc=31FA
L31FD:
    ReDim tmp_FF24(0 To 0)  ' pc=320C
    tmp_FF24(0) = "TION"  ' pc=3223
    tmp_FF28 = VBA.Array("TION")  ' pc=322B
    Erase tmp_FF24  ' pc=3233
    If IsInArry(pWord, nCurrent, tmp_FF28) Then GoTo L3248 Else GoTo L3274  ' pc=3245
L3248:
    tmp_FF28 = "X"  ' pc=3252
    Call MetaphAdd(tmp_FF28)  ' pc=3258
    nCurrent = CInt((nCurrent + 3))  ' pc=326C
    GoTo L3CD3  ' pc=3271
L3274:
    ReDim tmp_FF24(0 To 1)  ' pc=3285
    tmp_FF24(0) = "TIA"  ' pc=329C
    tmp_FF24(1) = "TCH"  ' pc=32AB
    tmp_FF28 = VBA.Array("TIA", "TCH")  ' pc=32B3
    Erase tmp_FF24  ' pc=32BB
    If IsInArry(pWord, nCurrent, tmp_FF28) Then GoTo L32D0 Else GoTo L32FC  ' pc=32CD
L32D0:
    tmp_FF28 = "X"  ' pc=32DA
    Call MetaphAdd(tmp_FF28)  ' pc=32E0
    nCurrent = CInt((nCurrent + 3))  ' pc=32F4
    GoTo L3CD3  ' pc=32F9
L32FC:
    tmp_FF28 = pWord(nCurrent)  ' pc=330A
    tmp_FED4 = (tmp_FF28 = "T")  ' pc=3316
    tmp_FF04 = CInt((nCurrent + 1))  ' pc=3320
    tmp_FEC4 = pWord(tmp_FF04)  ' pc=3327
    tmp_FEB4 = (tmp_FEC4 = "H")  ' pc=3333
    tmp_FEA4 = (tmp_FED4 And tmp_FEB4)  ' pc=3337
    ReDim tmp_FF24(0 To 0)  ' pc=3348
    tmp_FF24(0) = "TTH"  ' pc=335F
    tmp_FE94 = VBA.Array("TTH")  ' pc=3367
    Erase tmp_FF24  ' pc=336F
    tmp_FE64 = CBool(IsInArry(pWord, nCurrent, tmp_FE94))  ' pc=337E
    tmp_FE54 = (tmp_FEA4 Or tmp_FE64)  ' pc=3382
    If tmp_FE54 Then GoTo L3396 Else GoTo L34EE  ' pc=3393
L3396:
    ReDim tmp_FF24(0 To 1)  ' pc=33A5
    tmp_FF24(0) = "OM"  ' pc=33BC
    tmp_FF24(1) = "AM"  ' pc=33CB
    tmp_FF28 = VBA.Array("OM", "AM")  ' pc=33D3
    Erase tmp_FF24  ' pc=33DB
    tmp_FF3A = (nCurrent + 2)  ' pc=33E5
    ReDim tmp_FDE0(0 To 1)  ' pc=33FD
    tmp_FDE0(0) = "VAN "  ' pc=3414
    tmp_FDE0(1) = "VON "  ' pc=3423
    tmp_FED4 = VBA.Array("VAN ", "VON ")  ' pc=342B
    Erase tmp_FDE0  ' pc=3433
    tmp_FD7A = 1  ' pc=3439
    ReDim tmp_FD7C(0 To 0)  ' pc=3452
    tmp_FD7C(0) = "SCH"  ' pc=3469
    tmp_FEC4 = VBA.Array("SCH")  ' pc=3471
    Erase tmp_FD7C  ' pc=3479
    tmp_FD72 = 0  ' pc=347F
    If ((IsInArry(pWord, tmp_FF3A, tmp_FF28) Or IsInArry(pWord, tmp_FD7A, tmp_FED4)) Or IsInArry(pWord, tmp_FD72, tmp_FEC4)) Then GoTo L3497 Else GoTo L34B6  ' pc=3494
L3497:
    tmp_FF28 = "T"  ' pc=34A1
    Call MetaphAdd(tmp_FF28)  ' pc=34A7
    GoTo L34DC  ' pc=34B3
L34B6:
    tmp_FED4 = "T"  ' pc=34BF
    tmp_FF28 = "0"  ' pc=34CA
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=34D0
L34DC:
    nCurrent = CInt((nCurrent + 2))  ' pc=34E6
    GoTo L3CD3  ' pc=34EB
L34EE:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=34F8
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=34FF
    tmp_FED4 = (tmp_FF28 = "T")  ' pc=350B
    tmp_FEF4 = CInt((nCurrent + 2))  ' pc=3515
    tmp_FEC4 = pWord(tmp_FEF4)  ' pc=351C
    tmp_FEB4 = (tmp_FEC4 = "D")  ' pc=3528
    tmp_FEA4 = (tmp_FED4 And tmp_FEB4)  ' pc=352C
    If tmp_FEA4 Then GoTo L353C Else GoTo L354A  ' pc=3539
L353C:
    nCurrent = CInt((nCurrent + 2))  ' pc=3544
    GoTo L3573  ' pc=3547
L354A:
    nCurrent = CInt((nCurrent + 1))  ' pc=3554
    tmp_FF28 = "T"  ' pc=3561
    Call MetaphAdd(tmp_FF28)  ' pc=3567
L3573:
    GoTo L3CD1  ' pc=3575
L3578:
    If (tmp_FE84 = "V") Then GoTo L3588 Else GoTo L35E7  ' pc=3585
L3588:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=3590
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=3597
    If (tmp_FF28 = "V") Then GoTo L35AB Else GoTo L35B9  ' pc=35A8
L35AB:
    nCurrent = CInt((nCurrent + 2))  ' pc=35B3
    GoTo L35E2  ' pc=35B6
L35B9:
    nCurrent = CInt((nCurrent + 1))  ' pc=35C3
    tmp_FF28 = "F"  ' pc=35D0
    Call MetaphAdd(tmp_FF28)  ' pc=35D6
L35E2:
    GoTo L3CD1  ' pc=35E4
L35E7:
    If (tmp_FE84 = "W") Then GoTo L35F7 Else GoTo L3932  ' pc=35F4
L35F7:
    tmp_FF28 = pWord(nCurrent)  ' pc=3603
    tmp_FED4 = (tmp_FF28 = "W")  ' pc=360F
    tmp_FF04 = CInt((nCurrent + 1))  ' pc=3619
    tmp_FEC4 = pWord(tmp_FF04)  ' pc=3620
    tmp_FEB4 = (tmp_FEC4 = "R")  ' pc=362C
    tmp_FEA4 = (tmp_FED4 And tmp_FEB4)  ' pc=3630
    If tmp_FEA4 Then GoTo L3640 Else GoTo L366C  ' pc=363D
L3640:
    tmp_FF28 = "R"  ' pc=364A
    Call MetaphAdd(tmp_FF28)  ' pc=3650
    nCurrent = CInt((nCurrent + 2))  ' pc=3664
    GoTo L3CD3  ' pc=3669
L366C:
    tmp_FEF4 = CBool((nCurrent = 0))  ' pc=3676
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=3680
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=3687
    tmp_FED4 = (tmp_FF28 Like "[aeiouy]")  ' pc=3692
    tmp_FEC4 = (tmp_FEF4 And tmp_FED4)  ' pc=3696
    tmp_FEB4 = pWord(nCurrent)  ' pc=36A4
    tmp_FEA4 = (tmp_FEB4 = "W")  ' pc=36B0
    tmp_FE64 = CInt((nCurrent + 1))  ' pc=36BA
    tmp_FE94 = pWord(tmp_FE64)  ' pc=36C1
    tmp_FE54 = (tmp_FE94 = "H")  ' pc=36CD
    tmp_FE44 = (tmp_FEA4 And tmp_FE54)  ' pc=36D1
    tmp_FE34 = (tmp_FEC4 Or tmp_FE44)  ' pc=36D5
    If tmp_FE34 Then GoTo L36E9 Else GoTo L3756  ' pc=36E6
L36E9:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=36F1
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=36F8
    tmp_FED4 = (tmp_FF28 Like "[aeiouy]")  ' pc=3703
    If tmp_FED4 Then GoTo L370F Else GoTo L3736  ' pc=370C
L370F:
    tmp_FED4 = "F"  ' pc=3716
    tmp_FF28 = "A"  ' pc=3721
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=3727
    GoTo L3754  ' pc=3733
L3736:
    tmp_FF28 = "R"  ' pc=3742
    Call MetaphAdd(tmp_FF28)  ' pc=3748
L3754:
L3756:
    tmp_FF04 = CBool((nCurrent = (nLast - 1)))  ' pc=3764
    tmp_FF28 = pWord(nCurrent)  ' pc=3772
    tmp_FED4 = (tmp_FF28 Like "[aeiouy]")  ' pc=377D
    tmp_FEC4 = (tmp_FF04 And tmp_FED4)  ' pc=3781
    ReDim tmp_FF24(0 To 3)  ' pc=3792
    tmp_FF24(0) = "EWSKI"  ' pc=37A9
    tmp_FF24(1) = "EWSKY"  ' pc=37B8
    tmp_FF24(2) = "OWSKI"  ' pc=37C7
    tmp_FF24(3) = "OWSKY"  ' pc=37D6
    tmp_FEB4 = VBA.Array("EWSKI", "EWSKY", "OWSKI", "OWSKY")  ' pc=37DE
    Erase tmp_FF24  ' pc=37E6
    tmp_FE24 = CBool(IsInArry(pWord, nCurrent, tmp_FEB4))  ' pc=37F5
    tmp_FEA4 = (tmp_FEC4 Or tmp_FE24)  ' pc=37F9
    ReDim tmp_FDE0(0 To 0)  ' pc=380A
    tmp_FDE0(0) = "SCH"  ' pc=3821
    tmp_FE94 = VBA.Array("SCH")  ' pc=3829
    Erase tmp_FDE0  ' pc=3831
    tmp_FF3A = 1  ' pc=3837
    tmp_FE04 = CBool(IsInArry(pWord, tmp_FF3A, tmp_FE94))  ' pc=3842
    tmp_FE54 = (tmp_FEA4 Or tmp_FE04)  ' pc=3846
    If tmp_FE54 Then GoTo L385E Else GoTo L3892  ' pc=385B
L385E:
    tmp_FED4 = "F"  ' pc=3865
    tmp_FF28 = ""  ' pc=3870
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=3876
    nCurrent = CInt((nCurrent + 1))  ' pc=388A
    GoTo L3CD3  ' pc=388F
L3892:
    ReDim tmp_FF24(0 To 1)  ' pc=38A3
    tmp_FF24(0) = "WICZ"  ' pc=38BA
    tmp_FF24(1) = "WITZ"  ' pc=38C9
    tmp_FF28 = VBA.Array("WICZ", "WITZ")  ' pc=38D1
    Erase tmp_FF24  ' pc=38D9
    If IsInArry(pWord, nCurrent, tmp_FF28) Then GoTo L38EE Else GoTo L3922  ' pc=38EB
L38EE:
    tmp_FED4 = "FX"  ' pc=38F5
    tmp_FF28 = "TS"  ' pc=3900
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=3906
    nCurrent = CInt((nCurrent + 4))  ' pc=391A
    GoTo L3CD3  ' pc=391F
L3922:
    nCurrent = CInt((nCurrent + 1))  ' pc=392C
    GoTo L3CD1  ' pc=392F
L3932:
    If (tmp_FE84 = "X") Then GoTo L3942 Else GoTo L3B29  ' pc=393F
L3942:
    If (nCurrent > 2) Then GoTo L394D Else GoTo L39AD  ' pc=394A
L394D:
    ReDim tmp_FF24(0 To 1)  ' pc=395C
    tmp_FF24(0) = "IAU"  ' pc=3973
    tmp_FF24(1) = "EAU"  ' pc=3982
    tmp_FF28 = VBA.Array("IAU", "EAU")  ' pc=398A
    Erase tmp_FF24  ' pc=3992
    tmp_FF3A = (nCurrent - 3)  ' pc=399C
    PreviousFlag = CInt(IsInArry(pWord, tmp_FF3A, tmp_FF28))  ' pc=39A7
L39AD:
    If (nCurrent > 1) Then GoTo L39BA Else GoTo L3A1A  ' pc=39B7
L39BA:
    ReDim tmp_FF24(0 To 1)  ' pc=39C9
    tmp_FF24(0) = "AU"  ' pc=39E0
    tmp_FF24(1) = "OU"  ' pc=39EF
    tmp_FF28 = VBA.Array("AU", "OU")  ' pc=39F7
    Erase tmp_FF24  ' pc=39FF
    tmp_FF3A = (nCurrent - 2)  ' pc=3A09
    PreviousFlag2 = CInt(IsInArry(pWord, tmp_FF3A, tmp_FF28))  ' pc=3A14
L3A1A:
    If (Not ((nCurrent = (nLast - 1)) And (PreviousFlag Or PreviousFlag2))) Then GoTo L3A34 Else GoTo L3A50  ' pc=3A31
L3A34:
    tmp_FF28 = "KS"  ' pc=3A3E
    Call MetaphAdd(tmp_FF28)  ' pc=3A44
L3A50:
    ReDim tmp_FF24(0 To 0)  ' pc=3A61
    tmp_FF24(0) = "AUX"  ' pc=3A78
    tmp_FF28 = VBA.Array("AUX")  ' pc=3A80
    Erase tmp_FF24  ' pc=3A88
    tmp_FF3A = 0  ' pc=3A8E
    If IsInArry(pWord, tmp_FF3A, tmp_FF28) Then GoTo L3A9F Else GoTo L3ABB  ' pc=3A9C
L3A9F:
    tmp_FF28 = "KS"  ' pc=3AA9
    Call MetaphAdd(tmp_FF28)  ' pc=3AAF
L3ABB:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=3AC5
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=3ACC
    tmp_FED4 = (tmp_FF28 = "C")  ' pc=3AD8
    tmp_FEF4 = CInt((nCurrent + 2))  ' pc=3AE2
    tmp_FEC4 = pWord(tmp_FEF4)  ' pc=3AE9
    tmp_FEB4 = (tmp_FEC4 = "X")  ' pc=3AF5
    tmp_FEA4 = (tmp_FED4 And tmp_FEB4)  ' pc=3AF9
    If tmp_FEA4 Then GoTo L3B09 Else GoTo L3B17  ' pc=3B06
L3B09:
    nCurrent = CInt((nCurrent + 2))  ' pc=3B11
    GoTo L3B24  ' pc=3B14
L3B17:
    nCurrent = CInt((nCurrent + 1))  ' pc=3B21
L3B24:
    GoTo L3CD1  ' pc=3B26
L3B29:
    If (tmp_FE84 = "Z") Then GoTo L3B39 Else GoTo L3CC4  ' pc=3B36
L3B39:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=3B41
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=3B48
    If (tmp_FF28 = "H") Then GoTo L3B5C Else GoTo L3B8B  ' pc=3B59
L3B5C:
    tmp_FF28 = "J"  ' pc=3B66
    Call MetaphAdd(tmp_FF28)  ' pc=3B6C
    nCurrent = CInt((nCurrent + 2))  ' pc=3B80
    GoTo L3CD3  ' pc=3B85
    GoTo L3CBF  ' pc=3B88
L3B8B:
    ReDim tmp_FF24(0 To 2)  ' pc=3B9C
    tmp_FF24(0) = "ZO"  ' pc=3BB3
    tmp_FF24(1) = "ZI"  ' pc=3BC2
    tmp_FF24(2) = "ZA"  ' pc=3BD1
    tmp_FF28 = VBA.Array("ZO", "ZI", "ZA")  ' pc=3BD9
    Erase tmp_FF24  ' pc=3BE1
    tmp_FF3A = (nCurrent + 1)  ' pc=3BEB
    tmp_FE64 = CBool(IsInArry(pWord, tmp_FF3A, tmp_FF28))  ' pc=3BF6
    tmp_FE74 = CBool(SlavoGermanic(pWord))  ' pc=3C02
    tmp_FED4 = pWord(nCurrent)  ' pc=3C10
    tmp_FEC4 = (tmp_FED4 <> "T")  ' pc=3C1C
    tmp_FEB4 = (tmp_FE74 And tmp_FEC4)  ' pc=3C20
    tmp_FEA4 = (tmp_FE64 Or tmp_FEB4)  ' pc=3C24
    If tmp_FEA4 Then GoTo L3C38 Else GoTo L3C5F  ' pc=3C35
L3C38:
    tmp_FED4 = "TS"  ' pc=3C3F
    tmp_FF28 = "S"  ' pc=3C4A
    Call MetaphAdd(tmp_FF28, tmp_FED4)  ' pc=3C50
    GoTo L3C7D  ' pc=3C5C
L3C5F:
    tmp_FF28 = "S"  ' pc=3C6B
    Call MetaphAdd(tmp_FF28)  ' pc=3C71
L3C7D:
    tmp_FF3C = CInt((nCurrent + 1))  ' pc=3C87
    tmp_FF28 = pWord(tmp_FF3C)  ' pc=3C8E
    If (tmp_FF28 = "Z") Then GoTo L3CA2 Else GoTo L3CB0  ' pc=3C9F
L3CA2:
    nCurrent = CInt((nCurrent + 2))  ' pc=3CAA
    GoTo L3CBD  ' pc=3CAD
L3CB0:
    nCurrent = CInt((nCurrent + 1))  ' pc=3CBA
L3CBD:
L3CBF:
    GoTo L3CD1  ' pc=3CC1
L3CC4:
    nCurrent = CInt((nCurrent + 1))  ' pc=3CCE
L3CD1:
L3CD3:
    GoTo L013C  ' pc=3CD5
L3CD8:
    MetaPh = cache_m8_0004  ' pc=3CDF
    If cache_m8_0000 Then GoTo L3CED Else GoTo L3CF8  ' pc=3CEA
L3CED:
    MetaPh2 = cache_m8_0014  ' pc=3CF4
L3CF8:
    DoubleMetaphone = CInt(-1)  ' pc=3CFE
    Exit Function  ' pc=3D03
End Function

Public Sub MetaphAdd(ByRef pChr As Variant, Optional ByRef pChr2 As Variant)
    Dim tmp_FF5C As Variant

    tmp_FF5C = (cache_m8_0004 & pChr)  ' pc=000F
    cache_m8_0004 = tmp_FF5C  ' pc=0013
    If (Not IsMissing(pChr2)) Then GoTo L0027 Else GoTo L0090  ' pc=0024
L0027:
    cache_m8_0000 = CInt(-1)  ' pc=002B
    If (pChr2 <> " ") Then GoTo L0043 Else GoTo L005D  ' pc=0040
L0043:
    tmp_FF5C = (cache_m8_0014 & pChr2)  ' pc=0050
    cache_m8_0014 = tmp_FF5C  ' pc=0054
    GoTo L008B  ' pc=005A
L005D:
    If (pChr <> " ") Then GoTo L0072 Else GoTo L0089  ' pc=006F
L0072:
    tmp_FF5C = (cache_m8_0014 & pChr)  ' pc=007F
    cache_m8_0014 = tmp_FF5C  ' pc=0083
L0089:
L008B:
    GoTo L00A9  ' pc=008D
L0090:
    tmp_FF5C = (cache_m8_0014 & pChr)  ' pc=009F
    cache_m8_0014 = tmp_FF5C  ' pc=00A3
L00A9:
    Exit Sub  ' pc=00AD
End Sub

Public Function IsVowel(ByRef pChr As Variant, ByRef pos As Integer) As Boolean
    Dim tmp_FF28 As Variant
    Dim tmp_FF48 As Variant

    tmp_FF48 = Mid(pChr, CLng(pos), 1)  ' pc=0013
    tmp_FF28 = (tmp_FF48 Like "[aeiouy]")  ' pc=0020
    IsVowel = CInt(CBool(tmp_FF28))  ' pc=0026
    Exit Function  ' pc=0032
End Function

Public Function SlavoGermanic(ByRef pArry As Variant) As Boolean
    Dim tmp_FF42 As Integer
    Dim tmp_FF44 As Variant
    Dim tmp_FF74() As Variant

    ReDim tmp_FF74(0 To 1)  ' pc=0011
    tmp_FF74(0) = "WK"  ' pc=0028
    tmp_FF74(1) = "CZ"  ' pc=0037
    tmp_FF44 = VBA.Array("WK", "CZ")  ' pc=003F
    Erase tmp_FF74  ' pc=0047
    tmp_FF42 = 0  ' pc=004D
    SlavoGermanic = CInt(IsInArry(pArry, tmp_FF42, tmp_FF44))  ' pc=0058
    If (Not SlavoGermanic) Then GoTo L0067 Else GoTo L00B4  ' pc=0064
L0067:
    ReDim tmp_FF74(0 To 0)  ' pc=0076
    tmp_FF74(0) = "WITZ"  ' pc=008D
    tmp_FF44 = VBA.Array("WITZ")  ' pc=0095
    Erase tmp_FF74  ' pc=009D
    tmp_FF42 = 0  ' pc=00A3
    SlavoGermanic = CInt(IsInArry(pArry, tmp_FF42, tmp_FF44))  ' pc=00AE
L00B4:
    Exit Function  ' pc=00B6
End Function

Public Function IsInStr(ByRef pStr As Variant, ByRef StartDX As Integer, ByRef pLen As Variant, ByRef pList As Variant) As Boolean
    Dim tmp_FEC0 As Variant
    Dim tmp_FED0 As Variant
    Dim tmp_FEE0 As Variant
    Dim tmp_FEF0 As Variant
    Dim tmp_FF10 As Variant
    Dim tmp_FF24 As Variant
    Dim tmp_FF44 As Variant
    Dim Str2Check As Variant
    Dim Increment As Integer
    Dim X As Integer

    tmp_FF44 = Len(pStr)  ' pc=0010
    If (pLen > tmp_FF44) Then GoTo L0019 Else GoTo L001C  ' pc=0016
L0019:
    Exit Function  ' pc=001B
L001C:
    If (StartDX < 1) Then GoTo L0029 Else GoTo L002C  ' pc=0026
L0029:
    Exit Function  ' pc=002B
L002C:
    tmp_FF44 = Mid(pStr, CLng(StartDX), pLen)  ' pc=003D
    Str2Check = tmp_FF44  ' pc=0045
    tmp_FF44 = InStr(1, pList, ",", 2)  ' pc=0060
    Increment = CInt(CInt(tmp_FF44))  ' pc=0065
    tmp_FF44 = (pList & ",")  ' pc=0078
    pList = tmp_FF44  ' pc=007C
    tmp_FF44 = Len(pList)  ' pc=008C
    tmp_FF24 = (tmp_FF44 - 1)  ' pc=0095
    For X = 1 To CInt(tmp_FF24) Step Increment  ' pc=009D
    tmp_FF24 = Mid(pList, CLng(X))  ' pc=00BF
    tmp_FF10 = InStr(1, tmp_FF24, ",", 2)  ' pc=00D1
    tmp_FEF0 = (tmp_FF10 - 1)  ' pc=00DA
    tmp_FEE0 = tmp_FEF0  ' pc=00DE
    tmp_FED0 = Mid(pList, CLng(X), tmp_FEE0)  ' pc=00EF
    tmp_FEC0 = InStr(1, Str2Check, tmp_FED0, 2)  ' pc=00FC
    If (tmp_FEC0 > 0) Then GoTo L011A Else GoTo L0126  ' pc=0117
L011A:
    IsInStr = CInt(-1)  ' pc=011E
    GoTo L0132  ' pc=0123
L0126:
    Next X  ' pc=012D
L0132:
    Exit Function  ' pc=0134
End Function

Public Sub RApad(ByRef pArry As Variant, ByRef NumChrs As Integer, ByRef pChr As Variant)
    Dim ALen As Integer
    Dim X As Integer

    ALen = CInt(CInt((UBound(pArry, 1) + CLng(NumChrs))))  ' pc=0014
    ReDim Preserve pArry(0 To CLng((ALen - 1)))  ' pc=0028
    For X = (ALen - NumChrs) To (ALen - 1)  ' pc=0040
    pArry(X) = pChr  ' pc=0059
    Next X  ' pc=0062
    Exit Sub  ' pc=0069
End Sub

Public Function IsInArry(ByRef pArry As Variant, ByRef StartDX As Integer, ByRef pListArry As Variant) As Boolean
    Dim tmp_FEFC As Variant
    Dim tmp_FF0C As Variant
    Dim tmp_FF1C As Variant
    Dim tmp_FF2C As Variant
    Dim Y As Integer
    Dim StrLen As Integer
    Dim ListArryLen As Integer
    Dim TmpStr As Variant
    Dim z As Integer
    Dim ArryLen As Integer
    Dim X As Integer

    On Error GoTo L0130  ' pc=0004
    ArryLen = CInt(CInt(UBound(pArry, 1)))  ' pc=0014
    tmp_FF0C = CInt(ArryLen)  ' pc=001C
    tmp_FF2C = pListArry(0)  ' pc=0029
    tmp_FF1C = Len(tmp_FF2C)  ' pc=002F
    If (tmp_FF0C < tmp_FF1C) Then GoTo L003B Else GoTo L003E  ' pc=0038
L003B:
    Exit Function  ' pc=003D
L003E:
    ListArryLen = CInt(CInt(UBound(pListArry, 1)))  ' pc=004B
    tmp_FF2C = pListArry(0)  ' pc=0059
    tmp_FF1C = Len(tmp_FF2C)  ' pc=005F
    tmp_FEFC = (tmp_FF1C - 1)  ' pc=0068
    StrLen = CInt(CInt(tmp_FEFC))  ' pc=006D
    For X = 0 To ListArryLen  ' pc=007D
    For Y = StartDX To ArryLen  ' pc=008E
    TmpStr = ""  ' pc=009B
    If ((Y + StrLen) <= ArryLen) Then GoTo L00AF Else GoTo L00EE  ' pc=00AC
L00AF:
    For z = Y To (Y + StrLen)  ' pc=00BE
    tmp_FF2C = pArry(z)  ' pc=00D3
    tmp_FF1C = (TmpStr & tmp_FF2C)  ' pc=00D9
    TmpStr = tmp_FF1C  ' pc=00DD
    Next z  ' pc=00E9
L00EE:
    tmp_FF2C = pListArry(X)  ' pc=00FF
    If (TmpStr = tmp_FF2C) Then GoTo L010D Else GoTo L0117  ' pc=010A
L010D:
    IsInArry = CInt(-1)  ' pc=0111
    Exit Function  ' pc=0116
L0117:
    Next Y  ' pc=011E
    Next X  ' pc=0128
L012D:
    Exit Function  ' pc=012F
L0130:
    Resume L012D  ' pc=0132
    Exit Function  ' pc=0138
End Function

