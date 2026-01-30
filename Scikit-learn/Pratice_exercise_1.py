##---------------------------------------KNN based imputers-------------------------------------------

"""from sklearn.impute import KNNImputer
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
"""
##------------------------------------Creation of 1D datasets with some noise --------------------------------

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.RandomState(42)

X = np.sort(5*rng.rand(80,1),axis=0)

y = np.sin(X).ravel()

fig , axes = plt.subplots(1,2)
axes[0].plot(X,y)

y[::5] = y[::5]+3*(0.5-rng.rand(16))

axes[1].plot(X,y)

plt.show()


