from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app as app

auth_bp = Blueprint('auth', __name__)

users = {
    "admin": {"password": generate_password_hash("adminpass"), "role": "admin"},
    "employee": {"password": generate_password_hash("employeepass"), "role": "employee"},
    "manager": {"password": generate_password_hash("managerpass"), "role": "manager"}
}

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return jsonify({"message": "Login bem-sucedido", "role": user["role"]}), 200
    return jsonify({"message": "Credenciais inválidas"}), 401
