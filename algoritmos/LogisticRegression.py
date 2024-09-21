from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, f1_score, confusion_matrix

def tratar_strings(params):
    for key, value in params.items():
        try:
            if value.isdigit():
                params[key] = int(value)
            else: params[key] = float(value)
        except ValueError:
            print(f"Não foi possível converter o valor de {key}: {value}")
    return params
    
def run(norm, paramets):
    
    params = tratar_strings(paramets)

    model = LogisticRegression(**params)
    model.fit(norm["x_train"],norm["y_train"])
    
    try:
        y_pred = model.predict(norm["x_test"])
        confusion  =  confusion_matrix(norm["y_test"], y_pred)
        print(confusion)
        return confusion
    
    except ValueError:
        print("Sem dados para teste.")
        


