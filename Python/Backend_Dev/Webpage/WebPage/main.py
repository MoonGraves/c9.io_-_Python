from http.server import HTTPServer, BaseHTTPRequestHandler


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

#
#default sivusto on index.html
##
#voit käyttää cmd tai VsCode käynnistät tämän main.py
#sitten tyhjän sivuston avaat localhost:8080
#voidaan avata olemassa olevia sivustoja esim. localhost:8080/index2.html
#jos ei ole niitä olevia sivustoja sitten muodostuu "file not found" ja cmd:ssä syntyy error 404
