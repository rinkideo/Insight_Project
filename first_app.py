import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('HomeBirth-SAFE')
st.write("Predict if Home Birth is SAFE for you")

import pickle

#
# Load model
## Save to file in the current working directory
pkl_filename = "hb_lgbm_model.pkl"
# Load from file
with open(pkl_filename, 'rb') as file:
    my_model = pickle.load(file)

# Prediction
def predict_home_birth_safe(data):
    result = my_model.predict(data)
    return result

def bmi_calc(wt,ht):
    BMI = round((wt/2.2) / ((ht*0.0254)**2))
    if BMI<18.5:
        BMI_R = 1
    if 18.5 < BMI< 25:
        BMI_R = 2
    if 25.0 <= BMI< 30.0:
        BMI_R = 3
    if 30 <= BMI< 35.0:
        BMI_R = 4
    if 35.0 <= BMI< 40:
        BMI_R = 5
    elif BMI >= 40.0:
        BMI_R = 6
    return BMI_R

def age_code_calc(age):
    if age <= 15:
        age_code = 1
    if 15< age <= 19:
        age_code = 2
    if 20<= age <= 24:
        age_code = 3
    if 25<= age <= 29:
        age_code = 4
    if 30<= age <= 34:
        age_code = 5
    if 35<= age <= 39:
        age_code = 6
    if 40<= age <= 44:
        age_code = 7
    if 45<= age <= 49:
        age_code = 8
    if 50 <=age <= 54:
        age_code = 9
    return age_code

def previs_code_calc(previss):
    if previss == 0:
        previss_code = 1
    if 1<= previss <= 2:
        previss_code = 2
    if 3<= previss <= 4:
        previss_code = 3
    if 5<= previss <= 6:
        previss_code = 4
    if 7<= previss <= 8:
        previss_code = 5
    if 9<= previss <= 10:
        previss_code = 6
    if 11<= previss <= 12:
        previss_code = 7
    if 13<= previss <= 14:
        previss_code = 8
    if 15<= previss <= 16:
        previss_code = 9
    if 17<= previss <= 18:
        previss_code = 10
    if 19<= previss:
        previss_code = 11
    
    return previss_code

def illb_code_calc(illbs):
    if 0<= illbs <= 3:
        illb_code = 0
    if 4<= illbs <= 11:
        illb_code = 1
    if 12<= illbs <= 17:
        illb_code = 2
    if 18<= illbs <= 23:
        illb_code = 3
    if 24<= illbs <= 35:
        illb_code = 4
    if 36<= illbs <= 47:
        illb_code = 5
    if 48<= illbs <= 59:
        illb_code = 6
    if 60<= illbs <= 71:
        illb_code =7
    if 72<= illbs:
        illb_code = 8
    
    return illb_code

def tbo_code_calc(tbo_val):
    if 1 <= tbo_val <= 7:
        tbo_code = tbo_val
    if tbo_val >= 8:
        tbo_code = 8   
    return tbo_code

Age = st.slider("Choose your age: ", min_value=10,   
                   max_value=54, value=44, step=1)
MAGER9 = age_code_calc(Age)
##input2a
Pre_Preg_Weight = st.slider("Choose your pre-pregnancy weight(lb): ", min_value=50, max_value=350, value=300, step=1)
    ##input2b
Height = st.slider("Choose your height(inch): ", min_value=35,max_value=100, value=65, step=1)
    ##Input2 calculated from 2a and 2b
BMI_R = bmi_calc(Pre_Preg_Weight,Height)

Curr_Weight = st.slider("Choose your Current weight in pounds: ", min_value=100,   
                   max_value=400, value=280, step=1)

Wt_gain = Curr_Weight-Pre_Preg_Weight
ILP_R = st.slider("Interval since last pregnancy(months): ", min_value=0,   
                   max_value=300, value=300, step=1)

PRECARE = st.slider("Month from which prenatal care began: ", min_value=0,   
                   max_value=10, value=10, step=1)

previs = st.slider("Number of prenatal visits done: ", min_value=1,   
                   max_value=30, value=30, step=1)
previs_rec = previs_code_calc(previs)

smoke =st.selectbox('Do you smoke 1: YES, 0:NO', (0,1))

priorterm = st.text_input("No. of prior other terminations","Type Here")
#priorterm = int(priorterm)

illb = st.slider("Interval Since Last Live Birth(months): ", min_value=0,   
                   max_value=84, value=84, step=1)
illb_r11 = illb_code_calc(illb)

TBO = st.slider("Total Birth order: ", min_value=0,   
                   max_value= 10, value=10, step=1)
TBO_rec = tbo_code_calc(TBO)

rf_cesarean = st.text_input("Number of Previous Cesareans ","Type Here")
#rf_cesarean = int(rf_cesarean)


test_data = [Wt_gain,Curr_Weight,Pre_Preg_Weight,ILP_R,Height,PRECARE,previs_rec,MAGER9,illb_r11,TBO_rec,priorterm,smoke,BMI_R,rf_cesarean]


COLUMN_NAMES = ['WTGAIN', 'DWGT_R', 'PWGT_R', 'ILP_R', 'M_HT_IN', 'PRECARE',
       'PREVIS_REC', 'MAGER9', 'ILLB_R11', 'TBO_REC', 'PRIORTERM', 'WIC',
       'BMI_R', 'RF_CESARN']
test = pd.DataFrame(columns=COLUMN_NAMES,dtype='int')
test.loc[0,:]=test_data
df_test = test

if st.button("Predict"):
    result = predict_home_birth_safe(df_test)
    if result[0] == 0:
        prediction = 'Home Birth is SAFE for you'
    else:
        result[0] == 1
        prediction = 'THERE IS RISK: Home Birth NOT SAFE for you'
    st.write(prediction)    
       




















