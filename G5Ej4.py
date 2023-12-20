import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as spy
import math 
pi = math.pi
#H(s) <--> H(z)
#z = e^(sT) con esta formula
#s=ln(z)/T
#Como nos queda en terminos no polinomiales hay que aplicar transformaciones conformes
#Usar bilineal y euler 

#1. Frecuencia de corte: A_max - 3 dB 20 log_10(A(f)/A_max)=-3
#para que frecuencia esta ultima ecuacion se cumple, esa frecuencia se va a llamar frecuencia de corte
#Encontrar frecuencia de corte en un sistema continuo (matlab: freqs)
#Esta frecuencia de muestreo * 4 nos va a dar el t que tenemos que meter en euler y bilineal
#2. Graficar el sistema continuo vs euler vs bilineal (grafica amplitud-frecuencia) 

#----------------------------------------Determinar frecuencia de corte-------------------------------------------------
#para encontrar frecuencia de corte del sistema primero definimos el sistema
w = np.arange(0,7000,1)
frecuencias = w/(2*pi)
s = 1j*w
H_s = (12500*s)/(44*s**2+60625*s+625*10**4)
#encuentro frecuencia de corte y luego la multiplico por 4 para usarla en transf conformes
indiceFc = np.where(np.isclose(abs(H_s), max(abs(H_s))/2, 1e-3))[0][0]
fc = frecuencias[indiceFc]
fm = 4*fc
#---------------------------------------------Transformaciones------------------------------------------------
T = 1/fm
omega = np.arange(0,pi,pi/len(w))
z = np.exp(1j*omega) #e^jw

sBilineal = (2/T)*(1-(1/z))/(1+(1/z))
H_bilineal = (12500*sBilineal)/(44*sBilineal**2+60625*sBilineal+625*10**4)

sEuler = (1-(1/z))/T
H_euler = (12500*sEuler)/(44*sEuler**2+60625*sEuler+625*10**4)

plt.plot(frecuencias,np.abs(H_s),label='Respuesta sistema continuo')
plt.plot(frecuencias,np.abs(H_euler),label='Respuesta Euler')
plt.plot(frecuencias,np.abs(H_bilineal),label='Respuesta Bilineal')

plt.scatter(frecuencias[indiceFc],np.abs(H_s[indiceFc]))
plt.annotate('$H(f_c)$', (fc,np.abs(H_s[indiceFc])))
plt.legend()
plt.grid()

plt.show()