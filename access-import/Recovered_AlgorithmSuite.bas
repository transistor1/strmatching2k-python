Attribute VB_Name = "Recovered_AlgorithmSuite"
' EXPERIMENTAL reconstruction: not compiled or runtime verified.
' Instructions fully traversed; this does not prove semantic equivalence.
Option Compare Database
Option Explicit

Public Sub Bigram(ByVal input_pStr As Variant, ByRef BGArray() As Variant)
    Dim tmp_FF24 As Variant
    Dim tmp_FF44 As Variant
    Dim StrLen As Integer
    Dim BGCount As Integer
    Dim X As Integer
    Dim pStr As Variant

    pStr = input_pStr  ' pc=0002
    tmp_FF44 = ("%" & pStr)  ' pc=0012
    tmp_FF24 = (tmp_FF44 & "#")  ' pc=001B
    pStr = tmp_FF24  ' pc=001F
    tmp_FF44 = Len(pStr)  ' pc=002B
    StrLen = CInt(CInt(tmp_FF44))  ' pc=0030
    BGCount = CInt((StrLen - 1))  ' pc=003B
    ReDim BGArray(0 To CLng(BGCount))  ' pc=004C
    For X = 0 To (BGCount - 1)  ' pc=0063
    tmp_FF24 = Mid(pStr, CLng((X + 1)), 2)  ' pc=007D
    BGArray(CLng(X)) = tmp_FF24  ' pc=008C
    Next X  ' pc=0099
    Exit Sub  ' pc=00A0
End Sub

Public Function LevDist(ByVal input_pStr1 As Variant, ByVal input_pStr2 As Variant) As Integer
    Dim tmp_FE7C As Variant
    Dim tmp_FEAC As Variant
    Dim tmp_FEBC As Variant
    Dim tmp_FECC As Variant
    Dim tmp_FEE0 As Variant
    Dim tmp_FF00 As Variant
    Dim trans As Integer
    Dim cell As Integer
    Dim diag As Integer
    Dim Left As Integer
    Dim above As Integer
    Dim s_i As Variant
    Dim t_j As Variant
    Dim cost As Integer
    Dim j As Integer
    Dim i As Integer
    Dim matrix() As Integer
    Dim m As Integer
    Dim n As Integer
    Dim pStr2 As Variant
    Dim pStr1 As Variant

    pStr1 = input_pStr1  ' pc=0002
    pStr2 = input_pStr2  ' pc=0008
    n = CInt(CInt(UBound(pStr1, 1)))  ' pc=001B
    m = CInt(CInt(UBound(pStr2, 1)))  ' pc=002B
    If (n = 0) Then GoTo L0039 Else GoTo L0045  ' pc=0036
L0039:
    LevDist = CInt(0)  ' pc=003D
    GoTo L0308  ' pc=0042
L0045:
    If (m = 0) Then GoTo L0052 Else GoTo L005E  ' pc=004F
L0052:
    LevDist = CInt(0)  ' pc=0056
    GoTo L0308  ' pc=005B
L005E:
    ReDim matrix(0 To CLng((n + 1)), 0 To CLng((m + 1)))  ' pc=007D
    For i = 0 To n  ' pc=0091
    matrix(CLng(i), 0) = CInt(i)  ' pc=00AB
    Next i  ' pc=00B3
    For j = 0 To m  ' pc=00C2
    matrix(0, CLng(j)) = CInt(j)  ' pc=00DC
    Next j  ' pc=00E4
    For i = 1 To n  ' pc=00F3
    tmp_FF00 = CInt((i - 1))  ' pc=0101
    tmp_FEE0 = pStr1(tmp_FF00)  ' pc=0108
    s_i = tmp_FEE0  ' pc=010E
    For j = 1 To m  ' pc=011C
    tmp_FF00 = CInt((j - 1))  ' pc=012A
    tmp_FEE0 = pStr2(tmp_FF00)  ' pc=0131
    t_j = tmp_FEE0  ' pc=0137
    cost = CInt(0)  ' pc=013F
    If ((Not IsEmpty(s_i)) And (Not IsEmpty(t_j))) Then GoTo L015A Else GoTo L0170  ' pc=0157
L015A:
    If (s_i <> t_j) Then GoTo L0167 Else GoTo L016E  ' pc=0164
L0167:
    cost = CInt(1)  ' pc=016B
L016E:
L0170:
    above = CInt(matrix(CLng((i - 1)), CLng(j)))  ' pc=0188
    Left = CInt(matrix(CLng(i), CLng((j - 1))))  ' pc=01A1
    diag = CInt(matrix(CLng((i - 1)), CLng((j - 1))))  ' pc=01BD
    tmp_FEAC = CInt((diag + cost))  ' pc=01CC
    tmp_FECC = CInt((Left + 1))  ' pc=01D5
    tmp_FEE0 = CInt((above + 1))  ' pc=01DE
    tmp_FE7C = Minimum(tmp_FEE0, tmp_FECC, tmp_FEAC)  ' pc=01E4
    cell = CInt(CInt(tmp_FE7C))  ' pc=01ED
    If ((i > 1) And (j > 1)) Then GoTo L020F Else GoTo L02C6  ' pc=020C
L020F:
    trans = CInt((matrix(CLng((i - 2)), CLng((j - 2))) + 1))  ' pc=022B
    tmp_FF00 = CInt((i - 2))  ' pc=0236
    tmp_FEE0 = pStr1(tmp_FF00)  ' pc=023D
    tmp_FEBC = CInt((j - 1))  ' pc=0249
    tmp_FECC = pStr2(tmp_FEBC)  ' pc=0250
    If (tmp_FEE0 <> tmp_FECC) Then GoTo L0262 Else GoTo L026D  ' pc=025F
L0262:
    trans = CInt((trans + 1))  ' pc=026A
L026D:
    tmp_FF00 = CInt((i - 1))  ' pc=0277
    tmp_FEE0 = pStr1(tmp_FF00)  ' pc=027E
    tmp_FEBC = CInt((j - 2))  ' pc=028A
    tmp_FECC = pStr2(tmp_FEBC)  ' pc=0291
    If (tmp_FEE0 <> tmp_FECC) Then GoTo L02A3 Else GoTo L02AE  ' pc=02A0
L02A3:
    trans = CInt((trans + 1))  ' pc=02AB
L02AE:
    If (cell > trans) Then GoTo L02BC Else GoTo L02C4  ' pc=02B9
L02BC:
    cell = CInt(trans)  ' pc=02C1
L02C4:
L02C6:
    matrix(CLng(i), CLng(j)) = CInt(cell)  ' pc=02DB
    Next j  ' pc=02E3
    Next i  ' pc=02ED
    LevDist = CInt(matrix(CLng(n), CLng(m)))  ' pc=0305
L0308:
    Exit Function  ' pc=030A
End Function

Public Function IsSimilar(ByVal inputRefStr As Variant, ByVal inputTestStr As Variant, Optional ByRef Alg2Use As String = "") As Single
    Dim tmp_FD84 As Object
    Dim tmp_FD88 As Object
    Dim tmp_FD8C As Object
    Dim tmp_FD90 As Object
    Dim tmp_FDA6 As Boolean
    Dim tmp_FDA8 As String
    Dim tmp_FDB4 As Variant
    Dim tmp_FDC4 As Variant
    Dim tmp_FDD4 As Variant
    Dim tmp_FDF4 As Variant
    Dim tmp_FE14 As Variant
    Dim tmp_FE64 As Long
    Dim tmp_FE68 As Single
    Dim tmp_FE6C As Variant
    Dim tmp_FE7C As Variant
    Dim tmp_FE9C As Variant
    Dim tmp_FEAC As Variant
    Dim tmp_FEBC As Variant
    Dim tmp_FECC As Variant
    Dim bMetaPh2() As Variant
    Dim bMetaPh1() As Variant
    Dim aMetaPh2() As Variant
    Dim aMetaPh1() As Variant
    Dim TestArry() As Variant
    Dim RefArry() As Variant
    Dim X As Integer
    Dim TestQG() As Variant
    Dim RefQG() As Variant
    Dim MPhLen As Integer
    Dim TestLen As Integer
    Dim RefLen As Integer
    Dim MetaPh2b As Variant
    Dim MetaPh1b As Variant
    Dim MetaPh2a As Variant
    Dim MetaPh1a As Variant
    Dim LCSValu As Single
    Dim DiceValu As Single
    Dim DblMetaPh As Single
    Dim LevDistValu As Single
    Dim TestStr As Variant
    Dim RefStr As Variant

    RefStr = inputRefStr  ' pc=0002
    TestStr = inputTestStr  ' pc=0008
    If IsMissing(Alg2Use) Then GoTo L0020 Else GoTo L0029  ' pc=001D
L0020:
    Alg2Use = CStr("")  ' pc=0025
L0029:
    If (IsNull(RefStr) Or IsNull(TestStr)) Then GoTo L003F Else GoTo L0044  ' pc=003C
L003F:
    GoTo L0B63  ' pc=0041
L0044:
    If (Alg2Use = "") Then GoTo L0051 Else GoTo L0089  ' pc=004E
L0051:
    tmp_FEBC = (RefStr = TestStr)  ' pc=0063
    tmp_FEAC = tmp_FEBC  ' pc=0067
    tmp_FE6C = IIf(tmp_FEAC, 1, 0)  ' pc=0071
    IsSimilar = CSng(CDbl(tmp_FE6C))  ' pc=007B
L0089:
    If (IsSimilar = CDbl(1)) Then GoTo L0097 Else GoTo L009C  ' pc=0094
L0097:
    GoTo L0B63  ' pc=0099
L009C:
    tmp_FEBC = (RefStr Like "*.*")  ' pc=00A6
    If tmp_FEBC Then GoTo L00AF Else GoTo L00F0  ' pc=00AC
L00AF:
    tmp_FE64 = 0  ' pc=00B6
    tmp_FE68 = 1  ' pc=00BE
    tmp_FEAC = ""  ' pc=00C6
    tmp_FEBC = "."  ' pc=00D1
    tmp_FE9C = StrReplace(RefStr, tmp_FEBC, tmp_FEAC, CLng(tmp_FE68), tmp_FE64)  ' pc=00DD
    RefStr = tmp_FE9C  ' pc=00E5
L00F0:
    tmp_FEBC = (TestStr Like "*.*")  ' pc=00FC
    If tmp_FEBC Then GoTo L0105 Else GoTo L0146  ' pc=0102
L0105:
    tmp_FE64 = 0  ' pc=010C
    tmp_FE68 = 1  ' pc=0114
    tmp_FEAC = ""  ' pc=011C
    tmp_FEBC = "."  ' pc=0127
    tmp_FE9C = StrReplace(TestStr, tmp_FEBC, tmp_FEAC, CLng(tmp_FE68), tmp_FE64)  ' pc=0133
    TestStr = tmp_FE9C  ' pc=013B
L0146:
    tmp_FEBC = (RefStr Like "*-*")  ' pc=0152
    If tmp_FEBC Then GoTo L015B Else GoTo L020E  ' pc=0158
