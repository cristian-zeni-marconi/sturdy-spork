import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


data = pd.read_csv("C:\Lavoro-Temp\zeni\dataset.csv", sep=";", engine="python")

df = pd.DataFrame(data)

X = list(df.iloc[:,0])
Y1 = list(df.iloc[:,1])
Y2 = list(df.iloc[:,2])

#X_axis = np.arange(len(X))
#plt.figure(figsize=(20,15))
#plt.barh(X_axis-0.2, Y1, 0.4, color="orange")
#plt.barh(X_axis+0.2, Y2, 0.4, color="blue")
#plt.yticks(X_axis,X)
#plt.show()

for i in range(len(X)):
    plt.xlim(0,float(max(Y1)))
    plt.ylim(0,len(X))
    plt.figure(figsize=(20,15))
    plt.barh(list(range(len(X))), Y1, 0.4, color="orange")
    plt.xticks(X_axis,X)
    plt.pause(0.001)
   

plt.show()
