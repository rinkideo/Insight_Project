# Insight Project 
## Home Birth Risk Prediction
<img src="baby21.JPG" alt="Drawing" style="width: 200px;"/>

As part of the [Insight Data Science Fellowship](https://insightfellows.com/), I did a project on homebirth risk prediction wherein I built an [web app](https://homebirth-safe.herokuapp.com) which would help the expectant mother in Decision-Making about Birthplace Choices.This project was completed in 3 weeks.

**Context:** There has been an increasing trend in the number of homebirths in US because of several reasons like desire for minimum medical intervention, cost factors, familiar environmnet, religious concerns etc. According to an article in Birth [Birth. 2019;46(2):279?288](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6642827/#:~:text=Home%20births%20increased%20by%2077%25%2C%20from%200.56%25%20of%20births,%E2%80%932017%20(Figure%202)), between year 2004-2017 there has been an increase in the number of home births by 77%. We anticipate a further increase in this number amid COVID pandemic as pregnant women are worried about the hospitals and turning to home birth.)

**Problem:** Due to unpredicted  complications the case has to be transferred to hospital. This may turn out to be expensive in terms of money as well as life of the mother and child.

**Solution:** Using historical data to predict if the home birth is safe based on mother physical characteristics and medical history.

**Dataset used:** Statistics of live births records in the United States by [CDC](https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm) for the year 2017 and 2018.

### Overall Steps of the project:

#### A. Data Pre-processing

* Extracted out-of-hospital live births records from the dataset.


* *Target Variable:* Considered 14 post pregnancy factors: Maternal morbidity factors (Admit to Intensive Care, Mother transferred, Maternal Transfusion, Ruptured Uterus etc) and Child abnormality condition (Admit to NICU, APGAR, Seizures, antibiotics etc.) to label the target variable. If any of these factors existed the target was labelled as RISK and if none existed then it was NO-RISK.


* *Input Variables:* 35 relevant pre-delivery features including the maternal physical characteristics, maternal risk factors, pregnancy history, pregnancy risk factors considered as the input variables.


* *Data Cleaning:* Filtered out the unknown/not stated categories. Recoded the categories with very high numerical value to a value close to the other existing categories in that feature. Combined redundant and biased features to make the data more meaningful.


#### B.Model training:

Cost Sensitive Logistic regression model with heuristic class weightage was performed to handle the severe class imbalance in the data. Weighted Random forest and XGB were also were performed but Logistic regression out performed these models with a recall value(for minority class "positive") of 0.77, likely due to the linear relationship between the target and the input variables.

#### C. The outcome of the project:
An interactive web app link was built using Streamlit and Heroku to predict if the home birth is safe or not safe.This app will help expectant mother in Decision-Making about Birthplace Choices. Expectant mothers can provide required factors like their physical characteristics and medical history as inputs to the app and check if it safe enough to gor for home birth.






