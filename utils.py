algorithms = [
    {
        "name": "DecisionTreeClassifier",
        "parameters": [
            {"name": "criterion", "type": "select", "options": ["gini", "entropy", "log_loss"]},
            {"name": "max_features", "type": "select", "options": ["sqrt", "auto", "log2"]},
            {"name": "max_depth", "type": "input", "value": ""},
            {"name": "splitter", "type": "select", "options": ["best", "random"]}
        ]
    },
    {
        "name": "RandomForestClassifier",
        "parameters": [
            {"name": "n_estimators", "type": "input", "value": ""},
            {"name": "criterion", "type": "select", "options": ["gini", "entropy", "log_loss"]},
            {"name": "max_features", "type": "select", "options": ["sqrt", "auto", "log2"]},
            {"name": "max_depth", "type": "input", "value": ""},
            {"name": "min_samples_split", "type": "input", "value": ""},
            {"name": "min_samples_leaf", "type": "input", "value": ""}
        ]
    },
    {
        "name": "SVM",
        "parameters": [
            {"name": "C", "type": "input", "value": ""},
            {"name": "kernel", "type": "select", "options": ["rbf", "linear", "poly", "sigmoid"]},
            {"name": "gamma", "type": "select", "options": ["scale", "auto"]},
            {"name": "degree", "type": "input", "value": ""}
        ]
    },
    {
        "name": "XGBoost",
        "parameters": [
            {"name": "n_estimators", "type": "input", "value": ""},
            {"name": "learning_rate", "type": "input", "value": ""},
            {"name": "max_depth", "type": "input", "value": ""},
            {"name": "subsample", "type": "input", "value": ""},
            {"name": "colsample_bytree", "type": "input", "value": ""}
        ]
    },
    {
        "name": "CatBoost",
        "parameters": [
            {"name": "iterations", "type": "input", "value": ""},
            {"name": "learning_rate", "type": "input", "value": ""},
            {"name": "depth", "type": "input", "value": ""},
            {"name": "l2_leaf_reg", "type": "input", "value": ""},
            {"name": "subsample", "type": "input", "value": ""}
        ]
    },
    {
        "name": "LightGBM",
        "parameters": [
            {"name": "n_estimators", "type": "input", "value": ""},
            {"name": "learning_rate", "type": "input", "value": ""},
            {"name": "max_depth", "type": "input", "value": ""},
            {"name": "num_leaves", "type": "input", "value": ""},
            {"name": "subsample", "type": "input", "value": ""}
        ]
    },
    {
        "name": "KNeighborsClassifier",
        "parameters": [
            {"name": "n_neighbors", "type": "input", "value": ""},
            {"name": "weights", "type": "select", "options": ["uniform", "distance"]},
            {"name": "algorithm", "type": "select", "options": ["auto", "ball_tree", "kd_tree", "brute"]},
            {"name": "p", "type": "input", "value": ""},
            {"name": "leaf_size", "type": "input", "value": ""}
        ]
    },
    {
        "name": "LogisticRegression",
        "parameters": [
            {"name": "penalty", "type": "select", "options": ["l2", "l1", "elasticnet", "none"]},
            {"name": "C", "type": "input", "value": ""},
            {"name": "solver", "type": "select", "options": ["lbfgs", "newton-cg", "liblinear", "sag", "saga"]},
            {"name": "max_iter", "type": "input", "value": ""}
        ]
    },
    {
        "name": "GaussianNB",
        "parameters": [
            {"name": "var_smoothing", "type": "input", "value": ""},
        ]
    }
]
