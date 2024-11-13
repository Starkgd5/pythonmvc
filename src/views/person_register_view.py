from http_types.http_request import HttpRequest
from http_types.http_response import HttpReponse


class PersonRegisterView:
    def handle(self, http_request: HttpRequest) -> HttpReponse:
        body = http_request.body
        name = body.get("name")
        age = body.get("age")
        self.__validate_inputs(name, age)

        # person = {"id": 1, "name": "Jonas Martiniano", "age": 34}

        return HttpReponse(status_code=201, body=body)

    def __validate_inputs(self, name: any, age: any) -> None:
        if not name or not age or not isinstance(name, str) or not isinstance(age, int):
            raise Exception("Invalids inputs for person register")
