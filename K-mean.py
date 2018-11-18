import numpy as np
import matplotlib.pyplot as plt


a = np.random.rand(20,2)
b = np.random.rand(20,2)
b = b * [5, 5]
a = a * [-5, -5]
ax = a[:, 0]
ay = a[:, 1]
bx = b[:, 0]
by = b[:, 1]
plt.plot(ax, ay, 'go', label="points")
plt.plot(bx, by, 'go', label="points")
plt.axis([-5, 5, -5, 5])
plt.show()