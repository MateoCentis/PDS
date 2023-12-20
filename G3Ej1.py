import numpy as np
import matplotlib.pyplot as plt
from randomSignal import randomF
from senoidal import senoidal
from ondaCuadrada import ondaCuadrada
from funcionRampa import funcionRampa
import math

def potenciaMedia(x):
    return np.linalg.norm(x,2)**2/(len(x))

def raizValorCuadratico(x):
    return np.sqrt(potenciaMedia(x))

PI = math.pi

ta = -5
tb = 5
fm = 12
fs = 1
phi = 0
A = 1

ts,fSenoidal = senoidal(ta, tb, fm, fs, A, phi)
tc,fCuadrada = ondaCuadrada(ta, tb, fm, fs, A, phi)

n = np.arange(-20,20,1)
fRand = randomF(n)
fRampa = funcionRampa(n)

#1,2 y 3)Valor medio, max y min
medSenoidal = np.mean(fSenoidal)
maxSenoidal = max(fSenoidal)
minSenoidal = min(fSenoidal)

medCuadrada = np.mean(fCuadrada)
maxCuadrada = max(fCuadrada)
minCuadrada = min(fCuadrada)

medRand = np.mean(fRand)
maxRand = max(fRand)
minRand = min(fRand)

medRampa = np.mean(fRampa)
maxRampa = max(fRampa)
minRampa = min(fRampa)

#4,5 y 6) amplitud, energia y accion
infSenoidal = np.linalg.norm(fSenoidal,np.inf) #amplitud
energiaSenoidal = np.linalg.norm(fSenoidal,2)**2 #energia
accionSenoidal = np.linalg.norm(fSenoidal,1) #accion

infCuadrada = np.linalg.norm(fCuadrada,np.inf)
energiaCuadrada = np.linalg.norm(fCuadrada, 2)**2
accionCuadrada = np.linalg.norm(fCuadrada,1)

infRand = np.linalg.norm(fRand,np.inf)
energiaRand = np.linalg.norm(fRand, 2)**2
accionRand = np.linalg.norm(fRand,1)

infRampa = np.linalg.norm(fRampa,np.inf)
energiaRampa = np.linalg.norm(fRampa, 2)**2
accionRampa = np.linalg.norm(fRampa,1)

#7 y 8) potencia media y raiz del valor cuadratico
#energia sobre longitud
potMedCuadrada = potenciaMedia(fCuadrada)
raizCuadra = raizValorCuadratico(fCuadrada)

potMedRand = potenciaMedia(fRand)
raizRand = raizValorCuadratico(fRand)

potMedRampa = potenciaMedia(fRampa)
raizRampa = raizValorCuadratico(fRampa)

potMedSenoidal = potenciaMedia(fSenoidal)
raizSenoidal = raizValorCuadratico(fSenoidal)
#raiz(energia/longitud)

#SENOIDAL
print(' ')
print('SENOIDAL')
print('Máximo:',maxSenoidal)
print('Medio:',medSenoidal)
print('Mínimo:',minSenoidal)
print('Amplitud:',infSenoidal)
print('Energía:',energiaSenoidal)
print('Acción:',accionSenoidal)
print('Potencia media:',potMedSenoidal)
print('Raíz del valor cuadrático:',raizSenoidal)


#CUADRADA
print(' ')
print('CUADRADA')
print('Máximo:',maxCuadrada)
print('Medio:',medCuadrada)
print('Mínimo:',minCuadrada)
print('Amplitud:',infCuadrada)
print('Energía:',energiaCuadrada)
print('Acción:',accionCuadrada)
print('Potencia media:',potMedCuadrada)
print('Raíz del valor cuadrático:',raizCuadra)

#RAND
print(' ')
print('RAND')
print('Máximo:',maxRand)
print('Medio:',medRand)
print('Mínimo:',minRand)
print('Amplitud:',infRand)
print('Energía:',energiaRand)
print('Acción:',accionRand)
print('Potencia media:',potMedRand)
print('Raíz del valor cuadrático:',raizRand)

#RAMPA
print(' ')
print('RAMPA')
print('Máximo:',maxRampa)
print('Medio:',medRampa)
print('Mínimo:',minRampa)
print('Amplitud:',infRampa)
print('Energía:',energiaRampa)
print('Acción:',accionRampa)
print('Potencia media:',potMedRampa)
print('Raíz del valor cuadrático:',raizRampa)


fig,axs = plt.subplots(2,2)
#SENOIDAL
axs[0,0].stem(ts,fSenoidal)
axs[0,0].grid()
axs[0,0].title.set_text('Senoidal')
axs[0,0].set_xlabel('Tiempo (s)')
axs[0,0].set_ylabel('Amplitud')

#CUADRADA
axs[1,0].stem(tc,fCuadrada)
axs[1,0].grid()
axs[1,0].title.set_text('Cuadrada')
axs[1,0].set_xlabel('Tiempo (s)')
axs[1,0].set_ylabel('Amplitud')

#RAND
axs[0,1].stem(n,fRand)
axs[0,1].grid()
axs[0,1].title.set_text('Rand')
axs[0,1].set_xlabel('Tiempo (s)')
axs[0,1].set_ylabel('Amplitud')

#RAMPA
axs[1,1].stem(n,fRampa)
axs[1,1].grid()
axs[1,1].title.set_text('RAMPA')
axs[1,1].set_xlabel('Tiempo (s)')
axs[1,1].set_ylabel('Amplitud')

plt.tight_layout()
plt.show()  