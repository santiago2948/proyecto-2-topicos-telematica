from flask import Blueprint, request, redirect, url_for
from flask_login import login_required, current_user
from services.ApiGatewayService import ApiGatewayService

purchase = Blueprint('purchase', __name__)
api_gateway_service = ApiGatewayService(api_gateway_url="http://localhost:5001/purchase")

@purchase.route('/buy/<int:book_id>', methods=['POST'])
@login_required
def buy(book_id):
    purchase_data = {
        "quantity": int(request.form.get('quantity')),
        "price": float(request.form.get('price')),
        "user_id": current_user.id
    }
    response = api_gateway_service.create_purchase(book_id, purchase_data)
    if not response["success"]:
        return "Error creating purchase.", 500
    return redirect(url_for('payment.payment_page', purchase_id=response["data"]["id"]))
