import numpy as np
import matplotlib.pyplot as plt

def y(n):
    res = np.sqrt((x[n-1]*x[n])*(-2)+x[n]**2+x[n-1]**2)  
    return res

#y[n]=sqrt((x[n-1]*x[n])*(-2)+x[n]^2+x[n-1]^2)
