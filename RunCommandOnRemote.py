# how to run script SecureCRT.exe /SCRIPT "C:\path\to\RunCommandOnRemote.py"
# RunCommandOnRemote.py
import crt

def main():
    # Connect to the saved session
    crt.Session.Connect("/S MyClinicSession")
    
    # Send the command to the remote server
    crt.Screen.Send("bash /home/user/clinic_directory/myscript.sh\n")
    
    # Wait for the command to complete
    crt.Screen.WaitForString("$")

main()
