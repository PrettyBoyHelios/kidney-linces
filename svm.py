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
lda = PCA(n_components=2)
X_lda = lda.fit_transform(X, y)
print("ratio: ", lda.explained_variance_ratio_)
print(lda.score)

plt.xlabel('LD1')
plt.ylabel('LD2')
plt.scatter(
    X_lda[:,0],
    X_lda[:,1],
    c=y,
    cmap='rainbow',
    alpha=0.7,
    edgecolors='b',
    
)

plt.show()
#print(lda.predict([[4, 1, 6]]))