L015B:
    tmp_FE7C = InStr(1, RefStr, "-", 2)  ' pc=0172
    tmp_FE6C = (tmp_FE7C + 1)  ' pc=017B
    tmp_FE14 = Mid(RefStr, CLng(tmp_FE6C))  ' pc=0187
    tmp_FEBC = InStr(1, RefStr, "-", 2)  ' pc=019E
    tmp_FEAC = (tmp_FEBC + 1)  ' pc=01A7
    tmp_FE9C = Left(RefStr, CLng(tmp_FEAC))  ' pc=01B3
    tmp_FE64 = 0  ' pc=01C0
    tmp_FE68 = 1  ' pc=01C8
    tmp_FDD4 = ""  ' pc=01D0
    tmp_FDF4 = "-"  ' pc=01DB
    tmp_FDC4 = StrReplace(tmp_FE14, tmp_FDF4, tmp_FDD4, CLng(tmp_FE68), tmp_FE64)  ' pc=01E7
    tmp_FDB4 = (tmp_FE9C & tmp_FDC4)  ' pc=01EF
    RefStr = tmp_FDB4  ' pc=01F3
L020E:
    tmp_FEBC = (TestStr Like "*-*")  ' pc=021A
    If tmp_FEBC Then GoTo L0223 Else GoTo L02D6  ' pc=0220
L0223:
    tmp_FE7C = InStr(1, TestStr, "-", 2)  ' pc=023A
    tmp_FE6C = (tmp_FE7C + 1)  ' pc=0243
    tmp_FE14 = Mid(TestStr, CLng(tmp_FE6C))  ' pc=024F
    tmp_FEBC = InStr(1, TestStr, "-", 2)  ' pc=0266
    tmp_FEAC = (tmp_FEBC + 1)  ' pc=026F
    tmp_FE9C = Left(TestStr, CLng(tmp_FEAC))  ' pc=027B
    tmp_FE64 = 0  ' pc=0288
    tmp_FE68 = 1  ' pc=0290
    tmp_FDD4 = ""  ' pc=0298
    tmp_FDF4 = "-"  ' pc=02A3
    tmp_FDC4 = StrReplace(tmp_FE14, tmp_FDF4, tmp_FDD4, CLng(tmp_FE68), tmp_FE64)  ' pc=02AF
    tmp_FDB4 = (tmp_FE9C & tmp_FDC4)  ' pc=02B7
    TestStr = tmp_FDB4  ' pc=02BB
L02D6:
    tmp_FEBC = (RefStr Like "*[/-]*")  ' pc=02E2
    If tmp_FEBC Then GoTo L02EB Else GoTo L036D  ' pc=02E8
L02EB:
    tmp_FE64 = 0  ' pc=02F2
    tmp_FE68 = 1  ' pc=02FA
    tmp_FEAC = ""  ' pc=0302
    tmp_FEBC = "-"  ' pc=030D
    tmp_FE9C = StrReplace(RefStr, tmp_FEBC, tmp_FEAC, CLng(tmp_FE68), tmp_FE64)  ' pc=0319
    RefStr = tmp_FE9C  ' pc=0321
    tmp_FE64 = 0  ' pc=0333
    tmp_FE68 = 1  ' pc=033B
    tmp_FEAC = ""  ' pc=0343
    tmp_FEBC = "/"  ' pc=034E
    tmp_FE9C = StrReplace(RefStr, tmp_FEBC, tmp_FEAC, CLng(tmp_FE68), tmp_FE64)  ' pc=035A
    RefStr = tmp_FE9C  ' pc=0362
L036D:
    tmp_FEBC = (TestStr Like "*[/-]*")  ' pc=0379
    If tmp_FEBC Then GoTo L0382 Else GoTo L0404  ' pc=037F
L0382:
    tmp_FE64 = 0  ' pc=0389
    tmp_FE68 = 1  ' pc=0391
    tmp_FEAC = ""  ' pc=0399
    tmp_FEBC = "-"  ' pc=03A4
    tmp_FE9C = StrReplace(TestStr, tmp_FEBC, tmp_FEAC, CLng(tmp_FE68), tmp_FE64)  ' pc=03B0
    TestStr = tmp_FE9C  ' pc=03B8
    tmp_FE64 = 0  ' pc=03CA
    tmp_FE68 = 1  ' pc=03D2
    tmp_FEAC = ""  ' pc=03DA
    tmp_FEBC = "/"  ' pc=03E5
    tmp_FE9C = StrReplace(TestStr, tmp_FEBC, tmp_FEAC, CLng(tmp_FE68), tmp_FE64)  ' pc=03F1
    TestStr = tmp_FE9C  ' pc=03F9
L0404:
    tmp_FEBC = Trim(RefStr)  ' pc=040E
    RefStr = tmp_FEBC  ' pc=0416
    tmp_FEBC = Len(RefStr)  ' pc=041F
    RefLen = CInt(CInt(tmp_FEBC))  ' pc=0424
    tmp_FEBC = Trim(TestStr)  ' pc=042F
    TestStr = tmp_FEBC  ' pc=0437
    tmp_FEBC = Len(TestStr)  ' pc=0440
    TestLen = CInt(CInt(tmp_FEBC))  ' pc=0445
    If ((RefLen = 0) Or (TestLen = 0)) Then GoTo L045A Else GoTo L045F  ' pc=0457
L045A:
    GoTo L0B63  ' pc=045C
L045F:
    tmp_FEBC = (RefStr = TestStr)  ' pc=0469
    tmp_FECC = CBool((Alg2Use = ""))  ' pc=0475
    tmp_FEAC = (tmp_FEBC And tmp_FECC)  ' pc=0479
    If tmp_FEAC Then GoTo L0485 Else GoTo L0492  ' pc=0482
L0485:
    IsSimilar = CSng(CDbl(1))  ' pc=048A
    GoTo L0B63  ' pc=048F
L0492:
    ReDim RefArry(0 To CLng(RefLen))  ' pc=04A2
    ReDim TestArry(0 To CLng(TestLen))  ' pc=04BA
    For X = 0 To (RefLen - 1)  ' pc=04D1
    tmp_FEAC = Mid(RefStr, CLng((X + 1)), 1)  ' pc=04EB
    RefArry(CLng(X)) = tmp_FEAC  ' pc=04FA
    Next X  ' pc=0507
    For X = 0 To (TestLen - 1)  ' pc=0519
    tmp_FEAC = Mid(TestStr, CLng((X + 1)), 1)  ' pc=0533
    TestArry(CLng(X)) = tmp_FEAC  ' pc=0542
    Next X  ' pc=054F
    Call Bigram(RefStr, RefQG)  ' pc=055D
    Call Bigram(TestStr, TestQG)  ' pc=056B
    tmp_FDA8 = CStr(Alg2Use)  ' pc=0575
    If (tmp_FDA8 = "Lev") Then GoTo L0585 Else GoTo L058D  ' pc=0582
L0585:
    GoTo L0615  ' pc=0587
    GoTo L05B4  ' pc=058A
L058D:
    If (tmp_FDA8 = "SSLCS") Then GoTo L059A Else GoTo L05A2  ' pc=0597
L059A:
    GoTo L0667  ' pc=059C
    GoTo L05B4  ' pc=059F
L05A2:
    If (tmp_FDA8 = "DblMetaPh") Then GoTo L05AF Else GoTo L05B4  ' pc=05AC
L05AF:
    GoTo L06C3  ' pc=05B1
L05B4:
    tmp_FDA6 = 0  ' pc=05BA
    DiceValu = CSng(Dice(RefQG, TestQG, CBool(tmp_FDA6)))  ' pc=05D4
    If (Alg2Use = "Dice") Then GoTo L05E4 Else GoTo L05F1  ' pc=05E1
L05E4:
    IsSimilar = CSng(DiceValu)  ' pc=05E9
    GoTo L0B63  ' pc=05EE
L05F1:
    If (DiceValu < CSng(0.2)) Then GoTo L0606 Else GoTo L0613  ' pc=0603
L0606:
    IsSimilar = CSng(CDbl(0))  ' pc=060B
    GoTo L0B63  ' pc=0610
L0613:
L0615:
    LevDistValu = CSng(CDbl(LevDist(RefArry, TestArry)))  ' pc=062F
    If (Alg2Use = "Lev") Then GoTo L063F Else GoTo L064C  ' pc=063C
L063F:
    IsSimilar = CSng(LevDistValu)  ' pc=0644
    GoTo L0B63  ' pc=0649
L064C:
    LevDistValu = CSng((CDbl(1) - ((LevDistValu / CDbl((RefLen + TestLen))) / CDbl(2))))  ' pc=0664
L0667:
    LCSValu = CSng(LCS(RefArry, TestArry, Alg2Use))  ' pc=0688
    If (Alg2Use = "SSLCS") Then GoTo L0698 Else GoTo L06A5  ' pc=0695
L0698:
    IsSimilar = CSng(LCSValu)  ' pc=069D
    GoTo L0B63  ' pc=06A2
L06A5:
    If (CSng(((LevDistValu + LCSValu) / CDbl(2))) < CSng(0.84)) Then GoTo L06C3 Else GoTo L0B3B  ' pc=06C0
L06C3:
    If (DoubleMetaphone(RefArry, MetaPh1a, MetaPh1b) And DoubleMetaphone(TestArry, MetaPh2a, MetaPh2b)) Then GoTo L06F1 Else GoTo L0B36  ' pc=06EE
L06F1:
    If (MetaPh1a <> "") Then GoTo L0701 Else GoTo L07F0  ' pc=06FE
L0701:
    tmp_FEBC = Len(MetaPh1a)  ' pc=0706
    MPhLen = CInt(CInt(tmp_FEBC))  ' pc=070B
    ReDim aMetaPh1(0 To CLng(MPhLen))  ' pc=071C
    For X = 0 To (MPhLen - 1)  ' pc=0733
    tmp_FEAC = Mid(MetaPh1a, CLng((X + 1)), 1)  ' pc=074D
    aMetaPh1(CLng(X)) = tmp_FEAC  ' pc=075C
    Next X  ' pc=0769
    If (MetaPh1b <> "") Then GoTo L077E Else GoTo L07EB  ' pc=077B
L077E:
    tmp_FEBC = Len(MetaPh1b)  ' pc=0783
    MPhLen = CInt(CInt(tmp_FEBC))  ' pc=0788
    ReDim bMetaPh1(0 To CLng(MPhLen))  ' pc=0799
    For X = 0 To (MPhLen - 1)  ' pc=07B0
    tmp_FEAC = Mid(MetaPh1b, CLng((X + 1)), 1)  ' pc=07CA
    bMetaPh1(CLng(X)) = tmp_FEAC  ' pc=07D9
    Next X  ' pc=07E6
L07EB:
    GoTo L07F7  ' pc=07ED
L07F0:
    GoTo L0B36  ' pc=07F4
L07F7:
    If (MetaPh2a <> "") Then GoTo L0809 Else GoTo L08F8  ' pc=0806
