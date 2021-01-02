import socket
#This is client1

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 8080)) #yhteys sama portti kuin serveri mitä siellä on määritetty

cmd = 'GET http://127.0.0.1/Client1.txt HTTP/1.0\r\n\r\n'.encode() #tyhjään välilehti joko avaan toi tai perus localhost:8080/client1.txt
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
