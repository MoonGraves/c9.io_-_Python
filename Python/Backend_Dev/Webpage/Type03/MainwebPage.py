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
    
################################################################
######cmd tai vscode aktivoit tämän python tiedoston
#####
####Jonka jälkeen avaat tyhjän välilehden sijoitat localhost:8080
###avatesassi muodostuu tyhjä sivu, että näkyy hello world & toimminalta pitäisi toimia
##jos ei näy hello world, pelkä Error response , koska methodin Get jossakin on error
###
######
#######################
