import tkinter as tk

# Define una función que muestra un mensaje personalizado para tu novia
def decir_te_quiero(nombre):
    mensaje = f"Querida {nombre}, quería tomarme un momento para decirte lo mucho que te quiero. Eres la persona más importante en mi vida y no puedo imaginar mi vida sin ti. Eres mi todo y te amo con todo mi corazón."
    mensaje_label.config(text=mensaje)

# Crea una ventana con un campo de entrada y un botón para enviar el mensaje
ventana = tk.Tk()
ventana.title("Mensaje para mi novia")
nombre_label = tk.Label(ventana, text="Por favor, introduce el nombre de tu novia:")
nombre_label.pack()
nombre_entry = tk.Entry(ventana)
nombre_entry.pack()
boton_enviar = tk.Button(ventana, text="Enviar", command=lambda: decir_te_quiero(nombre_entry.get()))
boton_enviar.pack()

# Crea un widget de etiqueta donde se mostrará el mensaje personalizado
mensaje_label = tk.Label(ventana, text="")
mensaje_label.pack()

# Inicia el bucle principal de la ventana
ventana.mainloop()
