from flask import Flask, render_template, request, jsonify, Blueprint
import pandas as pd
import os
import importlib
import json
from process_functions.preprocessamento import preprocessing
from utils import algorithms

app_algorithm = Blueprint('route_algorithms', __name__, url_prefix="/algorithm", template_folder="frontend/templates", static_folder="frontend/static")

# Configure MySQL connection

selected_algorithms = []


@app_algorithm.route('/index')
def index():
    return render_template('index.html', algorithms=algorithms, selected_algorithms=selected_algorithms)

@app_algorithm.route('/add_algorithm', methods=['POST'])
def add_algorithm():
    algorithm_name = request.json['algorithm']
    selected_algorithm = next(algo for algo in algorithms if algo['name'] == algorithm_name)
    selected_algorithms.append(selected_algorithm)
    rendered_html = render_template('algorithm_item.html', algorithm=selected_algorithm)
    return jsonify({"html": rendered_html})

@app_algorithm.route('/remove_algorithm', methods=['POST'])
def remove_algorithm():
    algorithm_name = request.json['algorithm']
    global selected_algorithms
    selected_algorithms = [algo for algo in selected_algorithms if algo['name'] != algorithm_name]
    return jsonify({"success": True})

@app_algorithm.route('/file', methods=["POST"])
def file():
    uploaded_file = request.files['file']
    try:
        df = pd.read_csv(uploaded_file)
        columns = df.columns
        return jsonify({"columns": columns.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app_algorithm.route('/submit', methods=['POST'])
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
            # algorithm_time.append(result['execution_time'])   

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