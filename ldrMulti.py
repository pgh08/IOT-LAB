import RPi.GPIO as GPIO
import time

ldr_pin = 12
light_pin1 = 13
light_pin2 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(ldr_pin, GPIO.IN)
GPIO.setup(light_pin1, GPIO.OUT)
GPIO.setup(light_pin2, GPIO.OUT)

try:
	while True:
		if(GPIO.input(ldr_pin) == 1):
			GPIO.output(light_pin1, True)
			GPIO.output(light_pin2, False)
		else:
			GPIO.output(light_pin1, False)
			GPIO.output(light_pin2, True)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit()
