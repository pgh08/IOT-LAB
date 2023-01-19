import RPi.GPIO as GPIO
import time

pin1 = 18
pin2 = 22
pin3 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)

try:
	for i in range (0,8):
		if i == 0:
			GPIO.output(pin1, False)
			GPIO.output(pin2, False)
			GPIO.output(pin3, False)
		if i%2 != 0:
			GPIO.output(pin1, True)
		if i%4 == 2 or i%4 == 3:
			GPIO.output(pin2, True)
		if i%8 == 4 or i%8 == 5 or i%8 == 6 or i%8 == 7:
			GPIO.output(pin3, True)
		time.sleep(2)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit()
