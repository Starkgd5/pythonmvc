from src.controllers.person_register_controller import PersonRegisterController

from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

from src.errors.types.http_bad_resquest import HttpBadRequestError
from src.errors.error_handler import handle_errors


class PersonRegisterView:
    def __init__(self) -> None:
        self.__controller = PersonRegisterController()

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body = http_request.body
            name = body.get("name")
            age = body.get("age")
            self.__validate_inputs(name, age)
            response = self.__controller.create_person(name, age)
            return HttpResponse(status_code=201, body={"data": response})
        except Exception as exception:
            response = handle_errors(exception)
            return response

    def __validate_inputs(self, name: any, age: any) -> None:
        if not name or not age or not isinstance(name, str) or not isinstance(age, int):
            raise HttpBadRequestError("Invalids inputs for person register")
