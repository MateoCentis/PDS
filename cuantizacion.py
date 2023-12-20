import numpy as np
import matplotlib.pyplot as plt

def cuantizacion(x,N,H):
    minimo = min(x)
    x = x - minimo
    for i in np.arange(0,len(x),1):
        #x[i] -= minimo
        if x[i] < 0:
            x[i] = 0
        elif (x[i] >= H*int(x[i]/H) and x[i] < (N-1)*H):
            x[i] = H*np.round(x[i]/H)
        else:
            x[i] = (N-1)*H
        #x[i] += minimo
    x = x + minimo
    return x


