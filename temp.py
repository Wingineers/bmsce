# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

a=pd.read_csv("C:/Users/Shreyash/Downloads/data1.csv")
a=a.dropna()
#creating Function to retreive given and predicted data of a person given by its unique id

def fun():
    x=input("Enter Id\n")
    x=int(x)
    b= a[['hypertension','heart_disease','avg_glucose_level','CKD(%)','diabetes_positive_proba','bmi']][a['id']==x].values
    print("Hypertension: ",b[0][0],'\n')
    print("heart_diesease: ",b[0][1],'\n')
    print("Glucose_Level: ",b[0][2],'\n')
    print("BMI: ",b[0][5],'\n')
    
    print("\n")
    print("Probability of being a Diabeties Patient is: ",b[0][4],'%','\n')
    print("Probability of being a Kidney Disease Patient is: ",b[0][3],'%','\n')

fun()
