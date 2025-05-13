from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.user import User
from extensions import db
from flask_login import login_user, logout_user, login_required
from services.auth import login as auth_service_login  
from services.auth import register as auth_service_register  

auth = Blueprint('auth', __name__)

  

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        response = auth_service_login(email, password)  
        
        if response != None and response["success"]:
            user = User(name=response["data"]["name"], email=email, token=response["data"]["token"], id=response["data"]["id"])
            login_user(user)
            session["name"]= response["data"]["name"]
            session["email"]= email
            return redirect(url_for('book.catalog'))
        else:
            flash('Login failed')
    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        response = auth_service_register(email, password, name)
        
        if response["success"]:
            flash('User registered successfully')
            return redirect(url_for('auth.login'))
        else:
            flash('Registration failed: ' + response["message"])
    return render_template('register.html')

@auth.route('/logout')
@login_required
def logout():
    session.pop("name", None)
    session.pop("email", None)
    logout_user() 
    return redirect(url_for('auth.login'))

