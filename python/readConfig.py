#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import ConfigParser
cfg = ConfigParser.ConfigParser()
cfg.read("/home/pi/.config/GM_software/lin-guider.conf")
for section in cfg.sections():
			print
			print "================ "+section+" ================"
			for item in cfg.items(section):
				print item
