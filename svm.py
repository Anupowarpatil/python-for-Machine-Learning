from sklearn.datasets import make_blobs
X, Y = make_blobs(n_samples=500, centers=2,random_state=0, cluster_std=0.40)
import matplotlib.pyplot as plt
plt.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap='spring');
plt.show() 
