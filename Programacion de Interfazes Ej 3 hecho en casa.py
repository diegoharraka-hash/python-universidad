import tkinter as tk  # importamos la libreria tk
ventana = tk.Tk() # accedemos a la clases y a las funciones y creamos una ventana 
ventana.title ("Saludar") # creamos  el titulo de la ventana 
ventana.geometry("300x200") # le ponemos las dimensiones a la ventana 

def saludar():
    nombre = entrada_nombre.get() # aca solicitamos el nombre 
    saludo = tk.Label (ventana , text= "hola , " + nombre) # guardamos el nombre 
    saludo.pack() # mostramos el nombre 


etiqueta_pregunta = tk.Label (ventana , text= "como te llamas?") # mostramos un texto no modificable 
etiqueta_entrada = tk.Entry (ventana , text= " escriba su nombre" ) # mostramos texto modificable 
entrada_nombre = tk.Entry(ventana) # creamos la variable entrada_nombre que vamos a usar en la funcion 
etiqueta_boton = tk.Button (ventana , text= "saludar" , command=saludar)  # creamos un boton que al pulsar muestre hola con el nombre 

etiqueta_pregunta.pack()
etiqueta_boton.pack()
entrada_nombre.pack()

ventana.mainloop()






