from scipy.stats import nbinom
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,21)
y1 = nbinom(n=2, p=0.5).pmf(x)
print(y1)

plt.figure(figsize=(12, 8))
plt.plot(x, y1, 'ro--')
plt.xlabel('X')
plt.ylabel('P(X)')
plt.title('Negative Binomial Distribution(success = 2, failure = 20, p = 0.1)')
plt.grid()
plt.show()
