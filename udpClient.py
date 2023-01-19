import socket
import time
bufferSize = 1024

msgFromClient = "I am ready to chat"
byteToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1",20001)
UDPClientSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
	
while True:
	UDPClientSocket.sendto(byteToSend,serverAddressPort)
	msgFromServer = UDPClientSocket.recvfrom(bufferSize)
	msg = "Message from server {}".format(msgFromServer[0])
	print(msg)
	msgFromClient = input('Replay to server : ')
	byteToSend = str.encode(msgFromClient)
