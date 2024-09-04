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
                print("ovos")
                df[colum] = label_encoder.fit_transform(df[colum])
    
    y = df.pop("Case Closed")
    
     
    if normalize:
        df=MinMaxScaler(df)
    df = pd.DataFrame(df)
    
    
    return (df, y)