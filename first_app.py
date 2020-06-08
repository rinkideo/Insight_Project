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
    df = pd.read_csv('cleandata.csv',nrows=100)
    return df

# Will only run once if already cached
df = load_data()

st.write(df.shape[0])

import pickle

#
# Load model
## Save to file in the current working directory
pkl_filename = "logreg_model.pkl"
# Load from file
with open(pkl_filename, 'rb') as file:
    my_model = pickle.load(file)

# Prediction
def predict_nicu_ad(data):
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

           
Age = st.slider("Choose your age: ", min_value=10,   
                   max_value=60, value=50, step=1)
##input2a
Pre_Preg_Weight = st.slider("Choose your weight(lb): ", min_value=50, max_value=350, value=300, step=1)
    ##input2b
Height = st.slider("Choose your height(inch): ", min_value=35,max_value=100, value=65, step=1)
    ##Input2 calculated from 2a and 2b
BMI_R = bmi_calc(Pre_Preg_Weight,Height)

Weight = st.slider("Choose your weight in pounds: ", min_value=70,   
                   max_value=350, value=280, step=1)


bfacil_option = st.selectbox('Where do you like the birthplace to be? 1: Hospital, 2: Freestanding Birth Center, 3: Home (intended), 4: Home (not intended), 5: Home (unknown if intended), 6: Clinic / Doctor’s Office, 7: Other',
                  (1,2,3,4,5,6,7))


priorterm = st.text_input("No. of prior other terminations","Type Here")
#priorterm = int(priorterm_option)

illb_r = st.text_input("Interval Since Last Live Birth(months)","Type Here")
#illb_r = int(illb_option)

previs = st.text_input("Number of prenatal visits done","Type Here")
#previs = int(previs_option)

rf_cesarean = st.text_input("Number of Previous Cesareans ","Type Here")
#rf_cesarean = int(rf_ces_option)

rf_option=st.selectbox('Count the Number of Pre-pregnancy risk factors out of following  exists/existed: Pre-pregnancy Diabetes, Gestational Diabetes, Pre-pregnancy Hypertension, Gestational Hypertension, Hypertension Eclampsia, Previous Preterm Birth, Infertility Treatment Used, Fertility Enhancing Drugs, Asst. Reproductive Technology',
                      (0,1,2,3,4,5,6,7,8,9))
cig_r = st.text_input('total Number of cigarettes (or packs) smoked from 3months prior to becoming pregnant till date ',"Type Here")

#cig_r = int(cig_options)

ip_option=st.selectbox('Count the Number of infections exists/existed: among gonorrhea; syphilis; chlamydia; hepatitis B; and hepatitis C ', (0,1,2,3,4,5))


test_data = [Age,bfacil_option,priorterm,illb_r,previs,BMI_R,rf_cesarean,rf_option,cig_r,ip_option]


COLUMN_NAMES = ['MAGER9', 'BFACIL', 'PRIORTERM', 'ILLB_R11', 'PREVIS_REC', 
                'BMI_R','RF_CESARN', 'RF_Total', 'CIG_Total', 'IP_Total']
test = pd.DataFrame(columns=COLUMN_NAMES,dtype='int')
test.loc[0,:]=test_data
df_test = test

if st.button("Predict"):
    result = predict_nicu_ad(df_test)
    if result[0] == 0:
        prediction = 'NO RISK OF NICU Admission'
    else:
        result[0] == 1
        prediction = 'YES THERE IS RISK OF NICU Admission'
    st.write(prediction)    
       




















