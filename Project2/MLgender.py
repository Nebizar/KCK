# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 15:16:05 2018

@author: Krzysztof Pasiewicz
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('voice.csv')
dataset = dataset.rename(columns={'label': 'gender'})
dataset2=dataset[['median','IQR','Q25','sp.ent','sd','sfm','meanfreq','gender']]
X = np.array(dataset2.drop(['gender'], 1))
y = np.array(dataset2['gender'])

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting classifier to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)