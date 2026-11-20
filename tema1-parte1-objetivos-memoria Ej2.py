def crear_tarea(titulo : str , descripcion : str , priroidad : int ):
    return {"titulo" : titulo , "descripcion" : descripcion , "prioridad" : priroidad}

def mostrar_tarea(tarea):
    print   (f" el titulo es { tarea ['titulo']} , descripcion : {tarea ['descripcion']} y prioridad {tarea ['prioridad']}")

def calcular_prioridad(tarea):
    if tarea['prioridad'] == 1 or tarea ['prioridad'] == 3 :
        return "baja"

    elif tarea['prioridad'] == 4:
        return "media"

    elif tarea['prioridad'] == 5:
        return "alta"

    else:
        return "critica"


def menu_interactivo():
    lista = []
    pregunta = ''

    while (pregunta != "finalizar"):
        pregunta = input ( "Que dese crear-listar-finalizar?")
        if (pregunta == "crear"):

         t = input ("introduzca una tarea :") 
         d = input ("introduzca una descripcion")
         p = input ("introduzca una prioridad")

         tarea = crear_tarea (t , d , p)
         lista.append(tarea)

        if (pregunta == "listar"):
            for listas in lista:
                 mostrar_tarea(listas)











tarea1 = crear_tarea("matematicas" , "es buena asignatura" , 4  )
mostrar_tarea(tarea1)
menu_interactivo()
