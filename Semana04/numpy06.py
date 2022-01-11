import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.linspace(0, 5, 500)

xv, yv = np.meshgrid(x, y)

zv = xv**2 + yv**2

plt.contourf(xv, yv, zv,levels=30)
plt.colorbar()
plt.show()


