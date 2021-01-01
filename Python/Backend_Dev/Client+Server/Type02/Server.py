import socket 

# take the server name and port name 

host = 'local host'
port = 5000

# create a socket at client side 
# using TCP / IP protocol 
s = socket.socket(socket.AF_INET, 
				socket.SOCK_STREAM) 

# connect it to server and port 
# number on local computer & and same ip address as client
# NO gateway
s.connect(('127.0.0.1', port)) 

# receive message string from 
# server, at a time 1024 B 
msg = s.recv(2048) 

# repeat all message, what it's coming from client as received them
while msg: 
	print('Recived:' + msg.decode()) 
	msg = s.recv(2048) 

# disconnect the client 
s.close() 
