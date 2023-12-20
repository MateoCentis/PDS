import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scipy.signal as spy

def animacionConvolucion(n,res1,xAxis,yAxis,titulo):
    i=0
    def dibujarConovolucion(i):
        plt.xlim([xAxis[0],xAxis[1]])
        plt.ylim([yAxis[0],yAxis[1]])
        plt.stem(n[i],res1[i])
        i += 1

    fig = plt.figure(titulo)
    plt.title(titulo)
    sizeN = len(n)
    animate = FuncAnimation(fig,
                            func = dibujarConovolucion,
                            frames = sizeN,
                            interval = 200)
    plt.show()
    # return animate