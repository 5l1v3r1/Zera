import os

from zera.request_handler import RequestHandler


class StaticHandler(RequestHandler):
    def __init__(self):
        self.file_types = {
            ".css": "text/css",
            ".js": "text/javascript",
            ".jpg": "image/jpeg",
            ".png": "image/png",
            "notfound": "text/plain",
        }

    def find_static(self, file_path):
        self.split_path = os.path.splitext(file_path)
        self.extension = self.split_path[1]

        try:
            if self.extension in (".jpg", ".jpeg", ".png"):
                self.contents = open(f"static{file_path}", "rb")
            else:
                self.contents = open(f"static{file_path}", "r")

            self.set_content_type(self.extension)
            self.set_status(200)
            return True
        except:
            self.set_content_type("notfound")
            self.set_status(404)
            return False

    def set_content_type(self, ext):
        self.content_type = self.file_types[ext]
