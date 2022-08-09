import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(BCM)
GPIO.setup(14,input)

while True:
	if(GPIO.input(14) == HIGH):
		print('Object is detected')
	else:
		print('Object is not detected')
