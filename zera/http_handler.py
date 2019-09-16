import os
from http.server import BaseHTTPRequestHandler
from pathlib import Path

from markdown_handler import MarkdownHandler
from static_handler import StaticHandler
from template_handler import TemplateHandler
from request_handler import BadRequest
from urls import urls


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.split_path = os.path.splitext(self.path)
        self.extension = self.split_path[1]

        if self.extension == "" or self.extension == ".html":
            if self.path in urls:
                handler = TemplateHandler()
                handler.find_template(urls[self.path])
            else:
                handler = BadRequest()

        if self.extension == "" or self.extension == ".md":
            if self.path in urls:
                handler = MarkdownHandler()
                handler.find_template(urls[self.path])
            else:
                handler = BadRequest()

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
