import numpy as np
import matplotlib.pyplot as plt
from senoidal import senoidal
def iLineal(t):#interpolador lineal
    if abs(t)<1:
        res = (1-abs(t))
    else:
        res = 0 
    return res

fm = 10
fs = 0.5
T = 1/fm
fmi = 4*fm
Ti = 1/fmi
ta=0
tb=2

t,x = senoidal(ta,tb,fm,fs,1,0)
tm = np.arange(ta,tb,Ti)
xm= np.zeros(len(tm))
#xm =[] y luego xm.append(x)
#m(sobremuestreada), n(normal)
#recorro todos los m para los cuales debo recorrer todos los n, ya que m es 4*n
for i in np.arange(ta,len(tm),1):
    suma=0
    for j in np.arange(ta,len(t),1):
        suma += x[j]*iLineal((tm[i]-t[j])/T)
    xm[i]=suma
figure1 = plt.figure()
plt.title('Señal original')
plt.stem(t,x)

figure2 = plt.figure()
plt.title('señal interpolada linealmente')
plt.stem(tm,xm)
plt.show()

