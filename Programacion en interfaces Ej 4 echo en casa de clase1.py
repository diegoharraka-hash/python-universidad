
# # Ejercisio 1 

# import tkinter as tk 
# ventana = tk.Tk()
# ventana.title ("Ficha")
# ventana.geometry ("300x250")
# def crear_persona():
#     nombre = etiqueta_nombre.get()
#     edad = etiqueta_edad.get()
#     saludo = tk.Label (ventana , text=nombre + " tiene " + edad + " anios ")
#     saludo.pack()

# etiqueta_nombre2 = tk.Label(ventana , text= "Nombre : ")
# etiqueta_nombre = tk.Entry(ventana)
# etiqueta_edad2 = tk.Label (ventana , text="Edad : ")
# etiqueta_edad = tk.Entry(ventana)
# etiqueta_boton = tk.Button (ventana , text= "mostrar" , command=crear_persona)

# etiqueta_nombre2.pack()
# etiqueta_nombre.pack()
# etiqueta_edad2.pack()
# etiqueta_edad.pack()
# etiqueta_boton.pack()



# ventana.mainloop()




# # Ejercisio 2 
# import tkinter as tk 
# ventana = tk.Tk()
# ventana.title("Ciudad")
# ventana.geometry ("300x200")

# def mostar_ciudad ():
#     ciudad = etiqueta_ciudad.get()
#     mostar = tk.Label (ventana , text= "Vives en:  " + ciudad)
#     etiqueta_ciudad.delete (0 , tk.END)
#     mostar.pack()
    



# etiqueta_pregunta = tk.Label (ventana , text= "Donde vives? ")
# etiqueta_ciudad = tk.Entry (ventana) 
# etiqueta_boton = tk.Button (ventana , text= "Mostar" , command=mostar_ciudad)

# etiqueta_pregunta.pack()
# etiqueta_ciudad.pack()
# etiqueta_boton.pack()

# ventana.mainloop()
    

