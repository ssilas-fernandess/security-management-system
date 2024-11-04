from flask import Blueprint, request, jsonify

resources_bp = Blueprint('resources', __name__)

resources = []

@resources_bp.route('/', methods=['GET'])
def get_resources():
    return jsonify(resources), 200

@resources_bp.route('/', methods=['POST'])
def add_resource():
    data = request.get_json()
    resources.append(data)
    return jsonify({"message": "Recurso adicionado com sucesso"}), 201

@resources_bp.route('/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    data = request.get_json()
    if 0 <= resource_id < len(resources):
        resources[resource_id].update(data)
        return jsonify({"message": "Recurso atualizado com sucesso"}), 200
    return jsonify({"message": "Recurso não encontrado"}), 404
