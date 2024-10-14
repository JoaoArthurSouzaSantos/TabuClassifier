from sklearn.svm import SVC

class SVM:
    def __init__(self, **kwargs):
        """
        Inicializa o classificador SVM com parâmetros dinâmicos.
        :param kwargs: Parâmetros como kernel, C, gamma, etc.
        """
        # Parâmetros padrão
        default_params = {
            'kernel': 'rbf',
            'C': 1.0,
            'gamma': 'scale'
        }
        
        # Atualiza os parâmetros padrão com os valores recebidos no kwargs
        params = {**default_params, **kwargs}

        # Cria o modelo com os parâmetros recebidos
        self.model = SVC(**params)

    def fit(self, X_train, y_train):
        """
        Treina o modelo SVM.
        :param X_train: Dados de treino.
        :param y_train: Labels de treino.
        """
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        """
        Faz previsões no conjunto de dados de teste.
        :param X_test: Dados de teste.
        :return: Previsões do modelo.
        """
        return self.model.predict(X_test)
