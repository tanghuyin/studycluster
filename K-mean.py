import numpy as np
import matplotlib.pyplot as plt

group_a = np.random.rand(20, 2) * [5, 5]
group_b = np.random.rand(20, 2) * [-5, -5]
cluster_centroids = np.random.rand(2, 2) * 10 - 5

dis_to_centroid_1 = ((group_a[:, 0] - cluster_centroids[0, 0])**2 + (group_a[:, 1] - cluster_centroids[0, 1])**2)**0.5
dis_to_centroid_2 = ((group_b[:, 0] - cluster_centroids[0, 0])**2 + (group_b[:, 1] - cluster_centroids[0, 1])**2)**0.5
print(dis_to_centroid_1)
print(dis_to_centroid_2)
plt.plot(np.append(group_a[:, 0], group_b[:, 0]), np.append(group_a[:, 1], group_b[:, 1]), "go", label="data points")
plt.plot(cluster_centroids[0, 0], cluster_centroids[0, 1], "bo", label="cluster centroid 1")
plt.plot(cluster_centroids[1, 0], cluster_centroids[1, 1], "ro", label="cluster centroid 2")
plt.axis([-5, 5, -5, 5])
plt.legend()
plt.show()

