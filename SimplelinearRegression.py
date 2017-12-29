# Machine-Learning-in-Python
# Simple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


#splitting the dataset into training set and test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train,y_test = train_test_split(X,y,test_size = 1/3, random_state = 0)

#FEATURE SCALING
"""sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

#fitting Linear Regession to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#predicting the test results
y_pred= regressor.predict(X_test)
#visualizing the training set results
plt.scatter(X_train,y_train, color = 'red')
plt.plot(X_train,regressor.predict(X_train), color = 'blue')
plt.title('salary vs experience(training set)')
plt.xlabel('years of experience')
plt.ylabel('Salary')
plt.show()
#visualizing the test set results
plt.scatter(X_test,y_test, color = 'red')
plt.plot(X_train,regressor.predict(X_train), color = 'blue')
plt.title('salary vs experience(training set)')
plt.xlabel('years of experience')
plt.ylabel('Salary')
plt.show()