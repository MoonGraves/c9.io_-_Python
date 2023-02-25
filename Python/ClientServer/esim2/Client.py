import socket 

# take the server name and port name 
host = 'local host'
port = 5000

# create a socket at server side 
# using TCP / IP protocol 
s = socket.socket(socket.AF_INET, 
				socket.SOCK_STREAM) 

# bind the socket with server 
# and port number 
s.bind(('192.168.1.101', port)) 

# allow maximum 1 connection to 
# the socket 
s.listen(1) 

# wait till a client accept 
# connection 
c, addr = s.accept() 

# display client address 
print("CONNECTION FROM:", str(addr)) 

# send message to the client after 
# encoding into binary string 
c.send(b"Happy New Year, Fellas !! \n + Olen Tantta xD") 

msg = "New year , old me.... "
c.send(msg.encode()) 

# disconnect the server 
c.close() 
