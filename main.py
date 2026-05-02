from http.server import SimpleHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"   # important: allows access from other devices
PORT = 8000

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print(f"Serving on http://{HOST}:{PORT}")
server.serve_forever()