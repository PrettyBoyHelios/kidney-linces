import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


X = np.array([[-1, 1, 6], [-2, 1, -2], [10, -2, -4], [1, 1, 4], [2, 1, 8], [3, 2, 10]])
y = np.array([1, 1, 3, 1, 2, 2])
lda = LinearDiscriminantAnalysis()
X_lda = lda.fit_transform(X, y)
print("ratio: ", lda.explained_variance_ratio_)

plt.xlabel('LD1')
plt.ylabel('LD2')
plt.scatter(
    X_lda[:,0],
    X_lda[:,1],
    c=y,
    cmap='rainbow',
    alpha=0.7,
    edgecolors='b'
)
plt.show()
print(lda.predict([[4, 1, 6]]))