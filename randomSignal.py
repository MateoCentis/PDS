import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(1, 10)

def randomF(n):
    return np.sin(n) + np.random.normal(scale=0.1, size=len(n))

# plt.plot(n, randomF(n))
# plt.show()