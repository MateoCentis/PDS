import numpy as np
import matplotlib.pyplot as plt
from senoidal import senoidal

fs = 5
ta=0
tb=1
A=1
phi=0
fm0=100
figure1 = plt.figure()
plt.title('Senoidal con 100 muestras por segundo')
t,x=senoidal(ta,tb,fm0,fs,A,phi)
plt.stem(t,x)
# plt.plot(t,x)
# plt.show()

fm1=25
figure2 = plt.figure()
plt.title('Senoidal con 25 muestras por segundo')
t,x=senoidal(ta,tb,fm1,fs,A,phi)
plt.stem(t,x)
# plt.plot(t,x)
# plt.show()

fm2=10
figure3 = plt.figure()
plt.title('Senoidal con 10 muestras por segundo')
t,x=senoidal(ta,tb,fm2,fs,A,phi)
plt.stem(t,x)
# plt.plot(t,x)
# plt.show()

fm3=4
figure4 = plt.figure()
plt.title('Senoidal con 4 muestras por segundo')
t,x=senoidal(ta,tb,fm3,fs,A,phi)
plt.stem(t,x)

fm4=1
figure5 = plt.figure()
plt.title('Senoidal con 1 muestra por segundo')
t,x=senoidal(ta,tb,fm4,fs,A,phi)
plt.stem(t,x)
# plt.show()

fm5=0.5
figure6 = plt.figure()
plt.title('Senoidal con 0.5 muestras por segundo')
t,x=senoidal(ta,tb,fm5,fs,A,phi)
plt.stem(t,x)
plt.show()
#se ve claramente en los casos de 100 y 25 porque cumplen firmemente con el teorema del muestreo
#el de 10 aunque lo cumple no se logra diferenciar con claridad la frecuencia de 5 hz, todos los valores son
    #cercanos a cero porque son multiplos de pi por el espaciado elegido 
#en el plot con fs=4 hz s