import socket
import datetime

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.101" #ONLY IP-osoite, EI yhdyskäytävä (gateway)
ADDR = (SERVER, PORT) #IP-address , port
#https://www.youtube.com/watch?v=3QiPPX-KeSc
#https://www.techwithtim.net/tutorials/socket-programming/

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

pvKk = datetime.datetime.now()

#(client) näkyy cmd:ssä tai muu komento tämmöinen tervehdys 
print("Welcome today is: " + (pvKk.strftime("%d %b %Y")))

#Sent sms 
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

#TÄSTÄ ALHAALTA OLEVAT ASIAT LÄHETTÄVÄT KOHTI SERVER:iin
send("From client ")

#A = viikonpv, Y = vuosi, X: aika (hh:min:ss)
send(pvKk.strftime("Tänään on : %A , %Y , %X "))

print("message here:: ") #user input sms if have
userMSG = input()

send(userMSG)
input()

send("Connection end")
send(DISCONNECT_MESSAGE)