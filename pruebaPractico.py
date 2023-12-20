import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definimos las dimensiones del reticulado
n = 50
m = 50

# Creamos la matriz para el reticulado
reticulado = np.zeros((n, m))

# Función para actualizar la animación
def update(frame_number, reticulado, plot):
    # Generamos un nuevo estado del reticulado
    reticulado = np.random.randint(2, size=(n, m))

    # Actualizamos los datos del plot
    plot.set_data(reticulado)
    return plot,

# Creamos la figura y el plot
fig, ax = plt.subplots()
plot = ax.imshow(reticulado, cmap='Greys')

# Creamos la animación
ani = animation.FuncAnimation(fig, update, fargs=(reticulado, plot), frames=100, interval=50, save_count=None)

# Mostramos la animación
plt.show()
