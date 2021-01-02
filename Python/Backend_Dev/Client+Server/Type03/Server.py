from socket import *

#Tässä sisältyy client1.py ja client2.py

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try :
        serversocket.bind(('localhost',8080)) #toimii 8000, 8080 tai 9000
        serversocket.listen(5)
        while(1):
            (clientsocket, address) = serversocket.accept()

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if ( len(pieces) > 0 ) : print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body><h2> WAU, TANTTA   <br> <p> Done </p> </h2></body></html>\r\n\r\n <b> asdfsdaf </b>"
            #\n newline & \r carriage return

            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt :
        print("\nShutting down...\n") #lopettaminen: ctrl + c
    except Exception as exc :
        print("Error:\n")
        print(exc)

    serversocket.close()

print('Access http://localhost:9000')
createServer()

#####CMD output####
#Access http://localhost:9000
#GET / HTTP/1.1
#
#
#
#
