
import streamlit as st
import pandas as pd
import numpy as np
import sklearn


st.title('Machine learning app')

st.info('This is an app for a machine learning model that predicts penguin body mass')
df = pd.read_excel('C:\Users\HP\OneDrive\Desktop\personal stuff\penguins_clean.xls')
df
