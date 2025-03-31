# RunMultipleCommands.py
import crt

def main():
    # Connect to the saved session
    crt.Session.Connect("/S MyClinicSession")
    
    # Change permissions
    crt.Screen.Send("chmod 755 /home/user/myscript.sh\n")
    crt.Screen.WaitForString("$")

    # Rename the file
    crt.Screen.Send("mv /home/user/myscript.sh /home/user/myscript_renamed.sh\n")
    crt.Screen.WaitForString("$")

    # Run the script
    crt.Screen.Send("bash /home/user/myscript_renamed.sh\n")
    crt.Screen.WaitForString("$")

main()
