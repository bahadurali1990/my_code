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
#from Testing import X_test

##------------------------------------Creation of 1D datasets with some noise --------------------------------

"""import matplotlib.pyplot as plt
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
"""

##-------------------------------Decision Tree for Multi-class Regresser-------------------------------------

"""from sklearn.tree  import DecisionTreeRegressor
import matplotlib.pyplot as plt
import numpy as np
rng = np.random.RandomState(10)

X = np.sort(200*np.random.rand(100,1)-100,axis=0)
y = np.array([np.pi * np.sin(X).ravel(), np.pi * np.cos(X).ravel()]).T

y[::5,:] = y[::5,:]+0.5-rng.rand(20,2)

reg_1 = DecisionTreeRegressor(max_depth=2)
reg_2 = DecisionTreeRegressor(max_depth=5)
reg_3 = DecisionTreeRegressor(max_depth=8)

reg_1.fit(X,y)
reg_2.fit(X,y)
reg_3.fit(X,y)

X_test1 = np.arange(-100,100,0.01)[:,np.newaxis]

y_1 = reg_1.predict(X_test1)
y_2 = reg_2.predict(X_test1)
y_3 = reg_3.predict(X_test1)

plt.figure()

plt.scatter(y[:,0],y[:,1],s=25,c="red",edgecolors="black")
plt.scatter(y_1[:,0],y_1[:,1],s=25,c="blue",edgecolors="black")
plt.scatter(y_2[:,0],y_2[:,1],s=25,c="black",edgecolors="red")
plt.scatter(y_3[:,0],y_3[:,1],s=25,c="green",edgecolors="black")

plt.show()
"""

"""from sklearn.datasets import load_iris
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.tree import DecisionTreeClassifier

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

import numpy as np

n_classes = 3
plot_colors = "ryb"
plot_step = 0.02

iris = load_iris()

for pairidx, pair in enumerate([[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]):
    X = iris.data[:,pair]
    y = iris.target

    model = DecisionTreeClassifier()
    model.fit(X,y)

    ax = plt.subplot(2,3,pairidx+1)
    DecisionBoundaryDisplay.from_estimator(
        model,
        X,
        cmap=plt.cm.RdYlBu,
        response_method="predict",
        ax=ax,
        xlabel=iris.feature_names[pair[0]],
        ylabel=iris.feature_names[pair[1]]
    )

    # plot the training point






plt.show()
model = DecisionTreeClassifier()
model.fit(X,y)
plot_tree(model)

plt.show()

"""
##--------------------------------------------Demonstration of PCA on Iris Dataset -----------------------

"""from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

iris = load_iris(as_frame=True)
data = pd.DataFrame(iris.data)
data['target'] = iris.target
##sns.pairplot(data,hue='target')
##plt.show()

##--------------------------------------Plot a PCA represenation --------------------------------------------

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

from sklearn.decomposition import PCA

fig = plt.figure(1,figsize=(10,5))
ax = fig.add_subplot(111,projection="3d")

X_reduced = PCA(n_components=3).fit_transform(iris.data)

scatter = ax.scatter(
    X_reduced[:,0],
    X_reduced[:,1],
    X_reduced[:,2],
    c=iris.target,
    s=40
)

plt.show()
"""

##----------------------------------------------IPCA------------------------------------------------------

"""import matplotlib.pyplot as plt
import numpy as np


from sklearn.datasets import load_iris
from sklearn.decomposition import PCA,IncrementalPCA

iris = load_iris()
X = iris.data
y = iris.target

n_components = 2

ipca = IncrementalPCA(n_components=n_components,batch_size=10)
X_ipca =ipca.fit_transform(X)

pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X)

colors = ["navy", "turquoise", "darkorange"]

for X_transformed, title in [(X_ipca, "Incremental PCA"), (X_pca, "PCA")]:

    plt.figure(figsize=(8, 8))

    for color,i,target_name in zip(colors,[0,1,2],iris.target_names):

        plt.scatter(X_transformed[y==i,0],X_transformed[y==i,1],color=color)

plt.show()
"""
















































