from http.server import HTTPServer

from http_handler import HttpHandler


class Main:
    def __init__(self):
        self.port = 8080

    def run(self):
        self.server = HTTPServer(("", self.port), HttpHandler)
        print(f"Starting zera at:http://127.0.0.1:{self.port}/")
        self.server.serve_forever()
