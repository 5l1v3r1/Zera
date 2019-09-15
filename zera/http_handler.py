from http.server import BaseHTTPRequestHandler
from pathlib import Path

from urls import urls


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.respond()

    def handle_http(self):
        self.status_code = 200
        self.content_type = "text/plain"
        self.response_content = ""

        if self.path in urls:
            print(self.path)
            self.url_content = urls[self.path]["template"]
            self.file_path = Path(f"templates/{self.url_content}/")
            if self.file_path.is_file():
                self.content_type = "text/html"
                self.response_content = open(f"templates/{self.url_content}")
                self.response_content = self.response_content.read()
            else:
                self.content_type = "text/plain"
                self.response_content = "File not found!"
        else:
            self.content_type = "text/plain"
            self.response_content = "Path not found!"

        self.send_response(self.status_code)
        self.send_header("Content-type", self.content_type)
        self.end_headers()
        return bytes(self.response_content, "UTF-8")

    def respond(self):
        self.content = self.handle_http()
        self.wfile.write(self.content)
