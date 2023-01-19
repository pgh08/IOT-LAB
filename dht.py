import time
import adafruit_dht
import board
import psutil

for proc in psutil.process_iter():
	if proc.name() = 'libgpio.pulsein' or proc.name() = 'libgpio.pulsei':
		proc.kill()
		
	sensor = adafruit_dht.DHT11(board.D4)
	
	while True:
		try:
			temperature = sensor.temperature
			humidity = sensor.humidity
			print('Temperature : {}*C Humidity : {}%'.format(temperature, humidity))
		except RuntimeError as error:
			print(error.args[0])
			time.sleep(2)
			continue
		except Exception as error:
			sensor.exit()
			raise error
			time.sleep(2)
			
