import http.server

class RequstHandler(http.server.BaseHTTPRequestHandler):

    def do_PUT(self):

        file = open('temp', 'w')
        line = self.rfile.peek().decode()

        for l in line:
            file.write(l)
        self.send_response(http.server.HTTPStatus.OK, 'ACCEPT')
        self.wfile.write(b'200')
        

if __name__ == "__main__":
    handler = RequstHandler
    address = ('', 8000)

    server = http.server.HTTPServer(address, handler)
    print("Server Start")
    server.serve_forever()
    print("test")