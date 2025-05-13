from flask import Blueprint, jsonify, request
from models.delivery import DeliveryProvider
from models.delivery_assignment import DeliveryAssignment
from extensions import db

delivery = Blueprint('delivery', __name__)

@delivery.route('/providers', methods=['GET'])
def get_providers():
    providers = DeliveryProvider.query.all()
    return jsonify({"success": True, "data": [provider.to_dict() for provider in providers]})

@delivery.route('/assign/<int:purchase_id>', methods=['POST'])
def assign_delivery(purchase_id):
    provider_id = request.json.get('provider_id')
    new_assignment = DeliveryAssignment(purchase_id=purchase_id, provider_id=provider_id)
    db.session.add(new_assignment)
    db.session.commit()
    return jsonify({"success": True, "message": "Delivery assigned successfully"})