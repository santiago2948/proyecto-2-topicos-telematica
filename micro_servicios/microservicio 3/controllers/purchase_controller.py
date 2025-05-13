from flask import Blueprint, request, redirect, url_for
from models.purchase import Purchase
from models.book import Book
from extensions import db
from utils.response import response

purchase = Blueprint('purchase', __name__)

@purchase.route('/buy/<int:book_id>', methods=['POST'])
def buy(book_id):
    data = request.json
    quantity = int(data['quantity'])
    price = float(data['price'])
    book = Book.query.get_or_404(book_id)

    if book.stock < quantity:
        return "No hay suficiente stock disponible.", 400

    total_price = price * quantity

    new_purchase = Purchase(
        user_id=data["user_id"],
        book_id=book_id,
        quantity=quantity,
        total_price=total_price,
        status='Pending Payment'
    )
    book.stock -= quantity  # Reducir stock
    db.session.add(new_purchase)
    db.session.commit()
    
    return response(True, "Compra realizada con éxito", {"purchase_id": new_purchase.id, "total_price": total_price})
