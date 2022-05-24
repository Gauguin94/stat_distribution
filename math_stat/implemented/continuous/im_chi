from scipy.stats import chi2
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,101)
y1 = chi2(10).pdf(x)
print(y1)

plt.figure(figsize=(12, 8))
plt.plot(x, y1, 'ro--')
plt.xlabel('X')
plt.ylabel('P(X)')
plt.title('Chi-Squared Distribution(degree of freedom = 10)')
plt.grid()
plt.show()
