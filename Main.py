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

#print(param1 , param0)

plt.scatter(X, Y, marker='o', s=70, c='g')
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='m', linewidth = 6)
plt.xlabel("X value", fontsize = 20)
plt.ylabel("Y value", fontsize = 20)
plt.show()





# new changes 

print("Slope - %1.4f\nCoefficient - %1.4f\n" %(param1, param0))

#function for finding output
def Value(x):
    y = param1*x + param0
    return y


x_val = float(input("Enter the X value - "))
print("Y value for this X is - %1.3f" %(Value(x_val)))



