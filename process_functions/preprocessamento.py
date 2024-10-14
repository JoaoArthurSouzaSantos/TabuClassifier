import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

def preprocessing(upload_file, label ,train ,normalize, dropNan, encode):    
    
    df=pd.read_csv(upload_file)
    df = df.sample(frac=1).reset_index(drop=True)

    train_size =  int(train) / 100
    print(f"Size para treino: {train_size}")
    train = int(train_size * len(df))
    
    print(f"Para treino: {train}")
    if dropNan:
       df.dropna(inplace=True)
        
    if encode:
        label_encoder = LabelEncoder()
        
        for colum in df.columns:
           
            if (type(df[colum][0]) == str):
                df[colum] = label_encoder.fit_transform(df[colum])
    #df.pop('Report Number')
    y = df.pop(label)
    
    if normalize:
        scaler=MinMaxScaler()
        scaled_data=scaler.fit_transform(df)
        
        df=pd.DataFrame(scaled_data,columns=df.columns)
        
    x_train = df[:train]
    y_train = y[:train]

    x_test  = df[train:]
    y_test  = y[train:]
    
    return {"x_train":x_train, "y_train": y_train, "x_test": x_test, "y_test": y_test}