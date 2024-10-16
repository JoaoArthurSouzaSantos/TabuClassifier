from flask import render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from utils import algorithms

app_main = Blueprint('route_main', __name__, template_folder="frontend/templates", static_folder="frontend/static")

selected_algorithms = []

@app_main.route('/')
@app_main.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app_main.route('/sobre-nos', methods=['GET', 'POST'])
def sobre_nos():
    return render_template('Equipe.html')

@app_main.route('/parceiros', methods=['GET', 'POST'])
def parceiros():
    return render_template('parceiros.html')

@app_main.route('/software', methods=['GET', 'POST'])
def software():
    return render_template('Software.html')