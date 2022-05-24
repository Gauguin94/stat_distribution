from scipy.stats import gamma
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,101)
y1 = gamma(5, 0.5).pdf(x)
print(y1)

plt.figure(figsize=(12, 8))
plt.plot(x, y1, 'ro--')
plt.xlabel('X')
plt.ylabel('P(X)')
plt.title('Gamma Distribution(alpha=5, beta=0.5)')
plt.grid()
plt.show()
