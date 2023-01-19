import RPi.GPIO as GPIO
import time
import csv
import MySQLdb
import datetime

GPIO.setwarnings(False)
pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

db = MySQLdb.connect(host="localhost",user="EC086",passwd="temp@123",db="temp");
cur = db.cursor()

try:
	while True:
		degree = GPIO.input(pin)
		timenow = datetime.datetime.utcnow()
		print(degree)
		
		cur.execute('''INSERT INTO Sensorstats(date_time,irsensordata) VALUES(%s,%s);''',(timenow,degree));
		db.commit()
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit()
