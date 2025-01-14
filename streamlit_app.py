
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
                     
  df
  st.write('**X**')
  X = df.drop(columns= 'Body Mass (g)', axis =1)
  X
  st.write('**y**')
  y = df['Body Mass (g)']
  y
with st.expander('Data visualization'):
  st.scatter_chart(df, x= 'Flipper Length (mm)', y ='Body Mass (g)', color ='Species')
  st.scatter_chart(df, x= 'Culmen Length (mm)', y ='Body Mass (g)', color ='Species')
  st.scatter_chart(df, x= 'Culmen Depth (mm)', y ='Body Mass (g)', color ='Species')
  st.scatter_chart(df, x= 'Delta 15 N (o/oo)', y ='Body Mass (g)', color ='Species')

# input features
with st.sidebar:
  st.header('Input features')
  Species = st.selectbox('Species',('Adelie Penguin','Gentoo penguin','Chinstrap penguin'))
  Culmen_length = st.slider('Culmen Length (mm)',32.1,59.6,44.25)
  Culmen_Depth = st.slider('Culmen Depth (mm)',13.1,21.5,17.4)
  Flipper_Length =st.slider('Flipper length (mm)',172,231,197)
  Sex = st.selectbox('Sex',('MALE','FEMALE'))
  Delta_15_N = st.slider('Delta 15 (o/oo)',7.6,10.0,8.7)
  Delta_13_C  =st.slider('Delta 13 (o/oo)',-27.01,-23.8,-25.8)
#create a dataframe
data = {'Species':Species,
        'Culmen Length (mm)':Culmen Length (mm),
         'Culmen Depth (mm)':Culmen Depth (mm),
        'Flipper length (mm)': Flipper length (mm),
        'Sex':Sex,
        'Delta 15 (o/oo)': Delta 15 (o/oo),
        'Delta 13 (o/oo)': Delta 13 (o/oo)}
input_df = pd.DataFrame(data, index=[0])
input_penguins = pd.concat([input_df, X], axis =0)
# build pipeline and model
# Select the numerical/categorical columns
numerical_cols = X.select_dtypes(include= ['float64']).columns
categorical_cols = X.select_dtypes(include= ['object']).columns

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

#train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=X['Species'], random_state=0
)
#ridge_model_building
model = Ridge(alpha =0.1)
#model evaluation using train data
complete_pipeline = Pipeline([('preprocessor',preprocessor),
                 ('estimator',Ridge(alpha =0.1))
                 ])
complete_pipeline.fit(X_train, y_train)

 #apply model to make predictions
predictions = complete_pipeline.predict(X_train)
predicted_mass = complete_pipeline.predict(input_df)
predicted_mass
                     
                     
                     
                     
  
  
  
  
 
 