L0809:
    tmp_FEBC = Len(MetaPh2a)  ' pc=080E
    MPhLen = CInt(CInt(tmp_FEBC))  ' pc=0813
    ReDim aMetaPh2(0 To CLng(MPhLen))  ' pc=0824
    For X = 0 To (MPhLen - 1)  ' pc=083B
    tmp_FEAC = Mid(MetaPh2a, CLng((X + 1)), 1)  ' pc=0855
    aMetaPh2(CLng(X)) = tmp_FEAC  ' pc=0864
    Next X  ' pc=0871
    If (MetaPh2b <> "") Then GoTo L0886 Else GoTo L08F3  ' pc=0883
L0886:
    tmp_FEBC = Len(MetaPh2b)  ' pc=088B
    MPhLen = CInt(CInt(tmp_FEBC))  ' pc=0890
    ReDim bMetaPh2(0 To CLng(MPhLen))  ' pc=08A1
    For X = 0 To (MPhLen - 1)  ' pc=08B8
    tmp_FEAC = Mid(MetaPh2b, CLng((X + 1)), 1)  ' pc=08D2
    bMetaPh2(CLng(X)) = tmp_FEAC  ' pc=08E1
    Next X  ' pc=08EE
L08F3:
    GoTo L08FF  ' pc=08F5
L08F8:
    GoTo L0B36  ' pc=08FC
L08FF:
    If (Alg2Use = "DblMetaPh") Then GoTo L090E Else GoTo L0A98  ' pc=090B
L090E:
    tmp_FEBC = "Dmph"  ' pc=0915
    DblMetaPh = CSng(LCS(aMetaPh1, aMetaPh2, tmp_FEBC))  ' pc=0932
    Set tmp_FD90 = Application.Forms  ' pc=095C
    Set tmp_FD8C = tmp_FD90.Item("Double Metaphone Input Compare")  ' pc=0964
    Set tmp_FD88 = tmp_FD8C.Controls  ' pc=096C
    Set tmp_FD84 = tmp_FD88.Item("MetaPh1")  ' pc=0974
    tmp_FD84 = MetaPh1a  ' pc=097C
    Set tmp_FD90 = Nothing  ' pc=0981
    Set tmp_FD8C = Nothing  ' pc=0981
    Set tmp_FD88 = Nothing  ' pc=0981
    Set tmp_FD84 = Nothing  ' pc=0981
    Set tmp_FD90 = Application.Forms  ' pc=09B0
    Set tmp_FD8C = tmp_FD90.Item("Double Metaphone Input Compare")  ' pc=09B8
    Set tmp_FD88 = tmp_FD8C.Controls  ' pc=09C0
    Set tmp_FD84 = tmp_FD88.Item("MetaPh2")  ' pc=09C8
    tmp_FD84 = MetaPh2a  ' pc=09D0
    Set tmp_FD90 = Nothing  ' pc=09D5
    Set tmp_FD8C = Nothing  ' pc=09D5
    Set tmp_FD88 = Nothing  ' pc=09D5
    Set tmp_FD84 = Nothing  ' pc=09D5
    Set tmp_FD90 = Application.Forms  ' pc=0A04
    Set tmp_FD8C = tmp_FD90.Item("Double Metaphone Input Compare")  ' pc=0A0C
    Set tmp_FD88 = tmp_FD8C.Controls  ' pc=0A14
    Set tmp_FD84 = tmp_FD88.Item("Alt1")  ' pc=0A1C
    tmp_FD84 = MetaPh1b  ' pc=0A24
    Set tmp_FD90 = Nothing  ' pc=0A29
    Set tmp_FD8C = Nothing  ' pc=0A29
    Set tmp_FD88 = Nothing  ' pc=0A29
    Set tmp_FD84 = Nothing  ' pc=0A29
    Set tmp_FD90 = Application.Forms  ' pc=0A58
    Set tmp_FD8C = tmp_FD90.Item("Double Metaphone Input Compare")  ' pc=0A60
    Set tmp_FD88 = tmp_FD8C.Controls  ' pc=0A68
    Set tmp_FD84 = tmp_FD88.Item("Alt2")  ' pc=0A70
    tmp_FD84 = MetaPh2b  ' pc=0A78
    Set tmp_FD90 = Nothing  ' pc=0A7D
    Set tmp_FD8C = Nothing  ' pc=0A7D
    Set tmp_FD88 = Nothing  ' pc=0A7D
    Set tmp_FD84 = Nothing  ' pc=0A7D
    IsSimilar = CSng(DblMetaPh)  ' pc=0A8D
    GoTo L0B63  ' pc=0A92
    GoTo L0B34  ' pc=0A95
L0A98:
    DblMetaPh = CSng(LCS(aMetaPh1, aMetaPh2))  ' pc=0AB6
    tmp_FEBC = (MetaPh1b <> "")  ' pc=0AC7
    tmp_FEAC = (MetaPh2b <> "")  ' pc=0AD4
    tmp_FE9C = (tmp_FEBC And tmp_FEAC)  ' pc=0AD8
    If tmp_FE9C Then GoTo L0AE1 Else GoTo L0B32  ' pc=0ADE
L0AE1:
    tmp_FE68 = CSng(LCS(bMetaPh1, bMetaPh2))  ' pc=0AFD
    tmp_FEAC = CSng(tmp_FE68)  ' pc=0B09
    tmp_FE6C = Maximum(DblMetaPh, tmp_FEAC)  ' pc=0B18
    DblMetaPh = CSng(CDbl(tmp_FE6C))  ' pc=0B22
L0B32:
L0B34:
L0B36:
    GoTo L0B4D  ' pc=0B38
L0B3B:
    DblMetaPh = CSng(((LevDistValu + LCSValu) / CDbl(2)))  ' pc=0B4A
L0B4D:
    IsSimilar = CSng((((LevDistValu + LCSValu) + DblMetaPh) / CDbl(3)))  ' pc=0B60
L0B63:
    Erase RefArry  ' pc=0B68
    Erase TestArry  ' pc=0B6E
    Erase aMetaPh1  ' pc=0B74
    Erase aMetaPh2  ' pc=0B7A
    Erase bMetaPh1  ' pc=0B80
    Erase bMetaPh2  ' pc=0B86
    Erase RefQG  ' pc=0B8C
    Erase TestQG  ' pc=0B92
    Exit Function  ' pc=0B95
End Function

Public Function Dice(ByVal input_Qgram1 As Variant, ByVal input_Qgram2 As Variant, Optional ByRef DMPH As Boolean) As Single
    Dim tmp_FEA4 As Variant
    Dim tmp_FED4 As Variant
    Dim tmp_FEE4 As Variant
    Dim tmp_FF08 As Variant
    Dim q2 As Integer
    Dim q1 As Integer
    Dim SharedQgrams As Integer
    Dim BG2 As Variant
    Dim BG1 As Variant
    Dim QgramCount2 As Integer
    Dim QgramCount1 As Integer
    Dim Qgram2 As Variant
    Dim Qgram1 As Variant

    Qgram1 = input_Qgram1  ' pc=0002
    Qgram2 = input_Qgram2  ' pc=0008
    If IsMissing(DMPH) Then GoTo L0020 Else GoTo L0027  ' pc=001D
L0020:
    DMPH = CInt(0)  ' pc=0024
L0027:
    If (IsNull(Qgram1) Or IsNull(Qgram2)) Then GoTo L003D Else GoTo L0040  ' pc=003A
L003D:
    Exit Function  ' pc=003F
L0040:
    QgramCount1 = CInt(CInt(UBound(Qgram1, 1)))  ' pc=004F
    QgramCount2 = CInt(CInt(UBound(Qgram2, 1)))  ' pc=005F
    If ((QgramCount1 = 0) Or (QgramCount2 = 0)) Then GoTo L0074 Else GoTo L0077  ' pc=0071
L0074:
    Exit Function  ' pc=0076
L0077:
    For q1 = 0 To QgramCount1  ' pc=0081
    tmp_FF08 = Qgram1(q1)  ' pc=0093
    BG1 = tmp_FF08  ' pc=0099
    For q2 = 0 To QgramCount2  ' pc=00A7
    tmp_FF08 = Qgram2(q2)  ' pc=00B9
    BG2 = tmp_FF08  ' pc=00BF
    If ((Not IsEmpty(BG1)) And (Not IsEmpty(BG2))) Then GoTo L00DB Else GoTo L00F5  ' pc=00D8
L00DB:
    If (BG1 = BG2) Then GoTo L00E8 Else GoTo L00F3  ' pc=00E5
L00E8:
    SharedQgrams = CInt((SharedQgrams + 1))  ' pc=00F0
L00F3:
L00F5:
    Next q2  ' pc=00FC
    Next q1  ' pc=0106
    tmp_FEE4 = "0.00"  ' pc=011C
    tmp_FF08 = CDbl((CDbl((2 * SharedQgrams)) / CDbl((QgramCount1 + QgramCount2))))  ' pc=0132
    tmp_FED4 = Format(tmp_FF08, tmp_FEE4, 1, 1)  ' pc=0139
    Dice = CSng(CSng(tmp_FED4))  ' pc=0143
    If DMPH Then GoTo L0159 Else GoTo L0190  ' pc=0156
L0159:
    tmp_FEA4 = Minimum(Dice, 0.75)  ' pc=0178
    Dice = CSng(CDbl(tmp_FEA4))  ' pc=0182
L0190:
    Exit Function  ' pc=0192
End Function

Public Function NameSimilarity(ByRef RefStr As Variant, ByRef TestStr As Variant) As Single
    Dim tmp_FD2C As String
    Dim tmp_FD30 As String
    Dim tmp_FD36 As Integer
    Dim tmp_FD38 As Variant
    Dim tmp_FD48 As Variant
    Dim tmp_FD58 As Variant
    Dim tmp_FD78 As Variant
    Dim tmp_FD88 As Variant
    Dim tmp_FD98 As Variant
    Dim tmp_FDA8 As Variant
    Dim tmp_FDC8 As Variant
    Dim tmp_FE08 As Variant
    Dim tmp_FE18 As Long
    Dim tmp_FE1C As Long
    Dim tmp_FE20 As Variant
    Dim tmp_FE30 As Variant
    Dim tmp_FE50 As Variant
    Dim MFirstSameLetter As Boolean
    Dim FFirstSameLetter As Boolean
    Dim RF_in_TM As Boolean
    Dim LastInMiddle As Boolean
    Dim MSimValu As Single
    Dim FSimValu As Single
    Dim LSimValu As Single
    Dim SimScore As Single
    Dim RM_in_TF As Boolean
    Dim DashNameR As Variant
    Dim DashNameL As Variant
    Dim TestMLen As Variant
    Dim TestFLen As Variant
    Dim TestLLen As Variant
    Dim RefMLen As Variant
    Dim RefFLen As Variant
    Dim RefLLen As Variant
    Dim FullNameSimValu As Single
    Dim DashInBoth As Boolean
    Dim DashInOne As Boolean
    Dim DashName As Variant
    Dim TestM As Variant
    Dim TestF As Variant
    Dim TestL As Variant
    Dim RefM As Variant
    Dim RefF As Variant
    Dim RefL As Variant

    tmp_FE30 = (RefStr Like "*.*")  ' pc=000F
    If tmp_FE30 Then GoTo L0018 Else GoTo L0058  ' pc=0015
