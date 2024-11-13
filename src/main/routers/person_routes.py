from flask import Blueprint, jsonify

person_routes_bp = Blueprint("person_routes", __name__)


@person_routes_bp.route("/persons", methods=["GET"])
def create_person():
    person = [
        {"id": 1, "name": "Jonas Martiniano", "age": 34, "email": "jonas@gmail.com"}
    ]
    return jsonify(person), 201
