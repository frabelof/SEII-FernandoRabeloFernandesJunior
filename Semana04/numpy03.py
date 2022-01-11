import numpy as np
import matplotlib.pyplot as plt

# Média, desvio padrão e percentuais

a1 = 2*np.random.randn(10000) + 10
pprint(np.mean(a1))
print(np.std(a1))
print(np.percentile(a1, 80))

# Integrais e Derivadas

x = np.linspace(1, 10, 100)
y = 1/x**2 * np.sin(x)
dydx = np.gradient(y,x)
y_integral = np.cumsum(y) * (x[1]-x[0])
plt.plot(x,y)
plt.plot(x,dydx)
plt.plot(x,y_integral)