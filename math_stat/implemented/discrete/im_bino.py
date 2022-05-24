from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1, 51)
y1 = binom(n=50, p=0.1).pmf(x)
print(y1)

plt.figure(figsize=(12, 8))
plt.plot(x, y1, 'ro--')
plt.xlabel('X')
plt.ylabel('P(X)')
plt.title('Binomial Distribution(n = 50, p = 0.1)')
plt.grid()
plt.show()
