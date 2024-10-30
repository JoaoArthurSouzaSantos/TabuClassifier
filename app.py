# app.py
from flask import Flask
from config import db
from routes.route import app_main as blueprint_main
from routes.route_algorith import app_algorithm as blueprint_algorithm
from routes.route_auth import app_auth as blueprint_auth

app = Flask(__name__, template_folder="frontend/templates", static_folder="frontend/static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/catador'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'teste'

# Inicialize o banco de dados com a instância do app
db.init_app(app)

# Registre os blueprints
app.register_blueprint(blueprint_main)
app.register_blueprint(blueprint_auth)
app.register_blueprint(blueprint_algorithm)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no MySQL
    app.run(host='0.0.0.0', debug=True)
