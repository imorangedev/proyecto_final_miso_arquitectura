from flask import Blueprint, jsonify, request
from src.commands.crear_pedido import CrearPedido
from src.commands.health_check import HealthCheck

blueprint = Blueprint('pedidos', __name__)


@blueprint.route('/', methods=['GET'])
def health_check():
    return HealthCheck().execute()


@blueprint.route('/crear', methods=['POST'])
def crear_pedido():
    body = request.get_json()
    response = CrearPedido(body).execute()
    return jsonify(response['response']), response['status_code']