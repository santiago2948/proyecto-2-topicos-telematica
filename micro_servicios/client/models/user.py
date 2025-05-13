
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, name, email, token, id):
        self.name = name
        self.email = email
        self.token = token
        self.id = id

    def get_id(self):
        return self.id