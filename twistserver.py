#!/usr/bin/python

from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

GPIO.output(5, 1)
GPIO.output(7, 1)
GPIO.output(8, 1)

class lampAPI(Resource):
   def render_GET(self, request):
            if 'light' in request.args:
                        if request.args['light'][0] == "on":
                                GPIO.output(5, 0)
                                return "Light on"
                        elif request.args['light'][0] == "off":
                                GPIO.output(5, 1)   
                                return "Light off"
	    if 'fan' in request.args:
                        if request.args['fan'][0] == "on":
                                GPIO.output(7, 0)
                                return "Fan on"
                        elif request.args['fan'][0] == "off":
                                GPIO.output(7, 1)
                                return "Fan off"
	    if 'tv' in request.args:
                        if request.args['tv'][0] == "on":
                                GPIO.output(8, 0)
                                return "TV on"
                        elif request.args['tv'][0] == "off":
                                GPIO.output(8, 1)
                                return "TV off"
   
try:	
	root = Resource()
	root.putChild("API", lampAPI())
	factory = Site(root)
	reactor.listenTCP(11, factory) 
	reactor.run()

except KeyboardInterrupt:
	GPIO.cleanup()
	print "Exiting...."
	sys.exit(0)
