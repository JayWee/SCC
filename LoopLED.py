import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO:OUT)

state = True
while True:
	GPIO.output(18,True)
	time.sleep(1)
	GPIO.output(18,False)
	time,sleep(1)
	
