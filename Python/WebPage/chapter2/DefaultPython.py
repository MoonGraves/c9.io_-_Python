import http.server
import socketserver

#https://stackabuse.com/serving-files-with-pythons-simplehttpserver-module/

#Porttia voidaan käyttää mm. 8080 , 8000 tai 9000
#Käynnistäessä sitten avaat tyhjän sivun ja sijoitat localhost:8080
PORT = 8000

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()