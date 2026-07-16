# Clustering Techniques Comparison Report

## Project Overview
This project implements and compares three unsupervised learning algorithms—K-Means, Hierarchical Clustering, and DBSCAN—using the Mall Customer Segmentation dataset. The objective is to identify customer groups based on their purchasing behavior and evaluate the effectiveness of each clustering algorithm using standard clustering evaluation metrics.

## Dataset
**Dataset:** Mall Customer Segmentation Dataset

**Features Used:**
- Age
- Annual Income (k$)
- Spending Score (1–100)

Before clustering, the selected features were standardized using **StandardScaler** to ensure equal contribution of each feature.


# Algorithms Implemented

## 1. K-Means Clustering

### Description
K-Means partitions the dataset into a predefined number of clusters by minimizing the distance between data points and their cluster centroids.

### Performance
- Number of Clusters: 5
- Silhouette Score: **0.55**
- Davies-Bouldin Index: **0.57**

### Advantages
- Simple and computationally efficient.
- Works well on spherical and well-separated clusters.
- Easy to interpret and visualize.

### Limitations
- Requires specifying the number of clusters in advance.
- Sensitive to outliers.
- Performance depends on centroid initialization.



## 2. Hierarchical Clustering

### Description
Hierarchical Clustering builds a hierarchy of clusters using Ward's linkage method. A dendrogram is used to determine an appropriate number of clusters.

### Performance
- Number of Clusters: 5
- Silhouette Score: **0.55**
- Davies-Bouldin Index: **0.58**

### Advantages
- Does not require centroid initialization.
- Produces a dendrogram for cluster visualization.
- Suitable for understanding hierarchical relationships.

### Limitations
- Computationally expensive for large datasets.
- Difficult to modify clusters once formed.



## 3. DBSCAN

### Description
DBSCAN groups points based on density and identifies noise or outliers without requiring a predefined number of clusters.

### Performance
- Silhouette Score: **0.35**
- Davies-Bouldin Index: **0.83**

### Advantages
- Detects arbitrarily shaped clusters.
- Automatically identifies outliers.
- Does not require specifying the number of clusters.

### Limitations
- Sensitive to parameter selection (`eps` and `min_samples`).
- Performance decreases on datasets with varying densities.



# Performance Comparison

# | Algorithm | Silhouette Score | Davies-Bouldin Index |

 | K-Means   |       0.55       |      0.57            |

 | Hierarchical
  Clustering  |       0.55       |       0.58           |
 
 | DBSCAN    |       0.35       |      0.83            |

**Interpretation**
- A **higher Silhouette Score** indicates better-defined clusters.
- A **lower Davies-Bouldin Index** indicates better separation between clusters.

Among the three algorithms, **K-Means achieved the best overall performance**, followed closely by Hierarchical Clustering. DBSCAN produced comparatively lower clustering quality 
for this dataset due to the distribution of customer data.


# Visualization Plots

The following visualizations were generated during the analysis:

- Exploratory Data Analysis (EDA)
- Elbow Method plot
- K-Means Cluster Visualization
- Hierarchical Clustering Dendrogram
- Hierarchical Cluster Visualization
- DBSCAN Cluster Visualization
- Algorithm Performance Comparison Table



# Findings

- Feature scaling significantly improved clustering performance.
- The Elbow Method suggested **5 clusters** as the optimal choice for K-Means.
- Hierarchical Clustering produced a cluster structure similar to K-Means.
- DBSCAN successfully identified density-based clusters but was more sensitive to parameter tuning.
- K-Means provided the best balance between cluster separation and compactness for the Mall Customer Segmentation dataset.

---

# Conclusion

This project demonstrated the application of three popular clustering algorithms on customer segmentation data. Based on the evaluation metrics, 
**K-Means was the most effective algorithm** for this dataset, while Hierarchical Clustering provided comparable results with the added benefit of dendrogram visualization. 
DBSCAN proved useful for density-based clustering and outlier detection but was less effective for this particular dataset due to its sensitivity to parameter selection.

Overall, the project highlights the importance of selecting an appropriate clustering algorithm based on the characteristics of the dataset and the analysis objective.
