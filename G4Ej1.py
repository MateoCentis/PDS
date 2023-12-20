import numpy as np
import numpy.fft as fft
import scipy as spy
import matplotlib.pyplot as plt
from senoidal import senoidal
from DFT import graficarDFT
from DFT import DFT
#---------------------------------------------Parte 1--------------------------------------------
fs1=10 
fs2=20
Tm=0.001
fm= 1/Tm
A1=1
A2=4 #amplitud = 4
phi=0
ta=0
tb=1
t,s1 = senoidal(ta, tb, fm, fs1, A1, phi)
_,s2 = senoidal(ta, tb, fm, fs2, A2, phi)
s =  s1 + s2

# fig1 = plt.figure()
graficarDFT(t,s,'Senoidal s1+s2')


#---------------------------------------------Parte 2--------------------------------------------

N = len(s)
P1 = np.sum(s**2)
S = np.fft.fft(s) 
P2 = (1/N)*np.sum(abs(S)**2)
if P1 == P2:
    print('Son iguales')#Las energías son iguales
#---------------------------------------------Con cambios--------------------------------------------
#---------------------------------------------Parte 1-------------------------------------------------
# t,s1 = senoidal(ta, tb, fm, fs1, A, phi)
# _,s2 = senoidal(ta, tb, fm, fs2, A, phi)
s = s1 + s2 + 4 
#que va a pasar con la transformada:
    #RESPUESTA: Al adicionar una constante, la cual tiene frecuencia 0, lo que se sucede es que se
                #  puede ver en el espectro frecuencial que se agrega una componente en el 0
# fig2 = plt.figure()
graficarDFT(t,s, 'Senoidal: s1+s2+4')

#---------------------------------------------Parte 2-------------------------------------------------
fs1 = 10
fs2 = 11
#En este caso se ve una componente frecuencial en la frecuencia 10 y 11 en vez de 10 y 20.
t,s1 = senoidal(ta, tb, fm, fs1, A1, phi)
_,s2 = senoidal(ta, tb, fm, fs2, A2, phi)
s = s1 + s2 
graficarDFT(t,s,'Senoidal fs1=10,fs2=11')
#---------------------------------------------Parte 3-------------------------------------------------
fs1 = 10
fs2 = 10.5
t,s1 = senoidal(ta, tb, fm, fs1, A1, phi)
_,s2 = senoidal(ta, tb, fm, fs2, A2, phi)
s = s1 + s2 
graficarDFT(t,s,'Senoidal fs1=10,fs2=10.5')
#En este caso pueden verse frecuencias aparentes que no estaban presentes en la señal original,
# ya que ambas frecuencias se encuentran muy cercanas entre sí con lo cual el aporte de cada
#  una de ellas en el espectro se ve interferido uno con otro.
#---------------------------------------------Parte 4-------------------------------------------------
#Al considerar un tiempo de análisis mayor el espacio entre frecuencias el delta f 
# se vuelve lo suficientemente grande como para que no exista presencia de alias.


fs1 = 10
fs2 = 10.5
tb=2
t,s1 = senoidal(ta, tb, fm, fs1, A1, phi)
_,s2 = senoidal(ta, tb, fm, fs2, A2, phi)
s = s1 + s2 
graficarDFT(t,s,'Senoidal fs1=10,fs2=10.5, tb=2')
plt.show()