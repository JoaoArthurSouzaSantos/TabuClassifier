import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

def preprocessing(upload_file, train ,normalize, dropNan, encode):
    
    train = int(train)
    teste = 100 - train
    
    
    
    df=pd.read_csv(upload_file)
    
    
    if dropNan:
       df = df.dropna()
        
    if encode:
        label_encoder = LabelEncoder()
        
        for colum in df.columns:
           
            if (type(df[colum][0]) == str):
                df[colum] = label_encoder.fit_transform(df[colum])
    
    y = df.pop("Case Closed")
    
     
    if normalize:
        scaler=MinMaxScaler()
        scaled_data=scaler.fit_transform(df)
        
        df=pd.DataFrame(scaled_data,columns=df.columns)
        
    
    
    return df, y