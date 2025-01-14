
import streamlit as st
import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import Ridge  
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split



st.title('Machine learning app')

st.info('This is an app for a machine learning model that predicts penguin body mass')
with st.expander('Data'):
  st.write('**raw data**')
  
  df = pd.read_csv('https://raw.githubusercontent.com/shamiim611/penguin_body_mass/refs/heads/master/penguins_clean.xls')
  df.columns = df.columns.str.replace(' ', '_')
                  
  df
  st.write('**X**')
  X = df.drop(columns= 'Body_Mass_(g)', axis =1)
  X.dropna()
  st.write('**y**')
  y = df['Body_Mass_(g)']
  y
with st.expander('Data visualization'):
  st.scatter_chart(df, x= 'Flipper_Length_(mm)', y ='Body_Mass_(g)', color ='Species')
  st.scatter_chart(df, x= 'Culmen_Length_(mm)', y ='Body_Mass_(g)', color ='Species')
  st.scatter_chart(df, x= 'Culmen_Depth_(mm)', y ='Body_Mass_(g)', color ='Species')
  st.scatter_chart(df, x= 'Delta_15_N_(o/oo)', y ='Body_Mass_(g)', color ='Species')

# input features
with st.sidebar:
  st.header('Input features')
  Species = st.selectbox('Species',('Adelie Penguin','Gentoo penguin','Chinstrap penguin'))
  Culmen_Length= st.slider('Culmen_Length_(mm)',32.1,59.6,44.25)
  Culmen_Depth = st.slider('Culmen_Depth_(mm)',13.1,21.5,17.4)
  Flipper_length =st.slider('Flipper_length_(mm)',172,231,197)
  Sex = st.selectbox('Sex',('MALE','FEMALE'))
  Delta_15= st.slider('Delta_15_N_(o/oo)',7.6,10.0,8.7)
  Delta_13  =st.slider('Delta_13_C_(o/oo)',-27.01,-23.8,-25.8)
#create a dataframe
data = {'Species': Species,
        'Culmen_Length_(mm)':Culmen_Length ,
         'Culmen_Depth_(mm)':Culmen_Depth,
        'Flipper_length_(mm)':Flipper_length ,
        'Sex':Sex,
        'Delta_15_N_(o/oo)': Delta_15,
        'Delta_13_C_(o/oo)':Delta_13  }
input_df = pd.DataFrame(data, index=[0])
input_df
input_penguins = pd.concat([input_df, X], axis =0)
input_penguins
# build pipeline and model
# Select the numerical/categorical columns
numerical_cols = input_penguins.select_dtypes(include= ['float64']).columns
categorical_cols = input_penguins.select_dtypes(include= ['object']).columns

# Numerical pipeline
numerical_transformer = Pipeline([('scaler',StandardScaler())])
#categorical pipeline
categorical_transformer = Pipeline([('encoder',OneHotEncoder( handle_unknown='ignore', drop='first'))
                                     ])
#combine 
preprocessor =  ColumnTransformer([
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
])


#ridge_model_building
model = Ridge(alpha =0.1)
#model evaluation using train data
complete_pipeline = Pipeline([('preprocessor',preprocessor),
                 ('estimator',Ridge(alpha =0.1))
                 ])
complete_pipeline.fit(input_penguins.dropna(), y)

 #apply model to make predictions
predictions = complete_pipeline.predict(input_penguins.dropna())
predicted_mass = complete_pipeline.predict(input_df.dropna())
st.write('Predicted Mass:', predicted_mass)

                     
                     
                     
                     
  
  
  
  
 
 
