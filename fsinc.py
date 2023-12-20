import numpy as np
import matplotlib.pyplot as plt
import math
pi = math.pi
def fSinc(t_a,t_b,fm,fs,A,phi):
  T=1/fm
  t = np.arange(t_a,t_b-T,T)
  x=2*pi*fs*t+phi
  y= (A*(np.sin(x)/x))*(x!=0)+ 1*(x==0)
  return t,y

# fm=100
# fs=3
# phi=pi
# A=1
# a= -5
# b = 5
# t,y = fSinc(a, b, fm, fs, A, phi)
# plt.plot(t,y)
# plt.show()