L0018:
    tmp_FE18 = 0  ' pc=001F
    tmp_FE1C = 1  ' pc=0027
    tmp_FE20 = ""  ' pc=002F
    tmp_FE30 = "."  ' pc=003A
    tmp_FE08 = StrReplace(RefStr, tmp_FE30, tmp_FE20, tmp_FE1C, tmp_FE18)  ' pc=0046
    RefStr = tmp_FE08  ' pc=004E
L0058:
    tmp_FE30 = (TestStr Like "*.*")  ' pc=0067
    If tmp_FE30 Then GoTo L0070 Else GoTo L00B0  ' pc=006D
L0070:
    tmp_FE18 = 0  ' pc=0077
    tmp_FE1C = 1  ' pc=007F
    tmp_FE20 = ""  ' pc=0087
    tmp_FE30 = "."  ' pc=0092
    tmp_FE08 = StrReplace(TestStr, tmp_FE30, tmp_FE20, tmp_FE1C, tmp_FE18)  ' pc=009E
    TestStr = tmp_FE08  ' pc=00A6
L00B0:
    tmp_FE30 = (RefStr Like "*-*")  ' pc=00BF
    If tmp_FE30 Then GoTo L00C8 Else GoTo L0175  ' pc=00C5
L00C8:
    tmp_FE08 = InStr(1, RefStr, "-", 2)  ' pc=00E2
    tmp_FDC8 = (tmp_FE08 + 1)  ' pc=00EB
    tmp_FD98 = Mid(RefStr, CLng(tmp_FDC8))  ' pc=00F7
    tmp_FE30 = InStr(1, RefStr, "-", 2)  ' pc=0111
    tmp_FE20 = Left(RefStr, CLng(tmp_FE30))  ' pc=011D
    tmp_FE18 = 0  ' pc=012A
    tmp_FE1C = 1  ' pc=0132
    tmp_FD58 = ""  ' pc=013A
    tmp_FD78 = "-"  ' pc=0145
    tmp_FD48 = StrReplace(tmp_FD98, tmp_FD78, tmp_FD58, tmp_FE1C, tmp_FE18)  ' pc=0151
    tmp_FD38 = (tmp_FE20 & tmp_FD48)  ' pc=0159
    RefStr = tmp_FD38  ' pc=015D
L0175:
    tmp_FE30 = (TestStr Like "*-*")  ' pc=0184
    If tmp_FE30 Then GoTo L018D Else GoTo L023A  ' pc=018A
L018D:
    tmp_FE08 = InStr(1, TestStr, "-", 2)  ' pc=01A7
    tmp_FDC8 = (tmp_FE08 + 1)  ' pc=01B0
    tmp_FD98 = Mid(TestStr, CLng(tmp_FDC8))  ' pc=01BC
    tmp_FE30 = InStr(1, TestStr, "-", 2)  ' pc=01D6
    tmp_FE20 = Left(TestStr, CLng(tmp_FE30))  ' pc=01E2
    tmp_FE18 = 0  ' pc=01EF
    tmp_FE1C = 1  ' pc=01F7
    tmp_FD58 = ""  ' pc=01FF
    tmp_FD78 = "-"  ' pc=020A
    tmp_FD48 = StrReplace(tmp_FD98, tmp_FD78, tmp_FD58, tmp_FE1C, tmp_FE18)  ' pc=0216
    tmp_FD38 = (tmp_FE20 & tmp_FD48)  ' pc=021E
    TestStr = tmp_FD38  ' pc=0222
L023A:
    tmp_FE30 = InStr(1, RefStr, "~", 2)  ' pc=0253
    tmp_FE20 = (tmp_FE30 - 1)  ' pc=025C
    tmp_FE08 = Left(RefStr, CLng(tmp_FE20))  ' pc=0268
    tmp_FDC8 = Trim(tmp_FE08)  ' pc=0273
    RefL = tmp_FDC8  ' pc=027B
    tmp_FE08 = "~"  ' pc=028D
    tmp_FD88 = CInt((GetLastChrPos(RefStr, tmp_FE08) - 1))  ' pc=029E
    tmp_FDC8 = InStr(1, RefStr, "~", 2)  ' pc=02B6
    tmp_FDA8 = (tmp_FD88 - tmp_FDC8)  ' pc=02BA
    tmp_FD98 = tmp_FDA8  ' pc=02BE
    tmp_FE30 = InStr(1, RefStr, "~", 2)  ' pc=02DA
    tmp_FE20 = (tmp_FE30 + 1)  ' pc=02E3
    tmp_FD78 = Mid(RefStr, CLng(tmp_FE20), tmp_FD98)  ' pc=02EF
    tmp_FD58 = Trim(tmp_FD78)  ' pc=02FA
    RefF = tmp_FD58  ' pc=0302
    tmp_FE30 = "~"  ' pc=031C
    tmp_FD36 = CInt(GetLastChrPos(RefStr, tmp_FE30))  ' pc=032A
    tmp_FE08 = Mid(RefStr, CLng((tmp_FD36 + 1)))  ' pc=033D
    tmp_FDC8 = Trim(tmp_FE08)  ' pc=0348
    RefM = tmp_FDC8  ' pc=0350
    tmp_FE30 = InStr(1, TestStr, "~", 2)  ' pc=0374
    tmp_FE20 = (tmp_FE30 - 1)  ' pc=037D
    tmp_FE08 = Left(TestStr, CLng(tmp_FE20))  ' pc=0389
    tmp_FDC8 = Trim(tmp_FE08)  ' pc=0394
    TestL = tmp_FDC8  ' pc=039C
    tmp_FE08 = "~"  ' pc=03AE
    tmp_FD88 = CInt((GetLastChrPos(TestStr, tmp_FE08) - 1))  ' pc=03BF
    tmp_FDC8 = InStr(1, TestStr, "~", 2)  ' pc=03D7
    tmp_FDA8 = (tmp_FD88 - tmp_FDC8)  ' pc=03DB
    tmp_FD98 = tmp_FDA8  ' pc=03DF
    tmp_FE30 = InStr(1, TestStr, "~", 2)  ' pc=03FB
    tmp_FE20 = (tmp_FE30 + 1)  ' pc=0404
    tmp_FD78 = Mid(TestStr, CLng(tmp_FE20), tmp_FD98)  ' pc=0410
    tmp_FD58 = Trim(tmp_FD78)  ' pc=041B
    TestF = tmp_FD58  ' pc=0423
    tmp_FE30 = "~"  ' pc=043D
    tmp_FD36 = CInt(GetLastChrPos(TestStr, tmp_FE30))  ' pc=044B
    tmp_FE08 = Mid(TestStr, CLng((tmp_FD36 + 1)))  ' pc=045E
    tmp_FDC8 = Trim(tmp_FE08)  ' pc=0469
    TestM = tmp_FDC8  ' pc=0471
    tmp_FE30 = Len(RefL)  ' pc=0483
    RefLLen = tmp_FE30  ' pc=0487
    tmp_FE30 = Len(RefF)  ' pc=0490
    RefFLen = tmp_FE30  ' pc=0494
    tmp_FE30 = Len(RefM)  ' pc=049D
    RefMLen = tmp_FE30  ' pc=04A1
    tmp_FE30 = Len(TestL)  ' pc=04AA
    TestLLen = tmp_FE30  ' pc=04AE
    tmp_FE30 = Len(TestF)  ' pc=04B7
    TestFLen = tmp_FE30  ' pc=04BB
    tmp_FE30 = Len(TestM)  ' pc=04C4
    TestMLen = tmp_FE30  ' pc=04C8
    tmp_FE30 = (RefL Like "*-*")  ' pc=04D6
    tmp_FE20 = (TestL Like "*-*")  ' pc=04E2
    tmp_FE08 = (tmp_FE30 And tmp_FE20)  ' pc=04E6
    DashInBoth = CInt(CBool(tmp_FE08))  ' pc=04EC
    If (Not DashInBoth) Then GoTo L04F8 Else GoTo L051B  ' pc=04F5
L04F8:
    tmp_FE30 = (RefL Like "*-*")  ' pc=0502
    tmp_FE20 = (TestL Like "*-*")  ' pc=050E
    tmp_FE08 = (tmp_FE30 Or tmp_FE20)  ' pc=0512
    DashInOne = CInt(CBool(tmp_FE08))  ' pc=0518
L051B:
    tmp_FD30 = CStr(0)  ' pc=0524
    tmp_FE08 = (TestL & TestF)  ' pc=0530
    tmp_FDC8 = (tmp_FE08 & TestM)  ' pc=0537
    tmp_FE30 = (RefL & RefF)  ' pc=0542
    tmp_FE20 = (tmp_FE30 & RefM)  ' pc=0549
    FullNameSimValu = CSng(IsSimilar(tmp_FE20, tmp_FDC8, tmp_FD30))  ' pc=0553
    If ((Not DashInBoth) And (Not DashInOne)) Then GoTo L0572 Else GoTo L0695  ' pc=056F
L0572:
    tmp_FE30 = (RefL = TestM)  ' pc=057A
    tmp_FE20 = (RefM = TestL)  ' pc=0584
    tmp_FE08 = (tmp_FE30 Or tmp_FE20)  ' pc=0588
    If tmp_FE08 Then GoTo L0591 Else GoTo L05B7  ' pc=058E
L0591:
    LSimValu = CSng(0.81)  ' pc=059C
    MSimValu = CSng(0.81)  ' pc=05AA
    LastInMiddle = CInt(-1)  ' pc=05B1
    GoTo L064C  ' pc=05B4
L05B7:
    tmp_FD30 = CStr(0)  ' pc=05C0
    LSimValu = CSng(IsSimilar(RefL, TestM, tmp_FD30))  ' pc=05D3
    If (LSimValu > CSng(0.9)) Then GoTo L05EC Else GoTo L05FB  ' pc=05E9
L05EC:
    MSimValu = CSng(LSimValu)  ' pc=05F1
    LastInMiddle = CInt(-1)  ' pc=05F8
L05FB:
    If (Not LastInMiddle) Then GoTo L0606 Else GoTo L064A  ' pc=0603
L0606:
    tmp_FD30 = CStr(0)  ' pc=060D
    LSimValu = CSng(IsSimilar(RefM, TestL, tmp_FD30))  ' pc=0620
    If (LSimValu > CSng(0.9)) Then GoTo L0639 Else GoTo L0648  ' pc=0636
L0639:
    MSimValu = CSng(LSimValu)  ' pc=063E
    LastInMiddle = CInt(-1)  ' pc=0645
L0648:
L064A:
L064C:
    If (Not LastInMiddle) Then GoTo L0657 Else GoTo L0693  ' pc=0654
L0657:
    If (RefL = TestL) Then GoTo L0664 Else GoTo L066F  ' pc=0661
L0664:
    LSimValu = CSng(CDbl(1))  ' pc=0669
    GoTo L0691  ' pc=066C
L066F:
    tmp_FD30 = CStr(0)  ' pc=0678
    LSimValu = CSng(IsSimilar(RefL, TestL, tmp_FD30))  ' pc=068B
L0691:
L0693:
L0695:
    If DashInBoth Then GoTo L069F Else GoTo L0916  ' pc=069C
