# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:42:17 2023

@author: wania
"""

#IMPORTING THE LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt

#READING THE DATA FROM CSV FILE
data = pd.read_csv('advertising.csv')
print(data.head())

#TO VISUALISE DATA
fig, axs = plt.subplots(1,3,sharey = True)
data.plot(kind='scatter',x='TV',y='Sales',ax=axs[0],figsize=(16,8))
data.plot(kind='scatter',x='Radio',y='Sales',ax=axs[1])
data.plot(kind='scatter',x='Newspaper',y='Sales',ax=axs[2])

#CREATING X & Y FOR LINEAR REGRESSION
feature_cols = ['TV']
X = data[feature_cols]
y = data.Sales

#IMPORTING LINEAR REGRESSION ALGO
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,y)

print(lr.intercept_)
print(lr.coef_)

result = 6.97+0.0554*50
print(result)

#CREATE A DATAFRAME WITH MIN AND MAX VALUE OF THE TABLE
X_new = pd.DataFrame({'TV':[data.TV.min(),data.TV.max()]})
print(X_new.head())

preds = lr.predict(X_new)
print(preds)

data.plot(kind = 'scatter',x='TV',y='Sales')
plt.plot(X_new,preds,c='red',linewidth=3)

import statsmodels.formula.api as smf
lm = smf.ols(formula='Sales ~ TV', data=data).fit()
print(lm.conf_int())

#FINDING THE PROBABILITY VALUES
print(lm.pvalues)

#FINDING THE R_SQUARED VALUES
print(lm.rsquared)

#MULTI LINEAR REGRESSION
feature_cols = ['TV','Radio','Newspaper']
X = data[feature_cols]
y = data.Sales

lr = LinearRegression()
lr.fit(X,y)

print(lr.intercept_)
print(lr.coef_)

lm = smf.ols(formula='Sales ~ TV+Radio+Newspaper',data=data).fit()
print(lm.conf_int())
print(lm.summary())