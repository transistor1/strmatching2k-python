Attribute VB_Name = "Recovered_Globals"
' EXPERIMENTAL reconstruction: not compiled or runtime verified.
' Instructions fully traversed; this does not prove semantic equivalence.
Option Compare Database
Option Explicit

Public Function Minimum(ByRef pVal1 As Variant, ByRef pVal2 As Variant, Optional ByRef pVal3 As Variant, Optional ByRef pVal4 As Variant) As Variant
    Dim tmp_FF56 As Variant
    Dim TopVal As Integer

    Minimum = pVal1  ' pc=000A
    TopVal = CInt(2)  ' pc=0012
    If (Not IsMissing(pVal3)) Then GoTo L0023 Else GoTo L0041  ' pc=0020
L0023:
    TopVal = CInt(3)  ' pc=0027
    If (Not IsMissing(pVal4)) Then GoTo L0038 Else GoTo L003F  ' pc=0035
L0038:
    TopVal = CInt(4)  ' pc=003C
L003F:
L0041:
    tmp_FF56 = CInt(TopVal)  ' pc=0048
    If (tmp_FF56 = 2) Then GoTo L0056 Else GoTo L0075  ' pc=0053
L0056:
    If (pVal2 < Minimum) Then GoTo L0066 Else GoTo L0072  ' pc=0063
L0066:
    Minimum = pVal2  ' pc=006E
L0072:
    GoTo L011A  ' pc=0072
L0075:
    If (tmp_FF56 = 3) Then GoTo L0080 Else GoTo L00BB  ' pc=007D
L0080:
    If (pVal2 < Minimum) Then GoTo L0090 Else GoTo L009C  ' pc=008D
L0090:
    Minimum = pVal2  ' pc=0098
L009C:
    If (pVal3 < Minimum) Then GoTo L00AC Else GoTo L00B8  ' pc=00A9
L00AC:
    Minimum = pVal3  ' pc=00B4
L00B8:
    GoTo L011A  ' pc=00B8
L00BB:
    If (tmp_FF56 = 4) Then GoTo L00C6 Else GoTo L011A  ' pc=00C3
L00C6:
    If (pVal2 < Minimum) Then GoTo L00D6 Else GoTo L00E2  ' pc=00D3
L00D6:
    Minimum = pVal2  ' pc=00DE
L00E2:
    If (pVal3 < Minimum) Then GoTo L00F2 Else GoTo L00FE  ' pc=00EF
L00F2:
    Minimum = pVal3  ' pc=00FA
L00FE:
    If (pVal4 < Minimum) Then GoTo L010E Else GoTo L011A  ' pc=010B
L010E:
    Minimum = pVal4  ' pc=0116
L011A:
    Exit Function  ' pc=011E
End Function

Public Function Maximum(ByRef pVal1 As Variant, ByRef pVal2 As Variant, Optional ByRef pVal3 As Variant, Optional ByRef pVal4 As Variant) As Variant
    Dim tmp_FF56 As Variant
    Dim TopVal As Integer

    Maximum = pVal1  ' pc=000A
    TopVal = CInt(2)  ' pc=0012
    If (Not IsMissing(pVal3)) Then GoTo L0023 Else GoTo L0041  ' pc=0020
L0023:
    TopVal = CInt(3)  ' pc=0027
    If (Not IsMissing(pVal4)) Then GoTo L0038 Else GoTo L003F  ' pc=0035
L0038:
    TopVal = CInt(4)  ' pc=003C
L003F:
L0041:
    tmp_FF56 = CInt(TopVal)  ' pc=0048
    If (tmp_FF56 = 2) Then GoTo L0056 Else GoTo L0075  ' pc=0053
L0056:
    If (pVal2 > Maximum) Then GoTo L0066 Else GoTo L0072  ' pc=0063
L0066:
    Maximum = pVal2  ' pc=006E
L0072:
    GoTo L011A  ' pc=0072
L0075:
    If (tmp_FF56 = 3) Then GoTo L0080 Else GoTo L00BB  ' pc=007D
L0080:
    If (pVal2 > Maximum) Then GoTo L0090 Else GoTo L009C  ' pc=008D
