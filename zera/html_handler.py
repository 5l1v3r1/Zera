from request_handler import RequestHandler


class HtmlHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self.content_type = "text/html"

    def find_template(self, url_template):
        try:
            self.template_file = open(f"templates/" + url_template)
            self.contents = self.template_file
            self.set_status(200)
            return True
        except:
            self.set_status(404)
            return False