L069F:
    tmp_FE30 = InStr(1, RefL, "-", 2)  ' pc=06B6
    tmp_FE20 = (tmp_FE30 + 1)  ' pc=06BF
    tmp_FDC8 = Mid(RefL, CLng(tmp_FE20))  ' pc=06CB
    tmp_FDA8 = Trim(tmp_FDC8)  ' pc=06D6
    DashNameR = tmp_FDA8  ' pc=06DE
    tmp_FE30 = InStr(1, RefL, "-", 2)  ' pc=0701
    tmp_FE20 = (tmp_FE30 - 1)  ' pc=070A
    tmp_FE08 = Left(RefL, CLng(tmp_FE20))  ' pc=0716
    tmp_FDC8 = Trim(tmp_FE08)  ' pc=0721
    DashNameL = tmp_FDC8  ' pc=0729
    If (RefL = TestL) Then GoTo L0741 Else GoTo L074C  ' pc=073E
L0741:
    LSimValu = CSng(CDbl(1))  ' pc=0746
    GoTo L0789  ' pc=0749
L074C:
    tmp_FD30 = CStr(0)  ' pc=0755
    LSimValu = CSng(IsSimilar(RefL, TestL, tmp_FD30))  ' pc=0768
    If (LSimValu < CSng(0.8)) Then GoTo L0781 Else GoTo L0789  ' pc=077E
L0781:
    LSimValu = CSng(CDbl(0))  ' pc=0786
L0789:
    If (LSimValu = CDbl(0)) Then GoTo L0797 Else GoTo L0833  ' pc=0794
L0797:
    tmp_FE30 = InStr(1, TestL, "-", 2)  ' pc=07AE
    tmp_FE20 = (tmp_FE30 - 1)  ' pc=07B7
    tmp_FE08 = Left(TestL, CLng(tmp_FE20))  ' pc=07C3
    If (DashNameR = tmp_FE08) Then GoTo L07D7 Else GoTo L07E2  ' pc=07D4
L07D7:
    LSimValu = CSng(CDbl(1))  ' pc=07DC
    GoTo L0831  ' pc=07DF
L07E2:
    tmp_FE30 = InStr(1, TestL, "-", 2)  ' pc=07FC
    tmp_FE20 = (tmp_FE30 + 1)  ' pc=0805
    tmp_FDC8 = Mid(TestL, CLng(tmp_FE20))  ' pc=0811
    If (DashNameL = tmp_FDC8) Then GoTo L0829 Else GoTo L0831  ' pc=0826
L0829:
    LSimValu = CSng(CDbl(1))  ' pc=082E
L0831:
L0833:
    If (LSimValu = CDbl(0)) Then GoTo L0841 Else GoTo L0914  ' pc=083E
L0841:
    tmp_FE30 = InStr(1, TestL, "-", 2)  ' pc=0858
    tmp_FE20 = (tmp_FE30 + 1)  ' pc=0861
    tmp_FDC8 = Mid(TestL, CLng(tmp_FE20))  ' pc=086D
    tmp_FDA8 = InStr(1, TestL, "-", 2)  ' pc=0884
    tmp_FD98 = (tmp_FDA8 - 1)  ' pc=088D
    tmp_FD78 = Left(TestL, CLng(tmp_FD98))  ' pc=0899
    tmp_FD2C = CStr(0)  ' pc=08A3
    tmp_FE1C = CSng(IsSimilar(DashNameR, tmp_FD78, tmp_FD2C))  ' pc=08B6
    tmp_FD30 = CStr(0)  ' pc=08BE
    LSimValu = CSng(((IsSimilar(DashNameL, tmp_FDC8, tmp_FD30) + tmp_FE1C) / CDbl(2)))  ' pc=08D9
    If (LSimValu < CSng(0.8)) Then GoTo L0905 Else GoTo L0912  ' pc=0902
L0905:
    SimScore = CSng(CDbl(0))  ' pc=090A
    GoTo L19F9  ' pc=090F
L0912:
L0914:
L0916:
    If DashInOne Then GoTo L0920 Else GoTo L0D6F  ' pc=091D
L0920:
    tmp_FE30 = (RefL Like "*-*")  ' pc=092A
    tmp_FE20 = (TestL Like "*-*")  ' pc=0936
    tmp_FE08 = (Not tmp_FE20)  ' pc=093A
    tmp_FDC8 = (tmp_FE30 And tmp_FE08)  ' pc=093E
    If tmp_FDC8 Then GoTo L0947 Else GoTo L0B48  ' pc=0944
L0947:
    tmp_FE30 = InStr(1, RefL, "-", 2)  ' pc=095E
    tmp_FE20 = (tmp_FE30 + 1)  ' pc=0967
    tmp_FDC8 = Mid(RefL, CLng(tmp_FE20))  ' pc=0973
    tmp_FDA8 = Trim(tmp_FDC8)  ' pc=097E
    DashNameR = tmp_FDA8  ' pc=0986
    tmp_FE30 = InStr(1, RefL, "-", 2)  ' pc=09A9
    tmp_FE20 = (tmp_FE30 - 1)  ' pc=09B2
    tmp_FE08 = Left(RefL, CLng(tmp_FE20))  ' pc=09BE
    tmp_FDC8 = Trim(tmp_FE08)  ' pc=09C9
    DashNameL = tmp_FDC8  ' pc=09D1
    tmp_FE30 = (TestL Like "* *")  ' pc=09E6
    If tmp_FE30 Then GoTo L09EF Else GoTo L0A6D  ' pc=09EC
L09EF:
    tmp_FE18 = 0  ' pc=09F6
    tmp_FE1C = 1  ' pc=09FE
    tmp_FE20 = " "  ' pc=0A06
    tmp_FE30 = "-"  ' pc=0A11
    tmp_FE08 = StrReplace(RefL, tmp_FE30, tmp_FE20, tmp_FE1C, tmp_FE18)  ' pc=0A1D
    DashName = tmp_FE08  ' pc=0A25
    tmp_FD30 = CStr(0)  ' pc=0A37
    LSimValu = CSng(IsSimilar(DashName, TestL, tmp_FD30))  ' pc=0A4A
    If (LSimValu < CSng(0.8)) Then GoTo L0A63 Else GoTo L0A6B  ' pc=0A60
L0A63:
    LSimValu = CSng(CDbl(0))  ' pc=0A68
L0A6B:
L0A6D:
    If (LSimValu = CDbl(0)) Then GoTo L0A7B Else GoTo L0AAA  ' pc=0A78
L0A7B:
    If (DashNameR = TestL) Then GoTo L0A88 Else GoTo L0A93  ' pc=0A85
L0A88:
    LSimValu = CSng(CDbl(1))  ' pc=0A8D
    GoTo L0AA8  ' pc=0A90
L0A93:
    If (DashNameL = TestL) Then GoTo L0AA0 Else GoTo L0AA8  ' pc=0A9D
L0AA0:
    LSimValu = CSng(CDbl(1))  ' pc=0AA5
L0AA8:
L0AAA:
    If (LSimValu = CDbl(0)) Then GoTo L0AB8 Else GoTo L0B43  ' pc=0AB5
L0AB8:
    tmp_FD30 = CStr(0)  ' pc=0ABF
    LSimValu = CSng(IsSimilar(DashNameL, TestL, tmp_FD30))  ' pc=0AD2
    If (LSimValu < CSng(0.8)) Then GoTo L0AEB Else GoTo L0AF3  ' pc=0AE8
L0AEB:
    LSimValu = CSng(CDbl(0))  ' pc=0AF0
L0AF3:
    If (LSimValu = CDbl(0)) Then GoTo L0AFF Else GoTo L0B1F  ' pc=0AFC
L0AFF:
    tmp_FD30 = CStr(0)  ' pc=0B06
    LSimValu = CSng(IsSimilar(DashNameR, TestL, tmp_FD30))  ' pc=0B19
L0B1F:
    If (LSimValu < CSng(0.8)) Then GoTo L0B34 Else GoTo L0B41  ' pc=0B31
L0B34:
    SimScore = CSng(CDbl(0))  ' pc=0B39
    GoTo L19F9  ' pc=0B3E
L0B41:
L0B43:
    GoTo L0D6D  ' pc=0B45
L0B48:
    tmp_FE30 = (RefL Like "*-*")  ' pc=0B52
    tmp_FE20 = (Not tmp_FE30)  ' pc=0B56
    tmp_FE08 = (TestL Like "*-*")  ' pc=0B62
    tmp_FDC8 = (tmp_FE20 And tmp_FE08)  ' pc=0B66
    If tmp_FDC8 Then GoTo L0B6F Else GoTo L0D6D  ' pc=0B6C
L0B6F:
    tmp_FE30 = InStr(1, TestL, "-", 2)  ' pc=0B86
    tmp_FE20 = (tmp_FE30 + 1)  ' pc=0B8F
    tmp_FDC8 = Mid(TestL, CLng(tmp_FE20))  ' pc=0B9B
    tmp_FDA8 = Trim(tmp_FDC8)  ' pc=0BA6
    DashNameR = tmp_FDA8  ' pc=0BAE
    tmp_FE30 = InStr(1, TestL, "-", 2)  ' pc=0BD1
    tmp_FE20 = (tmp_FE30 - 1)  ' pc=0BDA
    tmp_FE08 = Left(TestL, CLng(tmp_FE20))  ' pc=0BE6
    tmp_FDC8 = Trim(tmp_FE08)  ' pc=0BF1
    DashNameL = tmp_FDC8  ' pc=0BF9
    tmp_FE30 = (RefL Like "* *")  ' pc=0C0E
    If tmp_FE30 Then GoTo L0C17 Else GoTo L0C95  ' pc=0C14
L0C17:
    tmp_FE18 = 0  ' pc=0C1E
    tmp_FE1C = 1  ' pc=0C26
    tmp_FE20 = " "  ' pc=0C2E
    tmp_FE30 = "-"  ' pc=0C39
    tmp_FE08 = StrReplace(TestL, tmp_FE30, tmp_FE20, tmp_FE1C, tmp_FE18)  ' pc=0C45
    DashName = tmp_FE08  ' pc=0C4D
    tmp_FD30 = CStr(0)  ' pc=0C5F
    LSimValu = CSng(IsSimilar(DashName, RefL, tmp_FD30))  ' pc=0C72
    If (LSimValu < CSng(0.8)) Then GoTo L0C8B Else GoTo L0C93  ' pc=0C88
L0C8B:
    LSimValu = CSng(CDbl(0))  ' pc=0C90
L0C93:
L0C95:
    If (LSimValu = CDbl(0)) Then GoTo L0CA3 Else GoTo L0CD2  ' pc=0CA0
L0CA3:
    If (DashNameR = RefL) Then GoTo L0CB0 Else GoTo L0CBB  ' pc=0CAD
L0CB0:
    LSimValu = CSng(CDbl(1))  ' pc=0CB5
    GoTo L0CD0  ' pc=0CB8
L0CBB:
    If (DashNameL = RefL) Then GoTo L0CC8 Else GoTo L0CD0  ' pc=0CC5
L0CC8:
    LSimValu = CSng(CDbl(1))  ' pc=0CCD
