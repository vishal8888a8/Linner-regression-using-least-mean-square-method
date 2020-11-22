import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 

data = pd.read_csv('Data.csv')
X = data.iloc[:, 0]
Y = data.iloc[:, 1]

x_mean = np.mean(X)
y_mean = np.mean(Y)

nr = dr = 0
for i,j in zip(X,Y):
	nr+=(i-x_mean)*(j-y_mean)
	dr+=(i-x_mean)**2

param1 = nr/dr
param0 = y_mean - param1*x_mean
Y_pred = param1*X + param0

print(param1 , param0)

plt.scatter(X,Y,color='b')
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')
plt.show()