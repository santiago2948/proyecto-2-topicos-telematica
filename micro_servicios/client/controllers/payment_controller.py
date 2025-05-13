from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from services.ApiGatewayService import ApiGatewayService

payment = Blueprint('payment', __name__)
api_gateway_service = ApiGatewayService(api_gateway_url="http://localhost:5001/payment")

@payment.route('/payment/<int:purchase_id>', methods=['GET', 'POST'])
@login_required
def payment_page(purchase_id):
    if request.method == 'POST':
        payment_data = {
            "method": request.form.get('method'),
            "amount": request.form.get('amount')
        }
        response = api_gateway_service.process_payment(purchase_id, payment_data)
        if not response["success"]:
            return "Error processing payment.", 500
        return redirect(url_for('delivery.select_delivery', purchase_id=purchase_id))
    
    return render_template('payment.html', purchase_id=purchase_id)