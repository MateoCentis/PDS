import numpy as np
import matplotlib.pyplot as plt
from senoidal import senoidal
import math
PI = math.pi
ta = -5
tb = 5
fm = 50
fs = 2
phi = 0
A = 1
t1,sen1 = senoidal(ta, tb, fm, fs, A, phi)
#ver que A, phi, f
A2 = 1 #al duplicar la amplitud te da algo el doble de grande, lo que tiene sentido por la linealidad
        #del producto interno, sin embargo: las señales son menos parecidas
phi2 = 0 #Al variar el phi una cantidad n*pi el producto interno nos da el inverso
            #y si vario n*pi/2 nos da un valor muy cercano a 0 ya que las senoidales son iguales pero
            #estan desfasadas y son ortogonales
fs2 = 4 #Al aumentar la frecuencia de la senoidal los valores del producto interno tienden a 0,
        #por lo tanto, son ortogonales entre si
        #senoidales de distintas frecuencias nunca son parecidas
t2,sen2 = senoidal(ta, tb, fm, fs2, A2, phi2)  

prodInterno = np.dot(sen1,sen2)
print(prodInterno)
#comun 
fig,axs = plt.subplots(2,1)#subplot(nFila nColumna nIndice)
plt.suptitle('Senoidales')
axs[0].stem(t1,sen1)

axs[1].stem(t2,sen2)
plt.show()
