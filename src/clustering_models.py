import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score, davies_bouldin_score
from scipy.cluster.hierarchy import dendrogram, linkage
from preprocessing import X_scaled

# K-Means Clustering

wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X_scaled)

silhouette_kmeans = silhouette_score(X_scaled, kmeans_labels)
db_kmeans = davies_bouldin_score(X_scaled, kmeans_labels)


# Hierarchical Clustering

plt.figure(figsize=(10, 5))
dendrogram(linkage(X_scaled, method='ward'))
plt.title("Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean Distance")
plt.show()

hc = AgglomerativeClustering(n_clusters=5)
hc_labels = hc.fit_predict(X_scaled)

silhouette_hc = silhouette_score(X_scaled, hc_labels)
db_hc = davies_bouldin_score(X_scaled, hc_labels)


# DBSCAN

dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan_labels = dbscan.fit_predict(X_scaled)

silhouette_dbscan = silhouette_score(X_scaled, dbscan_labels)
db_dbscan = davies_bouldin_score(X_scaled, dbscan_labels)


# Model Comparison

comparison = pd.DataFrame({
    "Algorithm": [
        "K-Means",
        "Hierarchical Clustering",
        "DBSCAN"
    ],
    "Silhouette Score": [
        silhouette_kmeans,
        silhouette_hc,
        silhouette_dbscan
    ],
    "Davies-Bouldin Index": [
        db_kmeans,
        db_hc,
        db_dbscan
    ]
})

print(comparison)
