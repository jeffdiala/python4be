from helpers import http_code


class GeneralError(Exception):
    def __init__(self, error, details):
        self.error = error
        self.details = details
        self.severity = 'error'
        self.status = http_code.HTTP_412_PRECONDITION_FAILED
