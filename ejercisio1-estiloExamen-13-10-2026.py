
# #ejercisio 1  , CTRL + K, luego CTRL + C: Para comentar , CTRL + K, luego CTRL + U: Para descomentar. 

# class TareaPersonal:
#     def __init__(self , lugar : str , titulo : str ):
#         self.lugar = lugar
#         self.titulo = titulo


# class TareaTrabajo:
#     def __init__(self , titulo : str , proyecto : str):
#         self.titulo = titulo
#         self.proyecto = proyecto

# class TareaEstudio:
#     def __init__(self , titulo : str , asignatura : str ):
#         self.titulo = titulo
#         self.asignatura = asignatura




# def crear_tarea(tipo , titulo , detalle): # esto lo que nos permite centralizar los objetos en una unica funcion , sin tener que llamar a cada clase 
#     if tipo == "personal":
    
#         return TareaPersonal (titulo , lugar = detalle )

#     elif tipo == "trabajo":
#         return TareaTrabajo(titulo , proyecto = detalle )

#     elif tipo == "estudio":
#         return TareaEstudio(titulo , asignatura = detalle )

    


# t1 = crear_tarea( "madrid" , " la bola negra ")
# t2 = crear_tarea( "la psicologia de el dinero" , "pagina web de aviones")
# t3 = crear_tarea( "la manana sonada " , "mates")



#Ejercisio 2
class Producto:
    def __init__(self , stock : int ):
        self.stock = 0 
        self.stock = stock


p1 = Producto(0)

lista = [p1]
agotados = lista 
it = iter (agotados)

for agotado in it:
    if agotado.stock == 0 :
         

    









        


