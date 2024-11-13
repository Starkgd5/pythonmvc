class HttpResponse:
    def __init__(self, status_code: int, body: dict) -> None:
        self.body = body
        self.status_code = status_code
