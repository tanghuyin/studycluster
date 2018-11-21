import numpy as np
import matplotlib.pyplot as plt
#init data
group_a = np.random.rand(20, 2) * [5, 5]
group_b = np.random.rand(20, 2) * [-5, -5]
cluster_centroids = np.random.rand(2, 2) * 6 - 3
group = np.append(group_a, group_b, axis=0)
bluex = 0
bluey = 0
bluen = 0
redx = 0
redy = 0
redn = 0
repeat_time = 10
#calculate the distance
for i in range(repeat_time):
    dis_to_centroid_1 = np.sqrt(np.square(group[:, 0] - cluster_centroids[0][0]) + np.square(group[:, 1] - cluster_centroids[0][1]))
    dis_to_centroid_2 = np.sqrt(np.square(group[:, 0] - cluster_centroids[1][0]) + np.square(group[:, 1] - cluster_centroids[1][1]))
    group = np.insert(group, 2, values=dis_to_centroid_1, axis=1)
    group = np.insert(group, 3, values=dis_to_centroid_2, axis=1)
    group = np.insert(group, 4, 0, axis=1)

    for i in range(40):
        if group[i][2] < group[i][3]:
            group[i][4] = 1
            bluen += 1
            bluex += group[i][0]
            bluey += group[i][1]
        else:
            group[i][4] = 2
            redn += 1
            redx += group[i][0]
            redy += group[i][1]
    cluster_centroids[1][0] = redx / redn
    cluster_centroids[1][1] = redy / redn
    cluster_centroids[0][0] = bluex / bluen
    cluster_centroids[0][1] = bluey / bluen
# only repeat one time 
        
# print
for i in range(40):
    if group[i][2] < group[i][3]:
        plt.plot(group[i][0], group[i][1], 'bo')
    else:
        plt.plot(group[i][0], group[i][1], 'ro')   
plt.plot(cluster_centroids[0, 0], cluster_centroids[0, 1], "bx", label="cluster centroid 1")
plt.plot(cluster_centroids[1, 0], cluster_centroids[1, 1], "rx", label="cluster centroid 2")
plt.axis([-5, 5, -5, 5])
plt.legend()
plt.show()

