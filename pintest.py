import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
print " "
print "||||||||\\\\\\------ WELCOME TO GPIO PIN TESTER------//////||||||||"
print "[[[[[{{{{{\\\\\|||||---by NaySo Technologies---|||||/////}}}}}]]]]]"
print " "
def prog():
	pin = input("Which Pin do you want to use(According to Pin Number)? ")
	status = input("Input(1) or Output(2)?")
	if status == 1:
		read = raw_input("Start Reading Pin Input?(y/n)")
		if read == "y":
			inread(pin)
		elif read == "n":
			reload()
		else:
			inc = raw_input("Please Enter y/n: ")
			if inc == "y":
				inread()
			elif inc == "n":
				reload()
			else:
				print "Sorry!Can't Process output. Please try again! Thank you for using!"
				sys.exit(0)
	elif status == 2:
		stat = "GPIO.OUT"
		outs = input("Pin output High(1) or Low(0)?")
		pinout(outs, pin)
def inread(pin):
	try:
		GPIO.setup(pin, GPIO.IN)
		while True:
			print GPIO.input(pin)
			time.sleep(1)
	except KeyboardInterrupt():
		reload()
def reload():
	re = raw_input("Do you want to run the program again?(y/n) ")
	if re == "y":
		prog()
	elif re == "n":
		print "Thank you for using RPi GPIO Pins!Bye"
		sys.exit(0)
	else:
		an = raw_input("Please type y/n: ")
		if an == "y":
			prog()
		elif an == "n":
			print "Thank you for using RPi GPIO Pins!Bye"
			sys.exit(0)
def pinout(outs, pin):
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, outs)
	reload()
prog()
