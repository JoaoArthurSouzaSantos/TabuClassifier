from flask import Flask, render_template, request, jsonify, redirect, url_for
from utils import algorithms
import pandas as pd
import json
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

@app.route('/submit', methods=['POST'])
def submit():
    # Aqui você pode processar os dados de todos os algoritmos selecionados
    # Por exemplo, renderizar uma página de resumo ou salvar em um banco de dados
    uploaded_file = request.files['file']
    data = request.form['data']
    
    json_data = json.loads(data)  
    print("Arquivo recebido:", uploaded_file.filename)
    print("Dados recebidos:", json_data)
    
    return jsonify( {"status":"success", "received_data": json_data})
    #return redirect(url_for('index'))
