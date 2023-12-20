import numpy as np
import matplotlib.pyplot as plt
from senoidal import senoidal
from ondaCuadrada import ondaCuadrada
from fsinc import fSinc
import math
pi = math.pi
#Ejercicio 1
fm=100
fs=3
phi=0
A=1
#1
a = 0
b = 1
t,x = senoidal(a,b,fm,fs,A,phi)
figure1 = plt.figure()
plt.title('Senoidal',color='blue')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.stem(t,x)
#2
#rand(a,b) a:filas b:columnas
a=-1
b=1
t,x = fSinc(a,b,fm,fs,A,phi)
figure2 = plt.figure()
plt.title('Función sinc',color='orange')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.stem(t,x)

#3
a=0
b=1
t,x = ondaCuadrada(a,b,fm,fs,A,phi)
figure3 = plt.figure()
plt.title('Onda cuadrada',color='red')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.stem(t,x)
#anda todo

plt.show()
