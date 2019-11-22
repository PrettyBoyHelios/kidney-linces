import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

from sklearn.decomposition import PCA
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

sum = np.zeros((1, 8))
score = 0
train_data = pd.read_csv("hematomic_lifestyle.csv")
train_data = train_data.sample(frac=1).reset_index(drop=True)
test_data = pd.read_csv("hematomic_lifestyle_test.csv")
test_data = test_data.sample(frac=1).reset_index(drop=True)
x_columns = ["hemo", "pcv", "htn", "dm"]

#train_data, test_data = train_test_split(data, train_size=0.7)

x_fit = train_data[x_columns]
y_fit = train_data['class']

x_eval = test_data[x_columns]
#y_true = test_data['class']

x_fit = np.array(x_fit)
y_fit = np.array(y_fit)

# clf = svm.SVC(kernel='linear', probability=True)
clf = RandomForestClassifier(n_estimators=100, class_weight={0: 1.2, 1: 1})
clf.fit(x_fit, y_fit)

feature_imp = pd.Series(clf.feature_importances_, index=x_columns).sort_values(ascending=False)
#print(feature_imp)

y_pred = clf.predict(x_eval)

df = pd.DataFrame(y_pred)
df.to_csv("results.csv")
