#import tkinter as tk 
#ventana = tk.Tk() # crea una ventana 
#ventana.title ("gestor de tares") # el nombre de la ventana sera ("")
#ventana.geometry ("400x300") # aca le damos las dimensiones  a la ventana 

#etiqueta = tk.Label (ventana , text="titulo de la tarea") # muestar el siguiente texto fijo , no se pude modificar
#entrada = tk.Entry (ventana)
#boton = tk.Button (ventana , text="Crear") # crea un boton llamado crear 

#etiqueta.pack() # esto es como el print lo necesitamos para mostrar el widget 
#entrada.pack()
#boton.pack()


import tkinter as tk

def crear_tarea():
    titulo = entrada_titulo.get()          # lee lo que se escribe en la caja 
    prioridad = entrada_prioridad.get()

    tarea = tk.Label(ventana, text=titulo + " - Prioridad: " + prioridad)
    tarea.pack()                           # lo coloca en la ventana 

    entrada_titulo.delete(0, tk.END)       # vacía las cajas , osea despues de que se escribe se vacian 
    entrada_prioridad.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("gestor de tareas")
ventana.geometry("400x300")

etiqueta_titulo = tk.Label(ventana, text="Título de la tarea")
entrada_titulo = tk.Entry(ventana)

etiqueta_prioridad = tk.Label(ventana, text="Prioridad")
entrada_prioridad = tk.Entry(ventana)

boton = tk.Button(ventana, text="Crear", command=crear_tarea)

etiqueta_titulo.pack()
entrada_titulo.pack()
etiqueta_prioridad.pack()
entrada_prioridad.pack()
boton.pack()

ventana.mainloop()
