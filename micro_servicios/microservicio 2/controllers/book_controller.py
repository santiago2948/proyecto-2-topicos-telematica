from flask import Blueprint, request
from models.book import Book
from models.user import User  # Import the User model
from utils.response import response

from extensions import db


book = Blueprint('book', __name__)

@book.route('/catalog')
def catalog():
    try:
        books = Book.query.all()
        books_serialized = [book.to_dict() for book in books]  # Serialize books
        return response(True, 'catalog.html', books_serialized)
    except Exception as e:
        return response(False, 'Error retrieving books')

@book.route('/my_books', methods=['POST'])
def my_books():
    data = request.json
    try:
        books = Book.query.filter_by(seller_id=data["user_id"]).all()
        books_serialized = [book.to_dict() for book in books]  # Serialize books
        return response(True, 'Books retrieved successfully', books_serialized)
    except Exception as e:
        return response(False, f'Error retrieving books {e}')
