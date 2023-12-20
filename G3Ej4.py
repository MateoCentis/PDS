import numpy as np
import matplotlib.pyplot as plt
import math
from senoidal import senoidal
PI = math.pi
from ondaCuadrada import ondaCuadrada
#-------------------------------------------------------------------------FUNCIONES------------------------------------------------------------------------

def senoidales(phi):
    res = [0]
    ta = 0
    tb = 5
    fm = 50
    A=1
    fs = 1
    for i in range(1,11):
        fs = i + 1 
        if phi != 0:
            phi = fs-1
        _, aux = senoidal(ta, tb, fm, fs, A, phi*(PI/2))
        res.append(aux)
    return res

def generarSignal(a,phi):#combinacion lineal de funciones seno
    sins = senoidales(phi)
    y =  a[0]*sins[1] + a[1]*sins[2] + a[2]*sins[3] +a[3]*sins[4] +a[4]*sins[5] \
         + a[5]*sins[6] + a[6]*sins[7] + a[7]*sins[8] +a[8]*sins[9] + a[9]*sins[10]

    return y
#-------------------------------------------------------------------------GENERAL------------------------------------------------------------------------
#1) y[n] = sum a_i * sin_i
#donde los i son funciones seno
#mido el parecido de y con cada 
#uno de los e_i y con eso hacer 
#el grafico de barras

coeficientesA = np.array([2,-5,3,1,8,-3,-1,7,-4,6])

y1 = generarSignal(coeficientesA,0)
ei = senoidales(0)
prodInterno = []
for i in range(1,11):
    prodInterno.append(np.dot(y1,ei[i]))

xBarras = ['e1','e2','e3','e4','e5','e6','e7','e8','e9','e10']
figure1 = plt.figure()
plt.bar(xBarras,prodInterno,color='black') 
plt.xlabel('Valores según frecuencia')
plt.ylabel('Resultado del producto interno')
plt.title('Grado de parecido de combinación lineal de senoidales')


#2)lo mismo que el y anterior pero ahora a los e_i se les varia la fase
# y1 = generarSignal(coeficientesA,PI)
ei2 = senoidales(PI)
prodInterno = []
for i in range(1,11):
    prodInterno.append(np.dot(y1,ei2[i]))

xBarras = ['e1','e2','e3','e4','e5','e6','e7','e8','e9','e10']
figure2 = plt.figure()
plt.bar(xBarras,prodInterno,color='orange') 
plt.xlabel('Valores según frecuencia (desfasada)')
plt.ylabel('Resultado del producto interno')
plt.title('Grado de parecido de combinación lineal de senoidales (desfasadas)')

#3)hacemos una onda cuadrada
#y la comparamos con las e_i de (1)
ta = 0
tb = 5
fm = 50
A=1
fs = 5.5
phi=0
_,y3 = ondaCuadrada(ta, tb, fm, fs, A, phi)
prodInterno = []
for i in range(1,11):
    prodInterno.append(np.dot(y3,ei[i]))

xBarras = ['e1','e2','e3','e4','e5','e6','e7','e8','e9','e10']
figure3 = plt.figure()
plt.bar(xBarras,prodInterno,color='blue') 
plt.xlabel('Valores según frecuencia')
plt.ylabel('Resultado del producto interno')
plt.title('Grado de parecido onda cuadrada')
plt.show()
#hacer conclusiones acerca de la magnitud
#de los graficos de barra

