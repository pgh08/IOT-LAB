import RPi.GPIO as GPIO
import time

ldr_pin = 13
light_pin = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(ldr_pin, GPIO.IN)
GPIO.setup(light_pin, GPIO.OUT)

try:
	while True:
		if(GPIO.input(ldr_pin) == 1):
			GPIO.output(light_pin, True)
		else:
			GPIO.output(light_pin, False)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit()
