import urllib.request
#This is client2 & toinen tyyppinen versio

fhand = urllib.request.urlopen('http://127.0.0.1:8080/Client2.txt') #yhteys sama portti kuin serveri mitä siellä on määritetty & jos tiedettään se portti numero
#tyhjään välilehti joko avaan toi tai perus localhost:8080/client2.txt

for line in fhand:
    print(line.decode().strip())
