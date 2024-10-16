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
