import numpy as np
import matplotlib.pyplot as plt

A = np.array([[3, 2, 1],[5,-5,4],[6,0,1]])
b1 = np.array([1,2,3])
b2 = np.array([-1,2,-5])

print(A)
print(b1)
print(b2)

print(A@b1)
print(A.T)
print(np.dot(b1, b2))
print(np.cross(b1, b2))

