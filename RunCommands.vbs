' $language = "VBScript"
' $interface = "1.0"

Sub Main
    On Error Resume Next

    ' Connect to the saved session
    crt.Session.Connect "/S MyClinicSession"
    If crt.Session.Connected Then
        crt.Dialog.MessageBox "Connected to MyClinicSession"
    Else
        crt.Dialog.MessageBox "Failed to connect to MyClinicSession"
        Exit Sub
    End If

    ' Change permissions on the remote file
    crt.Screen.Send "chmod 755 /home/user/myscript.sh" & vbCr
    crt.Screen.WaitForString "$"

    ' Rename the file
    crt.Screen.Send "mv /home/user/myscript.sh /home/user/myscript_renamed.sh" & vbCr
    crt.Screen.WaitForString "$"

    ' Run the renamed script
    crt.Screen.Send "bash /home/user/myscript_renamed.sh" & vbCr
    crt.Screen.WaitForString "$"

    ' Check for errors
    If Err.Number <> 0 Then
        crt.Dialog.MessageBox "Error occurred: " & Err.Description
        Err.Clear
    Else
        crt.Dialog.MessageBox "Commands executed successfully!"
    End If
End Sub
