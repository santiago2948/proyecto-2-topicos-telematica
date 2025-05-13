from flask import Flask, render_template
from extensions import db, login_manager
from config import SQLALCHEMY_DATABASE_URI, SECRET_KEY, SQLALCHEMY_TRACK_MODIFICATIONS
from models.user import User  # Import the User model


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI  # Explicitly set the database URI
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'


from controllers.book_controller import book


app.register_blueprint(book, url_prefix='/book')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure the user table is created
    app.run(host="0.0.0.0", debug=True, port=5002)
