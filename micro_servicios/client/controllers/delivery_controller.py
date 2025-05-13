from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from services.ApiGatewayService import ApiGatewayService

delivery = Blueprint('delivery', __name__)
api_gateway_service = ApiGatewayService(api_gateway_url="http://localhost:5001/delivery")

@delivery.route('/delivery/<int:purchase_id>', methods=['GET', 'POST'])
@login_required
def select_delivery(purchase_id):
    if request.method == 'POST':
        selected_provider_id = request.form.get('provider')
        response = api_gateway_service.assign_delivery(purchase_id, selected_provider_id)
        if not response["success"]:
            return "Error assigning delivery.", 500
        return redirect(url_for('book.catalog'))
    
    response = api_gateway_service.get_delivery_providers()
    if not response["success"]:
        return "Error retrieving delivery providers.", 500
    return render_template('delivery_options.html', providers=response["data"], purchase_id=purchase_id)