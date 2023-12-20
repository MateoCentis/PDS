import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft
# from scipy.signal import hamming
from senoidal import senoidal
from DFT import DFT
from DFT import graficarDFT
import math
pi = math.pi

#Hacer con varios niveles de dispersion de la señal temporal
#graficar la señal en el dominio del tiempo y de frecuencia y ver como 
#al concentrar en una se dispersa en la otra

ta=0
tb=1


fig,axs = plt.subplots(4,2)

#
N=15
ventanaHamming = np.hamming(N)
zeros = np.zeros((100-len(ventanaHamming))//2)
ventanaHamming = np.concatenate([zeros,ventanaHamming])
ventanaHamming = np.concatenate([ventanaHamming,zeros])
t = np.arange(ta,tb,1/len(ventanaHamming))
axs[0,0].stem(t,ventanaHamming)
axs[0,0].grid()
axs[0,0].title.set_text(str(N)+' muestras')
axs[0,0].set_xlabel('Tiempo (s)')
axs[0,0].set_ylabel('Amplitud')
freqs,ventanaHammingF = DFT(t,ventanaHamming)
axs[0,1].stem(freqs,ventanaHammingF)
axs[0,1].title.set_text('Espectro de Fourier')
axs[0,1].grid()
axs[0,1].set_xlabel('Frecuencia (Hz)')
axs[0,1].set_ylabel('Amplitud de fft |S(f)|')

N=30
ventanaHamming = np.hamming(N)
zeros = np.zeros((100-len(ventanaHamming))//2)
ventanaHamming = np.concatenate([zeros,ventanaHamming])
ventanaHamming = np.concatenate([ventanaHamming,zeros])
t = np.arange(ta,tb,1/len(ventanaHamming))
axs[1,0].stem(t,ventanaHamming)
axs[1,0].grid()
axs[1,0].title.set_text(str(N)+' muestras')
axs[1,0].set_xlabel('Tiempo (s)')
axs[1,0].set_ylabel('Amplitud')
freqs,ventanaHammingF = DFT(t,ventanaHamming)
axs[1,1].stem(freqs,ventanaHammingF)
axs[1,1].title.set_text('Espectro de Fourier')
axs[1,1].grid()
axs[1,1].set_xlabel('Frecuencia (Hz)')
axs[1,1].set_ylabel('Amplitud de fft |S(f)|')

N=45
ventanaHamming = np.hamming(N)
zeros = np.zeros((100-len(ventanaHamming))//2)
ventanaHamming = np.concatenate([zeros,ventanaHamming])
ventanaHamming = np.concatenate([ventanaHamming,zeros])
t = np.arange(ta,tb,1/len(ventanaHamming))
axs[2,0].stem(t,ventanaHamming)
axs[2,0].grid()
axs[2,0].title.set_text(str(N)+' muestras')
axs[2,0].set_xlabel('Tiempo (s)')
axs[2,0].set_ylabel('Amplitud')
freqs,ventanaHammingF = DFT(t,ventanaHamming)
axs[2,1].stem(freqs,ventanaHammingF)
axs[2,1].title.set_text('Espectro de Fourier')
axs[2,1].grid()
axs[2,1].set_xlabel('Frecuencia (Hz)')
axs[2,1].set_ylabel('Amplitud de fft |S(f)|')

N=60
ventanaHamming = np.hamming(N)
zeros = np.zeros((100-len(ventanaHamming))//2)
ventanaHamming = np.concatenate([zeros,ventanaHamming])
ventanaHamming = np.concatenate([ventanaHamming,zeros])
t = np.arange(ta,tb,1/len(ventanaHamming))
axs[3,0].stem(t,ventanaHamming)
axs[3,0].grid()
axs[3,0].title.set_text(str(N)+' muestras')
axs[3,0].set_xlabel('Tiempo (s)')
axs[3,0].set_ylabel('Amplitud')
freqs,ventanaHammingF = DFT(t,ventanaHamming)
axs[3,1].stem(freqs,ventanaHammingF)
axs[3,1].title.set_text('Espectro de Fourier')
axs[3,1].grid()
axs[3,1].set_xlabel('Frecuencia (Hz)')
axs[3,1].set_ylabel('Amplitud de fft |S(f)|')



plt.tight_layout()













plt.show()