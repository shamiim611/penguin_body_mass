
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
  
  
 
 
