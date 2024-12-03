from src.controllers.todo_list_controller import TodoListController
from src.views.http_types.http_response import HttpResponse
from src.errors.error_handler import handler_errors


class TodoListView:
    def __init__(self, controller: TodoListController = None) -> None:
        """Inicializa o TodoListView com um controlador."""
        self.__controller = controller or TodoListController()

    def handle(self) -> HttpResponse:
        """Lida com a requisição para listar todos os TODOs."""
        try:
            todos = self.__controller.get_todos()
            return HttpResponse(status_code=200, body=todos)
        except Exception as error:
            return handler_errors(error)
