from flask import Flask, render_template, request, redirect, url_for

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        algorithm_name = request.form['algorithm']
        selected_algorithm = next(algo for algo in algorithms if algo['name'] == algorithm_name)
        selected_algorithms.append(selected_algorithm)
    return render_template('index.html', algorithms=algorithms, selected_algorithms=selected_algorithms)

@app.route('/submit', methods=['POST'])
def submit():
    return render_template('submit.html', selected_algorithms=selected_algorithms)

if __name__ == "__main__":
    app.run(debug=True)
