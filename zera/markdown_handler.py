import markdown2

from zera.request_handler import RequestHandler


class MarkdownHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self.content_type = "text/html"

    def utf8_decorate(func):
        def func_wrapper(content):
            return f'<meta charset="UTF-8">{func(content)}'

        return func_wrapper

    @utf8_decorate
    def get_contents(self):
        return markdown2.markdown(self.contents.read())

    def find_template(self, url_template):
        file = str("templates/" + url_template)
        try:
            self.template_file = open(f"{file}")
            self.contents = self.template_file
            self.set_status(200)
            return True
        except:
            self.set_status(404)
            return False
