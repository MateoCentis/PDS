import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as spy
from animacionConvolucion import animacionConvolucion

def convolucionCircular(x,h):
    sizeX = len(x)
    sizeH = len(h)
    #Si un vector es mayor que otro entonces debo rellenar con ceros
    if (sizeX > sizeH):
        # for i in np.arange(sizeH,sizeX,1):
        h = np.append(h,np.zeros(sizeX-sizeH))
        N = sizeX
    elif(sizeH > sizeX):
        # for i in np.arange(sizeX,sizeH,1):
            # np.append(x,0)
        x = np.append(x,np.zeros(sizeH-sizeX))
        N = sizeH
    else:#son iguales
        N = len(x)
    y = np.zeros(N) #Relleno con zeros

    for k in range(N):
        suma = 0
        for l in range(N):
            modulo = np.mod((N+k-l),N)
            suma += h[l]*x[modulo]
        y[k] = suma
    return y


#prueba
x = np.array([1,2,2])
h = np.array([2,1,0.5])

res = convolucionCircular(x, h)
n = np.arange(0,len(res),1)
#animacion
# animacionConvolucion(n, res,[-1,3],[0,10],'Convolucion circular')
# plt.stem(n,res)
# plt.show()

#Codigo de internet para probar
def shifter(matrix):
    last = matrix[len(matrix)-1]
    x = len(matrix)
    result = [0] * x
    for i in range(1,len(matrix)):
        result[i] = matrix[i-1]
    result[0] = last
    return result
#  finding circular convolution
def findCircularConvolution(x,h,n,m):
    primary_matrix = np.zeros((max(n,m),max(n,m)))
    for i in range(0,len(primary_matrix[0])):
        primary_matrix[0][i] = x[i]
    for i in range(1,max(n,m)):
        primary_matrix[i] = shifter(primary_matrix[i-1])
        ultimate_matrix = np.transpose(primary_matrix)
    difference_in_length = abs(n-m)
    # for i in range(m,m+difference_in_length):
    #      h.append(0)
    h = np.append(h,np.zeros(difference_in_length))
    resultant = np.dot(ultimate_matrix,h)
    return resultant

circular_convolution_result = findCircularConvolution(x,h,len(x),len(h))
print(res)
print(circular_convolution_result)

