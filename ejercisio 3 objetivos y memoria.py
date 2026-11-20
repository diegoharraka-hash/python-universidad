def crear_tarea (titulo : str , descripcion : str , prioridad : int):
    return {"titulo" : titulo , "descripcion" : descripcion , "prioridad" : prioridad}


def mostar_tarea (tarea : dict ):
    print (f"el titulo es : {tarea['titulo']} | la descripcion es : {tarea ['descripcion']} | la prioridad es : {tarea ['prioridad']}")
    return tarea


import copy 
miTarea = crear_tarea ("Mates" , "la tengo que entregar  para el viernes" , 5) 
lista = []
lista.append(miTarea)
print (lista) #esta va a hacer mi lista 1


copia = copy.deepcopy (lista) 
print ("-----la copia profunda es : -------")
print (copia) # esta va a ser mi lista 2 mismo contenido pero diferentes listas copia.append ("fisica")
print (lista is copia)

copia[0]['prioridad'] = 999 # accedemos al primer elemento de la lista , el cual es un diccionario y accedemos por su clave 
print ("lista:" , lista)
print ("copia:" , copia)





