#!/usr/bin/env python
# Echo client program
import socket
import sys

HOST = '127.0.0.1'    # The remote host (This needs to be changed appropriately)
PORT = 11710          # The same port as used by the server
MAXDATASIZE = 1024
#Do Exception Handling here
try:
	#Getting an IP version 4 and TCP Socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, (value, message):
	print "Could not open socket" + message
	sys.exit(1)
try: 
	#Trying TCP's 3 Way Handshake
	s.connect((HOST, PORT))
except socket.error, (value,message):
	print "Could not connect" + message
	sys.exit(1)
print "Connected to Server!!"
while 1:
	#Accepts user input
	datatosend = raw_input("Enter a String:")
	#if user presses exit, client closes the connection
	if datatosend == "exit":
		s.close()
		break
	if len(datatosend) > 0:
		s.sendall(datatosend)
		data = s.recv(MAXDATASIZE)
		print "Received from Server- ", data
	else:
		print "Cannot Send Empty String!!type exit to stop"
		continue
