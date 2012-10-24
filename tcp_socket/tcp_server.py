#!/usr/bin/env python
# Echo server program
import socket
import sys

HOST = ''                 #Like INADDR_ANY in C 
PORT = 11710              # Arbitrary non-privileged port
MAXDATASIZE = 1024
#Adding Error Handlings too
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, (value,message): 
	if s:
        	s.close()
   	print "Could not open socket: " + message
    	sys.exit(1)
try:
	s.bind((HOST, PORT))
except socket.error, (value,message):
	print "Bind Fails - Is your Port Busy??" + message
	sys.exit(1)
s.listen(5)
#Iterative server Loop
while 1:
	print "Waiting for client request"
	conn, addr = s.accept()
	print 'Connected by', addr
	#Receive data and send back to client till user presses exit 
	#in the client side
	while 1:
    		data = conn.recv(MAXDATASIZE)
		print "Received from client: ", data
    		if not data:	
			 print "Connection closed by client!!"
			 break
		#Multiple send will be done by sendall
    		conn.sendall(data)
	#Close Connection Socket
	conn.close()
s.close()
