import pandas as pd
import csv
dataset=pd.read_csv("Multi.csv", delimiter=',')
print(dataset) #Print entire dataset
X = dataset[['AA','BB','CC','DD']].values
Y = dataset[['C1','C2','C3']].values
print(Y) #Prints output values
print(X) #Prints intput values
X1 = dataset[['AA','BB','CC']].values
print(X1) #Prints first 5 columns of intput values
print(X[0:5])