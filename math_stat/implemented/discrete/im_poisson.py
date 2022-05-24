from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,21)
y1 = poisson(2).pmf(x)
print(y1)

plt.figure(figsize=(12, 8))
plt.plot(x, y1, 'ro--')
plt.xlabel('X')
plt.ylabel('P(X)')
plt.title('Poisson Distribution(lambda = 2)')
plt.grid()
plt.show()
