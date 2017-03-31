#!/usr/bin/python

from gpiozero import MotionSensor
import time
import MySQLdb

pir = MotionSensor(17)
db = MySQLdb.connect("localhost","root","manuvava","pixer")
cursor = db.cursor()

while True:
    status = "Not Motion"
    if pir.motion_detected:
	   print("Motion detected!")
    	   #status = "Motion detected"
           yquer = "UPDATE sensors SET Motion='Motion Detected' WHERE Name='Alok N'"
    	   cursor.execute(yquer)
	   db.commit()
    else:
    	   mquer = "UPDATE sensors SET Motion='No Motion' WHERE Name='Alok N'" 
           if cursor.execute(mquer):
		print "updated"
           db.commit()
#    time.sleep(1)
