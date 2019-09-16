class RequestHandler:
    def __init__(self):
        self.content_type = ""
        self.contents = ""

    def read(self):
        return self.contents

    def get_contents(self):
        return self.contents.read()

    def get_status(self):
        return self.status

    def get_content_type(self):
        return self.content_type

    def get_type(self):
        return "static"

    def set_status(self, status):
        self.status = status


class BadRequest(RequestHandler):
    def __init__(self):
        super().__init__()
        self.content_type = "text/plain"
        self.set_status(404)
