import numpy as np
import matplotlib.pyplot as plt
import math

def cuadrada(ta , tb, fm, fs, phi):
  Tm = 1/fm
  t = np.arange(ta, tb, Tm)  
  cond = np.mod(2*math.pi*fs*t+phi, 2*math.pi)
  idx_noceros = np.where(cond>= math.pi)
  y = np.ones(len(t))
  y[idx_noceros] = -1
  return t, y