# -*- coding: utf-8 -*-
"""loan_status_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mWjK6mgyNo4ZuvWQFOx6M__0mFEl0m38

### **Importing the dependencies**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""### **Importing the dataset**"""

dataset=pd.read_csv("train.csv")
dataset.shape

"""### **Visualizing various parameters of dataset**"""

import seaborn as sns
sns.set_theme(style="darkgrid")
sns.countplot(x="Gender", hue="Loan_Status", data=dataset)

sns.countplot(x="Education", hue="Loan_Status", data=dataset)

dataset.head(n=3)

"""### **Data Preprocessing**

> Dealing with 'Not Available' data
"""

dataset.isna().sum() # here isna() means "is not available"

# drop those not available rows
dataset.dropna(axis=0,inplace=True) # axis=0 means drop those 'rows' axis=1 means drop those 'columns'
dataset.isna().sum()

dataset.shape

""">Processing categorical data




"""

dataset=dataset.replace({'Gender':{'Male':0,'Female':1},'Married':{'Yes':1,'No':0},'Dependents':{'3+':4},'Education':{'Graduate':1,'Not Graduate':0},'Self_Employed':{'Yes':1, 'No':0}, 'Property_Area':{'Urban':2, 'Rural':0, 'Semiurban': 1}, 'Loan_Status':{'Y':1, 'N':0}})

#dropping 'Loan_ID' column
dataset=dataset.drop(columns=['Loan_ID',])

X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

print(X)

"""### **Splitting dataset into train and test set**"""

#Splitting dataset into training and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.1, random_state=2)

print(X_train.shape)
print(X_test.shape)
print(X.shape)

"""### **Feature Scaling**"""

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
print(X_train)

"""### **Initializing and training the model**"""

from sklearn.svm import SVC
model=SVC(kernel='linear')
model.fit(X_train, y_train)

"""### **Predicting with the model**"""

y_pred=model.predict(sc.transform(X_test))

from sklearn.metrics import confusion_matrix, accuracy_score
print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))