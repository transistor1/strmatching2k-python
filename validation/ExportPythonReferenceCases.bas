Attribute VB_Name = "ExportPythonReferenceCases"
Option Compare Database
Option Explicit

Private Type SingleForBits
    Value As Single
End Type

Private Type LongForBits
    Value As Long
End Type

Private Function SingleHex(ByVal score As Single) As String
    Dim s As SingleForBits
    Dim l As LongForBits
    s.Value = score
    LSet l = s
    SingleHex = Right$("00000000" & Hex$(l.Value), 8)
End Function

Private Function CsvQuote(ByVal text As String) As String
    CsvQuote = Chr$(34) & Replace(text, Chr$(34), Chr$(34) & Chr$(34)) & Chr$(34)
End Function

Public Sub ExportPythonParityCases(Optional ByVal outputPath As String = "")
    Dim pairs As Variant
    Dim pair As Variant
    Dim modes As Variant
    Dim mode As Variant
    Dim score As Single
    Dim channel As Integer
    If outputPath = "" Then outputPath = CurrentProject.Path & "\python-reference.csv"
    pairs = Array( _
        Array("OMEPRA TEST", "GENERIC OMEPRA TEST"), _
        Array("LEFLUNOMIDE            20 MG", "LEFLUNOMIDE"), _
        Array("FUROSEMIDE             10 MG/M", "FUROSEMIDE"), _
        Array("ALLERGY STOP", "ALLERGY-STOP"), _
        Array("PAIN RELIEF", "PAINT REMOVER"), _
        Array("Smith", "Smyth"), Array("Robert", "Rupert"), _
        Array("John", "Jon"), Array("AB", "BA"), _
        Array("AAAA", "AA"), Array("A-B", "AB"), _
        Array("A/B", "AB"), Array("", ""), Array("", "A"))
    ' DblMetaPh is omitted because it writes to an Access comparison form.
    modes = Array("", "Dice", "Lev", "SSLCS")
    channel = FreeFile
    On Error GoTo Failed
    Open outputPath For Output As #channel
    Print #channel, "reference,candidate,algorithm,expected_6dp,single_hex"
    For Each pair In pairs
        For Each mode In modes
            score = IsSimilar(CStr(pair(0)), CStr(pair(1)), CStr(mode))
            Print #channel, CsvQuote(CStr(pair(0))) & "," & _
                CsvQuote(CStr(pair(1))) & "," & CsvQuote(CStr(mode)) & "," & _
                CsvQuote(Format$(score, "0.000000")) & "," & CsvQuote(SingleHex(score))
        Next mode
    Next pair
    Close #channel
    Debug.Print outputPath
    Exit Sub
Failed:
    Close #channel
    Err.Raise Err.Number, "ExportPythonParityCases", Err.Description
End Sub
