import socket
localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP,localPort))
print("UDP server up and running")

while True:
	byteAddressPair = UDPServerSocket.recvfrom(bufferSize)
	message = byteAddressPair[0]
	address = byteAddressPair[1]
	clientmsg = "Message from client : {}".format(message)
	clientIP = "Client IP is : {}".format(address)
	print(clientmsg)
	print(clientIP)
	msgFromServer = input('Enter the message : ')
	byteToSend = str.encode(msgFromServer)
	
	UDPServerSocket.sendto(byteToSend,address)
