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

	SSHelper required 3 arguments:
	The IP address/dns name of the remote host
	The Username of the remote host
	The password of the remote host

	Examples:
	./SSHelper 127.0.0.1 admin supersecretpassword
	python SSHelper.py my.dns.com p@ssW0rd	
		""")

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(
			paramiko.AutoAddPolicy())
ssh.connect('127.0.0.1', username= "joseph", password= "")

data=""
while data is not "8":

	data = raw_input("SSH> ")
	stdin, stdout, stderr = ssh.exec_command(data)
	type(stdin)

	for lines in stdout.readlines():
		print lines

