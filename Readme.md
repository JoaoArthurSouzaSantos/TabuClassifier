
<img src="https://img.shields.io/static/v1?label=Python&message=language&color=blue&style=for-the-badge&logo=Python"/>
<img src="https://img.shields.io/static/v1?label=Pandas&message=library&color=yellow&style=for-the-badge&logo=Pandas"/>
<img src="https://img.shields.io/static/v1?label=sklearn&message=library&color=red&style=for-the-badge&logo=scikitlearn"/>
<img src="https://img.shields.io/static/v1?label=numpy&message=library&color=red&style=for-the-badge&logo=numpy"/>


Flask
Pandas
Sklearn
Numpy

| Dados        | Tipo     | Descrição   |
| :----------  | :-----   | :---------- |
| `Archive`    | `txt/csv`| Define o arquivo a ser enviado |
| `processing` | `Object` | Objeto contendo escolhas de pré-processamento  |
| `alghoritms` | `Object` | Objeto contendo todos os Algoritmos a ser utilizado |


### Processamento 

| Parâmetro                  | Tipo         | Descrição   |
| :----------                | :-----       | :---------- |
| `label`|
| `Normalize`                | `Boolean`    | Define se os dados devem ser normalizados ou não  |
| `Input Missing Values`     | `Boolean`    | Define se os dados ausentes devem ser tratados ou não. |
| `Stardardize`              | `Boolean`    | Define se os dados devem ser transformados para ter média zero e desvio padrão um. |
| `Enconde Categorical Data` | `Boolean`    | Especifica se dados categóricos devem ser convertidos em formato numérico. |


## Algoritmos de classificação 


### Random Forest Classifier
| Parâmetro   | Tipo   | Descrição   |
| :---------- | :----- | :---------- |
| `n_estimators` | `inteiro` | Defrine o número de árvores na floresta. |
| `criterion` | `string` | Define a função usada para medir a qualidade da divisão, podendo ser gini ou entropy. |
| `Max_deph` | `inteiro` | Define a profundidade maxima das arvores. |
| `min_samples_split` | `inteiro` | Define número mínimo de amostras. |
|`n_jobs`|  `inteiro` | número de Threads a serem utilizadas para as operações |



### SVM
| Parâmetro   | Tipo   | Descrição   |
| :---------- | :----- | :---------- |
| `C` | `float` |  |
| `kernel` | `string` | |
| `gamma` | `float` |  |
| `degree` | `inteiro` |  |


### KNeighborsClassifier
| Parâmetro   | Tipo   | Descrição   |
| :---------- | :----- | :---------- |
| `n_neighbors` | `inteiro` |  |
| `weights` | `string` | |
| `algorithm` | `string` |  |
| `p` | `inteiro` |  |


### LogisticRegression
| Parâmetro   | Tipo   | Descrição   |
| :---------- | :----- | :---------- |
| `penalty` | `string` |  |
| `C` | `float` | |
| `solver` | `string` |  |
| `max_iter` | `inteiro` |  |
