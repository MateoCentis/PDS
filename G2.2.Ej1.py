import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scipy.signal as spy
from animacionConvolucion import animacionConvolucion
#Definicion de convolucion-------------------------------------------------------
#Impulso de entrada (x)
#Respuestea al impulso (h)
#Se multiplica todos los coeficientes de h por uno de x y para el siguiente x 
    #se desplaza y se vuelve a hacer lo mismo
def convolucion(x,h):
    #el size de la convolucion es len(x)+len(h)-1
    size = (len(x) + len(h)) - 1
    y = np.zeros(size)
    for k in np.arange(0,len(x),1):
        suma = 0
        for i in np.arange(0,len(h),1):
            suma = x[k]*h[i] #voy multiplicando uno por unos los x por las respuestas al impulso i
            y[k+i] += suma   #y los voy guardando desplazados según corresponda la i 
    return y

#forma alternativa 
def convolucion2(x,h):
    size = (len(x) + len(h) - 1)
    y = np.zeros(size)
    # Realizar la convolución
    for k in range(size):
        suma = 0
        for n in range(len(x)):
            if k - n < 0 or k - n >= len(h):
                continue
            suma += x[n] * h[k - n]
        y[k] = suma
    return y

#vectores de prueba---------------------------------------------------------------
x = np.array([1,2,2])
h = np.array([2,1,0.5])

res1 = convolucion(x, h)
res2 = np.convolve(x, h)
n = np.arange(0,len(res1),1)
# plt.stem(n,res1)
# plt.show()
# plt.stem(n,res2)
# plt.show()
#Funciona
#--------------------------------------------------------------------------------
#Animacion
animacionConvolucion(n, res2,[-1,5],[0,10],'Convolución')
#--------------------------------------------------------------------------------
#Filtro--------------------------------------------------------------------------
#coeficientes de y
# a = np.zeros()
# a[0] = 1
#coeficientes de x
b = h
#Hacer zero padding
y = spy.lfilter(b,[1.0],x) #Da longitud porque usa la circular, [1.0] multiplica al y[n]
yZP = spy.lfilter(b,[1.0],x)
n = np.arange(0,len(y),1)
# plt.stem(n,y)
# plt.show()

print(res1)
print(res2)
print(y)
print(yZP)

