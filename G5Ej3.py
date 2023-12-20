import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as spy
from zplane import zplane
#Sacar raices numerador y denominador 

#Para determinar la respuesta al impulso:
#-Pasamos a negativo las z^n multiplicando por z elevado al coeficiente mas alto negativo
#Numerador: z=1, z= 1/2 +- j\sqrt(3)/2
#Denominador: z=1
#numerador (ceros)
b = np.array([1,-2,2,-1])
#denominador (polos)
a = np.array([1,-1.7,0.8,-0.1])
# -0.2z + 0.3 - 0.1 z^-1
# a = np.array([-0.2,0.3,-0.1,0,0])
#polos y ceros, es estable
raicesB, raicesA, k = zplane(b, a)
print('Raices numerador: ',raicesB)
print('Raices denominador: ',raicesA)
print('k: ',k)

#Respuesta al impulso del sistema
h = np.zeros(10)
h[0] = 1
respuestaImpulso = spy.lfilter(b,a,h)
fig2 = plt.figure()
plt.stem(respuestaImpulso)
plt.title('Respuesta al impulso')
plt.xlabel('Muestras')
plt.ylabel('h[n]')
plt.show()