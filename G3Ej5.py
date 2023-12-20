import numpy as np
import matplotlib.pyplot as plt
from senoidal import senoidal
import math
PI = math.pi
#---------------------------------------------------GENERAL------------------------------------------------------------------  
#agarrar para cada tramo de senial y probar el producto interno con cada valor numerico "sintetico"
#quedarse con el mejor de estos.

#hacer la decodificacion por filas y luego por columnas aprovechando la linealidad
def chequeo(data,frecuencias):
    ta = 0
    fm = 11025
    tb = len(data)/fm
    A = 1
    #chequear frecuencias y por cada frecuencia chequear fases
    mayoresFrecuencias = np.zeros(len(frecuencias))
    phis = np.linspace(0,2*PI,500)
    sizePhis = len(phis)
    for i in np.arange(0,len(frecuencias),1):#en frecuencias mandamos la lista con frecuencias correspondiente a las filas o columnas
        fs = frecuencias[i]
        frecuenciasPorFase = np.zeros(sizePhis)
        for j in np.arange(0,sizePhis,1):
            _,sen = senoidal(ta, tb, fm, fs, A, phis[i])
            frecuenciasPorFase[j] = np.dot(sen,data)    
        mayoresFrecuencias[i] = np.max(frecuenciasPorFase) #vector con los maximos valores para cada frecuencia
    maximo = np.max(mayoresFrecuencias)
    return np.where(mayoresFrecuencias == maximo)[0]


#---------------------------------------------------CALCULO------------------------------------------------------------------
datos = np.loadtxt('te.txt')
#print(len(datos))
n = np.arange(0,len(datos),1)
plt.plot(n,datos)
plt.show()
frecuenciaSignal = 11025
#697, 770, 852, 941
#1209, 1336, 1477
frecuenciasFilas = np.array([697, 770, 852, 941])
frecuenciasColumnas = np.array([1209, 1336, 1477])

#1er ventana(17000,21300)--------------------------------------
numero1 = datos[17500:21700]
fila1 = chequeo(numero1, frecuenciasFilas)
columna1 = chequeo(numero1, frecuenciasColumnas)
print(fila1,'-',columna1,'tendria que ser (0,1)')#(0,1)

#2da ventana(30300,34500)---------------------------------
numero2 = datos[29600:33700]
fila2 = chequeo(numero2, frecuenciasFilas)
columna2 = chequeo(numero2, frecuenciasColumnas)
print(fila2,'-',columna2,'tendria que ser (1,0)')#(1,0)

#3era ventana(39500,43300)---------------------------------
numero3 = datos[39700:43400]
fila3 = chequeo(numero3, frecuenciasFilas)
columna3 = chequeo(numero3, frecuenciasColumnas)
print(fila3,'-',columna3,'tendria que ser (0,1)')#(0,1)

#4ta ventana(48500,52500)--------------------------------------
numero4 = datos[48000:52700]
fila4 = chequeo(numero4, frecuenciasFilas)
columna4 = chequeo(numero4, frecuenciasColumnas)
print(fila4,'-',columna4,'tendria que ser (2,1)')#(2,1)

#5ta ventana(59000,63200)--------------------------------------
numero5 = datos[58500:64000]
fila5 = chequeo(numero5, frecuenciasFilas)
columna5 = chequeo(numero5, frecuenciasColumnas)
print(fila5,'-',columna5,'tendria que ser (0,1)')#()

#6ta ventana(69700,74100)--------------------------------------------
numero6 = datos[69900:75000]
fila6 = chequeo(numero6, frecuenciasFilas)
columna6 = chequeo(numero6, frecuenciasColumnas)
print(fila6,'-',columna6,'tendria que ser (1,2)')#
#7ma ventana(80800,85200)--------------------------------------------
numero7 = datos[79000:85900]
fila7 = chequeo(numero7, frecuenciasFilas)
columna7 = chequeo(numero7, frecuenciasColumnas)
print(fila7,'-',columna7,'tendria que ser (1,1)')#

#1 2 3
#4 5 6
#7 8 9
#* 0 #
#2428265