from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.views.todo_register_view import TodoRegisterView

todo_routes_bp = Blueprint("todo_routes", __name__)


@todo_routes_bp.route("/todos", methods=["POST"])
def create_todo():
    http_request = HttpRequest(body=request.json)
    http_response = TodoRegisterView().handle(http_request)

    return jsonify(http_response.body), http_response.status_code
