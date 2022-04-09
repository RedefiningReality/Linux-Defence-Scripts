import argparse, sys

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--setup", action="store_true", help="sets default shell to bash - be sure to check /etc/passwd file for other shells before running")
parser.add_argument("-u", "--user", help="the name of the user to save command history of")

args = parser.parse_args(sys.argv[1:])

import os
import pwd, grp

if args.setup:
    with open("/etc/passwd") as file:
        for line in file:
            if ("nologin" not in line) and ("sync" not in line) and ("halt" not in line) and ("shutdown" not in line) and ("false" not in line):
                ID = line.split(":")[2]
                user = line.split(":")[0]
                
                shell = "/bin/bash "
                if int(ID) < 1000 and int(ID) != 0:
                    shell = "/sbin/nologin "
                os.system("usermod -s "+shell+user)
    os.system("rm /bin/zsh ; rm /bin/dash")
    os.system("ln -s /bin/bash /bin/sh.bash ; mv /bind/sh.bash /bin/sh")

if args.user:
    home_dir = "/home/"+args.user
    if args.user == "root":
        home_dir = "/root"
    
    hist_dir = "/opt/.kernel/"+args.user
    with open(home_dir+"/.bashrc", "a") as file:
        file.write("\n")
        file.write("export HISTFILE="+hist_dir+"/.history\n")
        file.write("shopt -s histappend\n")
        file.write("export PROMPT_COMMAND=\"history -a ; history -r\"\n")
        file.write("export HISTSIZE=\n")
        file.write("export HISTFILESIZE=")
    
    hist_dir = "/opt/.kernel/"+args.user
    os.makedirs("/opt/.kernel", mode=0o600, exist_ok=True)
    
    os.makedirs(hist_dir, mode=0o600, exist_ok=True)
    uid = pwd.getpwnam(args.user).pw_uid
    gid = grp.getgrnam(args.user).gr_gid
    os.chown(hist_dir, uid, gid)
