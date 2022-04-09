import os

content = "#!/bin/bash\n\necho \"Why hello there red team! You are being kicked off. Better luck next time :(\"\nwall \"RED TEAM\"\ntemp=$(tty)\npkill -9 -t ${temp:5}"

def update(command):
    if os.path.exists("/bin/"+command):
        os.rename("/bin/"+command, "/bin/."+command)
        with open("/bin/"+command, "w") as file:
            file.write(content)

update("ls")
update("cat")
update("pwd")
update("nano")
update("vi")
update("vim")
update("whoami")
update("rm")
update("mv")
update("wget")
update("curl")
