#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from pyLinGuider import *


if __name__ == '__main__':
	lg=linguider()
	lg.test()
	lg.image(1)
	lgUDP=linguiderUDP()
	lgUDP.run()
