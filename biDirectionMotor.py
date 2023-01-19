import RPi.GPIO as GPIO
import time

pin1 = 18
pin2 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

try:
	while True:
		GPIO.output(pin1, True)
		time.sleep(2)
		GPIO.output(pin2, True)
		time.sleep(2)
		GPIO.output(pin1, False)
		time.sleep(2)
		GPIO.output(pin2, False)
		time.sleep(2)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit()
