from src.controllers.todo_register_controller import TodoRegisterController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.error_handler import handler_errors


class TodoRegisterView:
    def __init__(self, controller: TodoRegisterController = None) -> None:
        """Inicializa a view com o controlador."""
        self.__controller = controller or TodoRegisterController()

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """Processa a requisição para registrar um TODO."""
        try:
            task, person_name = self.__extract_and_validate_inputs(http_request)
            created_todo = self.__controller.create_todo(task, person_name)
            return HttpResponse(status_code=201, body={"data": created_todo})
        except Exception as error:
            return handler_errors(error)

    def __extract_and_validate_inputs(self, http_request: HttpRequest) -> tuple[str, str]:
        """Extrai e valida os dados da requisição."""
        body = http_request.body
        task = body.get("task")
        person_name = body.get("person_name")
        self.__validate_inputs(task, person_name)
        return task, person_name

    @staticmethod
    def __validate_inputs(task: any, person_name: any) -> None:
        """Valida os campos fornecidos para o registro de TODO."""
        if not task or not person_name or not isinstance(task, str) or not isinstance(person_name, str):
            raise HttpBadRequestError("Invalid inputs for TODO registration")
