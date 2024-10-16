from flask import Flask, url_for, render_template, request, redirect, session, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import os
import importlib
import json
from process_functions.preprocessamento import preprocessing
import importlib
from utils import algorithms 
# from frontend.routes import home

app = Flask(__name__, template_folder="frontend/templates", static_folder="frontend/static")
app.secret_key = 'your_secret_key'  # Necessário para usar sessões

# Configure MySQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/catador'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

selected_algorithms = []

class User(db.Model):
    """ Create user table"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)  # Senha não mais hash

    def __init__(self, username, password):
        self.username = username
        self.password = password  # Senha armazenada em texto simples

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/sobre-nos', methods=['GET', 'POST'])
def sobre_nos():
    print("Acessando a página Sobre Nós")  # Log para depuração
    return render_template('Equipe.html')

@app.route('/software', methods=['GET', 'POST'])
def software():
    return render_template('Software.html')

@app.route('/parceiros', methods=['GET', 'POST'])
def parceiros():
    return render_template('parceiros.html')

@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    """Login Form"""
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['username']
        passw = request.form['password']
        # Verificando diretamente no banco de dados se o usuário e a senha são válidos
        data = User.query.filter_by(username=name, password=passw).first()

        if data:
            session['logged_in'] = True
            return redirect(url_for('index'))  # Redireciona para a página principal
        else:
            # Se login inválido, retorna a página de login com mensagem de erro
            return render_template('login.html', error='Nome de usuário ou senha inválidos')


@app.route('/index')
def index():
    
    return render_template('index.html', algorithms=algorithms, selected_algorithms=selected_algorithms)

@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    """Register Form"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            return "User already exists", 400  # Evitar duplicação de usuários
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('login'))

@app.route('/add_algorithm', methods=['POST'])
def add_algorithm():
    algorithm_name = request.json['algorithm']
    selected_algorithm = next(algo for algo in algorithms if algo['name'] == algorithm_name)
    selected_algorithms.append(selected_algorithm)
    rendered_html = render_template('algorithm_item.html', algorithm=selected_algorithm)
    return jsonify({"html": rendered_html})

@app.route('/remove_algorithm', methods=['POST'])
def remove_algorithm():
    algorithm_name = request.json['algorithm']
    global selected_algorithms
    selected_algorithms = [algo for algo in selected_algorithms if algo['name'] != algorithm_name]
    return jsonify({"success": True})

@app.route('/file', methods=["POST"])
def file():
    uploaded_file = request.files['file']
    try:
        df = pd.read_csv(uploaded_file)
        columns = df.columns
        return jsonify({"columns": columns.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/submit', methods=['POST'])
def submit():
    # Processar o arquivo enviado e os dados do formulário
    uploaded_file = request.files['file']
    data = request.form['data']
    json_data = json.loads(data)
    
    print("Arquivo recebido:", uploaded_file.filename)
    print("Dados recebidos:", json_data)
    
    # Pré-processar os dados com base no label e parâmetros de processamento
    normalizados = preprocessing(uploaded_file, label=json_data['label'], **json_data['processing'])

    # Obter a lista de algoritmos
    algorithms = json_data["algorithms"]
    
    for algorithm in algorithms:
        # Construir o caminho do módulo
        ALGORITHMS_PATH = 'algoritmos'
        module_path = f'{ALGORITHMS_PATH}.{algorithm["algorithm"]}'
        
        # Importar o módulo dinamicamente
        try:
            module = importlib.import_module(module_path)
        except ModuleNotFoundError as e:
            print(f"Erro ao importar o módulo {module_path}: {e}")
            continue
        
        # Verificar se a função desejada está no módulo
        if hasattr(module, 'run'):
            function = getattr(module, 'run')
            # Passar parâmetros para a função
            del algorithm['algorithm']
            
            result = function(normalizados, algorithm)
            print(result)
        else:
            print(f"Função 'run' não encontrada no módulo {module_path}")
    return render_template("data.html", tables=[normalizados["x_train"].to_html(classes='data')], titles=normalizados["x_train"].columns.values)
