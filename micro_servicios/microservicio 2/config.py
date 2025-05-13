import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'shared'))
db_path = os.path.join(BASE_DIR, "bookstore.db")  # Use shared directory path
SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}'
SECRET_KEY = 'secretkey'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Ensure the shared directory exists
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)

# Ensure the database file exists in the shared directory
if not os.path.exists(db_path):
    import sqlite3
    conn = sqlite3.connect(db_path)
    conn.close()