L0CD0:
L0CD2:
    If (LSimValu = CDbl(0)) Then GoTo L0CE0 Else GoTo L0D6B  ' pc=0CDD
L0CE0:
    tmp_FD30 = CStr(0)  ' pc=0CE7
    LSimValu = CSng(IsSimilar(DashNameL, RefL, tmp_FD30))  ' pc=0CFA
    If (LSimValu < CSng(0.8)) Then GoTo L0D13 Else GoTo L0D1B  ' pc=0D10
L0D13:
    LSimValu = CSng(CDbl(0))  ' pc=0D18
L0D1B:
    If (LSimValu = CDbl(0)) Then GoTo L0D27 Else GoTo L0D47  ' pc=0D24
L0D27:
    tmp_FD30 = CStr(0)  ' pc=0D2E
    LSimValu = CSng(IsSimilar(DashNameR, RefL, tmp_FD30))  ' pc=0D41
L0D47:
    If (LSimValu < CSng(0.8)) Then GoTo L0D5C Else GoTo L0D69  ' pc=0D59
L0D5C:
    SimScore = CSng(CDbl(0))  ' pc=0D61
    GoTo L19F9  ' pc=0D66
L0D69:
L0D6B:
L0D6D:
L0D6F:
    If LastInMiddle Then GoTo L0D79 Else GoTo L0E88  ' pc=0D76
L0D79:
    If (RefF = TestF) Then GoTo L0D86 Else GoTo L0D91  ' pc=0D83
L0D86:
    FSimValu = CSng(CDbl(1))  ' pc=0D8B
    GoTo L0E6D  ' pc=0D8E
L0D91:
    tmp_FE30 = (RefFLen > 1)  ' pc=0D9E
    tmp_FE20 = (TestFLen = 1)  ' pc=0DAB
    tmp_FE08 = (tmp_FE30 And tmp_FE20)  ' pc=0DAF
    tmp_FDC8 = (RefFLen = 1)  ' pc=0DBC
    tmp_FDA8 = (TestFLen > 1)  ' pc=0DC9
    tmp_FD98 = (tmp_FDC8 And tmp_FDA8)  ' pc=0DCD
    tmp_FD78 = (tmp_FE08 Or tmp_FD98)  ' pc=0DD1
    If tmp_FD78 Then GoTo L0DDA Else GoTo L0E12  ' pc=0DD7
L0DDA:
    tmp_FE30 = Left(RefF, 1)  ' pc=0DE7
    tmp_FE20 = Left(TestF, 1)  ' pc=0DFA
    tmp_FE08 = (tmp_FE30 = tmp_FE20)  ' pc=0E02
    FFirstSameLetter = CInt(CBool(tmp_FE08))  ' pc=0E08
L0E12:
    If (Not FFirstSameLetter) Then GoTo L0E1D Else GoTo L0E40  ' pc=0E1A
L0E1D:
    tmp_FD30 = CStr(0)  ' pc=0E24
    FSimValu = CSng(IsSimilar(RefF, TestF, tmp_FD30))  ' pc=0E37
    GoTo L0E50  ' pc=0E3D
L0E40:
    FSimValu = CSng(0.8)  ' pc=0E4D
L0E50:
    If (FSimValu < CSng(0.7)) Then GoTo L0E65 Else GoTo L0E6D  ' pc=0E62
L0E65:
    FSimValu = CSng(CDbl(0))  ' pc=0E6A
L0E6D:
    SimScore = CSng((((LSimValu + FSimValu) + MSimValu) / CDbl(3)))  ' pc=0E80
    GoTo L19F9  ' pc=0E85
L0E88:
    If (RefF = TestF) Then GoTo L0E97 Else GoTo L0E9F  ' pc=0E94
L0E97:
    FSimValu = CSng(CDbl(1))  ' pc=0E9C
L0E9F:
    tmp_FE30 = (RefM = TestM)  ' pc=0EA9
    tmp_FE20 = (RefMLen > 0)  ' pc=0EB6
    tmp_FE08 = (TestMLen > 0)  ' pc=0EC3
    tmp_FDC8 = (tmp_FE20 And tmp_FE08)  ' pc=0EC7
    tmp_FDA8 = (tmp_FE30 And tmp_FDC8)  ' pc=0ECB
    If tmp_FDA8 Then GoTo L0ED4 Else GoTo L0EDC  ' pc=0ED1
L0ED4:
    MSimValu = CSng(CDbl(1))  ' pc=0ED9
L0EDC:
    tmp_FE30 = (RefF = TestF)  ' pc=0EE4
    tmp_FE20 = (RefM = TestM)  ' pc=0EEE
    tmp_FE08 = (RefMLen > 0)  ' pc=0EFB
    tmp_FDC8 = (TestMLen > 0)  ' pc=0F08
    tmp_FDA8 = (tmp_FE08 And tmp_FDC8)  ' pc=0F0C
    tmp_FD98 = (tmp_FE20 And tmp_FDA8)  ' pc=0F10
    tmp_FD78 = (tmp_FE30 And tmp_FD98)  ' pc=0F14
    If tmp_FD78 Then GoTo L0F1D Else GoTo L0F4B  ' pc=0F1A
L0F1D:
    If (LSimValu > CSng(0.86)) Then GoTo L0F30 Else GoTo L0F49  ' pc=0F2D
L0F30:
    SimScore = CSng((((LSimValu + FSimValu) + MSimValu) / CDbl(3)))  ' pc=0F41
    GoTo L19F9  ' pc=0F46
L0F49:
L0F4B:
    If (LSimValu > CSng(0.84)) Then GoTo L0F60 Else GoTo L14E1  ' pc=0F5D
L0F60:
    tmp_FE30 = (RefMLen > 1)  ' pc=0F6B
    tmp_FE20 = (TestMLen > 1)  ' pc=0F78
    tmp_FE08 = (tmp_FE30 Or tmp_FE20)  ' pc=0F7C
    If tmp_FE08 Then GoTo L0F85 Else GoTo L1093  ' pc=0F82
L0F85:
    tmp_FE30 = (RefF = TestF)  ' pc=0F8D
    tmp_FE20 = (Not tmp_FE30)  ' pc=0F91
    tmp_FE08 = (RefM = TestM)  ' pc=0F9B
    tmp_FDC8 = (Not tmp_FE08)  ' pc=0F9F
    tmp_FDA8 = (tmp_FE20 And tmp_FDC8)  ' pc=0FA3
    If tmp_FDA8 Then GoTo L0FAC Else GoTo L1091  ' pc=0FA9
L0FAC:
    tmp_FE30 = (RefF & RefM)  ' pc=0FB4
    tmp_FE20 = (tmp_FE30 = TestF)  ' pc=0FBB
    tmp_FE08 = (TestF & TestM)  ' pc=0FC8
    tmp_FDC8 = (RefF = tmp_FE08)  ' pc=0FCC
    tmp_FDA8 = (tmp_FE20 Or tmp_FDC8)  ' pc=0FD0
    If tmp_FDA8 Then GoTo L0FE0 Else GoTo L0FF6  ' pc=0FDD
L0FE0:
    SimScore = CSng(0.8)  ' pc=0FEB
    GoTo L19F9  ' pc=0FF0
    GoTo L108F  ' pc=0FF3
L0FF6:
    tmp_FD30 = CStr(0)  ' pc=0FFF
    tmp_FE30 = (RefF & RefM)  ' pc=100F
    If (CSng(IsSimilar(tmp_FE30, TestF, tmp_FD30)) > CSng(0.85)) Then GoTo L102E Else GoTo L1044  ' pc=102B
L102E:
    SimScore = CSng(0.8)  ' pc=1039
    GoTo L19F9  ' pc=103E
    GoTo L108D  ' pc=1041
L1044:
    tmp_FD30 = CStr(0)  ' pc=104B
    tmp_FE30 = (TestF & TestF)  ' pc=1057
    If (CSng(IsSimilar(RefF, tmp_FE30, tmp_FD30)) > CSng(0.85)) Then GoTo L107A Else GoTo L108D  ' pc=1077
L107A:
    SimScore = CSng(0.8)  ' pc=1085
    GoTo L19F9  ' pc=108A
L108D:
L108F:
L1091:
L1093:
    tmp_FE30 = (RefFLen > 1)  ' pc=10A0
    tmp_FE20 = (TestMLen > 1)  ' pc=10AD
    tmp_FE08 = (tmp_FE30 And tmp_FE20)  ' pc=10B1
    If tmp_FE08 Then GoTo L10BA Else GoTo L1106  ' pc=10B7
L10BA:
    If (RefF = TestM) Then GoTo L10C7 Else GoTo L10D1  ' pc=10C4
L10C7:
    RF_in_TM = CInt(-1)  ' pc=10CB
    GoTo L1104  ' pc=10CE
L10D1:
    tmp_FD30 = CStr(0)  ' pc=10D8
    If (CSng(IsSimilar(RefF, TestM, tmp_FD30)) > CSng(0.86)) Then GoTo L10FD Else GoTo L1104  ' pc=10FA
L10FD:
    RF_in_TM = CInt(-1)  ' pc=1101
L1104:
L1106:
    tmp_FE30 = (RefMLen > 1)  ' pc=1113
    tmp_FE20 = (TestFLen > 1)  ' pc=1120
    tmp_FE08 = (tmp_FE30 And tmp_FE20)  ' pc=1124
    If tmp_FE08 Then GoTo L112D Else GoTo L1179  ' pc=112A
L112D:
    If (RefM = TestF) Then GoTo L113A Else GoTo L1144  ' pc=1137
L113A:
    RM_in_TF = CInt(-1)  ' pc=113E
    GoTo L1177  ' pc=1141
L1144:
    tmp_FD30 = CStr(0)  ' pc=114B
    If (CSng(IsSimilar(RefM, TestF, tmp_FD30)) > CSng(0.86)) Then GoTo L1170 Else GoTo L1177  ' pc=116D
L1170:
    RM_in_TF = CInt(-1)  ' pc=1174
L1177:
L1179:
    If (((RF_in_TM And RM_in_TF) Or (RF_in_TM And (Not RM_in_TF))) Or ((Not RF_in_TM) And RM_in_TF)) Then GoTo L1199 Else GoTo L11AC  ' pc=1196
L1199:
    SimScore = CSng(0.8)  ' pc=11A4
    GoTo L19F9  ' pc=11A9
L11AC:
    tmp_FE30 = (RefFLen > 1)  ' pc=11B9
    tmp_FE20 = (TestFLen = 1)  ' pc=11C6
    tmp_FE08 = (tmp_FE30 And tmp_FE20)  ' pc=11CA
    tmp_FDC8 = (RefFLen = 1)  ' pc=11D7
    tmp_FDA8 = (TestFLen > 1)  ' pc=11E4
    tmp_FD98 = (tmp_FDC8 And tmp_FDA8)  ' pc=11E8
    tmp_FD78 = (tmp_FE08 Or tmp_FD98)  ' pc=11EC
    If tmp_FD78 Then GoTo L11F5 Else GoTo L122D  ' pc=11F2
L11F5:
    tmp_FE30 = Left(RefF, 1)  ' pc=1202
    tmp_FE20 = Left(TestF, 1)  ' pc=1215
    tmp_FE08 = (tmp_FE30 = tmp_FE20)  ' pc=121D
    FFirstSameLetter = CInt(CBool(tmp_FE08))  ' pc=1223
