
import streamlit as st
import pandas as pd
import numpy as np
import sklearn


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
  Culmen_length = st.slider('Culmen length (mm)',32.1,59.6,44.25)
  Culmen_Depth = st.slider('Culmen Depth (mm)',13.1,21.5,17.4)
  Flipper_Length =st.slider('Flipper length (mm)',172,231,197)
  Sex = st.select_box('Sex',('MALE','FEMALE'))
  Delta_15_N = st.slider('Delta 15 (o/oo)',7.6,10,8.7)
  Delta_13_C  =st.slider('Delta 13 (o/oo)',-27.01,-23.8,-25.8)                       
  
  
  
  
 
 
