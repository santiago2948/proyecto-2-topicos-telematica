from flask import Blueprint, request
from models.user import User
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from utils.response import response

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)

        return response(True, "Login successful", {"token": f"bearer {access_token}", "name": user.name, "id": user.id })
    else:
        return response(False, "User not found or password incorrect")

@auth.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        email = data.get('email')
        user = User.query.filter_by(email=email).first()
        
        if(user):
            return response(False, "User already exists")

        name = data.get('name')
        password =data.get('password')
        new_user = User(name=name, email=email, password=generate_password_hash(password, method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()
        return response(True, "User registred successfully")
    except Exception as e:
        db.session.rollback()
        return response(False,'Error creating user')
