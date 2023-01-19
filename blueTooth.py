import RPi.GPIO as GPIO
import time
import bluetooth

pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

host = ""
port = 1

server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print("Bluetooth Socket Created")

try:
	server.bind((host,port))
	print("Bluetooth Binding Completed")
except:
	print("Bluetooth Binding Failed")

server.listen(1)
client, address = server.accept()
print("Connected to : ",address)
print("Client is : ",client)

try:
	while True:
		data = client.recv(1024)
		print(data)
		
		if data == '1':
			GPIO.output(pin, True)
			send_data = "Light is ON"
		elif data == '0':
			GPIO.output(pin, False)
			sned_data = "Light is OFF"
		else:
			send_data = "Type 1 or 0"
		
		client.send(send_data)
except:
	GPIO.cleanup()
	client.close()
	server.close()
