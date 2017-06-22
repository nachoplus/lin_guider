#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from config import *
import sys
import socket
import struct
import time
import signal
import subprocess

class linguiderUDP:
	def __init__(self):
		signal.signal(signal.SIGINT, self.signal_handler)
		self.initConn()
		self.RUN=True
		self.run()

	def initConn(self):
		UDP_IP = "localhost"
		UDP_PORT = 5656
		self.sock_UDP = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
		self.sock_UDP.bind((UDP_IP, UDP_PORT))
	def recv(self):
		try:
			data, addr = self.sock_UDP.recvfrom(24) # buffer size is 1024 bytes
		except:
			print "UDP server fail"
			data=""
		return data

	def signal_handler(self,signal, frame):
		print 'You pressed Ctrl+C!'
		self.sock_UDP.close()
		self.RUN=False

	@threaded
	def run(self):
		while self.RUN:
			print self.recv()





if __name__ == '__main__':
	lgUDP=linguiderUDP()
	while lgUDP.RUN:
		time.sleep(1)
	
