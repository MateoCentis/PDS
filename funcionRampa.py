import numpy as np
import matplotlib.pyplot as plt

def funcionRampa(n):
    y = np.zeros(len(n))
    for i in np.arange(0,len(n),1):
        if (n[i] < 0):
            y[i] = 0
        else:
            y[i] = n[i]
    return y


# n = np.arange(-20,20,1)
# y = funcionRampa(n)

# plt.plot(n,y)
# plt.show()