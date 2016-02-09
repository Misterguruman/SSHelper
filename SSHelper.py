#!/usr/bin/env python
import paramiko
import sys

def print_usage():
	#Prints usage of SSHelper
	print("""
SSHelper Utility
--------------------------------------------
Author : Joseph Paul Langford
Version 0.1

Usage:

Default:
	Without additional arguments SSHelper acts as a basic shell,
	best for basic system commands that don't require changing directories.

Default SSHelper required 3 arguments:

The IP address/dns name of the remote host
The Username of the remote host
The password of the remote host

Examples:
./SSHelper 127.0.0.1 admin supersecretpassword
python SSHelper.py my.dns.com p@ssW0rd	
		""")
ip, usr, pwd = sys.argv[1:4]
print ip
print usr
print pwd

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(
			paramiko.AutoAddPolicy())
ssh.connect(ip, username= usr, password= pwd)

data=""

while data is not "8":

	data = raw_input("SSH> ")
	stdin, stdout, stderr = ssh.exec_command(data)
	type(stdin)

	for lines in stdout.readlines():
		print lines

