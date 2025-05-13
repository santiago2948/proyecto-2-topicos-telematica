from flask import Blueprint, request, jsonify
import requests
from utils.generals import MICROSERVICE_3_URL

delivery = Blueprint('delivery', __name__)

@delivery.route('/providers', methods=['GET'])
def get_providers():
    response = requests.get(f"{MICROSERVICE_3_URL}/delivery/providers")
    return (response.content, response.status_code, response.headers.items())

@delivery.route('/assign/<int:purchase_id>', methods=['POST'])
def assign_delivery(purchase_id):
    response = requests.post(f"{MICROSERVICE_3_URL}/delivery/assign/{purchase_id}", json=request.json)
    return (response.content, response.status_code, response.headers.items())
