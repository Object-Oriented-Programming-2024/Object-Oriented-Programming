import numpy as np, pandas as pd, matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Loading the Iris dataset
iris = load_iris()
X = iris.data

X=StandardScaler().fit_transform(X)

# Initializing KMeans with 3 clusters
kmeans = KMeans(n_clusters=3, init="k-means++")

# Fitting the model
kmeans.fit(X)

# Getting the cluster centroids and labels
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# Plotting the clusters
plt.figure(figsize=(8, 6))

plt.scatter(X[labels == 0, 0], X[labels == 0, 1], s=50)
plt.scatter(X[labels == 1, 0], X[labels == 1, 1], s=50)
plt.scatter(X[labels == 2, 0], X[labels == 2, 1], s=50)

plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='black', marker='*', label='Centroids')

plt.title('K-Means Clustering')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()
