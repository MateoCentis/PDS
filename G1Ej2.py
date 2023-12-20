import numpy as np
import math
import matplotlib.pyplot as plt
from senoidal import senoidal
from cuantizacion import cuantizacion
from rectificacion import rectificacion
from inversion import inversion

def cuantizacionN (y, N,H):
#n son los niveles de cuantizacion

    ynuevo=y-np.min(y)
    cuant=ynuevo

    #de acuerdo a qué valor de y me encuentre le asigno los distintos valores a cuant
    idx_menor_0 = np.where(ynuevo<0)
    idx_medio = np.where(np.logical_and(ynuevo>=0, ynuevo<(N-1)*H))
    idx_mayor = np.where(ynuevo>=(N-1)*H)

    cuant[idx_menor_0] = 0
    cuant[idx_medio] = H * np.fix(ynuevo[idx_medio]/H)
    cuant[idx_mayor] = (N-1) * H

    #sumo el minimo para volver a tener el rango original
    cuanti=cuant+min(y)
    return cuanti

#para subfig------------
fig,axs = plt.subplots(3,1)
plt.suptitle('Senoidales con operaciones')

#-----------------------
fm=100
fs=3
phi=math.pi
A=1;
t,x=senoidal(0,1,fm,fs,A,phi)
#invertida
xI = inversion(x)
axs[0].grid()
axs[0].title.set_text('Invertida')
axs[0].plot(t,xI)
# axs[0].title('Invertida')
# plt.plot(t,xI)
# plt.title('Invertida')
# plt.show()
#rectificacion
xR = rectificacion(x)
axs[1].grid()
axs[1].title.set_text('Rectificada')
axs[1].plot(t,xR)
# plt.plot(t,xR)
# plt.show()
#cuantizada
plt.plot(t,x)
N=8
H=(max(x)-min(x))/N
print(H)
x = cuantizacion(x, N, H)
# x = cuantizacionN(x, N, H)
axs[2].grid()
axs[2].title.set_text('Cuantizada')
axs[2].stem(t,x)
# plt.plot(t,x)
# plt.show()

#en subfig
plt.show()