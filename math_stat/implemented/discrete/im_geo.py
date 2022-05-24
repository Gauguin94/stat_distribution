from scipy.stats import geom
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,21)
y1 = geom(p=0.1).pmf(x)
print(y1)

plt.figure(figsize=(12, 8))
plt.plot(x, y1, 'ro--')
plt.xlabel('X')
plt.ylabel('P(X)')
plt.title('Geometric Distribution(failure=20, p = 0.1)')
plt.grid()
plt.show()
