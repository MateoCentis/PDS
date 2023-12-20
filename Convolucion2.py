import numpy as np
import matplotlib.pyplot as plt

def convolution(x, h):
    """Calcula la convolución discreta entre dos señales.

    Args:
        x (list): Una señal de entrada.
        h (list): Una señal de respuesta al impulso.

    Returns:
        list: Una señal convolucionada.
    """
    # Obtener la longitud de las señales de entrada
    M = len(x)
    N = len(h)

    # Inicializar la señal de salida
    y = [0] * (M + N - 1)

    # Realizar la convolución
    for n in range(M + N - 1):
        y[n] = 0
        for k in range(M):
            if n - k < 0 or n - k >= N:
                continue
            y[n] += x[k] * h[n - k]

    return y

x = [1, 2, 3, 4, 5]
h = [1, 2, 3]

y = convolution(x, h)

n = np.arange(len(x)+len(h)-1)
plt.stem(n,y)
plt.show()
