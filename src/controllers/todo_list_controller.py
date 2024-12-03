from src.models.db.repositories.todo_repository import TodoRepository


class TodoListController:
    def __init__(self, repository: TodoRepository = None):
        """Inicializa o controlador com o repositório."""
        self.__todo_repository = repository or TodoRepository()

    def get_todos(self) -> list[dict]:
        """Obtém a lista de TODOs formatada."""
        todos_data = self.__todo_repository.get_todo_list()
        return self.__format_response(todos_data)

    def __format_response(self, todos_data: list[tuple]) -> list[dict]:
        """Formata a lista de TODOs obtida do repositório."""
        return [
            {
                "id": todo[0],
                "task": todo[1],
                "status": todo[2],
                "due_date": todo[3],
                "person_name": todo[4],
            }
            for todo in todos_data
        ]
