from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from utils import algorithms
import pandas as pd
import os
import json
from process_functions.preprocessamento import preprocessing
import importlib
# from frontend.routes import home

app = Flask(__name__, template_folder="frontend/templates", static_folder="frontend/static")
# app.register_blueprint(home)

selected_algorithms = []

#criar um arquivo só pra rotas
@app.route('/')
def index():
    return render_template('index.html', algorithms=algorithms, selected_algorithms=selected_algorithms)

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
    df = pd.read_csv(uploaded_file)
    columns = df.columns
    return jsonify({"columns": columns.tolist()})

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
