def crear_tarea(titulo : str , descripcion : str  , prioridad : int  ):
    return {"titulo" : titulo , "descripcion" : descripcion , "prioridad" : prioridad}

def mostrar_tarea():
    print (f"el titulo es {"titulo" ['titulo']} | descripcion {"descripcion"['descripcion']} | prioridad {"prioridad"['prioridad']}")


import copy
tarea1 = crear_tarea ("infrografia" , "es una mierda" , 3)
copia = tarea1.copy()
copia is tarea1


