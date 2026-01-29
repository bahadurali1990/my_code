##---------------------------------------KNN based imputers-------------------------------------------

from sklearn.impute import KNNImputer
import numpy as np

X = [
      [1, 2, np.nan],
      [3, 4, 3],
      [np.nan, 6, 5],
      [8, 8, 7]
    ]
imputer = KNNImputer(n_neighbors=2)

X_new = imputer.fit_transform(X)

print(X)
print(X_new)
