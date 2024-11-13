class HttpBadRequestError(Exeption):
    
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "Bad Request"
        self.status_code = 400


class NotFoundError:
    
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "Not found"
        self.status_code = 400