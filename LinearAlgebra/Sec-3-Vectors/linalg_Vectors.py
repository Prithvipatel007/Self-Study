import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mplot3d

'''
Algebraic and geometric representation of vectors
'''

# 2D vector
v2 = [3, -2]
v3 = [4, -3, 2]

v3t = np.transpose(v3)

# Plotting 2D vector
plt.plot([0, v2[0]], [0,v2[1]])
plt.axis('equal')

plt.plot([-4,4], [0,0], 'k--')
plt.plot([0,0], [-4,4], 'k--')
plt.grid()
plt.axis((-4, 4, -4, 4))
plt.show()


# Plotting 3D vector
fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(111, projection='3d')
ax.plot([0, v3[0]], [0, v3[1]], [0, v3[2]], linewidth=3)

# Make the plot look nicer
ax.plot([0,0], [0,0], [-4,4], 'k--')
ax.plot([0,0], [-4,4], [0,0], 'k--')
ax.plot([-4,4], [0,0], [0,0], 'k--')
plt.show()

# Add a vector values function in a new figure

x = np.linspace(-2*np.pi, 2*np.pi, 100)
vf = [np.sin(x), x * np.cos(x), x]

fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(111, projection='3d')
ax.plot(vf[0], vf[1], vf[2], 'b')
plt.show()
