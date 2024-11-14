from src.controllers.todo_register_controller import TodoRegisterController

from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.error_handler import handler_errors


class TodoRegisterView:
    def __init__(self) -> None:
        self.__controller = TodoRegisterController()

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body = http_request.body
            task = body.get("task")
            person_name = body.get("person_name")
            self.__validate_inputs(task, person_name)
            response = self.__controller.create_todo(task, person_name)
            return HttpResponse(status_code=201, body={"data": response})
        except Exception as e:
            response = handler_errors(e)
            return response

    def __validate_inputs(self, task: any, person_name: any) -> None:
        if (
            not task
            or not person_name
            or not isinstance(task, str)
            or not isinstance(person_name, str)
        ):
            raise HttpBadRequestError("Invalids inputs for todo register")
