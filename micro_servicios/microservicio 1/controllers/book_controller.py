from flask import Blueprint, request, jsonify
import requests
from utils.generals import MICROSERVICE_2_URL, MICROSERVICE_3_URL

book = Blueprint('book', __name__)

@book.route('/catalog', methods=['GET'])
def catalog():
    try:
        response = requests.get(f"{MICROSERVICE_2_URL}/book/catalog")
        return (response.content, response.status_code, response.headers.items())
    except requests.exceptions.RequestException as e:
        return jsonify({"success": False, "message": "Error connecting to microservice 2"}), 500

@book.route('/my_books', methods=['POST'])
def my_books():
    try:
        response = requests.post(f"{MICROSERVICE_2_URL}/book/my_books", json=request.json)
        return (response.content, response.status_code, response.headers.items())
    except requests.exceptions.RequestException as e:
        return jsonify({"success": False, "message": "Error connecting to microservice 2"}), 500

@book.route('/add_book', methods=['POST'])
def add_book():
    try:
        response = requests.post(f"{MICROSERVICE_3_URL}/book/add_book", json=request.json)
        return (response.content, response.status_code, response.headers.items())
    except requests.exceptions.RequestException as e:
        return jsonify({"success": False, "message": "Error connecting to microservice 3"}), 500

@book.route('/edit_book/<int:book_id>', methods=['POST'])
def edit_book(book_id):
    try:
        response = requests.post(f"{MICROSERVICE_3_URL}/book/edit_book/{book_id}", json=request.json)
        return (response.content, response.status_code, response.headers.items())
    except requests.exceptions.RequestException as e:
        return jsonify({"success": False, "message": "Error connecting to microservice 3"}), 500

@book.route('/delete_book/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    try:
        response = requests.post(f"{MICROSERVICE_3_URL}/book/delete_book/{book_id}", json=request.json)
        return (response.content, response.status_code, response.headers.items())
    except requests.exceptions.RequestException as e:
        return jsonify({"success": False, "message": "Error connecting to microservice 3"}), 500
