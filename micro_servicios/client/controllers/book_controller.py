from flask import Blueprint, render_template, request, redirect, url_for
import flask
from flask_login import login_required, current_user
from services.ApiGatewayService import ApiGatewayService

book = Blueprint('book', __name__)
api_gateway_service = ApiGatewayService(api_gateway_url="http://localhost:5001/book")  

@book.route('/catalog')
def catalog():
    data = api_gateway_service.get_books()
    if data["success"] == False:
        data["data"] = []
    return render_template('catalog.html', books=data["data"])

@book.route('/my_books')
@login_required
def my_books():
    response = api_gateway_service.get_books_by_seller(current_user.id)
    if response["success"] == False:
        flask("Error retrieving your books.")
    return render_template('my_books.html', books=response["data"])

@book.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    if request.method == 'POST':
        book_data = {
            "title": request.form.get('title'),
            "author": request.form.get('author'),
            "description": request.form.get('description'),
            "price": float(request.form.get('price')),
            "stock": int(request.form.get('stock')),
            "user_id": current_user.id
        }
        response = api_gateway_service.add_book(book_data)
        if response["success"] == False:
            return "Error adding book.", 500
        return redirect(url_for('book.catalog'))
    return render_template('add_book.html')

@book.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    if request.method == 'POST':
        book_data = {
            "title": request.form.get('title'),
            "author": request.form.get('author'),
            "description": request.form.get('description'),
            "price": float(request.form.get('price')),
            "stock": int(request.form.get('stock')),
            "user_id": current_user.id
        }
        api_gateway_service.update_book(book_id, book_data)
        return redirect(url_for('book.catalog'))
    
    response = api_gateway_service.get_books_by_seller(current_user.id)
    
    book_to_edit = next((book for book in response["data"] if book['id'] == book_id), None)
    if not book_to_edit:
        return "No tienes permiso para editar este libro.", 403

    return render_template('edit_book.html', book=book_to_edit)

@book.route('/delete_book/<int:book_id>', methods=['POST'])
@login_required
def delete_book(book_id):
    
    response = api_gateway_service.delete_book(book_id, current_user.id)
    if response != 200:
        return "Error deleting book.", 500
    return redirect(url_for('book.catalog'))
