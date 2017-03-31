#!/usr/bin/python
import MySQLdb
import time
import dht11
import sys
import RPi.GPIO as GPIO
from gpiozero import MotionSensor

GPIO.setmode(GPIO.BOARD)

db = MySQLdb.connect("localhost","root","manuvava","pixer")
cursor = db.cursor()
instance = dht11.DHT11(pin=13)

try:
	while True:
		result=instance.read()
		if result.is_valid():
			temp = result.temperature
			humid = result.humidity
			time.sleep(5)
			print "Temperaure :",temp
			print "Humidity :",humid
			sql = "UPDATE sensors SET Temperature=%s WHERE Name='Alok N'" % temp
			sqll = "UPDATE sensors SET Humidity=%s WHERE Name='Alok N'" % humid
			#motionsql = "UPDATE sensors SET Motion=%s WHERE Name='Alok'" % status
			cursor.execute(sql)
			cursor.execute(sqll)
			db.commit()
except KeyboardInterrupt:
	print "Thanks for using Temperature Server. Bye!"
	db.close()
	GPIO.cleanup()
	sys.exit(0)
db.close()
GPIO.cleanup()
