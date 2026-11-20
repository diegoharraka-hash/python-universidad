# class Tarea: 
#     def __init__(self , titulo : str , prioridad : int ):
#         self.titulo = titulo 
#         self.prioridad = prioridad



# def aplicar_tareas (tareas : list [Tarea] , operacion) -> list:
#     return [operacion (t) for t in tareas] # creamos una lista vacia , la lista guarda lo que devuelve en la operacion el titulo / priroidad



# mi_lista = []
# tarea1 = Tarea ("Mates" , 3)
# tarea2 = Tarea ("tecnicas" , 4)
# tarea3 = Tarea ("sistemas" , 5)
# mi_lista.append(tarea1)
# mi_lista.append (tarea2)
# mi_lista.append (tarea3)

# print (aplicar_tareas (mi_lista , lambda t : t.prioridad * 10))



# def filtar_tareas (tareas : list [Tarea] , condicion): 
#    resultados = []
#    for t in tareas :
#        if condicion (t):
#            resultados.append(t)
  
#    return resultados

# la_lista = mi_lista2 = []
# tarea4 = Tarea ("Procesadores" , 6)
# tarea5 = Tarea ("Fisica" , 7 )
# tarea6 = Tarea ("Lengua" , 8)
# mi_lista2.append (tarea4)
# mi_lista2.append (tarea5)
# mi_lista2.append (tarea6)








    

class Producto :
    def __init__(self , nombre : str , precio : float ):
        self.nombre = nombre 
        self.precio = precio


productos =  [

    Producto ("leche" , 1.9),
    Producto ("Queso" , 4.9),
    Producto ("Jamon" , 3.0) ,
    Producto ("huevo" , 1.3)

]

def barato (productos : list [Producto] , condicion):
    baratos = []
    for p in productos:
        if condicion (p) :
            baratos.append (p)
    return baratos 

def mayusculas (productos:list [Producto] , operacion) -> list:
   return [operacion (p) for p in productos]


baratos = barato (productos,lambda p : p.precio < 2 )
mayusucula = mayusculas (baratos , lambda p : p.nombre.upper())



print (baratos)
print (mayusucula)
