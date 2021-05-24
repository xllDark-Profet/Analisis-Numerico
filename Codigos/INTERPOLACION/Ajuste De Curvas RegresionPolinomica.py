import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Salaries.csv')
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2].values

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,Y)

from sklearn.preprocessing import PolynomialFeatures
poly_reg =  PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, Y)


plt.scatter(X , Y, color = 'red')
plt.plot(X , lin_reg_2.predict( poly_reg.fit_transform(X)), color = 'blue')
plt.title("Polynomial Regression")
plt.xlabel("Position level")
plt.ylabel("Salary")
plt.show()