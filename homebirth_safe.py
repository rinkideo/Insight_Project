import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('HomeBirth-SAFE')
st.image("baby1.jpg",width=200)
st.write("Predict if Home Birth is SAFE for you")
def main():
    import pickle

    # Load model
    pkl_filename = "cs_logreg_model.pkl"
    # Load from file
    with open(pkl_filename, 'rb') as file:
        my_model = pickle.load(file)
    
    # Prediction
    def predict_home_birth_safe(data):
        result = my_model.predict(data)
        return result
    
    def bmi_calc(wt,ht):
        BMI = round((wt/2.2) / ((ht*0.0254)**2))
        return BMI
    
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
    
    Age = st.slider("Choose your age: ", min_value=20,   
                       max_value=54, value=34, step=1)
    
    ##input2a
    Pre_Preg_Weight = st.slider("Choose your pre-pregnancy weight(lb): ", min_value=50, max_value=350, value=300, step=1)
        ##input2b
    Height = st.slider("Choose your height(inch): ", min_value=35,max_value=96, value=61, step=1)
        ##Input2 calculated from 2a and 2b
    BMI = bmi_calc(Pre_Preg_Weight,Height)
    Curr_Weight = st.slider("Choose your Current weight in pounds: ", min_value=100,   
                   max_value=260, value=160, step=1)

    Wt_gain = Curr_Weight-Pre_Preg_Weight
    
    PRECARE = st.number_input("Month from which prenatal care began: " ,0 ,9,1)
    
    previs = st.slider("Number of prenatal visits done: ", min_value=1,   
                       max_value=30, value=30, step=1)
    
    
    smoke = st.slider("Total No. of Cigarettes (packs) smoked from 3months before pregnancy till date : ", min_value=0,   
                       max_value=300, value=300, step=1)
    
    priorterm = st.number_input("No. of prior other terminations",0 ,10,1)
    #priorterm = int(priorterm)
    
    illb = st.slider("Interval Since Last Live Birth(months): ", min_value=0,   
                       max_value=84, value=84, step=1)
    illb_r11 = illb_code_calc(illb)
    
    TBO = st.slider("Total Birth order: ", min_value=1,   
                       max_value= 10, value=9, step=1)
    TBO_rec = tbo_code_calc(TBO)
    
    rf_cesarean = st.number_input("Number of Previous Cesareans ",0 ,10,1)
    
    rf_option=st.selectbox('Count the Number of Pre-pregnancy risk factors out of following  exists/existed: Pre-pregnancy Diabetes, Gestational Diabetes, Pre-pregnancy Hypertension, Gestational Hypertension, Hypertension Eclampsia, Previous Preterm Birth, Infertility Treatment Used, Fertility Enhancing Drugs, Asst. Reproductive Technology',
                          (0,1,2,3,4,5,6,7,8,9))
    
    
    test_data = [PRECARE,rf_option, rf_cesarean, TBO_rec, BMI, priorterm, illb_r11,previs,smoke, Wt_gain, Curr_Weight, Pre_Preg_Weight]
    
    
    COLUMN_NAMES = ['PRECARE', 'RF', 'RF_CESARN', 'TBO_REC', 'BMI', 'PRIORTERM', 'ILLB_R11', 'PREVIS', 'SMK', 
           'WTGAIN', 'DWGT_R', 'PWGT_R']
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
#st.write('Created by RInki Deo, Insight Data Fellow, Boston, MA')
if __name__=='__main__':
        main()
st.image("baby2.jpg",width=200)
st.write('** Created by: Rinki Deo, Insight Data Science Fellow, Boston, MA **')


















