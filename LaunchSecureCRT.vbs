Set WshShell = CreateObject("WScript.Shell")
' Run SecureCRT minimized
WshShell.Run """C:\Program Files\VanDyke Software\SecureCRT\SecureCRT.exe"" /SCRIPT ""C:\path\to\fdaa.vbs""", 7, False
