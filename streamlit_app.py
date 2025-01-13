
import streamlit as st
import pandas as pd
import numpy as np
import sklearn


st.title('Machine learning app')

st.info('This is an app for a machine learning model that predicts penguin body mass')
df = pd.read_excel('https://github.com/shamiim611/penguin_body_mass/blob/master/penguins_clean.xls')
df
