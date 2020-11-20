#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 22:05:17 2020

@author: shivam
"""

import numpy as np
import pandas as pd
import joblib
"""
df = pd.read_csv('Cat_Crop.csv')
#df=df.drop(['Water Requirement'],1)
df=df.dropna()
df.head()
X = np.array(df.drop(['Crop'],1))
Y = np.array(df['Crop'])

from sklearn import model_selection
x_train, x_test, y_train, y_test = model_selection.train_test_split(X,Y,test_size=0.20, shuffle = True)

"""
"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.datasets import make_classification
rfs = RandomForestClassifier(max_depth=9, random_state=40)                      
rfs.fit(x_train,y_train)
predictions=rfs.predict(x_test)
print(predictions)
print(accuracy_score(y_test, predictions)*100)
"""
"""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
neigh = KNeighborsClassifier()
neigh.fit(x_train,y_train)
predictions=neigh.predict(x_test)
print(predictions)
print(accuracy_score(y_test, predictions)*100)
"""
"""
from sklearn import tree
from sklearn.metrics import accuracy_score
dtree=tree.DecisionTreeClassifier()
dtree.fit(x_train,y_train)
predictions=dtree.predict(x_test)                                               #Main Model
print(predictions)
print(accuracy_score(y_test, predictions)*100)
filename = 'finalized_model.sav'
joblib.dump(dtree, filename)
"""

filename = "finalized_model.sav"
loaded_model = joblib.load(filename)
temp=[2,]
inp_array=np.array(temp)
inp_array=inp_array.reshape(1,-1)
print(inp_array)
prediction=loaded_model.predict(inp_array)
print(prediction)
    


"""
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
clf = GaussianNB()
clf.fit(x_train, y_train)
predictions = clf.predict(x_test)
print(predictions)
print(accuracy_score(y_test, predictions)*100)
print(confusion_matrix(y_test, predictions))
"""
