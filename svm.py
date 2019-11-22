import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import pandas as pd
from sklearn.decomposition import PCA
from sklearn import svm

data = pd.read_csv("datasets/lifestyle.csv")
data = data.sample(frac=1).reset_index(drop=True)
x_columns = ["bp", "grav", "htn", "dm", "cad", "appet", "pe", "ane"]
x = data[x_columns]
y = data['class']
for col in data:
    print(col)
print(x)
print(x_columns)



X = np.array(x)
y = np.array(y)
clf = svm.SVC(kernel='linear', probability=True)
clf.fit(x, y)

print(clf.coef_)

plt.show()
#print(lda.predict([[4, 1, 6]]))