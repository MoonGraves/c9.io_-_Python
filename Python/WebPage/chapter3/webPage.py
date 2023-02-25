from http.server import HTTPServer, BaseHTTPRequestHandler

class echoHandler(BaseHTTPRequestHandler):
    def do_Get(self):
        self.send_response(200)
        self.send_header('contnet-type', 'text/html')
        self.end_headers()
#       self.wfile.write(self.path[1:]. encode())
        self.wfile.write('Hello world'. encode())

def main():
    PORT = 8080 #toimii 8080, 8000 tai 9000
    server = HTTPServer(('', PORT), echoHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()

#Avaat localhost:8080
#https://www.youtube.com/watch?v=kogOfxg1c_g (part 1)
#https://www.youtube.com/watch?v=dgvLegLW6ek (part 2)

#ei lue oletuksen kansion olemassa olevia index.html sivustoja tai olemassa olevia index.html