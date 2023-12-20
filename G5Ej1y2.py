import numpy as np
import matplotlib.pyplot as plt
import math
from DFT import DFT
import numpy.fft as fft
import scipy.signal as spy
pi = math.pi
#multiplicar por z^-n es igual a retardar a n en el tiempo


#1. H(z)=Y(z)/X(z)=z^2/(z^2-1/2*z+1/4)
def H1(z):
    return (z**2)/(z**2-(1/2)*z+1/4)
#2. H(z)=Y(z)/X(z)=z/(z^2-z-1)
def H2(z):
    return (z)/(z**2-z-1)
#3. h(Z)=Y(z)/X(z)=7z^2/(z^2-2z+6)
def H3(z):
    return (7*(z**2))/(z**2-2*z+6)
#4. 
def H4(z):
    H = 2
    coef = [2]
    for i in range(7):
        H += np.power(1/(2*z),i+1)
        coef.append(np.power(1/2,i+1))
    return H,coef

#H(z)->H[k]-> h[n]
#Si el sistema es FIR siempre se puede porque puedo discretizar en esa cantidad de términos 
    #el omega de fourier

fm = 10000 
N = 512
# frecs = np.arange(-fm//2, fm//2, fm/N)  
frecs = np.arange(0,fm,fm/N)
omega = np.arange(0, 2*pi, 2*pi/N)    #omega de 0 a 2pi, con salto N
ejw = np.exp(1j * omega)    #e^jw
#en vez de pasarle z le pasamos e^-njw

fig,axs = plt.subplots(4,2)

#1.
respuesta1 = fft.fftshift(np.abs(H1(ejw))) #Calculo de respuesta, tomo amplitud y lo desplazo
axs[0,0].plot(frecs,respuesta1)
axs[0,0].grid()
axs[0,0].title.set_text('Respuesta sistema 1')
axs[0,0].set_xlabel('frecuencias [hz]')
axs[0,0].set_ylabel('|H1(Z)|')
respuesta1Freqz = fft.fftshift(spy.freqz([1],[1,-1/2,1/4],whole=True)[1])

axs[0,1].plot(frecs,respuesta1Freqz) 
axs[0,1].title.set_text('Respuesta sistema 1 - Freqz')
axs[0,1].grid()
axs[0,1].set_xlabel('frecuencias [hz]')
axs[0,1].set_ylabel('|H1(Z)|')

#2
respuesta2 = fft.fftshift(np.abs(H2(ejw)))
axs[1,0].plot(frecs,respuesta2)
axs[1,0].grid()
axs[1,0].title.set_text('Respuesta sistema 2')
axs[1,0].set_xlabel('frecuencias [hz]')
axs[1,0].set_ylabel('|H2(Z)|')
respuesta2Freqz = np.abs(fft.fftshift(spy.freqz([0,1],[1,-1,-1],whole=True)[1]))

axs[1,1].plot(frecs,respuesta2Freqz) 
axs[1,1].title.set_text('Respuesta sistema 2 - Freqz')
axs[1,1].grid()
axs[1,1].set_xlabel('frecuencias [hz]')
axs[1,1].set_ylabel('|H2(Z)|')


#3.
respuesta3 = fft.fftshift(np.abs(H3(ejw)))
axs[2,0].plot(frecs,respuesta3)
axs[2,0].grid()
axs[2,0].title.set_text('Respuesta sistema 3')
axs[2,0].set_xlabel('frecuencias [hz]')
axs[2,0].set_ylabel('|H3(Z)|')
respuesta3Freqz = np.abs(fft.fftshift(spy.freqz([7],[1,-2,6],whole=True)[1]))

axs[2,1].plot(frecs,respuesta3Freqz) 
axs[2,1].title.set_text('Respuesta sistema 3 - Freqz')
axs[2,1].grid()
axs[2,1].set_xlabel('frecuencias [hz]')
axs[2,1].set_ylabel('|H3(Z)|')

#4.
respuesta4,coef= H4(ejw)
respuesta4 = fft.fftshift(np.abs(respuesta4))
axs[3,0].plot(frecs,respuesta4)
axs[3,0].grid()
axs[3,0].title.set_text('Respuesta sistema 4')
axs[3,0].set_xlabel('frecuencias [hz]')
axs[3,0].set_ylabel('|H4(Z)|')
respuesta4Freqz = np.abs(fft.fftshift(spy.freqz(coef,whole=True)[1]))

axs[3,1].plot(frecs,respuesta4Freqz) 
axs[3,1].title.set_text('Respuesta sistema 4 - Freqz')
axs[3,1].grid()
axs[3,1].set_xlabel('frecuencias [hz]')
axs[3,1].set_ylabel('|H4(Z)|')





plt.show()