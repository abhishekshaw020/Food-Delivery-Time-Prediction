import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OneHotEncoder

X_train=pd.read_csv('X_train',index_col=0)
def select_column(data):
    return data[['Distance_km', 'Weather', 'Traffic_Level', 'Time_of_Day','Vehicle_Type', 'Preparation_Time_min']]

def create_speed(data):
    data['Speed_[km/m]']=data['Distance_km']/data['Preparation_Time_min']
    return data

def drop_column(df):
    columns = ['Weather_Windy', 'Traffic_Level_Medium','Time_of_Day_Night','Vehicle_Type_Scooter']
    new_df = df.drop(columns,axis = 1)
    return new_df

def apply_transformer(sample):
    transformer = ColumnTransformer(
        transformers=[
            ('numerical',StandardScaler(),['Distance_km','Preparation_Time_min',
           'Speed_[km/m]']),
            ('categorical',OneHotEncoder(),['Weather', 'Traffic_Level', 'Time_of_Day',
           'Vehicle_Type'])
                    ],
        remainder='passthrough')
    sample_X_train = select_column(X_train)
    new_sample_X_train= create_speed(sample_X_train)
    transformer.fit(new_sample_X_train)
    new_sample=transformer.transform(sample)
    new_sample_df=pd.DataFrame(new_sample,columns=['Distance_km','Preparation_Time_min','Speed_[km/m]','Weather_Clear', 'Weather_Foggy', 'Weather_Rainy', 'Weather_Snowy',
           'Weather_Windy', 'Traffic_Level_High', 'Traffic_Level_Low',
           'Traffic_Level_Medium', 'Time_of_Day_Afternoon',
           'Time_of_Day_Evening', 'Time_of_Day_Morning', 'Time_of_Day_Night',
           'Vehicle_Type_Bike', 'Vehicle_Type_Car', 'Vehicle_Type_Scooter'])
    new_sample_df=drop_column(new_sample_df)
    return new_sample_df
