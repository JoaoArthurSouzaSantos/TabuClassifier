from flask import Flask, url_for, render_template, request, redirect, session, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import os
import importlib
import json
from process_functions.preprocessamento import preprocessing
from utils import algorithms

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
    
    # Pré-processar os dados
    normalizados = preprocessing(uploaded_file, label=json_data['label'], **json_data['processing'])

    # Obter a lista de algoritmos
    algorithms = json_data["algorithms"]
    
    # Estruturar os resultados para diferentes métricas
    accuracy_results = []
    f1_score_results = []
    recall_results = []
    precision_results = []
    algorithm_names = []
    algorithm_time = []
    
    for algorithm in algorithms:
        # Construir o caminho do módulo
        ALGORITHMS_PATH = 'algorithms'
        module_path = f'{ALGORITHMS_PATH}.{algorithm["algorithm"]}'
        
        try:
            module = importlib.import_module(module_path)
        except ModuleNotFoundError as e:
            print(f"Erro ao importar o módulo {module_path}: {e}")
            continue
        
        if hasattr(module, 'run'):
            function = getattr(module, 'run')
            del algorithm['algorithm']
            
            # Executar a função e armazenar o resultado
            result = function(normalizados, algorithm)
            
            # Suponha que o resultado contenha as métricas (ajuste de acordo com seus dados reais)
            accuracy_results.append(result['accuracy'])
            f1_score_results.append(result['f1_score'])
            recall_results.append(result['recall'])
            precision_results.append(result['precision'])
            algorithm_names.append(result['name'])
            algorithm_time.append(result['execution_time'])

    # Passar os resultados para o template
    return render_template(
        "results.html", 
        accuracy=accuracy_results, 
        f1_score=f1_score_results, 
        recall=recall_results, 
        precision=precision_results, 
        algorithms=algorithm_names,
        time=algorithm_time
    )


    #return render_template("data.html", tables=[normalizados["x_train"].to_html(classes='data')], titles=normalizados["x_train"].columns.values)

if __name__ == '__main__':
    app.app_context().push()
    app.debug = True
    db.create_all()  # Create tables in MySQL
    app.run(host='0.0.0.0')
