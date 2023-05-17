import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("C:\Lavoro-Temp\zeni\dataset.csv", sep=";", engine="python")

df = pd.DataFrame(data)

X = list(df.iloc[:,0])
Y1 = list(df.iloc[:,1])
Y2 = list(df.iloc[:,2])

X_axis = np.arange(len(X))
plt.figure(figsize=(20,15))
plt.barh(X_axis-0.2, Y1, 0.4, color="orange")
plt.barh(X_axis+0.2, Y2, 0.4, color="blue")
plt.yticks(X_axis,X)
plt.show()
