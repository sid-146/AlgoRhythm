# Comprehensive Guide for K-Means Clustering

K Means Clustering is a popular method to group data by assigning the observations to clusters based on proximity to the cluster's center.It is unsupervised learning technique that groups data points into cluster on similarity.

Before understanding about K-Means we need to understand what is `Clustering`

## What is Clustering?

Cluster Analysis is a technique in data mining and machine learning that groups similar object into Clusters.

K-Means Clustering is one such technique, which aims to divide the dataset into K (pre-defined) clusters by minimizing the sum of squared distances between the datapoint and their respective clusters.

## Let's discuss Example

Let's assume, a bank wants to give credit card offers to its customer. Currently process is manual looking for details of each customers and based on this information they decide which offer should be given to that particular customer.

As the banks generally have millions of customers. It does not make sense to look into the details of each customer separately and then make decision.

Let's say bank decides to group the customers based on their incomes

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

The main objective of k-means clustering is to partition data into specific number of groups, where the the data points in same cluster have same properties and dissimilar to the other groups.
This is achieved by minimizing the distance between the data points and their assigned cluster's center (Centroid)

1. **Grouping similar data points:**

    - Identify pattern in your data by grouping data points that share similar characteristics together.
    - Discovering underlying structures within the data.

2. **Minimizing with-cluster distance**

    - The algorithm is responsible to make sure data points within cluster are as close as possible.
    - Generally distance is measured by the Euclidean Distance.
    - This ensures tight-knit clusters with high cohesiveness.

3. **Maximizing between-cluster distance**
    - K-Means also tries to maximize the separation between clusters.
    - Ideally, data points from different clusters should be far apart, making the clusters distinct from each other.

```
Euclidean Distance is like measuring the straightest and shortest path between two points.
```

$$
\text{Euclidean Distance (d)} = \sqrt{[(x_2 - x_1)^2 + (y_2 - y_1)^2]}
$$
