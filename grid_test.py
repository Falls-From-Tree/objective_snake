from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


plt.style.use('dark_background')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Grab some test data.
X = np.array([[0],[100],[0],[0]])
Y = np.array([[0],[0],[0],[0]])
Z = np.array([[0],[100],[0],[0]])

print(axes3d.get_test_data(0.05))
# Plot a basic wireframe.
ax.plot_wireframe(X, Y, Z,)

plt.show()