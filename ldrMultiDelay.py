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
			time.sleep(1)
			GPIO.output(light_pin2, False)
			time.sleep(2)
		else:
			GPIO.output(light_pin1, False)
			time.sleep(1)
			GPIO.output(light_pin2, True)
			time.sleep(2)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit()
