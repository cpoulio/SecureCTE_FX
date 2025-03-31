# $language = "python"
# $interface = "1.0"

import crt

def main():
    try:
        # Connect to the saved session
        crt.Session.Connect("/S MyClinicSession")

        # Confirm connection
        if crt.Session.Connected:
            crt.Dialog.MessageBox("Connected to MyClinicSession")

        # Change permissions on the remote file
        crt.Screen.Send("chmod 755 /home/user/myscript.sh\n")
        crt.Screen.WaitForString("$")

        # Rename the file
        crt.Screen.Send("mv /home/user/myscript.sh /home/user/myscript_renamed.sh\n")
        crt.Screen.WaitForString("$")

        # Run the renamed script
        crt.Screen.Send("bash /home/user/myscript_renamed.sh\n")
        crt.Screen.WaitForString("$")

        # Notify that the script executed successfully
        crt.Dialog.MessageBox("Commands executed successfully!")

    except Exception as e:
        crt.Dialog.MessageBox("Error: " + str(e))

main()