L0090:
    Maximum = pVal2  ' pc=0098
L009C:
    If (pVal3 > Maximum) Then GoTo L00AC Else GoTo L00B8  ' pc=00A9
L00AC:
    Maximum = pVal3  ' pc=00B4
L00B8:
    GoTo L011A  ' pc=00B8
L00BB:
    If (tmp_FF56 = 4) Then GoTo L00C6 Else GoTo L011A  ' pc=00C3
L00C6:
    If (pVal2 > Maximum) Then GoTo L00D6 Else GoTo L00E2  ' pc=00D3
L00D6:
    Maximum = pVal2  ' pc=00DE
L00E2:
    If (pVal3 > Maximum) Then GoTo L00F2 Else GoTo L00FE  ' pc=00EF
L00F2:
    Maximum = pVal3  ' pc=00FA
L00FE:
    If (pVal4 > Maximum) Then GoTo L010E Else GoTo L011A  ' pc=010B
L010E:
    Maximum = pVal4  ' pc=0116
L011A:
    Exit Function  ' pc=011E
End Function

Public Function StrReplace(ByRef cString As Variant, ByRef cSearch As Variant, ByRef cReplace As Variant, Optional ByRef nStart As Long, Optional ByRef nCount As Long) As Variant
    Dim tmp_FEEC As Variant
    Dim tmp_FEFC As Variant
    Dim tmp_FF0C As Variant
    Dim tmp_FF24 As Variant
    Dim tmp_FF34 As Variant
    Dim tmp_FF44 As Variant
    Dim cSrchLen As Long
    Dim cStringLen As Long
    Dim ReplCount As Long
    Dim NewString As String
    Dim cReplLen As Long
    Dim X As Long

    If IsNull(cString) Then GoTo L000F Else GoTo L001F  ' pc=000C
L000F:
    StrReplace = Null  ' pc=0015
    Exit Function  ' pc=001B
L001F:
    If (cString = "") Then GoTo L0034 Else GoTo L0045  ' pc=0031
L0034:
    StrReplace = ""  ' pc=003B
    Exit Function  ' pc=0041
L0045:
    If IsNull(cSearch) Then GoTo L0054 Else GoTo L0066  ' pc=0051
L0054:
    StrReplace = cString  ' pc=005C
    Exit Function  ' pc=0062
L0066:
    If (Not (nCount > 0)) Then GoTo L0077 Else GoTo L0088  ' pc=0074
L0077:
    tmp_FF24 = Len(cString)  ' pc=007F
    nCount = CLng(CLng(tmp_FF24))  ' pc=0085
L0088:
    tmp_FF24 = Len(cString)  ' pc=0092
    cStringLen = CLng(CLng(tmp_FF24))  ' pc=0098
    tmp_FF24 = Len(cReplace)  ' pc=00A3
    cReplLen = CLng(CLng(tmp_FF24))  ' pc=00A9
    tmp_FF24 = Len(cSearch)  ' pc=00B4
    cSrchLen = CLng(CLng(tmp_FF24))  ' pc=00BA
    For X = 1 To cStringLen  ' pc=00CA
    If (X >= nStart) Then GoTo L00DC Else GoTo L0205  ' pc=00D9
L00DC:
    tmp_FF24 = Mid(cString, X, cSrchLen)  ' pc=00EF
    tmp_FF0C = (tmp_FF24 = cSearch)  ' pc=00FD
    tmp_FEFC = CBool((ReplCount < nCount))  ' pc=0108
    tmp_FEEC = (tmp_FF0C And tmp_FEFC)  ' pc=010C
    If tmp_FEEC Then GoTo L011C Else GoTo L018A  ' pc=0119
L011C:
    If (X > 1) Then GoTo L012A Else GoTo L0146  ' pc=0127
L012A:
    tmp_FF44 = CStr(NewString)  ' pc=012F
    tmp_FF24 = (tmp_FF44 & cReplace)  ' pc=0138
    NewString = CStr(CStr(tmp_FF24))  ' pc=013D
    GoTo L0155  ' pc=0143
