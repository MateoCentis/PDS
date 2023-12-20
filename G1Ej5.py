import numpy as np
import matplotlib.pyplot as plt
from senoidal import senoidal
fs=4000
ta=0
tb=2
fm=129
amplitud=1
phi=0
t,x = senoidal(ta, tb, fm, fs, amplitud, phi)
plt.stem(t,x)
plt.title('Ejercicio 5')
plt.grid()
#plt.grid()
plt.show()
#estime la frecuencia de la onda sinusoidal?
#1 ciclo por segundo, ya que se observan dos ciclos en dos segundos
#teorema del muestreo => fm>=2fs