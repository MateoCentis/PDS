import numpy as np
import matplotlib.pyplot as plt
from senoidal import senoidal
from cuadrada import cuadrada
from DFT import graficarDFT
from DFT import DFT
#verificar que los vectores sean ortogonales en los dominios
#
fs1 = 2
fs2 = 4
phi = 0
fm = 100
ta = 0
tb = 1
A = 1
#Señal (a)
t,sen1 = senoidal(ta, tb, fm, fs1, A, phi) #a
t,cuadrada = cuadrada(ta, tb, fm, fs1, phi) #b 
t,sen2 = senoidal(ta, tb, fm, fs2, A, phi) #c

#---------------------------------------------Parte 1-------------------------------------------------
#a y b
prodAB = np.dot(sen1,cuadrada)
#b y c
prodBC = np.dot(sen2,cuadrada)
#a y c
prodAC = np.dot(sen1,sen2)

print('Producto a y b: ',prodAB) 
print('Producto b y c: ',prodBC) #ortogonales
print('Producto a y c: ',prodAC) #ortogonales
print(' ')
#---------------------------------------------Parte 2-------------------------------------------------
freqSen1,amplitudSen1 = DFT(t,sen1)
freqSen2,amplitudSen2 = DFT(t,sen2)
freqCuadrada,amplitudCuadrada = DFT(t,cuadrada)
prodTAB = np.dot(amplitudSen1,amplitudCuadrada)
prodTBC = np.dot(amplitudSen2,amplitudCuadrada)
prodTAC = np.dot(amplitudSen1,amplitudSen2)

print('Producto transformado a y b: ',prodTAB) 
print('Producto transformado b y c: ',prodTBC) #ortogonales
print('Producto transformado a y c: ',prodTAC) #ortogonales
print(' ')
#Al realizar el producto punto en el espacio frecuencial se puede verificar la propiedad de que
#se mantienen las ortogonalidades al cambiar el espacio, dado que se trata de una rotación 
#de las bases que no afecta a la ortogonalidad de las mismas. Del mismo modo, los vectores que 
#no eran ortogonales siguen sin serlo.
#---------------------------------------------Parte 3-------------------------------------------------
fs2 = 3.5
t,sen2 = senoidal(ta, tb, fm, fs2, A, phi) #redefino señal c
_,amplitudSen3 = DFT(t,sen2)
prodAC = np.dot(sen1,sen2)
prodTAC = np.dot(amplitudSen1,amplitudSen3)
print('Señal redefinida producto a y c',prodAC) #ortogonales
print('Señal redefinida transformada producto a y c',prodTAC)#no ortogonales

#En este caso a aparecer frecuencias aparentes en el espectro de la señal de 3.5 Hz
#de frecuencia, la ortogonalidad en el dominio frecuencial no se mantiene, 
#porque el espectro de la segunda señal contiene alias.

#grafico de a) y c)
graficarDFT(t, sen1, 'Señal a')
graficarDFT(t, sen2, 'Señal c fs=3')
plt.show()