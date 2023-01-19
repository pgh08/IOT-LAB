import RPi.GPIO as GPIO
import time

pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

try:
	while True:
		GPIO.output(pin, True)
		time.sleep(2)
		GPIO.output(pin, False)
		time.sleep(2)
except KeyboardInterrupt:
	#GPIO.cleanup() to clean up all the ports you’ve used. It only affects any ports you have set in the current program.
	GPIO.cleanup()
	exit()
