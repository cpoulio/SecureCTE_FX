@echo off
REM Upload the file
sfxcl C:\path\to\file.txt /S "MyClinicSession" /home/user/clinic_directory/

REM Run the script remotely
SecureCRT.exe /SCRIPT "C:\path\to\RunCommandOnRemote.py"
