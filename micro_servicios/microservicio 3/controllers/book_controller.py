from flask import Blueprint, request
from models.book import Book
from models.user import User  # Import the User model
from utils.response import response

from extensions import db


book = Blueprint('book', __name__)


@book.route('/add_book', methods=['POST'])
def add_book():
    data = request.json
    try:
        # Ensure the user exists in the user table
        user = User.query.get(data["user_id"])
        if not user:
            return response(False, 'User does not exist')

        title = data['title']
        author = data['author']
        description = data['description']
        price = float(data['price'])
        stock = int(data['stock'])
        new_book = Book(title=title, author=author, description=description, price=price, stock=stock, seller_id=data["user_id"])
        db.session.add(new_book)
        db.session.commit()
        return response(True, 'Book added successfully', new_book.to_dict())  # Serialize new book
    except Exception as e:
        db.session.rollback()
        return response(False, f'Error adding book {e}')

@book.route('/edit_book/<int:book_id>', methods=['POST'])
def edit_book(book_id):
    data = request.json
    book_to_edit = Book.query.get_or_404(book_id)
    
    if book_to_edit.seller_id != data["user_id"]:
        return "No tienes permiso para editar este libro.", 403
    try:
        book_to_edit.title = data['title']
        book_to_edit.author = data['author']
        book_to_edit.description = data['description']
        book_to_edit.price = float(data['price'])
        book_to_edit.stock = int(data['stock'])
        db.session.commit()
        return response(True, 'Book edited successfully')
    except Exception as e:
        db.session.rollback()
        return response(False, 'Error editing book')


@book.route('/delete_book/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    data = request.json
    print(book_id)
    book_to_delete = Book.query.get_or_404(book_id)
    if book_to_delete.seller_id != data["user_id"]:
        return "No tienes permiso para eliminar este libro.", 403
    try:
        db.session.delete(book_to_delete)
        db.session.commit()
        return response(True, 'Book deleted successfully')
    except Exception as e:
        db.session.rollback()
        return response(False, 'Error deleting book')
