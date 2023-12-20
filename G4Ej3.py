import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft
from senoidal import senoidal
from DFT import DFT
from DFT import graficarDFT
import math
pi = math.pi
#x[n] -> X[k]
#x[n-p] <--> X[k]*e^{(-j*2*pi*k*p)/N}
#Agarramos x[n] lo transformamos a X[k] y a X[k] le aplicamos el retardo y hacemos la inversa
#para llegar a x[n-p]
#verificar
fs=10
fm=100
ta=0
tb=1
A=1
phi = 0
t0 = 5
t,s = senoidal(ta, tb, fm, fs, A, phi)
s = np.concatenate([s,np.zeros(30)])
S = fft.fft(s)
retardo = 10
# Sretardada = S * np.exp((-1j*2*pi*np.arange(1,len(s)+1,1)*retardo)/len(s))
# k = np.arange(0,len(s),1)
k = np.arange(0,len(s),1)
Sretardada = S * np.exp((-1j*2*pi*k*retardo)/len(s))

sInvertida = fft.ifft(Sretardada)

fig, axs = plt.subplots(2)
axs[0].stem(s)
axs[0].title.set_text('senoidal original')
axs[0].set_xlabel('Tiempo (s)')
axs[0].set_ylabel('Amplitud')

axs[1].stem(np.real(sInvertida))
# axs[1].stem(sInvertida)
axs[1].title.set_text('senoidal desplazada')
axs[1].set_xlabel('Tiempo (s)')
axs[1].set_ylabel('Amplitud')

plt.tight_layout()
plt.show()