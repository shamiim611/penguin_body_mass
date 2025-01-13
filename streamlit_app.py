
import streamlit as st
import pandas as pd
import numpy as np
import sklearn


st.title('Machine learning app')

st.info('This is an app for a machine learning model that predicts penguin body mass')
with st.expander('Data'):
  st.write('**raw data**')
  df = pd.read_csv('https://github.com/shamiim611/penguin_body_mass/blob/master/penguins_clean.xls',
                    on_bad_lines = 'skip')
  df
 
