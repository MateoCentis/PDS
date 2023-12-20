import numpy as np
import matplotlib.pyplot as plt
import math

PI = math.pi

def ondaCuadrada(ta,tb,fm,fs,A,phi):
    T = 1/fm
    t = np.arange(ta,tb-T,T)
    x = 2*PI*fs*t+phi
    y = np.zeros(len(x))
    for i in np.arange(0,len(x),1):
        if (np.mod(x[i],2*PI)>PI):
            y[i] = -1
        else:
            y[i] = 1
    return t,y

# ta = 0
# tb = 5
# fm = 50
# A=1
# fs = 5.5
# phi=0
# t,y = ondaCuadrada(ta, tb, fm, fs, A, phi)
# plt.plot(t,y)
# plt.show()