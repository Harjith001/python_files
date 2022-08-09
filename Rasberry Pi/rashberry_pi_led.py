import RPi.GPIO as GPIO
import time.sleep as sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #can be set to BOARD or BCM
GPIO.setup(8,GPIO.OUT,initial = true) #setting up gpio pins for output 

while True:
	GPIO.output(8,GPIO.HIGH)
	sleep(1)
	GPIO.output(8,GPIO.LOW)
	sleep(1)