L122D:
    tmp_FE30 = (RefMLen > 1)  ' pc=123A
    tmp_FE20 = (TestMLen = 1)  ' pc=1247
    tmp_FE08 = (tmp_FE30 And tmp_FE20)  ' pc=124B
    tmp_FDC8 = (RefMLen = 1)  ' pc=1258
    tmp_FDA8 = (TestMLen > 1)  ' pc=1265
    tmp_FD98 = (tmp_FDC8 And tmp_FDA8)  ' pc=1269
    tmp_FD78 = (tmp_FE08 Or tmp_FD98)  ' pc=126D
    If tmp_FD78 Then GoTo L1276 Else GoTo L12AE  ' pc=1273
L1276:
    tmp_FE30 = Left(RefM, 1)  ' pc=1283
    tmp_FE20 = Left(TestM, 1)  ' pc=1296
    tmp_FE08 = (tmp_FE30 = tmp_FE20)  ' pc=129E
    MFirstSameLetter = CInt(CBool(tmp_FE08))  ' pc=12A4
L12AE:
    If FFirstSameLetter Then GoTo L12B8 Else GoTo L13DA  ' pc=12B5
L12B8:
    FSimValu = CSng(0.8)  ' pc=12C3
    tmp_FE30 = (RefMLen = 0)  ' pc=12D1
    tmp_FE20 = (TestMLen = 0)  ' pc=12DE
    tmp_FE08 = (tmp_FE30 And tmp_FE20)  ' pc=12E2
    If tmp_FE08 Then GoTo L12EB Else GoTo L1303  ' pc=12E8
L12EB:
    SimScore = CSng(((LSimValu + FSimValu) / CDbl(2)))  ' pc=12F8
    GoTo L19F9  ' pc=12FD
    GoTo L13D8  ' pc=1300
L1303:
    tmp_FE30 = (RefMLen > 1)  ' pc=130E
    tmp_FE20 = (TestMLen = 0)  ' pc=131B
    tmp_FE08 = (tmp_FE30 And tmp_FE20)  ' pc=131F
    tmp_FDC8 = (RefMLen = 0)  ' pc=132C
    tmp_FDA8 = (TestMLen > 1)  ' pc=1339
    tmp_FD98 = (tmp_FDC8 And tmp_FDA8)  ' pc=133D
    tmp_FD78 = (tmp_FE08 Or tmp_FD98)  ' pc=1341
    If tmp_FD78 Then GoTo L134A Else GoTo L136C  ' pc=1347
L134A:
    SimScore = CSng((((LSimValu + FSimValu) + 0.5) / CDbl(3)))  ' pc=1361
    GoTo L19F9  ' pc=1366
    GoTo L13D8  ' pc=1369
L136C:
    If (Not MFirstSameLetter) Then GoTo L1375 Else GoTo L13B1  ' pc=1372
L1375:
    tmp_FD30 = CStr(0)  ' pc=137C
    MSimValu = CSng(IsSimilar(RefM, TestM, tmp_FD30))  ' pc=138F
    SimScore = CSng((((LSimValu + FSimValu) + MSimValu) / CDbl(3)))  ' pc=13A6
    GoTo L19F9  ' pc=13AB
    GoTo L13D8  ' pc=13AE
L13B1:
    If MFirstSameLetter Then GoTo L13B9 Else GoTo L13D8  ' pc=13B6
L13B9:
    SimScore = CSng((((LSimValu + FSimValu) + 0.8) / CDbl(3)))  ' pc=13D0
    GoTo L19F9  ' pc=13D5
L13D8:
L13DA:
    tmp_FE30 = (RefF & RefM)  ' pc=13E4
    tmp_FE20 = (tmp_FE30 = TestF)  ' pc=13EB
    tmp_FE08 = (TestF & TestM)  ' pc=13F8
    tmp_FDC8 = (RefF = tmp_FE08)  ' pc=13FC
    tmp_FDA8 = (tmp_FE20 Or tmp_FDC8)  ' pc=1400
    If tmp_FDA8 Then GoTo L1410 Else GoTo L1426  ' pc=140D
L1410:
    SimScore = CSng(0.8)  ' pc=141B
    GoTo L19F9  ' pc=1420
    GoTo L14DF  ' pc=1423
L1426:
    If (RefMLen > 1) Then GoTo L1436 Else GoTo L1484  ' pc=1433
L1436:
    tmp_FD30 = CStr(0)  ' pc=143D
    tmp_FE30 = (RefF & RefM)  ' pc=144D
    If (CSng(IsSimilar(tmp_FE30, TestF, tmp_FD30)) > CSng(0.8)) Then GoTo L146C Else GoTo L147F  ' pc=1469
L146C:
    SimScore = CSng(0.8)  ' pc=1477
    GoTo L19F9  ' pc=147C
L147F:
    GoTo L14DF  ' pc=1481
L1484:
    If (TestMLen > 1) Then GoTo L1494 Else GoTo L14DF  ' pc=1491
L1494:
    tmp_FD30 = CStr(0)  ' pc=149B
    tmp_FE30 = (TestF & TestM)  ' pc=14A7
    If (CSng(IsSimilar(RefF, tmp_FE30, tmp_FD30)) > CSng(0.8)) Then GoTo L14CA Else GoTo L14DD  ' pc=14C7
L14CA:
    SimScore = CSng(0.8)  ' pc=14D5
    GoTo L19F9  ' pc=14DA
L14DD:
L14DF:
L14E1:
    If (RefF = TestF) Then GoTo L14F0 Else GoTo L14FB  ' pc=14ED
L14F0:
    FSimValu = CSng(CDbl(1))  ' pc=14F5
    GoTo L157B  ' pc=14F8
L14FB:
    tmp_FD30 = CStr(0)  ' pc=1504
    FSimValu = CSng(IsSimilar(RefF, TestF, tmp_FD30))  ' pc=1517
    If (CSng(((LSimValu + FSimValu) / CDbl(2))) < CSng(0.8)) Then GoTo L1539 Else GoTo L1579  ' pc=1536
L1539:
    If (FSimValu < CSng(0.5)) Then GoTo L154C Else GoTo L1554  ' pc=1549
L154C:
    FSimValu = CSng(CDbl(0))  ' pc=1551
L1554:
    If ((MSimValu > CDbl(0)) And (MSimValu < CSng(0.45))) Then GoTo L156F Else GoTo L1577  ' pc=156C
L156F:
    MSimValu = CSng(CDbl(0))  ' pc=1574
L1577:
L1579:
L157B:
    If MFirstSameLetter Then GoTo L1585 Else GoTo L15CA  ' pc=1582
L1585:
    If (CSng(((LSimValu + FSimValu) / CDbl(2))) > CSng(0.8)) Then GoTo L15A1 Else GoTo L15C8  ' pc=159E
L15A1:
    MSimValu = CSng(0.8)  ' pc=15AC
    SimScore = CSng((((LSimValu + FSimValu) + MSimValu) / CDbl(3)))  ' pc=15C0
    GoTo L19F9  ' pc=15C5
L15C8:
L15CA:
    tmp_FE30 = (RefMLen > 0)  ' pc=15D7
    tmp_FE20 = (TestMLen = 0)  ' pc=15E4
    tmp_FE08 = (tmp_FE30 And tmp_FE20)  ' pc=15E8
    If tmp_FE08 Then GoTo L15F1 Else GoTo L16B8  ' pc=15EE
L15F1:
    If (RefM = TestM) Then GoTo L15FE Else GoTo L161E  ' pc=15FB
L15FE:
    If (FSimValu > CSng(0.8)) Then GoTo L1611 Else GoTo L1619  ' pc=160E
L1611:
    MSimValu = CSng(CDbl(1))  ' pc=1616
L1619:
    GoTo L16B6  ' pc=161B
L161E:
    tmp_FE30 = (RefMLen > 0)  ' pc=1629
    tmp_FE20 = (TestMLen = 0)  ' pc=1636
    tmp_FE08 = (tmp_FE30 And tmp_FE20)  ' pc=163A
    tmp_FDC8 = (RefMLen = 0)  ' pc=1647
    tmp_FDA8 = (TestMLen > 0)  ' pc=1654
    tmp_FD98 = (tmp_FDC8 And tmp_FDA8)  ' pc=1658
    tmp_FD78 = (tmp_FE08 Or tmp_FD98)  ' pc=165C
    If tmp_FD78 Then GoTo L1665 Else GoTo L1694  ' pc=1662
L1665:
    If (CSng(((LSimValu + FSimValu) / CDbl(2))) > CSng(0.83)) Then GoTo L1681 Else GoTo L168F  ' pc=167E
L1681:
    MSimValu = CSng(0.5)  ' pc=168C
L168F:
    GoTo L16B6  ' pc=1691
L1694:
    tmp_FD30 = CStr(0)  ' pc=169D
    MSimValu = CSng(IsSimilar(RefM, TestM, tmp_FD30))  ' pc=16B0
L16B6:
L16B8:
    If (LSimValu < CSng(0.75)) Then GoTo L16CD Else GoTo L16D5  ' pc=16CA
L16CD:
    LSimValu = CSng(CDbl(0))  ' pc=16D2
L16D5:
    tmp_FE30 = (RefMLen > 0)  ' pc=16E0
    tmp_FE20 = (TestMLen = 0)  ' pc=16ED
    tmp_FE08 = (tmp_FE30 And tmp_FE20)  ' pc=16F1
    If tmp_FE08 Then GoTo L16FA Else GoTo L1746  ' pc=16F7
L16FA:
    tmp_FE30 = (RefF & RefM)  ' pc=1702
    tmp_FE20 = (TestF & TestM)  ' pc=170C
    tmp_FE08 = (tmp_FE30 = tmp_FE20)  ' pc=1710
    tmp_FE50 = CBool((LSimValu > CSng(0.7)))  ' pc=1722
    tmp_FDC8 = (tmp_FE08 And tmp_FE50)  ' pc=1726
    If tmp_FDC8 Then GoTo L1738 Else GoTo L1746  ' pc=1735
L1738:
    LSimValu = CSng(0.8)  ' pc=1743
L1746:
    If ((LSimValu = CDbl(1)) And (CSng(((LSimValu + FSimValu) / CDbl(2))) < CSng(0.84))) Then GoTo L176C Else GoTo L1839  ' pc=1769
L176C:
    tmp_FE30 = (RefMLen > 0)  ' pc=1777
    tmp_FE20 = (TestMLen = 0)  ' pc=1784
    tmp_FE08 = (tmp_FE30 And tmp_FE20)  ' pc=1788
    tmp_FDC8 = (RefMLen = 0)  ' pc=1795
    tmp_FDA8 = (TestMLen > 0)  ' pc=17A2
    tmp_FD98 = (tmp_FDC8 And tmp_FDA8)  ' pc=17A6
    tmp_FD78 = (tmp_FE08 Or tmp_FD98)  ' pc=17AA
    If tmp_FD78 Then GoTo L17B3 Else GoTo L17C4  ' pc=17B0
