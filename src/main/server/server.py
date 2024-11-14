from flask import Flask
from src.main.routers.person_routes import person_routes_bp
from src.main.routers.todo_routes import todo_routes_bp

app = Flask(__name__)
app.register_blueprint(person_routes_bp)
app.register_blueprint(todo_routes_bp)
