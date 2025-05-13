from extensions import db

class User(db.Model):
    __tablename__ = 'user'  # Ensure the table name matches the one used in the foreign key
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
