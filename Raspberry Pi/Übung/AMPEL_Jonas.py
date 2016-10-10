import RPi.Gpio as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(2,GPIO.IN)

state = True
#Ampel
#Rot Phase Fußgänger
while True:
	print "Stehenbleiben"
	GPIO.output(27,GPIO.HIGH)
	GPIO.output(22,GPIO.HIGH)

	#Wechsel auf Grün
	if GPIO.input(2) == GPIO.HIGH:
		time.sleep(0.5)
		GPIO.output(27,GPIO.LOW)
		GPIO.output(18,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(18,GPIO.LOW)
		GPIO.output(17,GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(22,GPIO.LOW)
		GPIO.output(23,GPIO.HIGH)
		time.sleep(10)

	#Wechsel auf Rot
	GPIO.output(23,GPIO.LOW)
	GPIO.output(22,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(18,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(17,GPIO.LOW)
	GPIO.output(18,GPIO.LOW)
	GPIO.output(27,GPIO.HIGH)