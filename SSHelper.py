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

print_usage()
#Creating Client Instance
#ssh = paramiko.SSHClient()

#ssh.set_missing_host_key_policy(
#	paramiko.AutoAddPolicy())

#ssh.connect(ip, username=usr, password=pwd)
