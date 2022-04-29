import numpy as np
import matplotlib.pyplot as plt

# set up a figure plus two axes (subplots), figure size.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 3), tight_layout=True)

# numerical arrays to plot
x = np.linspace(0, 1)
y1 = x**2
y2 = np.sqrt(x)

ax1.plot(x, y1)             # plot in the first subplot
ax1.set_title('Plot 1')     # set the title. Note this is different to plt.title().
ax1.set_xlabel(r'$x$')      # set the x-label. Note this is different to plt.xlabel().
ax1.set_ylabel(r'$y_1$')    # set the y-label. Note this is different to plt.ylabel().
ax1.axis('scaled')          # make x- and y-axis scaled

ax2.plot(x, y2)
ax2.set_title('Plot 2')
ax2.set_xlabel(r'$x$')
ax2.set_ylabel(r'$y_2$')
ax2.axis('scaled')

plt.savefig('./images/subplots.png', dpi=200)
plt.show()
