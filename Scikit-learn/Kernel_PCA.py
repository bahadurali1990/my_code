import matplotlib.pyplot as plt

from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split


X, y = make_circles(n_samples=10000,factor=0.3,noise=0.05,random_state=42)

X_train,  X_test,  y_train, y_test =  train_test_split(X, y,random_state=42)

_ , (train_ax ,test_ax) = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(8, 4))

train_ax.scatter(X_train[:,0],X_train[:,1],c=y_train)
train_ax.set_xlabel("Training data")
train_ax.set_ylabel("Training y data")
train_ax.set_title("Training information")

test_ax.scatter(X_test[:,0],X_test[:,1],c=y_test)
test_ax.set_xlabel("Training data")
test_ax.set_ylabel("Training y data")
test_ax.set_title("Training information")

plt.show()

from sklearn.decomposition import PCA, KernelPCA

pca = PCA(n_components=2)
kernel_pca = KernelPCA(n_components=None, kernel="rbf",gamma=10, fit_inverse_transform=True, alpha=0.1)








