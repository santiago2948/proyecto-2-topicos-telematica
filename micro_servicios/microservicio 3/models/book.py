# --- models/book.py ---
from extensions import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    author = db.Column(db.String(100))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)
    seller_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
            "seller_id": self.seller_id
        }