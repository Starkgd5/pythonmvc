from src.models.db.repositories.todo_repository import TodoRepository
from src.errors.types.http_conflict import HttpConflictError  # Exemplo de exceção personalizada


class TodoRegisterController:
    def __init__(self, repository: TodoRepository = None):
        """Inicializa o controlador com o repositório."""
        self.__todo_repository = repository or TodoRepository()

    def create_todo(self, task: str, person_name: str) -> dict:
        """Cria um novo TODO, garantindo validação e formatação da resposta."""
        self.__validate_todo_registry(task)
        self.__todo_repository.registry_todo(task, person_name)
        return self.__format_response(task)

    def __validate_todo_registry(self, task: str) -> None:
        """Valida se a tarefa já foi registrada."""
        if self.__todo_repository.get_todo_by_task(task):
            raise HttpConflictError("Task already registered")

    def __format_response(self, task: str) -> dict:
        """Formata a resposta com os dados do TODO criado."""
        todo = self.__todo_repository.get_todo_by_task(task)
        if not todo:
            raise Exception("Failed to retrieve the registered TODO")
        return {
            "id": todo[0],
            "task": todo[1],
            "status": todo[2],
            "due_date": todo[3],
            "person_name": todo[4],
        }
