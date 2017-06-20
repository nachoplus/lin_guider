#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import config
import sys
import socket
import struct

class linguider:
	def __init__(self):
		self.initConn()
		pass
	def test(self):
		pass
	def initConn(self):
		HOST = 'localhost' 
		PORT = 5656 
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_address = (HOST, PORT)
		self.sock.connect(server_address)
	def send(self,cmd,arg):
		l=len(arg)
		values = (2, cmd, l)
		packer = struct.Struct('HHL')
		packed_data = packer.pack(*values)
		self.sock.sendall(packed_data)
		if (l > 0):
			self.sock.sendall(arg)
		print self.sock.recv(24)
	

if __name__ == '__main__':
	lg=linguider()
	lg.send(8,'start')
