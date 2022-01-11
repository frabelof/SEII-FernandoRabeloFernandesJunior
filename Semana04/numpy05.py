import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([[4,6,4],[2,1,2],[5,6,7]])
print(a1)
print(a1*2)
print(2/a1)
print(a1.ravel())
print(a1>5)

a2 = np.random.randn(3,3)
print(a2)
print(a2[a1>5])
print(a1)
print(a1[0])
print(a1[:,1])
print(a1[1:][:,1])
print(a1)

b1 = np.resize(a1, (6,6))
print(b1)
print(b1[0:5:2][:,3:])


