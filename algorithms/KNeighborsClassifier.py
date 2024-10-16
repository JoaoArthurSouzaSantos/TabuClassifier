import logging
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score

# Configurar logging
logging.basicConfig(level=logging.INFO)

def tratar_strings(params):
    """Converte strings numéricas para inteiros ou floats, se necessário."""
    for key, value in params.items():
        try:
            if isinstance(value, str) and value.replace('.', '', 1).isdigit():
                params[key] = float(value) if '.' in value else int(value)
        except ValueError:
            logging.warning(f"Não foi possível converter o valor de {key}: {value}")
    return params

def run(norm, paramets):
    """Executa o KNeighborsClassifier com os parâmetros fornecidos e os dados normalizados."""
    try:
        params = tratar_strings(paramets)
        logging.info(f"Parâmetros tratados: {params}")
        
        model = KNeighborsClassifier(**params)
        model.fit(norm["x_train"], norm["y_train"])
        y_pred = model.predict(norm["x_test"])
        
        accuracy = accuracy_score(norm["y_test"], y_pred)
        precision = precision_score(norm["y_test"], y_pred, average='macro')
        recall = recall_score(norm["y_test"], y_pred, average='macro')
        f1 = f1_score(norm["y_test"], y_pred, average='macro')
        
        logging.info(f"Acurácia: {accuracy}")
        logging.info(f"Precisão: {precision}")
        logging.info(f"Recall: {recall}")
        logging.info(f"F1-Score: {f1}")
        
        return {
            'name': 'K-Nearest Neighbors',
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1
        }
    
    except ValueError as ve:
        logging.error(f"Erro de valor nos parâmetros: {ve}")
        return None
    except Exception as e:
        logging.error(f"Erro inesperado: {e}")
        return None
