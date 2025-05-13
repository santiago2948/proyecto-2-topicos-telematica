from flask import Blueprint, request
import requests
from utils.generals import MICROSERVICE_3_URL

purchase = Blueprint('purchase', __name__)

@purchase.route('/buy/<int:book_id>', methods=['POST'])
def create_purchase(book_id):
    response = requests.post(f"{MICROSERVICE_3_URL}/purchase/buy/{book_id}", json=request.json)
    print(response)
    return (response.content, response.status_code, response.headers.items())
