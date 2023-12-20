import numpy as np
import numpy.fft as fft
import scipy as spy
import matplotlib.pyplot as plt

def graficarDFT(t,s,titulo):
    fig, axs = plt.subplots(2)
    axs[0].stem(t,s)
    axs[0].title.set_text(titulo)
    axs[0].set_xlabel('Tiempo (s)')
    axs[0].set_ylabel('Amplitud')

    frecuencias, magnitudes = DFT(t,s)
    axs[1].stem(frecuencias, magnitudes)
    axs[1].title.set_text('Espectro de Fourier')
    axs[1].set_xlabel('Frecuencia (Hz)')
    axs[1].set_ylabel('Amplitud de fft |S(f)|')
    plt.tight_layout()

def graficarDFT2(t,s,titulo):
    fig, axs = plt.subplots(2)
    axs[0].stem(t,s)
    axs[0].title.set_text(titulo)
    axs[0].set_xlabel('Tiempo (s)')
    axs[0].set_ylabel('Amplitud')

    frecuencias, magnitudes = DFT2(s)
    axs[1].stem(frecuencias, magnitudes)
    axs[1].title.set_text('Espectro de Fourier')
    axs[1].set_xlabel('Frecuencia (Hz)')
    axs[1].set_ylabel('Amplitud de fft |S(f)|')
    plt.tight_layout()

def DFT(t,s):
    T = np.abs(t[0]-t[1])
    fm = 1/T
    S = np.abs(fft.fft(s))
    deltaF = fm/len(t)

    frecuencias = np.arange((-fm/2)+deltaF,(fm/2)+deltaF,deltaF)
    if (np.mod(len(S),2)==0):
        positivos = S[0:int((len(S)/2))+1]
        negativos = S[int((len(S)/2))+1:len(S)]
    else:
        positivos = S[0:int((len(S)/2))]
        negativos = S[int((len(S)/2)):len(S)]

    S = np.concatenate((negativos,positivos))
    return frecuencias,S


    
    return freqs,mag

def DFT2(s):
    S = np.fft.fft(s) 
    freqs = np.fft.fftfreq(len(s)) * len(s)#fftfreq devuelve las frecuencias de la fft
    mag = np.abs(S)
    freqs = freqs[:len(freqs)//2]
    mag = mag[:len(mag)//2]
    return freqs,mag