import RPi.GPIO as GPIO
import time

pin1 = 26
pin2 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.IN)
GPIO.setup(pin2, GPIO.OUT)

try:
	while True:
		if(GPIO.input(pin1) == 1):
			GPIO.output(pin2, False)
		else:
			GPIO.output(pin2, True)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit()
