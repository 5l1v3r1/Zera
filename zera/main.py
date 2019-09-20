from http.server import BaseHTTPRequestHandler, HTTPServer

from html_handler import HtmlHandler
from markdown_handler import MarkdownHandler
from request_handler import BadRequest
from static_handler import StaticHandler
from urls import urls


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in urls:
            self.url_template = urls[self.path]["template"]
            self.extension = self.url_template.split(".")[1]

            # rendering for html template
            if self.extension == "html":
                handler = HtmlHandler()
                handler.find_template(self.url_template)

            # rendering for markdown template
            elif self.extension == "md":
                handler = MarkdownHandler()
                handler.find_template(self.url_template)
        else:
            handler = StaticHandler()
            handler.find_static(self.path)

        self.respond(dict(handler=handler))

    def handle_http(self, handler):
        self.status_code = handler.get_status()
        self.send_response(self.status_code)

        if self.status_code == 200:
            self.content = handler.get_contents()
            self.send_header("Content-type", handler.get_content_type())
        else:
            self.content = "404 Not Found!"

        self.end_headers()
        return bytes(self.content, "UTF-8")

    def respond(self, opts):
        response = self.handle_http(opts["handler"])
        self.wfile.write(response)


class Main:
    def __init__(self):
        self.port = 8080

    def run(self):
        self.server = HTTPServer(("", self.port), HttpHandler)
        print(f"Starting zera at:http://127.0.0.1:{self.port}/")
        self.server.serve_forever()


if __name__ == "__main__":
    main = Main()
    main.run()

