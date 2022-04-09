#!/usr/bin/env python3

# Note: run with nohup ./monitor.py &

import subprocess, os
import time

old = ""

while True:
    # output = subprocess.check_output(["who","-l"])
    output = subprocess.check_output(["who"])
    output = str(output)
    if len(output) > len(old):
        print("New shell detected")
        new = output.split("\\n")[-2]
        os.system("echo \"NEW SHELL "+new+"\" | wall")
        old = output
    time.sleep(1)