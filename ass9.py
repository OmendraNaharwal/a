import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

iris = load_iris(as_frame=True)
df = iris.data                       # 4 features, no labels used for clustering
true_labels = iris.target            # only kept to check our result at the end

X = StandardScaler().fit_transform(df)
print(df.head())






from sklearn.cluster import KMeans

inertia = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    inertia.append(km.inertia_)

plt.plot(range(1, 11), inertia, marker="o")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow method")
plt.show()







kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
km_labels = kmeans.fit_predict(X)

df_result = df.copy()
df_result["KMeans_cluster"] = km_labels
print(df_result["KMeans_cluster"].value_counts())




from scipy.cluster.hierarchy import linkage, dendrogram

Z = linkage(X, method="ward")

plt.figure(figsize=(10, 5))
dendrogram(Z, truncate_mode="lastp", p=20)
plt.title("Dendrogram")
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.show()






from sklearn.cluster import AgglomerativeClustering

hc = AgglomerativeClustering(n_clusters=3, linkage="ward")
hc_labels = hc.fit_predict(X)

df_result["Hierarchical_cluster"] = hc_labels
print(df_result["Hierarchical_cluster"].value_counts())






print("Average of each feature in every K-Means cluster:")
print(df_result.groupby("KMeans_cluster")[list(df.columns)].mean().round(2))














plt.scatter(X[:, 2], X[:, 3], c=km_labels)
plt.scatter(kmeans.cluster_centers_[:, 2], kmeans.cluster_centers_[:, 3], c="red", marker="X", s=200)
plt.xlabel("petal length (scaled)")
plt.ylabel("petal width (scaled)")
plt.title("K-Means clusters (red X = centres)")
plt.show()









