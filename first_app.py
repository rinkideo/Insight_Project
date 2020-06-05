import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('predictNICU')
st.write("Here's our first attempt predict the risk of NICU admission")

@st.cache
def load_data():
    df = pd.read_csv("CSV2018Head1.csv")
    return df

# Will only run once if already cached
df = load_data()

st.write(df.shape)


option = st.selectbox(
    'Expectant Mothers Age? Choose from 1: Under 15 Years, 2: 15-19 years, 3: 20-24 years, 4: 25-29 years , 5: 30-34 years, 6: 35-39 years, 7: 40-44 years, 8: 45-49 years, 9: 50-54 years' ,
     df['MAGER9'].unique())

'You selected: ', option



option = st.selectbox(
    'Expectant Mothers BMI? Choose from 1: Underweight <18.5, 2: Normal 18.5-24.9 , 3: Overweight 25.0-29.9, 4: Obesity I 35.0-34.9, 5: Obesity II 35.0-39.9, 6: Extreme Obesity III ≥ 40.0 ',
     df['BMI_R'].unique())

'You selected: ', option

option = st.selectbox(
    'Expectant Mothers Risk Factors?' ,
     df['BMI_R'].unique())

'You selected: ', option


st.write('Probability of emergency is:')