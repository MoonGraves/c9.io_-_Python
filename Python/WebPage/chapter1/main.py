from http.server import HTTPServer, BaseHTTPRequestHandler

#https://github.com/howCodeORG/Simple-Python-Web-Server/blob/master/serv.py
class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()

#python main.py
#tyhjän sivustoon isket: localhost:8080, joka oletuksena on index.html sivusto muiden tiedoston kanssa
#voidaan myös etsiä muita sivustoja jos on olemassa, muuten "file not found"
#esim. olemassa localhost:8080/index2.html 
# ja cmd aina tulee päivitys vaikka olisi F5, jokin tiedosto ei löydy esim. kuva 404