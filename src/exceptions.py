from http import HTTPStatus


class URLError(Exception):
    def __init__(self, message: str, status_code: HTTPStatus):
        self.message = message
        self.status_code = status_code
        