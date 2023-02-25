import urllib.request
#https://www.dj4e.com/code/http/client2.py

fhand = urllib.request.urlopen('http://127.0.0.1:8080/Client2.txt')
for line in fhand:
    print(line.decode().strip())