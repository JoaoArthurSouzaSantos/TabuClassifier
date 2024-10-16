from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Create user table"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)  # Senha não hash

    def __init__(self, username, password):
        self.username = username
        self.password = password  # A senha ainda está em texto simples, considere usar hash
