import sys
import time
from datetime import datetime
from datetime import timedelta
import os
from gpiozero import MotionSensor

global pir,firstalarm, difference, whnwake, fwhnwake, tomalarm

pir = MotionSensor(pin=11)

def ringalarm(almtime):
	while True:
		ntime = datetime.now().replace(microsecond=0)
		alrmtime = almtime+timedelta(days=1)
		print ntime
		if ntime == alrmtime:
			print "Alarm Buzzz!!!"
			os.system("play alarm.mp3")
			os.system("play alarmtone.mp3")
			fwhnwake()
		time.sleep(1)

def tomalarm(whenwake):
	while True:
		difference = whenwake - setalarm
		fmin = timedelta(minutes=5)
		if difference>fmin:
			print "greater"
			alarmtime = setalarm - difference
			ringalarm(alarmtime)
		else:
			print "not greater"
			rngalm = setalarm+timedelta(days=1)
			print "Alarm set for "+str(rngalm)
			ringalarm(rngalm)
def fwhnwake():
	while True:
		if pir.motion_detected:
			haveuwoke = "y"
		if haveuwoke == "y":
			whnwake = datetime.now().replace(microsecond=0)
			tomalarm(whnwake)
		else:
			os.system("play alarm.mp3")
		
def firstalarm(setalrm):
	while True:
		print datetime.now().strftime("%I:%M %p")
		if setalrm == datetime.now().strftime('%I:%M %p'):
			print "Alarm Buzzer"
			os.system("play alarm.mp3")
			os.system("play alarmtone.mp3")
			global setalarm
			setalarm = datetime.now().replace(microsecond=0)
			fwhnwake()
		time.sleep(1)
def fsetalarm():
	a = sys.argv[1]
	b = sys.argv[2]
	setalm = a+" "+b
	firstalarm(setalm)
fsetalarm()
