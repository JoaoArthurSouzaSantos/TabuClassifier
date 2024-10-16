from flask import Flask

from models.user_model import db

from routes.route import app_main as blueprint_main
from routes.route_algorith import app_algorithm as blueprint_algorithm
from routes.route_auth import app_auth as blueprint_auth

app = Flask(__name__, template_folder="frontend/templates", static_folder="frontend/static")
app.register_blueprint(blueprint_main)
app.register_blueprint(blueprint_auth)
app.register_blueprint(blueprint_algorithm)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/catador'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'teste'

db.init_app(app)

if __name__ == '_main_':
    app.app_context().push()
    app.debug = True
    db.create_all()  # Create tables in MySQL
    app.run(host='0.0.0.0')