import numpy as np
import math

PI = math.pi

def senoidal(ta, tb, fm, fs,A,phi): 
    Tm = 1/fm
    t = np.arange(ta, tb, Tm)
    x = np.sin(2*PI*fs*t + phi) *A 
    return t,x

