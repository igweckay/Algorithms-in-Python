import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 	

#flower data
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)

y = df.iloc[0:100, 4].values
y = np.where(y=='Iris-setosa', -1, 1)


print df.tail()