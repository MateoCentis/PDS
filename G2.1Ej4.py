import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    y = np.zeros(len(x))
    for n in range(2,len(x)):
        y[n] = x[n] + y[n-2] 
    return y
#causal

x = np.zeros(30)
n = np.arange(0,len(x),1)
x[0]=1
x[7]=1
x[5]=1
y = f1(x)
print(x)
print(y)
plt.plot(n,y)
plt.show()
#opcional