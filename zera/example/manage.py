import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from importlib import reload

from zera.html_handler import HtmlHandler
from zera.markdown_handler import MarkdownHandler
from zera.static_handler import StaticHandler
import urls


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        reload(urls)
        url_patterns = urls.url_patterns

        if self.path in url_patterns:
            self.url_template = url_patterns[self.path]["template"]
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

        # for content from StaticHandler
        if isinstance(self.content, (bytes, bytearray)):
            return self.content

        return bytes(self.content, "UTF-8")

    def respond(self, opts):
        response = self.handle_http(opts["handler"])
        self.wfile.write(response)


class Main:
    def __init__(self):
        self.port = 8080

    def help(self):
        print("Unknown command!\nCommands:")
        print("run:Start the development server\ninit:Initialize example project.")
        sys.exit()

    def run(self):
        if len(sys.argv) < 2:
            self.help()
        elif sys.argv[1] == "run":
            try:
                self.server = HTTPServer(("", self.port), HttpHandler)
                print("Started zera on : http://127.0.0.1:8080/")
                self.server.serve_forever()
            except KeyboardInterrupt:
                self.server.server_close()
        else:
            self.help()


if __name__ == "__main__":
    main = Main()
    main.run()