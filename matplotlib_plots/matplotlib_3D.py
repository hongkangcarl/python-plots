import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5, 3))
ax = plt.axes(projection='3d')

x = np.linspace(-1, 1, 100)  # make the x-array with 100 numbers
y = np.linspace(-1, 1, 100)  # make the y-array with 100 numbers
X, Y = np.meshgrid(x, y)  # make the 2D meshgrid of the X-Y plane

Z = X ** 2 + Y ** 2  # make the 2D array 'Z' defined on the X-Y plane

ax.plot_surface(X, Y, Z, cmap='coolwarm')
ax.view_init(20, 35)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.tight_layout()
plt.savefig('./images/3D_surface_plot.png', dpi=200)
plt.show()
