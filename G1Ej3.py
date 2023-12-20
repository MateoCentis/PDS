import numpy as np
import matplotlib.pyplot as plt
from senoidal import senoidal
import math
pi = math.pi
Tm = 0.1/80#8 muestras cada 0.01 segundos
fs = 2/0.1 #2 ciclos en 0.1 s
t1 = 5*Tm
phi = -2*pi*fs*t1   #phi=2 pi fs t1 donde t1 es el retardo en segundos (tiempo que tarda en hacer en cruzar cero)
# t = np.arange(0,0.1-Tm,Tm) #periodo de muestreo
# arg = 2.*pi*fs*t+phi
A = 3;
# x = A*np.sin(arg)
ta = 0
tb = 0.1
fm = 1/Tm
t,x = senoidal(ta, tb, fm, fs, A, phi)
plt.stem(t,x)
plt.grid()
plt.title('Señal senoidal discreta')
plt.show()
