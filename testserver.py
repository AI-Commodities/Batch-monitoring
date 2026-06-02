from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, this is a Python server!")

server = HTTPServer(('localhost', 8000), MyHandler)
print("Server running on http://localhost:8000")

server.serve_forever()
