import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3D

# Vector addition and substraction

v1 = np.array([3, -1])
v2 = np.array([2, 4])

v3 = v1 + v2

# Plot them
plt.plot([0, v1[0]], [0, v1[1]], 'b', label='v1')
plt.plot([0, v2[0]] + v1[0], [0, v2[1]] + v1[1], 'r', label='v2')
plt.plot([0, v3[0]], [0, v3[1]], 'k', label='v1+v2')

plt.legend()
plt.axis('square')
plt.axis((-6, 6, -6, 6))
plt.grid()
plt.show()
