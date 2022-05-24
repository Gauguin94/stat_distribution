from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,101)
y1 = norm(50, 10).pdf(x)
print(y1)

plt.figure(figsize=(12, 8))
plt.plot(x, y1, 'ro--')
plt.xlabel('X')
plt.ylabel('P(X)')
plt.title('Gaussian Distribution(mew=50, variance=100)')
plt.grid()
plt.show()
