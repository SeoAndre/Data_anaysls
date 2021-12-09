# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 18:02:34 2021

@author: Hamartia
"""
'''
선형회귀분석
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import datasets, linear_model, tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsRegressor
model=KNeighborsRegressor(n_jobs=-1)
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import mean_squared_error,r2_score
'''
예시:당뇨병
'''
#diabetes_X,diabetes_Y=datasets.load_diabetes(return_X_y=(True))
#diabetes_X=diabetes_X[:,np.newaxis,2]
#diabetes_X_train=diabetes_X[:-20]
#diabetes_X_test=diabetes_X[-20:]
#diabetes_Y_train=diabetes_Y[:-20]
#diabetes_Y_test=diabetes_Y[-20:]
#plt.scatter(diabetes_X_train,diabetes_Y_train)
#regr=linear_model.LinearRegression()
#regr.fit(diabetes_X_train,diabetes_Y_train)
#diabetes_Y_pred=regr.predict(diabetes_X_test)
#print("Coefficients: \n",regr.coef_)
#print("Mean squared error: %.2f" % 
#      mean_squared_error(diabetes_Y_test,diabetes_Y_pred))
#print("Coefficient of determination: %.2f" % 
#      r2_score(diabetes_Y_test, diabetes_Y_pred))
#plt.scatter(diabetes_X_test, diabetes_Y_test, color="black")
#plt.plot(diabetes_X_test, diabetes_Y_pred, 
#         color="blue", linewidth=3)
#iris=load_iris()
#X,y=iris.data, iris.target
#clf=tree.DecisionTreeClassifier()
#clf=clf.fit(X,y)
#plt.figure(figsize=(12,12))
#tree.plot_tree(clf)
'''
따릉이 데이터를 활용한 시각화
'''
train=pd.read_csv("C:/Users/yjss1/Desktop/e스포츠 데이터 분석가 양성과정/따릉이/따릉이/train.csv")
test=pd.read_csv("C:/Users/yjss1/Desktop/e스포츠 데이터 분석가 양성과정/따릉이/따릉이/test.csv")
submission=pd.read_csv("C:/Users/yjss1/Desktop/e스포츠 데이터 분석가 양성과정/따릉이/따릉이/submission.csv")
'''
print(train.head())
print(test.head())
print(submission.head())
print(train.tail())
print(train.shape)
print(test.shape)
print(submission.shape)
train.info()
'''
#train[['hour','count']].groupby('hour').mean()
#plt.plot('hour','count','*',data=train)
#train.columns
#plt.plot('hour','hour_bef_humidity','yo',data=train)
#plt.plot('hour','count','r+',data=train)
#plt.plot('hour','hour_bef_visibility','c^',data=train)

#sns.boxplot(x='hour',y='hour_bef_humidity',data=train)
#sns.pairplot(train[['hour','hour_bef_humidity',
#                    'hour_bef_visibility']])
#sns.jointplot('hour','count',data=train, alpha=0.1)
#sns.violinplot(x='hour', y='hour_bef_humidity',data=train)
#sns.relplot(x='hour',y='hour_bef_humidity',
#            hue='hour_bef_precipitation',
#            size='count',data=train)
#plt.figure(figsize=(12,12))
#sns.heatmap(train.corr(),annot=True)
#sns.lmplot(x='hour',y='count',data=train)
#columns=['hour','hour_bef_temperature']
#X_train=train[columns]
#y_train=train['count']
#X_test=test[columns]

#model_5=KNeighborsRegressor(n_jobs=-1, n_neighbors=5)
#model_7=KNeighborsRegressor(n_jobs=-1, n_neighbors=7)
#model_9=KNeighborsRegressor(n_jobs=-1, n_neighbors=9)
#kfold=KFold(n_splits=5,shuffle=True,random_state=10)
#np.mean(cross_val_score(model_7,X_train,y_train,
#                        cv=kfold,scoring='neg_mean_squared_error'))
#model_9.fit(X_train,y_train)

