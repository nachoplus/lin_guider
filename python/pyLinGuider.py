#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from config import *
import sys
import socket
import struct
import time
import signal
import subprocess



class linguider:
	def __init__(self):
		self.startLinGuider()
		self.RUN=True
		#self.watchlog()
		self.CONNECTED=False
		while not self.CONNECTED:
			self.initConn()
			time.sleep(1)
		self.commands = {'GET_VER':1,'SET_GUIDER_SQUARE_POS':2,'SAVE_FRAME':3,'DITHER':4,'DITHER_NO_WAIT_XY':5,\
		'GET_DISTANCE':6,'SAVE_FRAME_DECORATED':7,'GUIDER':8,'GET_GUIDER_STATE':9,'SET_GUIDER_OVLS_POS':1,\
		'SET_GUIDER_RETICLE_POS':11,'FIND_STAR':12,'SET_DITHERING_RANGE':13,'GET_RA_DEC_DRIFT':14,'CALIBRATE':15,\
		'EXIT':16,'SET_VIDEO_GAIN':17}
		signal.signal(signal.SIGINT, self.signal_handler)



	def test(self):
		print self.send(self.commands['FIND_STAR'])
		print self.send(self.commands['CALIBRATE'])
		print self.send(self.commands['SET_VIDEO_GAIN'],'55')
		print self.send(self.commands['GUIDER'],'start')

	def initConn(self):
		HOST = 'localhost' 
		PORT = 5656 
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_address = (HOST, PORT)
		try:
			self.sock.connect(server_address)
			self.CONNECTED=True
		except:
			self.CONNECTED=False
			print "FAIL TO CONNECT TO LINGUIDER. IS STARTED?"

	def send(self,cmd,arg=''):
		l=len(arg)
		values = (2, cmd, l)
		packer = struct.Struct('HHL')
		packed_data = packer.pack(*values)
		print "Sending ",cmd
		try:
			self.sock.sendall(packed_data)
			if (l > 0):
				self.sock.sendall(arg)
			res=self.sock.recv(8)
			(wrp, cmd, l) = packer.unpack(res);
			if (l > 0):
				return self.sock.recv(l);
		except:
			print "Socket FAIL"

	@threaded
	def image(self,every=1):
		while self.RUN:
			print self.send(self.commands['SAVE_FRAME'],'linguider')
			time.sleep(every)
 

	def signal_handler(self,signal, frame):
		print 'You pressed Ctrl+C!'
		print self.send(self.commands['EXIT'])
		print "Wait for clossing..."
		self.sock.close()
		#self.linguider.kill()
		self.RUN=False




	def startLinGuider(self):
		self.linguider = subprocess.Popen(['../lin_guider'], 
                        stdout=subprocess.PIPE,
			bufsize=0
		        )



	@threaded
	def watchlog(self):
		while self.RUN:
		    line=self.linguider.stdout.read()
		    if ('SRV: listening on TCP port 5656' in line):
			print "LINGUIDER SERVER STARTED"
		    if ('ERROR: video thread: read_frame error' in line):
			print "VIDEO DEVICE FAIL"
		    print line





if __name__ == '__main__':
	lg=linguider()
	lg.test()
	lg.image(2)
	while lg.RUN:
		time.sleep(1)
	
