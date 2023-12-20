import numpy as np
import matplotlib.pyplot as plt
from animacionConvolucion import animacionConvolucion

def ha(x):
    y = np.sin(8*x)
    return y

def hb(x,a):
    for i in range(len(x)):
        if x[i] < 0:
            x[i] = 1/x[i]
        x[i] = np.power(a,x[i])
    # x = np.power(a,x)   
    return x

#El objetivo de hacer el ej es ver si la convolucion es conmutativa
a = 0.3 #arbitrario
N = 20
x = np.arange(0,N-1,1)
x[0] = 1
x[1] = -a
n = np.arange(0,len(x),1)
#|a|<1

ha = ha(n)
hb = hb(n,a)

#x[n] y ha[n] -> wa
wa = np.convolve(x,ha)
#wa ahora es entrada con hb
resB = np.convolve(wa,hb)

# print(wa)
# print(yb)
# print(resB)
n = np.arange(0,len(wa) + len(hb) -1,1)
# plt.stem(n,resB)
# plt.show()
sizeN = len(n)
minimo = min(resB)
maximo = max(resB)


# animacionConvolucion(n, 
#                     resB,
#                     [n[0]-1,
#                     sizeN+1],
#                     [minimo-1,
#                     maximo+1],
#                     'Convolucion hA->hB')
#Primero B luego A
wb = np.convolve(x,hb)
resA = np.convolve(wb,ha)
# animacionConvolucion(n,
#                     resA,
#                     [n[0]-1,
#                     len(n)+1],
#                     [min(resA)-1,
#                     max(resA)+1],
#                     'Convolucion hB->hA')

fig,axs = plt.subplots(1,2)
axs[0].stem(n,resA)
axs[0].grid()
axs[0].title.set_text('Convolucion hA->hB')
axs[0].set_xlabel('n')
# axs[0].set_ylabel('')

axs[1].stem(n,resB)
axs[1].grid()
axs[1].title.set_text('Convolucion hB->hA')
axs[1].set_xlabel('n')
# axs[1].set_ylabel('Amplitud')
# plt.stem(n,resA)
plt.show()
# print(resA)
# print(resB)