L0146:
    NewString = CStr(CStr(cReplace))  ' pc=0152
L0155:
    If (cSrchLen > 1) Then GoTo L0165 Else GoTo L0177  ' pc=0162
L0165:
    X = CLng((X + (cSrchLen - 1)))  ' pc=0174
L0177:
    ReplCount = CLng((ReplCount + 1))  ' pc=0184
    GoTo L0200  ' pc=0187
L018A:
    If (ReplCount < nCount) Then GoTo L0198 Else GoTo L01CA  ' pc=0195
L0198:
    tmp_FF34 = CStr(NewString)  ' pc=019D
    tmp_FF0C = Mid(cString, X, 1)  ' pc=01AE
    tmp_FEEC = (tmp_FF34 & tmp_FF0C)  ' pc=01B6
    NewString = CStr(CStr(tmp_FEEC))  ' pc=01BB
    GoTo L01FE  ' pc=01C7
L01CA:
    tmp_FF34 = CStr(NewString)  ' pc=01D1
    tmp_FF0C = Mid(cString, X)  ' pc=01E0
    tmp_FEEC = (tmp_FF34 & tmp_FF0C)  ' pc=01E8
    NewString = CStr(CStr(tmp_FEEC))  ' pc=01ED
    GoTo L0242  ' pc=01FB
L01FE:
L0200:
    GoTo L0236  ' pc=0202
L0205:
    tmp_FF34 = CStr(NewString)  ' pc=020C
    tmp_FF0C = Mid(cString, X, 1)  ' pc=021D
    tmp_FEEC = (tmp_FF34 & tmp_FF0C)  ' pc=0225
    NewString = CStr(CStr(tmp_FEEC))  ' pc=022A
L0236:
    Next X  ' pc=023D
L0242:
    tmp_FF44 = CStr(NewString)  ' pc=0247
    StrReplace = tmp_FF44  ' pc=024A
    Exit Function  ' pc=0250
End Function

Public Function GetLastChrPos(ByRef pStr As Variant, ByRef pChr As Variant) As Integer
    Dim tmp_FF18 As Variant
    Dim tmp_FF38 As Variant
    Dim pLen As Variant
    Dim X As Integer

    If (Not IsNull(pStr)) Then GoTo L0010 Else GoTo L00A3  ' pc=000D
L0010:
    tmp_FF38 = InStr(1, pStr, pChr, 2)  ' pc=0028
    If (tmp_FF38 > 0) Then GoTo L003A Else GoTo L00A1  ' pc=0037
L003A:
    tmp_FF38 = Len(pStr)  ' pc=0042
    pLen = tmp_FF38  ' pc=0046
    For X = CInt(pLen) To 1 Step -1  ' pc=0057
    tmp_FF18 = Mid(pStr, CLng(X), 1)  ' pc=006E
    If (tmp_FF18 = pChr) Then GoTo L0088 Else GoTo L008D  ' pc=0085
L0088:
    GoTo L0099  ' pc=008A
L008D:
    Next X  ' pc=0094
L0099:
    GetLastChrPos = CInt(X)  ' pc=009E
L00A1:
L00A3:
    Exit Function  ' pc=00A7
End Function

Public Sub Str2Arry(ByRef pStr As Variant, ByRef Arry As Variant)
    Dim tmp_FF24 As Variant
    Dim tmp_FF34 As Variant
    Dim tmp_FF48 As Variant
    Dim X As Integer
    Dim StrLen As Variant

    tmp_FF48 = Len(pStr)  ' pc=000A
    StrLen = tmp_FF48  ' pc=000E
    tmp_FF48 = (StrLen - 1)  ' pc=0021
    ReDim Arry(0 To CLng(tmp_FF48))  ' pc=002A
    For X = 1 To CInt(StrLen)  ' pc=003B
    tmp_FF24 = CInt((X - 1))  ' pc=0049
    tmp_FF34 = Mid(pStr, CLng(X), 1)  ' pc=005C
    Arry(tmp_FF24) = tmp_FF34  ' pc=0068
    Next X  ' pc=0078
    Exit Sub  ' pc=007F
End Sub

