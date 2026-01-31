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
from sympy.printing.pretty.pretty_symbology import line_width

rng = np.random.RandomState(42)

X = np.sort(5*rng.rand(80,1),axis=0)

y = np.sin(X).ravel()

fig , axes = plt.subplots(1,2)
axes[0].plot(X,y)

y[::5] = y[::5]+3*(0.5-rng.rand(16))

axes[1].plot(X,y)

plt.show()

##--------------------------------------Decision Tree with different Depth-----------------------------------

from sklearn.tree import DecisionTreeRegressor

tree1 = DecisionTreeRegressor(max_depth=2)
tree2 = DecisionTreeRegressor(max_depth=5)

tree1.fit(X,y)
tree2.fit(X,y)

X_test = np.arange(0,5.0,0.01)[:,np.newaxis]

y_1 = tree1.predict(X_test)
y_2 = tree2.predict(X_test)


##--------------------------------------- Plot the result ----------------------------------------------------

plt.figure()
plt.scatter(X,y,s=20,edgecolors='black',label='data')
plt.plot(X_test,y_1,linewidth=2)
plt.plot(X_test,y_2,linewidth=2)
plt.legend()
plt.show()














