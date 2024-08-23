| Dados        | Tipo     | Descrição   |
| :----------  | :-----   | :---------- |
| `Archive`    | `txt/csv`| Define o arquivo a ser enviado |
| `processing` | `Object` | Objeto contendo escolhas de pré-processamento  |
| `alghoritms` | `Object` | Objeto contendo todos os Algoritmos a ser utilizado |


### Processamento 

| Parâmetro                  | Tipo         | Descrição   |
| :----------                | :-----       | :---------- |
| `Normalize`                | `Boolean`    | Define o arquivo a ser enviado |
| `Input Missing Values`     | `Boolean`    | Objeto contendo escolhas de pré-processamento  |
| `Stardardize`              | `Boolean`    | Objeto contendo todos os Algoritmos a ser utilizado |
| `Enconde Categorical Data` | `Boolean`    | Objeto contendo todos os Algoritmos a ser utilizado |


## Algoritmos de classificação 


### Random Forest Classifier
| Parâmetro   | Tipo   | Descrição   |
| :---------- | :----- | :---------- |
| `n_estimators` | `inteiro` |  |
| `criterion` | `string` | |
| `Max_deph` | `Boolean` |  |
| `min_samples_split:` | `Boolean` |  |
|`n_jobs`|



### SVM
| Parâmetro   | Tipo   | Descrição   |
| :---------- | :----- | :---------- |
| `C` | `inteiro` |  |
| `kernel` | `string` | |
| `gamma` | `Boolean` |  |
| `degree` | `Boolean` |  |


### KNeighborsClassifier
| Parâmetro   | Tipo   | Descrição   |
| :---------- | :----- | :---------- |
| `n_neighbors` | `inteiro` |  |
| `weights` | `string` | |
| `algorithm` | `Boolean` |  |
| `p` | `Boolean` |  |


### LogisticRegression
| Parâmetro   | Tipo   | Descrição   |
| :---------- | :----- | :---------- |
| `penalty` | `inteiro` |  |
| `C` | `string` | |
| `solver` | `Boolean` |  |
| `max_iter` | `Boolean` |  |
