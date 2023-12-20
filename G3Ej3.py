import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math
# from scipy.special import lpmv
import scipy as spy
#-----------------------------------------------------------FUNCIONES------------------------------------------------------------
#1)
def funcionY(t):
    res = np.zeros(len(t))
    for i in np.arange(0,len(res),1):
        if t[i] < 0:
            res[i] = -1
        else:
            res[i] = 1
    # y = -1*(t<0) + 1*(t>=0)
    return res


def ArmoMatrizECM(t,alpha1,alpha3):
    sizeT = len(t)
    size = len(alpha1)
    Z = np.zeros((size,size))
    yReal = funcionY(t)
    for i in np.arange(0,size,1):#recorro los alpha1
        for j in np.arange(0,size,1): #recorro los alpha3
            #ahora debo hacer para cada combinacion de alphas, todos los valores de t
            suma = 0
            for k in np.arange(0,sizeT,1):
                yLeg = alpha1[i,j]*np.sqrt(3/2)*t[k]+alpha3[i,j]*np.sqrt(7/2)*((5/2)*(t[k]**3)-(3/2)*t[k])
                suma += np.square(yReal[k] - yLeg)
            Z[i,j] = suma
    return Z

def yLegendre(t,alpha1,alpha3):
    y = alpha1*np.sqrt(3/2)*t+alpha3*np.sqrt(7/2)*((5/2)*(t**3)-(3/2)*t)
    return y

def yLegendreMas(t,alpha1,alpha3,alpha5):
    y = alpha1*(np.sqrt(3/2)*t)+alpha3*np.sqrt(7/2)*((5/2)*(t**3)-(3/2)*t) + \
        alpha5*(np.sqrt(22)/61440*(63*t**5 - 70*t**3 + 15 * t))
    return y

def errorCuadratico(yReal,yLeg):
    return np.linalg.norm(yReal-yLeg,2)**2
#2)
def variacionCoeficientes(valor, cantidad, rango):
    return np.linspace(valor - rango, valor + rango, cantidad)

#3)


#-----------------------------------------------------------GENERAL------------------------------------------------------------
t = np.arange(-1,1,0.01)
yReal = funcionY(t)
alpha1 = np.sqrt(3/2) #
alpha3 = -np.sqrt(7/32) #
yLeg = yLegendre(t,alpha1,alpha3)
print(alpha1)
print(alpha3)

mejorError = errorCuadratico(yReal, yLeg)
print("-Mejor error cuadrático total:",mejorError)

#2)
cantidad = 50
rango = 2
variacionesAlpha1 = variacionCoeficientes(alpha1, cantidad, rango)
variacionesAlpha3 = variacionCoeficientes(alpha3, cantidad, rango)

fig = plt.figure(figsize = (12,10))
ax = plt.axes(projection='3d')

X, Y = np.meshgrid(variacionesAlpha1, variacionesAlpha3)

Z = ArmoMatrizECM(t,X,Y)
surf = ax.plot_surface(X, Y, Z, cmap = plt.cm.cividis)

# Set axes label
ax.set_xlabel('alpha1', labelpad=20)
ax.set_ylabel('alpha3', labelpad=20)
ax.set_zlabel('Error Cuadratico total', labelpad=10)

fig.colorbar(surf, shrink=0.5, aspect=8)

plt.show()
#3)Calcular el error cuadratico total con mas coeficientes

# alpha5 = np.sqrt(22)/16
alpha5 = 0.125*np.sqrt(11/2)

yLeg = yLegendreMas(t, alpha1, alpha3, alpha5)

mejorError2 = errorCuadratico(yReal, yLeg)

print("-Mejor error cuadrático total con 1 coef más:",mejorError2)


#es mejor pero en el orden de 10^-4
