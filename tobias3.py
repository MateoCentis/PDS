import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator





def senoidal(tIni,tFin,fm,A,phi,fs):
    tm = 1/fm
    t = np.arange(tIni,tFin,tm)
    x = A*np.sin(2*np.pi*fs*t+phi)
    return t,x

def rampa(tIni,tFin,fm):
    tm = 1/fm
    t = np.arange(tIni,tFin,tm)
    x = np.zeros(len(t))
    for i in range(len(t)):
        if t[i]<0:
            x[i] = 0
        else:
            x[i] = i
    return t,x
            

def aleatoria(tIni,tFin,fm):
    tm = 1/fm
    t = np.arange(tIni,tFin,tm)
    x = np.random.normal(1,10,len(t))
    return t,x

def cuadrada(tIni,tFin,fm,fs,phi):
    tm = 1/fm
    t = np.arange(tIni,tFin,tm)
    x = np.ones(len(t))
    for i in range(len(t)):
        aux = np.mod(2*np.pi*fs*t[i]+phi,2*np.pi)
        if aux >= np.pi:
            x[i] = - 1
    return t, x

# ejer 1

def valorMedio(x):
    sum = 0
    for n in range(len(x)):
        sum += x[n]
    return sum/len(x)
        
def maximo(x):
    return max(x)

def minimo(x):
    return min(x)

def amplitud(x):
    # duda: esta bien esto
    # norma infinito
    return max(np.abs(x))

def energia(x):
    #norma 2
    sum = 0
    for n in range(len(x)):
        sum += x[n]**2
    return sum

def accion(x):
    #norma 1
    sum = 0
    for n in range(len(x)):
        sum += np.abs(x[n])
    return sum

def potenciaMedia(x):

    sum = 0
    for n in range(len(x)):
        sum += x[n]**2
    return sum/len(x)

def raizValorCuadraticoMedio(x):
    sum = 0
    for n in range(len(x)):
        sum += x[n]**2
    sum = sum/len(x)
    return np.sqrt(sum)


tIni = 0
tFin = 5
fs = 5
fm = 200
phi = 0
A = 1

ts, xs = senoidal(tIni,tFin,fm,A,phi,fs)
tr, xr = rampa(tIni,tFin,fm)
tc, xc = cuadrada(tIni,tFin,fm,fs,phi)
ta, xa = aleatoria(tIni,tFin,fm)

print1 = 0
if (print1):
    print("senoidal")
    print("valor medio", valorMedio(xs))
    print("maximo", maximo(xs))
    print("minimo", minimo(xs))
    print("energia", energia(xs))
    print("accion", accion(xs))
    print("potencia media", potenciaMedia(xs))
    print("raiz del valor cuadratico medio", raizValorCuadraticoMedio(xs))


    print("rampa")
    print("valor medio", valorMedio(xr))
    print("maximo", maximo(xr))
    print("minimo", minimo(xr))
    print("energia", energia(xr))
    print("accion", accion(xr))
    print("potencia media", potenciaMedia(xr))
    print("raiz del valor cuadratico medio", raizValorCuadraticoMedio(xr))

    print("cuadrada")
    print("valor medio", valorMedio(xc))
    print("maximo", maximo(xc))
    print("minimo", minimo(xc))
    print("energia", energia(xc))
    print("accion", accion(xc))
    print("potencia media", potenciaMedia(xc))
    print("raiz del valor cuadratico medio", raizValorCuadraticoMedio(xc))


    print("aleatoria")
    print("valor medio", valorMedio(xa))
    print("maximo", maximo(xa))
    print("minimo", minimo(xa))
    print("energia", energia(xa))
    print("accion", accion(xa))
    print("potencia media", potenciaMedia(xa))
    print("raiz del valor cuadratico medio", raizValorCuadraticoMedio(xa))


# ejer 2 
A1 = 2
phi1 = 90
fs1 = 5
# a
A2 = 9
phi2 = 90
fs2 = 5
# phi
A3 = 2
phi3 = 270
fs3 = 5
fs
A4 = 2
phi4 = 90
fs4 = 2

t1, x1 = senoidal(tIni,tFin,fm,A1,phi1,fs1)
t2, x2 = senoidal(tIni,tFin,fm,A2,phi2,fs2)
t3, x3 = senoidal(tIni,tFin,fm,A3,phi3,fs3)
t4, x4 = senoidal(tIni,tFin,fm,A4,phi4,fs4)

