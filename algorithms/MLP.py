# algorithms/mlp.py
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def run(data, params):
    # Dividindo os dados em treino e teste
    X = data.drop(columns=[params['label']])  # Usando o label passado no JSON
    y = data[params['label']]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=params.get('test_size', 0.2), random_state=42)
    
    # Criando o modelo MLP
    mlp = MLPClassifier(hidden_layer_sizes=params.get('hidden_layer_sizes', (100,)),
                        activation=params.get('activation', 'relu'),
                        solver=params.get('solver', 'adam'),
                        max_iter=params.get('max_iter', 300),
                        random_state=42)
    
    # Treinando o modelo
    mlp.fit(X_train, y_train)
    
    # Fazendo previsões
    y_pred = mlp.predict(X_test)
    
    # Calculando métricas
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    
    # Retornando as métricas
    return {
        'algorithm': 'MLPClassifier',
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1
    }
