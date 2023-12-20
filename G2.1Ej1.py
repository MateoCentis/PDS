import numpy as np
import math
import matplotlib.pyplot as plt

pi = math.pi

#definir si son causales, lineales,
#invariantes en el tiempo y si poseen memoria

#Invariante en el tiempo: si la función que multiplica al impulso es constante,
    #(desplazamiento en la entrada produce mismo desplazamiento en la salida)
#causal: Salida depende solo de valores de la entrada anteriores o actuales
#Memoria: la salida depende de valores anteriores de la entrada
    #sin memoria: la salida depende solo de valores actuales
#lineales: la suma ponderada de entradas produce una suma ponderada en la salida, debe cumplir cono 
    #

def f1(x,fs,T,A):
    for n in np.arange(0,len(x),1):
        x[n] = A*np.sin(2*pi*fs*n*T)*x[n]
    return x
#f1: -Causal, -no lineal, -variante en el tiempo , -no tiene memoria

def f2(x,n0):
    for n in np.arange(0,len(x),1):
        a = n - n0
        b = n + n0
        suma = 0
        if (a > 0 and b < len(x)):
            for i in (a,b,1):
                suma += x[i]
        x[n] = suma
    return x
#f2: -No causal, -Lineal, -No variante, -Memoria

def f3(x):
    x = x + 2
    return x
#f3: -Causal, -no Lineal, -No variante, -Sin memoria

def f4(x):
    for n in np.arange(0,len(x),1):
        x[n] = n*x[n]
    return x
# -Causal, -lineal, -Variante, -Sin memoria


x = np.zeros(30)
n = np.arange(0,len(x),1)
x[0]=1
x[1]=1
x[5]=1
x[10]=1

#Problema (1) -----------
A=1
fs=20
T = 0.001
x1 = f1(x,fs,T,A)
fig,axs = plt.subplots(2,2)
axs[0,0].stem(n,x1)
axs[0,0].grid()
axs[0,0].title.set_text('Salida sistema 1')
axs[0,0].set_xlabel('Tiempo (s)')
axs[0,0].set_ylabel('Amplitud')

#Problema (2) ----------
n0=5
x2 = f2(x,2)
axs[1,0].stem(n,x2)
axs[1,0].grid()
axs[1,0].title.set_text('Salida sistema 2')
axs[1,0].set_xlabel('Tiempo (s)')
axs[1,0].set_ylabel('Amplitud')

#Problema (3) ---------
x3 = f3(x)
axs[0,1].stem(n,x3)
axs[0,1].grid()
axs[0,1].title.set_text('Salida sistema 3')
axs[0,1].set_xlabel('Tiempo (s)')
axs[0,1].set_ylabel('Amplitud')
#Problema (4) ---------
x4 = f4(x)
axs[1,1].stem(n,x4)
axs[1,1].grid()
axs[1,1].title.set_text('Salida sistema 4')
axs[1,1].set_xlabel('Tiempo (s)')
axs[1,1].set_ylabel('Amplitud')

plt.tight_layout()
plt.show()  
