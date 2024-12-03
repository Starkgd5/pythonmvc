from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.views.todo_register_view import TodoRegisterView
from src.views.todo_list_view import TodoListView

# Blueprint para rotas relacionadas a TODOs
todo_routes_bp = Blueprint("todo_routes", __name__)

# Função utilitária para lidar com as respostas
def handle_view(view, http_request=None):
    """Processa uma view e retorna uma resposta Flask."""
    http_response = view.handle(http_request) if http_request else view.handle()
    return jsonify(http_response.body), http_response.status_code

# Rota para criação de TODO
@todo_routes_bp.route("/todos", methods=["POST"])
def create_todo():
    http_request = HttpRequest(body=request.json)
    return handle_view(TodoRegisterView(), http_request)

# Rota para listar TODOs
@todo_routes_bp.route("/todos", methods=["GET"])
def get_todo_list():
    return handle_view(TodoListView())
