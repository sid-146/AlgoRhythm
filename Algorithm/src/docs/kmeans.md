# Comprehensive Guide for K-Means Clustering

K Means Clustering is a popular method to group data by assigning the observations to clusters based on proximity to the cluster's center.It is unsupervised learning technique that groups data points into cluster on similarity.

Before understanding about K-Means we need to understand what is `Clustering`

## What is Clustering?

## Let's discuss Example

## What is K-Means Clustering?

-   Unsupervised machine learning algorithm used for partitioning a dataset into pre-defined numbers of cluster.
-   Helps in discovering underlying patterns or structures within the data.
-   K-Means is a centroid based algorithm or distance-based algorithm
-   Optimal Centroid is obtained by minimizing the sum of squared distances between each data point and it's closest centroid.

`This is an algorithm that tries to minimize the distance between the points in a cluster with their centroid`

## How K-Means Clustering works?

1. **Initialization:**

    - Start by randomly selecting K points from the dataset.
    - This will act as initial cluster centroid.

2. **Assignment**

    - For Each data point in the dataset, calculate distance b/w that point and each centroid.
    - Assign data point to the cluster whose centroid is closest to it. `This Step forms K Clusters`

3. **Update Centroids**

    - Once all data points are assigned to any of one K centroid.
    - Re-Calculate the centroids by taking the mean of all data points assigned to each cluster.

4. **Repeat**

    - Repeat Step 2 and 3 until convergence.
    - Convergence occurs when the centroid's position no longer change significantly or when a specified number of iterations are reached.

5. **Results**
    - After convergence is achieved. The Algorithm outputs the final cluster centroids and assigns each data point to a cluster.

## Objective of K-Means Clustering
