from flask import Blueprint, request
import requests
from utils.generals import MICROSERVICE_3_URL

payment = Blueprint('payment', __name__)

@payment.route('/process/<int:purchase_id>', methods=['POST'])
def process_payment(purchase_id):
    response = requests.post(f"{MICROSERVICE_3_URL}/payment/process/{purchase_id}", json=request.json)
    return (response.content, response.status_code, response.headers.items())
