import pandas as pd 


def data_ingestion():
    
    ''' 
    * Title: Telecom Customer Churn Prediction Model
    
    * Independent Column [X]: 'customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
       'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
       'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
       'PaymentMethod', 'MonthlyCharges', 'TotalCharges'
    
    * Target Column [y]:  'Churn'
    
    * Problem Statement: 
    1. To predict the churn rate 
    2. Use Clustering apporach to predict and classify the cluster pattern such as {l1,l2 & l3}   
    
    '''    
    df = pd.read_csv(r'C:\MLops_Telecom_ChurnPredictionModel\data\raw\churn.csv')
    
    return df
