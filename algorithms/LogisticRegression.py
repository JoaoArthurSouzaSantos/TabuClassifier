import logging
from sklearn.linear_model import LogisticRegression
import time  # Importando o módulo time para medir o tempo de execução
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score, confusion_matrix

# Configurar logging
logging.basicConfig(level=logging.INFO)

def tratar_strings(params):
    """Converte strings numéricas para inteiros ou floats, se necessário."""
    for key, value in params.items():
        try:
            # Tenta converter se for um número em formato string
            if isinstance(value, str) and value.replace('.', '', 1).isdigit():
                if '.' in value:
                    params[key] = float(value)
                else:
                    params[key] = int(value)
        except ValueError:
            logging.warning(f"Não foi possível converter o valor de {key}: {value}")
    return params

def run(norm, paramets):
    """Executa o RandomForestClassifier com os parâmetros fornecidos e os dados normalizados."""
    try:
        # Iniciar a contagem de tempo
        start_time = time.time()
        
        # Tratar e validar os parâmetros
        params = tratar_strings(paramets)

        logging.info(f"Parâmetros tratados: {params}")
        
        # Instanciar o modelo RandomForestClassifier passando os parâmetros tratados diretamente
        model = LogisticRegression(**params)  # Descompactar os parâmetros no modelo
        
        # Treinar o modelo
        model.fit(norm["x_train"], norm["y_train"])
        
        # Prever no conjunto de teste
        y_pred = model.predict(norm["x_test"])
        
        # Calcular matriz de confusão e outras métricas
        accuracy = accuracy_score(norm["y_test"], y_pred)
        precision = precision_score(norm["y_test"], y_pred, average='macro')
        recall = recall_score(norm["y_test"], y_pred, average='macro')
        f1 = f1_score(norm["y_test"], y_pred, average='macro')
        
        # Calcular o tempo de execução
        execution_time = time.time() - start_time

        logging.info(f"Acurácia: {accuracy}")
        logging.info(f"Precisão: {precision}")
        logging.info(f"Recall: {recall}")
        logging.info(f"F1-Score: {f1}")
        logging.info(f"Tempo de execução: {execution_time:.4f} segundos")

        # Retornar resultados
        return {
            'name': 'Random Forest',  # Nome do algoritmo
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1,
            'execution_time': execution_time  # Adicionando o tempo de execução ao retorno
        }
    
    except ValueError as ve:
        logging.error(f"Erro de valor nos parâmetros: {ve}")
        return None
    except Exception as e:
        logging.error(f"Erro inesperado: {e}")
        return None
