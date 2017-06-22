#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import ConfigParser
import threading
cfg = ConfigParser.ConfigParser()
cfg.read("/home/pi/.config/GM_software/lin-guider.conf")
for section in cfg.sections():
			print
			print "================ "+section+" ================"
			for item in cfg.items(section):
				print item

def threaded(fn):
    def wrapper(*args, **kwargs):
        t1=threading.Thread(target=fn, args=args, kwargs=kwargs)
	t1.start()
	return t1
    return wrapper

