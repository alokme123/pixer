#!/usr/bin/python

import time
import subprocess
import sys
import os
from datetime import datetime 
import RPi.GPIO as GPIO
from threading import Thread
import MySQLdb

global recog,speak

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
light = 5
fan = 7
TV = 8
bout = 11
bin = 13
fake = 3

GPIO.setup(light, GPIO.OUT)
GPIO.setup(fan, GPIO.OUT)
GPIO.setup(TV, GPIO.OUT)
GPIO.setup(fake, GPIO.OUT)
GPIO.output(fake, 0)
GPIO.output(TV, 1)
GPIO.output(fan, 1)
GPIO.output(light, 1)

db = MySQLdb.connect("localhost","root","manuvava","pixer")
cursor = db.cursor()

def recog():
	p = subprocess.Popen(['./speech-recog.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        global out,err
        out, err = p.communicate()
        out.replace('"', '')
        print out
	hello()

def speak(wts):
        os.system("./ttsspeech.sh "+wts)

def music():
	os.system("find /home/pi/Music -type f | sort -R | xargs -I + play +")
	hello()

def remind(out):
	if 'exam' in out:
		prefval = 10
		speak("OK. I'll remind you")
	elif 'meeting' in out:
		prefval = 8
	elif 'paper' in out:
		prefval = 9
	elif 'submission' in out:
		prefval = 9
	elif 'party' in out:
		prefval = 4
		speak("Hmm... Let me check...")
	        time.sleep(0.5)
        	speak("Oh! I am sorry, you have your exams on 24th")
	elif 'tv' in out:
		prefval = 4
	#sql = "INSERT INTO Reminder(Name, PrefVal) VALUES('%s','%d')" % thing,prefval
	#cursor.execute(sql)
	#print sql
		
def hello():
	if 'weather' in out:
		os.system("python getweather.py")
	elif "thank you" in out:
		speak("You are welcome!")
	elif 'music' in out:
		global background_thread
                background_thread = Thread(target=music)
                background_thread.start()
	elif 'song' in out:
		global background_thread
		background_thread = Thread(target=music)
		background_thread.start()
	elif 'switch' in out:
		if "light" in out:
			if "on" in out:
				speak("OK! Switching on Light..")
				GPIO.output(light, 0)
			elif "off" in out:
				speak("OK! Switching off Light..")
				GPIO.output(light, 1)
		elif "fan" in out:
			if "on" in out:
				speak("OK! Switching on Fan..")
				GPIO.output(fan, 0)
			elif "off" in out:
				speak("OK! Switching off Fan..")
				GPIO.output(fan, 1)
		elif "TV" in out:
			if "on" in out:
				speak("OK! Switching on TV..")
				GPIO.output(TV, 0)
			elif "off" in out:
				speak("OK! Switching off TV..")
				GPIO.output(TV, 1)
		elif "everything"in out:
			if "on" in out:
				speak("OK! Switching on Everything..")
				GPIO.output(light, 0)
				GPIO.output(fan, 0)
				GPIO.output(TV, 0)
			elif "off" in out:
				speak("OK! Switching off everything")
				GPIO.output(light, 1)
				GPIO.output(fan, 1)
				GPIO.output(TV, 1)		
	elif 'turn' in out:
		os.system("python control.py "+out)
	elif 'how much' in out:
		os.system("python calc.py "+out)
	elif 'job' in out:
		speak("Thank You! Aloak")
	elif 'time' in out:
		ntime = datetime.now().strftime('%I:%M %p')
		speak("It is "+str(ntime))
	elif 'set the alarm' in out:
		numbers = [int(s) for s in out.split() if s.isdigit()]
		#nos = numbers.replace('[',"")
		#noss = nos.replace('[',"")
		#alm = "0"+str(noss)+":00 AM"
		speak("Ok! Alarm set for 6:00 AM")
		os.system("python intelm.py "+alm)
	elif 'stop' in out:
		system.exit(0)
	elif 'introduce' in out:
		speak("I am Pixer. An Artificially Intelligent System. I can talk to you, control your house,set Alarms, Sing you songs and much more being added. I am created by Aloak. Thank you aloak...")
	elif 'exam' in out:
		os.system("./ttsspeech.sh Ok! I will remind you")
	else:
		print "Nothing said"
	
speak("Hello")
while True:
	recog()
