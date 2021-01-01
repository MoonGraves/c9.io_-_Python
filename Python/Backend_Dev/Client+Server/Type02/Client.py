import socket 

#the server name and port name 
host = 'local host'
port = 5000

# using TCP/IP protocol
s = socket.socket(socket.AF_INET, 
				socket.SOCK_STREAM) 

# bind the socket with server & IP address only
# and port number 
s.bind(('127.0.0.1', port)) 

# allow maximum 1 connection to 
# the socket 
s.listen(1) 

# wait till a client accept it to connection 
c, addr = s.accept() 

# display client the address 
print("CONNECTION FROM:", str(addr)) 

# when connection is accepted, right away send the message right away
# from client after encoding
c.send(b"Happy New Year, Fellas !! 2021 ") 

msg = "New year , old me.... "
c.send(msg.encode()) 

# disconnect the server 
c.close() 