# diferente A. A mayor "A", mayor producto interno
# print(np.dot(x1,x2))
# diferente phi. Afecta el producto, por ejemplo si una sinoidal difiere en pi, el producto interno da negativo
# print(np.dot(x1,x3))
# difrente fs. Entonces las seniales son completamente diferentes
# print(np.dot(x1,x4))

# ejer 3-----------------------------------------------------------------------------------
def fun1minus1(tIni,tFin,fm):
    tm = 1/fm 
    t = np.arange(tIni,tFin,tm)
    x = np.ones(len(t))
    for i in range(len(t)):
        if (t[i]<0):
            x[i] = -1
    return t,x
    
def legendre(tIni,tFin,fm):
    tm = 1/fm 
    t = np.arange(tIni,tFin,tm)
    x = (45/16)*t-(35/16)*(t**3)
    return t,x

def errorCuadratico(y,yaprox):
    sum = 0
    for i in range(len(y)):
        sum += (y[i]-yaprox[i])**2
    return sum


tIni = -1
tFin = 1
fm = 10

t1, x1 = fun1minus1(tIni,tFin,fm)
tl, xl = legendre(tIni,tFin,fm)

# plt.plot(t1,x1)
# plt.plot(tl,xl)
# plt.show()

print("error cuadratico", errorCuadratico(x1,xl))

def legendre2(tIni,tFin,fm,a1,a3):
    tm = 1/fm 
    t = np.arange(tIni,tFin,tm)
    x = a1*(np.sqrt(3/2)*t)+a3*(np.sqrt(7/2)*((5/2)*(t**3)-(3/2)*t))
    return t,x

def legendre2withError(tIni,tFin,fm,a1,a3,xreal):
    tm = 1/fm 
    t = np.arange(tIni,tFin,tm)
    x = a1*(np.sqrt(3/2)*t)+a3*(np.sqrt(7/2)*((5/2)*(t**3)-(3/2)*t))

    return errorCuadratico(xreal,x)

a1 = np.sqrt(3/2)
a3 = -np.sqrt(7/32)
var1 = np.zeros(len(np.arange(-1,1.2,0.2)))
var3 = np.zeros(len(np.arange(-1,1.2,0.2)))
vlegendre = np.zeros(len(np.arange(-1,1.2,0.2)))

i = 0
for dif in np.arange(-1,1.2,0.2):
    var1[i] = a1+dif
    var3[i] = a3+dif
    # tl2, xl2 = legendre2(tIni,tFin,fm,a1+dif,a3+dif)
    i = i + 1

[m1,m3] = np.meshgrid(var1,var3)

z = np.zeros([m1.shape[0],m1.shape[1]])

for i in range(m1.shape[0]):
    for j in range(m1.shape[1]):
        z[i,j] = legendre2withError(tIni,tFin,fm,m1[i,j],m3[i,j],x1)
       
   
# plt.plot3D(var1,var3,vlegendre)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Plot the surface.
surf = ax.plot_surface(m1, m3, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)

# Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()


# ejer 4
tIni = 0
tFin = 10
fm = 200
A = 1
phi = 0

s = [0]
for i in range(1,11):
    _, aux = senoidal(tIni,tFin,fm,A,phi,i)
    s.append(aux)


snew = 2*s[1] + 3*s[2] + 4*s[3] + 5*s[4] + 5*s[5] + 11*s[6] + 13*s[7] + 2 *s[8] + 3*s[9] + 1*s[10]

barrasx = [1,2,3,4,5,6,7,8,9,10]
barras1 = []
print(len(s))
print(len(snew))
for i in range(1,11):
    barras1.append(np.dot(snew,s[i]))


# plt.bar(barrasx,barras1) 
# plt.show()


f = [0]
for i in range(1,11):
    _, aux = senoidal(tIni,tFin,fm,A,i*15,10)
    f.append(aux)


fnew = 2*f[1] + 3*f[2] + 4*f[3] + 5*f[4] + 5*f[5] + 11*f[6] + 13*f[7] + 2 *f[8] + 3*f[9] + 1*f[10]

barras2 = []
for i in range(1,11):
    barras2.append(np.dot(fnew,f[i]))

plt.bar(barrasx,barras2) 
plt.show()

# duda, no se como hacer el punto 3. Como es el tema de la senial cuadrada

# ejer 5

f = open("te.txt", "r")
sejer5 = []
for x in f:
    sejer5.append(x)

