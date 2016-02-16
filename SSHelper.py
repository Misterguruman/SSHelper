#!/usr/bin/env python
import paramiko
import sys

class hostInstance():
	def __init__(self, ip, usr, pwd):
		self.ip = ip
		self.usr = usr
		self.pwd = pwd
		self.data = ""

	def createConnection(self):
		self.ssh = paramiko.SSHClient()
		self.ssh.set_missing_host_key_policy(
			paramiko.AutoAddPolicy())
		self.ssh.connect(self.ip, username = self.usr, password= self.pwd)
	'''
	DEBUGGING CODE!
		self.stdin, self.stdout, self.stderr = self.ssh.exec_command('ifconfig -a')

		for lines in self.stdout.readlines():
			print lines
	'''
	def basic_shell(self):
		#ip, usr, pwd = sys.argv[2:5]
		#client = hostInstance(ip, usr, pwd)
		#client.createConnection()

		self.ssh.invoke_shell(term='vt100', width=80, height=24, width_pixels=100, height_pixels=100)
		while self.data != 'q':
			self.data = raw_input('>')
			self.stdin, self.stdout, self.stderr = self.ssh.exec_command(self.data)

			for line in self.stdout.readlines():
				print line
		

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

def inputHosts():
	hostFile = open(sys.argv[2])
	hosts = []
	for creds in hostFile.readlines():
		ip, usr, pwd = creds.rstrip().split(',')
		hosts.append(hostInstance(ip, usr, pwd))

	for host in hosts:
		host.createConnection()


clientInst = hostInstance('127.0.0.1','joseph','J$Money9')
clientInst.createConnection()
clientInst.basic_shell()
