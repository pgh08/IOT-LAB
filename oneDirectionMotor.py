import RPi.GPIO as GPIO
import time

pin1 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO.OUT)

try:
	while True:
		GPIO.output(pin1, True)
		time.sleep(2)
		GPIO.output(pin1, False)
		time.sleep(2)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit()
