from http.server import BaseHTTPRequestHandler, HTTPServer
import time, re, netifaces as ni

# Getting IP
ip = ni.ifaddresses("eth0")[ni.AF_INET][0]["addr"]
print(ip)

hostName = ""
serverPort = 80

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        path = self.path
        res = re.split(r'/|_|\.', path)
        exponent = str(int(res[2]) * int(res[4]))
        self.wfile.write(exponent.encode())
        #self.wfile.write(b'My name is Julesco and iChall.')

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{ip}/%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped!")