L17B3:
    MSimValu = CSng(0.45)  ' pc=17BE
    GoTo L1834  ' pc=17C1
L17C4:
    tmp_FE30 = (RefMLen > 1)  ' pc=17D1
    tmp_FE20 = (TestMLen > 1)  ' pc=17DE
    tmp_FE08 = (tmp_FE30 And tmp_FE20)  ' pc=17E2
    If tmp_FE08 Then GoTo L17EB Else GoTo L181C  ' pc=17E8
L17EB:
    If (MSimValu = CDbl(0)) Then GoTo L17F7 Else GoTo L1817  ' pc=17F4
L17F7:
    tmp_FD30 = CStr(0)  ' pc=17FE
    MSimValu = CSng(IsSimilar(RefM, TestM, tmp_FD30))  ' pc=1811
L1817:
    GoTo L1832  ' pc=1819
L181C:
    If MFirstSameLetter Then GoTo L1824 Else GoTo L1832  ' pc=1821
L1824:
    MSimValu = CSng(0.45)  ' pc=182F
L1832:
L1834:
    GoTo L1977  ' pc=1836
L1839:
    If (CSng(((LSimValu + FSimValu) / CDbl(2))) > CSng(0.85)) Then GoTo L1855 Else GoTo L1977  ' pc=1852
L1855:
    tmp_FE30 = (RefMLen > 0)  ' pc=1860
    tmp_FE20 = (TestMLen = 0)  ' pc=186D
    tmp_FE08 = (tmp_FE30 And tmp_FE20)  ' pc=1871
    tmp_FDC8 = (RefMLen = 0)  ' pc=187E
    tmp_FDA8 = (TestMLen > 0)  ' pc=188B
    tmp_FD98 = (tmp_FDC8 And tmp_FDA8)  ' pc=188F
    tmp_FD78 = (tmp_FE08 Or tmp_FD98)  ' pc=1893
    If tmp_FD78 Then GoTo L189C Else GoTo L18AD  ' pc=1899
L189C:
    MSimValu = CSng(0.5)  ' pc=18A7
    GoTo L1975  ' pc=18AA
L18AD:
    tmp_FE30 = (RefMLen > 1)  ' pc=18BA
    tmp_FE20 = (TestMLen > 1)  ' pc=18C7
    tmp_FE08 = (tmp_FE30 And tmp_FE20)  ' pc=18CB
    If tmp_FE08 Then GoTo L18D4 Else GoTo L1905  ' pc=18D1
L18D4:
    If (MSimValu = CDbl(0)) Then GoTo L18E0 Else GoTo L1900  ' pc=18DD
L18E0:
    tmp_FD30 = CStr(0)  ' pc=18E7
    MSimValu = CSng(IsSimilar(RefM, TestM, tmp_FD30))  ' pc=18FA
L1900:
    GoTo L1973  ' pc=1902
L1905:
    If MFirstSameLetter Then GoTo L190D Else GoTo L191E  ' pc=190A
L190D:
    MSimValu = CSng(0.5)  ' pc=1918
    GoTo L1973  ' pc=191B
L191E:
    tmp_FE30 = (RefMLen = 1)  ' pc=1929
    tmp_FE20 = (TestMLen = 1)  ' pc=1936
    tmp_FE08 = (tmp_FE30 And tmp_FE20)  ' pc=193A
    If tmp_FE08 Then GoTo L1943 Else GoTo L1973  ' pc=1940
L1943:
    If (RefM = TestM) Then GoTo L1950 Else GoTo L1961  ' pc=194D
L1950:
    MSimValu = CSng(0.75)  ' pc=195B
    GoTo L1971  ' pc=195E
L1961:
    MSimValu = CSng(0.45)  ' pc=196E
L1971:
L1973:
L1975:
L1977:
    tmp_FE30 = (RefL & RefF)  ' pc=1981
    tmp_FE20 = (TestL & TestF)  ' pc=198B
    If (tmp_FE30 = tmp_FE20) Then GoTo L199B Else GoTo L19A9  ' pc=1998
L199B:
    MSimValu = CSng(0.55)  ' pc=19A6
L19A9:
    tmp_FE30 = (RefMLen = 0)  ' pc=19B4
    tmp_FE20 = (TestMLen = 0)  ' pc=19C1
    tmp_FE08 = (tmp_FE30 And tmp_FE20)  ' pc=19C5
    If tmp_FE08 Then GoTo L19CE Else GoTo L19E1  ' pc=19CB
L19CE:
    SimScore = CSng(((LSimValu + FSimValu) / CDbl(2)))  ' pc=19DB
    GoTo L19F7  ' pc=19DE
L19E1:
    SimScore = CSng((((LSimValu + FSimValu) + MSimValu) / CDbl(3)))  ' pc=19F4
L19F7:
L19F9:
    If ((SimScore > CSng(0.77)) And (FullNameSimValu > CSng(0.78))) Then GoTo L1A1B Else GoTo L1A4F  ' pc=1A18
L1A1B:
    tmp_FE08 = Maximum(SimScore, FullNameSimValu)  ' pc=1A36
    NameSimilarity = CSng(CDbl(tmp_FE08))  ' pc=1A40
    GoTo L1A59  ' pc=1A4C
L1A4F:
    NameSimilarity = CSng(SimScore)  ' pc=1A56
L1A59:
    Exit Function  ' pc=1A5D
End Function

Public Function LCS(ByVal input_str1 As Variant, ByVal input_str2 As Variant, Optional ByRef AlgInUse As Variant) As Single
    Dim tmp_FEBC As String
    Dim tmp_FEC4 As Variant
    Dim tmp_FED4 As Variant
    Dim tmp_FEF4 As Variant
    Dim Str2Len As Integer
    Dim Str1Len As Integer
    Dim Y() As String
    Dim X() As String
    Dim B() As Integer
    Dim c() As Integer
    Dim n As Integer
    Dim m As Integer
    Dim j As Integer
    Dim i As Integer
    Dim str2 As Variant
    Dim str1 As Variant

    str1 = input_str1  ' pc=0002
    str2 = input_str2  ' pc=0008
    If IsMissing(AlgInUse) Then GoTo L001B Else GoTo L0026  ' pc=0018
L001B:
    AlgInUse = ""  ' pc=0022
L0026:
    Str1Len = CInt(CInt(UBound(str1, 1)))  ' pc=0033
    Str2Len = CInt(CInt(UBound(str2, 1)))  ' pc=0043
    tmp_FEC4 = Minimum(Str1Len, Str2Len)  ' pc=0061
    n = CInt(CInt(tmp_FEC4))  ' pc=006A
    tmp_FEC4 = Maximum(Str1Len, Str2Len)  ' pc=0091
    m = CInt(CInt(tmp_FEC4))  ' pc=009A
    ReDim X(0 To CLng(m))  ' pc=00B4
    ReDim Y(0 To CLng(m))  ' pc=00CC
    ReDim c(0 To CLng(m), 0 To CLng(m))  ' pc=00ED
    ReDim B(0 To CLng(m), 0 To CLng(m))  ' pc=010E
    If (Str1Len > Str2Len) Then GoTo L0124 Else GoTo L01A9  ' pc=0121
L0124:
    For i = 0 To (Str1Len - 1)  ' pc=0131
    tmp_FEF4 = str1(i)  ' pc=0143
    tmp_FEBC = CStr(CStr(tmp_FEF4))  ' pc=014A
    X(CLng(i)) = tmp_FEBC  ' pc=0154
    Next i  ' pc=0160
    For i = 0 To (Str2Len - 1)  ' pc=0172
    tmp_FEF4 = str2(i)  ' pc=0184
    tmp_FEBC = CStr(CStr(tmp_FEF4))  ' pc=018B
    Y(CLng(i)) = tmp_FEBC  ' pc=0195
    Next i  ' pc=01A1
    GoTo L022D  ' pc=01A6
L01A9:
    For i = 0 To (Str2Len - 1)  ' pc=01B8
    tmp_FEF4 = str2(i)  ' pc=01CA
    tmp_FEBC = CStr(CStr(tmp_FEF4))  ' pc=01D1
    X(CLng(i)) = tmp_FEBC  ' pc=01DB
    Next i  ' pc=01E7
    For i = 0 To (Str1Len - 1)  ' pc=01F9
    tmp_FEF4 = str1(i)  ' pc=020B
    tmp_FEBC = CStr(CStr(tmp_FEF4))  ' pc=0212
    Y(CLng(i)) = tmp_FEBC  ' pc=021C
    Next i  ' pc=0228
L022D:
    For i = 1 To m  ' pc=0239
    For j = 1 To n  ' pc=0249
    If (X(CLng((i - 1))) = Y(CLng((j - 1)))) Then GoTo L026C Else GoTo L02B1  ' pc=0269
L026C:
    c(CLng(i), CLng(j)) = CInt((c(CLng((i - 1)), CLng((j - 1))) + 1))  ' pc=0296
    B(CLng(i), CLng(j)) = CInt(1)  ' pc=02AB
    GoTo L035C  ' pc=02AE
L02B1:
    If (c(CLng((i - 1)), CLng(j)) >= c(CLng(i), CLng((j - 1)))) Then GoTo L02DF Else GoTo L031E  ' pc=02DC
L02DF:
    c(CLng(i), CLng(j)) = CInt(c(CLng((i - 1)), CLng(j)))  ' pc=0303
    B(CLng(i), CLng(j)) = CInt(2)  ' pc=0318
    GoTo L035C  ' pc=031B
L031E:
    c(CLng(i), CLng(j)) = CInt(c(CLng(i), CLng((j - 1))))  ' pc=0344
    B(CLng(i), CLng(j)) = CInt(3)  ' pc=0359
L035C:
    Next j  ' pc=0363
    Next i  ' pc=036D
    If (c(CLng(m), CLng(n)) > 0) Then GoTo L038B Else GoTo L042C  ' pc=0388
L038B:
    tmp_FEF4 = (AlgInUse = "Dmph")  ' pc=0399
    tmp_FED4 = (AlgInUse = "SSLCS")  ' pc=03A9
    tmp_FEC4 = (tmp_FEF4 Or tmp_FED4)  ' pc=03AD
    If tmp_FEC4 Then GoTo L03B6 Else GoTo L03D0  ' pc=03B3
L03B6:
    LCS = CSng(CDbl(c(CLng(m), CLng(n))))  ' pc=03CA
    GoTo L0427  ' pc=03CD
L03D0:
    tmp_FED4 = "#.##"  ' pc=03E3
    tmp_FEF4 = CDbl((CDbl(c(CLng(m), CLng(n))) / (CDbl((Str1Len + Str2Len)) / CDbl(2))))  ' pc=0408
    tmp_FEC4 = Format(tmp_FEF4, tmp_FED4, 1, 1)  ' pc=040F
    LCS = CSng(CSng(tmp_FEC4))  ' pc=0419
L0427:
    GoTo L0436  ' pc=0429
L042C:
    LCS = CSng(CDbl(0))  ' pc=0433
L0436:
    Erase X  ' pc=043D
    Erase Y  ' pc=0443
    Erase c  ' pc=0449
    Erase B  ' pc=044F
    Exit Function  ' pc=0452
End Function

