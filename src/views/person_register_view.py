from src.controllers.person_register_controller import PersonRegisterController

from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class PersonRegisterView:
    def __init__(self) -> None:
        self.__controller = PersonRegisterController()

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        name = body.get("name")
        age = body.get("age")
        self.__validate_inputs(name, age)

        # person = {"id": 1, "name": "Jonas Martiniano", "age": 34}
        response = self.__controller.create_person(name, age)
        return HttpResponse(status_code=201, body={"data": response})

    def __validate_inputs(self, name: any, age: any) -> None:
        if not name or not age or not isinstance(name, str) or not isinstance(age, int):
            raise Exception("Invalids inputs for person register")
