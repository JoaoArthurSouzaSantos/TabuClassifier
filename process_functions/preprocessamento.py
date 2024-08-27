import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

def preprocessing(upload_file,json_data, normalize, input, standardize, encode):
    
    y = df.pop(0)
    
    df=pd.read_csv(upload_file)
    proc=json_data['processing']
    
    if input:
       df= df.dropna()
        
    if encode:
        label_encoder = LabelEncoder()
        
        for colum in df.columns:
            if (type(df[colum][0]) == 'str'):
                df[colum] = label_encoder.fit_transform(df[colum])
            
    if normalize:
        df=MinMaxScaler(df)
    
    return (df, y)