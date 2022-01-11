import numpy as np
import matplotlib.pyplot as plt

# 3x + 2y + z = 4
# 5x -5y + 4z = 3
# 6x +z = 0

A = np.array([[3, 2, 1],[5,-5,4],[6,0,1]])
c = np.array([4,3,0])

np.linalg.solve(A,c)

