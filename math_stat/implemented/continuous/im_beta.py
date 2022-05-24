from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,0.99,100)
y1 = beta(0.5, 0.5).pdf(x)
print(y1)

plt.figure(figsize=(12, 8))
plt.plot(x, y1, 'ro--')
plt.xlabel('X')
plt.ylabel('P(X)')
plt.title('Beta Distribution(alpha = 0.5, beta = 0.5)')
plt.grid()
plt.show()
