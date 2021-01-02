from http.server import HTTPServer, BaseHTTPRequestHandler

class echoHandler(BaseHTTPRequestHandler):
    def do_Get(self):
        self.send_response(200)
        self.send_header('contnet-type', 'text/html')
        self.end_headers()
        self.wfile.write("hello to you!". encode())


def main():
    PORT = 8080 #other work even 8000, 8080 or 9000
    server = HTTPServer(('', PORT), echoHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
    
#Output cmd:ssä:
#python WebPage.py
#Server running on port 8080
#127.0.0.1 - - [02/Jan/2021 11:27:01] code 501, message Unsupported method ('GET')
#127.0.0.1 - - [02/Jan/2021 11:27:01] "GET / HTTP/1.1" 501 -
#127.0.0.1 - - [02/Jan/2021 11:27:01] code 501, message Unsupported method ('GET')
#127.0.0.1 - - [02/Jan/2021 11:27:01] "GET /favicon.ico HTTP/1.1" 501 -
#127.0.0.1 - - [02/Jan/2021 11:27:09] code 501, message Unsupported method ('GET')
#
#Google Chrome & muu edge sovellus, syötät välilehteen kuin:: localhost:8080
#
#  
#
#
#
