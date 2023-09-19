# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# Read DataSet
df = datasets.load_iris()
x = df.data
y = df.target

# Let's try with k=5 initially
kmeans5 = KMeans(n_clusters=5)
y_kmeans5 = kmeans5.fit_predict(x)
print(y_kmeans5)
print(kmeans5.cluster_centers_)

# To find the optimal number of clusters (k) in a dataset
Error = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i).fit(x)
    kmeans.fit(x)
    Error.append(kmeans.inertia_)

import matplotlib.pyplot as plt
plt.plot(range(1, 11), Error)

plt.title('Elbow method')
plt.xlabel('No of clusters')
plt.ylabel('Error')
plt.show()

# Now try with k=3 finally
kmeans3 = KMeans(n_clusters=3)
y_kmeans3 = kmeans3.fit_predict(x)
print(y_kmeans3)
print(kmeans3.cluster_centers_)
