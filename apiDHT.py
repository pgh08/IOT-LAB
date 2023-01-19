import time
import board
import thingspeak
import adafruit_dht
import os
import subprocess

channel_id = 1823121
write_key = 'GFDSGSDFGDGDFGDFG'

multi_run = subprocess.run(["killall","libgpio.pulsein"])

sensor = adafruit_dht.DHT11(board.D25)

def measure(channel):
	try:
		temperature = sensor.temperature
		humidity = sensor.humidity
		if humidity is not None and temperature is not None:
			print('Temperature : {0:0.1f}*C Humidity : {1:0.1f}%'.format(humidity,temperature))
		else;
			print('Did not receive any reading from sensor. Please check!')
		
		response = channel.update({'field1':temperature, 'field2':humidity})
		
	except:
		time.sleep(5)
		measure(channel)
		
if __name__ == '__main__':
	try:
		while True:
			channel = thingspeak.Channel(id=channel_id,api_key=write_key)
			measure(channel)
			time.sleep(5)
	except KeyboardInterrupt:
		kill()
