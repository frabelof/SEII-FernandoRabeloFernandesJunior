import numpy as np
import matplotlib.pyplot as plt

#EX1: Let y=e^{-x/10} \sin(x). Consider 10000 x intervals in the range [0,10]

#1 Plot the function y vs. x in the range [0, 10].

N = 10000
x = np.linspace(0, 10, N+1)
y = np.exp(-x/10) * np.sin(x)
plt.plot(x,y)

#2 Compute the mean and standard deviation of y for x values in [4,7]

print(np.mean(y[(x>=4)*(x<=7)]))
print(np.std(y[(x>=4)*(x<=7)]))

#3 For x in the range [4,7], find the value y_m such that 80% of y values are less than y_m

print(np.percentile(y[(x>=4)*(x<=7)], 80))

#4 Plot dy/dx vs x

plt.plot(x, np.gradient(y,x))

#5 Find the locations where dy/dx=0

dydx = np.gradient(y,x)
x[1:][dydx[1:] * dydx[:-1] < 0]

#EX2: Sum together every number from 0 to 10000 except for those than can be divided by 4 or 7. Do this in one line of code

sum = np.arange(0,10001,1)[(np.arange(0,10001,1)%4!=0)*(np.arange(0,10001,1)%7!=0)].sum()
print(sum)

#EX3: Consider the flower petal r(\theta) = 1+\frac{3}{4}\sin(3 \theta) for 0 \leq \theta \leq 2 \pi

#1 Make a plot of the flower (find x and y points)

theta = np.linspace(0, 2*np.pi, 10000)
r = 1 + 3/4 * np.sin(3*theta)
x = r*np.cos(theta)
y = r * np.sin(theta)
plt.plot(x,y)

#2 Compute the area using the calculus formula A = \int_{0}^{2\pi} \frac{1}{2} r^2 d\theta
 
A = 1/2 * sum(r**2) * (theta[1]-theta[0])
print(A)

#3 Compute the arclength using the calculus formula L = \int_{0}^{2 \pi} \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2} d\theta

L = sum(np.sqrt(r**2 + np.gradient(r, theta)**2)) * (theta[1]-theta[0])
print(L)

#EX4:The power emitted by a blackbody is P = A \sigma \epsilon T^4. After measuring the temperature of a star you find that 
#T(t) = T_0 \frac{1}{1+e^{-kt}}. Plot the total energy emitted by the star as a function of time using the fact that 
#E(t) = \int_{t'=0}^{t'=t} P(t') dt'

kt = np.linspace(0, 3, 100)
P = (1/(1+np.exp(-kt)))**4
E = np.cumsum(P) * (kt[1]-kt[0])

plt.plot(kt,E)
plt.xlabel('$kt$', fontsize=20)
plt.ylabel(r'$\left(\frac{k}{A \sigma \epsilon T_0^4}\right) E(kt)$', fontsize=20)
plt.show()