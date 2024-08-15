from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Lista de algoritmos com parâmetros
algorithms = [
    {
        "name": "RandomForestClassifier",
        "parameters": [
            {"name": "n_estimators", "type": "input", "value": ""},
            {"name": "criterion", "type": "select", "options": ["gini", "entropy"]},
            {"name": "max_depth", "type": "input", "value": ""},
            {"name": "min_samples_split", "type": "input", "value": ""}
        ]
    },
    {
        "name": "SVM",
        "parameters": [
            {"name": "C", "type": "input", "value": ""},
            {"name": "kernel", "type": "select", "options": ["linear", "poly", "rbf", "sigmoid"]},
            {"name": "gamma", "type": "select", "options": ["scale", "auto"]},
            {"name": "degree", "type": "input", "value": ""}
        ]
    },
    {
        "name": "KNeighborsClassifier",
        "parameters": [
            {"name": "n_neighbors", "type": "input", "value": ""},
            {"name": "weights", "type": "select", "options": ["uniform", "distance"]},
            {"name": "algorithm", "type": "select", "options": ["auto", "ball_tree", "kd_tree", "brute"]},
            {"name": "p", "type": "input", "value": ""}
        ]
    },
    {
        "name": "LogisticRegression",
        "parameters": [
            {"name": "penalty", "type": "select", "options": ["l1", "l2", "elasticnet", "none"]},
            {"name": "C", "type": "input", "value": ""},
            {"name": "solver", "type": "select", "options": ["newton-cg", "lbfgs", "liblinear", "sag", "saga"]},
            {"name": "max_iter", "type": "input", "value": ""}
        ]
    }
]

selected_algorithms = []

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
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
