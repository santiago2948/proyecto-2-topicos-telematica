from flask import Flask, render_template
from extensions import db, login_manager
from models.user import User
from flask import Flask
from flask_jwt_extended import JWTManager
from config import SQLALCHEMY_DATABASE_URI, SECRET_KEY, SQLALCHEMY_TRACK_MODIFICATIONS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI  # Explicitly set the database URI
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.config['JWT_SECRET_KEY'] = 'seguro_solo_la_merte'
jwt = JWTManager(app)

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Luego importar blueprints
from controllers.auth_controller import auth
from controllers.book_controller import book
from controllers.purchase_controller import purchase
from controllers.payment_controller import payment

app.register_blueprint(auth)
app.register_blueprint(book, url_prefix='/book')
app.register_blueprint(purchase, url_prefix='/purchase')
app.register_blueprint(payment, url_prefix='/payment')


@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
# OJO este conexto crea las tablas e inicia los proveedores de entrega, 
# se debe ejecutar cada que se reinstala y ejecuta la aplicación Bookstore
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", debug=True, port=5001)
