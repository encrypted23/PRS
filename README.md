# PRS - Python reverse shell
The reverse shell for python

## Description
A reverse shell written in python 3.This payload works with netcat and only netcat. Drop the shell any where while having netcat listing.

## Instructions
Be sure to change the following:
```
 host = "Your ip"  # Put your machines IP here 
 port = 4444       # You can change the port if you would like, this is just a defult one
 ```
 ## Installation
 ```
 git clone https://github.com/hackerman234/PRS.git
 chmod +x reverse_shell.py
 ```
 ## Netcat
 Heres a guide how to use netcat
 ```
 nc -lvp <the port you want to listen on>
 ```
 
 ## Authors
 @hackerman234
