import numpy as np
import matplotlib.pyplot as plt

# generate an x-array from 0 to 1, 100 numbers
x = np.linspace(0, 1, 100)
# y = x^2 (also an array, from 0 to 1, 100 numbers)
y = x**2

plt.figure(figsize=(4, 3))  # set the figure size
plt.plot(x, y)  # plot y against x
plt.axis('scaled')   # (optional) make x- and y-axis the same scale
plt.xlabel('x')      # set the x label
plt.ylabel('y')      # set the y label

plt.tight_layout()  # make sure nothing goes outside the figure
# save figure to directory ./image/ and set the resolution (dpi)
plt.savefig('./images/y=x2.png', dpi=200)
plt.show()      # show the figure

