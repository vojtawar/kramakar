from http.server import BaseHTTPRequestHandler, HTTPServer
import time
#import ssl

hostName = '25.48.3.101'
serverPort = 8080

class Kramakar(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("wwwroot/index.html") as index:
            for line in index:
                self.wfile.write(bytes(line, "utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        
if __name__ == "__main__":
    httpd = HTTPServer((hostName, serverPort), Kramakar)
    print("Server started https://%s:%s" % (hostName, serverPort))
 #   httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='ssl/key.pem', certfile='ssl/cert.pem',
 #       server_side=True)
    try:
         httpd.serve_forever()
    except KeyboardInterrupt:
         pass

    httpd.server_close()
    print("Server stopped.")

