#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import config
import sys
import socket
import struct

class linguider:
	def __init__(self):
		self.initConn()
		self.commands = {'GET_VER':1,'SET_GUIDER_SQUARE_POS':2,'SAVE_FRAME':3,'DITHER':4,'DITHER_NO_WAIT_XY':5,\
		'GET_DISTANCE':6,'SAVE_FRAME_DECORATED':7,'GUIDER':8,'GET_GUIDER_STATE':9,'SET_GUIDER_OVLS_POS':1,\
		'SET_GUIDER_RETICLE_POS':11,'FIND_STAR':12,'SET_DITHERING_RANGE':13,'GET_RA_DEC_DRIFT':14,'CALIBRATE':15,\
		'EXIT':16,'SET_VIDEO_GAIN':17}
		

	def initConn(self):
		HOST = 'localhost' 
		PORT = 5656 
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_address = (HOST, PORT)
		self.sock.connect(server_address)

		UDP_IP = "localhost"
		UDP_PORT = 5656
		self.sock_UDP = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
		self.sock_UDP.bind((UDP_IP, UDP_PORT))


	def send(self,cmd,arg=''):
		l=len(arg)
		values = (2, cmd, l)
		packer = struct.Struct('HHL')
		packed_data = packer.pack(*values)
		self.sock.sendall(packed_data)
		if (l > 0):
			self.sock.sendall(arg)
		res=self.sock.recv(8)
		(wrp, cmd, l) = packer.unpack(res);
		if (l > 0):
			return self.sock.recv(l);

	def image(self):
		for a in range(10):
			print lg.send(lg.commands['SAVE_FRAME'],'linguider')
			data, addr = self.sock_UDP.recvfrom(1024) # buffer size is 1024 bytes
			print "received message:", data






	

if __name__ == '__main__':
	lg=linguider()
	print lg.send(lg.commands['FIND_STAR'])
	#print lg.send(lg.commands['CALIBRATE'])
	print lg.send(lg.commands['SET_VIDEO_GAIN'],'55')
	print lg.send(lg.commands['GUIDER'],'start')
	#print lg.send(lg.commands['EXIT'])
	lg.image()

	
