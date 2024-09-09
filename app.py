from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from utils import algorithms
import pandas as pd
import os
import json
from process_functions.preprocessamento import preprocessing
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
    # Aqui você pode processar os dados de todos os algoritmos selecionados
    # Por exemplo, renderizar uma página de resumo ou salvar em um banco de dados
    uploaded_file = request.files['file']
    data = request.form['data']
    json_data = json.loads(data)  
    
    print("Arquivo recebido:", uploaded_file.filename)
    print("Dados recebidos:", json_data)
    
    df, y = preprocessing(uploaded_file, **json_data['processing'])
    print(df)
    return render_template("data.html", tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/teste', methods=['GET'])
def teste():
    t = request.args['t']
    f = request.files['file']
    print(t)
    
    return "TESTE"
