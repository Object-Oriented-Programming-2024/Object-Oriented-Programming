import pandas as pd, matplotlib.pyplot as plt, seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# Load the Iris dataset
iris = load_iris()
X = iris.data
X = StandardScaler().fit_transform(X)

# Performing PCA
pca = PCA(n_components=2)  # Reduce the data to 2 principal components
X_pca = pca.fit_transform(X)

# Create a dataframe with the principal components
df_pca = pd.DataFrame(data = X_pca, columns = ['PCA 1', 'PCA 2'])

# The number of dimensions after PCA
print("Number of dimensions after PCA:", df_pca.shape[1])

plt.figure(figsize=(8, 4))
sns.scatterplot(x='PCA 1', y='PCA 2', data=df_pca, palette='Set1', hue=iris.target)
plt.title('PCA of Iris Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
