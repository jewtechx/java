import http.server
import socketserver
import json

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()

        response = {'message':'Hello python devs'}
        self.wfile.write(json.dumps(response).encode())

port = 8080

with socketserver.TCPServer(("",port),MyHandler) as httpd:
    print(f'serving at port {port}')