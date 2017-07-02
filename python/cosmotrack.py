#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import  pyLinGuider
import remi.gui as gui
from remi import start, App
import signal
import time
import io

import PIL.Image


class PILImageViewverWidget(gui.Image):
    def __init__(self, pil_image=None, **kwargs):
        super(PILImageViewverWidget, self).__init__("/res/logo.png", **kwargs)
        self._buf = None

    def load(self, file_path_name):
        pil_image = PIL.Image.open(file_path_name)
        self._buf = io.BytesIO()
        pil_image.save(self._buf, format='png')
        self.refresh()

    def refresh(self):
        i = int(time.time() * 1e6)
        self.attributes['src'] = "/%s/get_image_data?update_index=%d" % (id(self), i)

    def get_image_data(self, update_index):
        if self._buf is None:
            return None
        self._buf.seek(0)
        headers = {'Content-type': 'image/png'}
        return [self._buf.read(), headers]

class cosmotrack(App,pyLinGuider.linguider):
    def __init__(self, *args):
        App.__init__(self,*args)
        pyLinGuider.linguider.__init__(self)
	#signal.signal(signal.SIGINT, self.end)



    def main(self):
        container = gui.VBox(width = 600, height = 800)
        self.lbl = gui.Label('Hello world!')
        self.btFindStar = gui.Button('FIND_STAR')
        self.btCalibrate = gui.Button('CALIBRATE')
        self.btStartGuide = gui.Button('START GUIDE')
        self.btStopGuide = gui.Button('STOP GUIDE')
        self.gain = gui.Slider(10, 0, 100, 5, width=200, height=20, margin='10px')
        self.gain.set_on_change_listener(self.slider_changed)
	self.image_widget = PILImageViewverWidget(width=200, height=200)

        # setting the listener for the onclick event of the button
        self.btFindStar.set_on_click_listener(self.on_button_pressed)
        self.btCalibrate.set_on_click_listener(self.on_button_pressed)
        self.btStartGuide.set_on_click_listener(self.on_button_pressed)
        self.btStartGuide.set_on_click_listener(self.StartGuide)
        self.btStopGuide.set_on_click_listener(self.StopGuide)

        # appending a widget to another, the first argument is a string key
        container.append(self.image_widget)
        container.append(self.lbl)
        container.append(self.btFindStar)
        container.append(self.btCalibrate)
        container.append(self.btStartGuide)
        container.append(self.btStopGuide)
        container.append(self.gain)

	self.image()
	self.image_widget.load('/home/pi/linguider.png')
        # returning the root widget
        return container

    # listener function
    def on_button_pressed(self, widget):
	cmd=self.commands[widget.get_text()]
        self.lbl.set_text(widget.get_text()+':'+self.send(cmd))

    def slider_changed(self,widget,value):
	cmd=self.commands['SET_VIDEO_GAIN']
        self.lbl.set_text('GAIN:'+self.send(cmd,value))

    def StartGuide(self,widget):
	cmd=self.commands['GUIDER']
        self.lbl.set_text('GUIDER:'+self.send(cmd,'start'))

    def StopGuide(self,widget):
	cmd=self.commands['GUIDER']
        self.lbl.set_text('GUIDER:'+self.send(cmd,'stop'))


if __name__ == '__main__':
	# starts the webserver
	start(cosmotrack,address='0.0.0.0', port=8081)
