import numpy as np
import matplotlib.pyplot as plt
from senoidal import senoidal
from DFT import graficarDFT
from DFT import DFT
A=2
phi=0
fm = 50
fs = 27
ta = 0
tb = 1
t,s = senoidal(ta, tb, fm, fs, A, phi)
graficarDFT(t,s,'Señal')
#a) 23 ciclos (no se cumple teorema de muestreo), se genera una frecuencia aparente

#b)Ecuacion f_0= |f_s-f_m*round(f_s/f_m)|

fs = 105 
t, s = senoidal(ta, tb, fm, fs, A, phi)
fTrucha = np.abs(fs-fm*np.round(fs/fm))
print('Frecuencia en el espectro',fTrucha)
graficarDFT(t, s, 'Senoidal de 105 hz')
#c)La relación entre la magnitud observada de la transformada y la amplitud de la señal original es
#A_e=(A*N)/2

plt.show()