import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import pandas as pd
from sklearn.decomposition import PCA
from sklearn import svm

sum = np.zeros((1,8))
for i in range(5):
    data = pd.read_csv("datasets/hematomic.csv")
    data = data.sample(frac=1).reset_index(drop=True)
    x_columns = ["bp", "rbc", "pc", "pcc", "hemo", "pcv", "wc", "rc"]
    #for col in x_columns:
        #print(data[col].dtype)
    x = data[x_columns]
    y = data['class']

    X = np.array(x)
    y = np.array(y)
    clf = svm.SVC(kernel='linear', probability=True)
    clf.fit(x, y)

    sum += clf.coef_

    plt.show()
    #print(lda.predict([[4, 1, 6]]))
avg = sum/5
print(avg)