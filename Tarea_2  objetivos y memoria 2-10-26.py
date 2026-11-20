def crear_tarea(titulo : str , descripcion : str , prioridad :int ):
    return {"titulo" : titulo , "descripcion" : descripcion , "prioridad" : prioridad}

def mostar_tarea(tarea : dict ):
    print (f" el titulo es : {tarea['titulo']} ,la descripcion es : {tarea['descripcion']} , y su prioridad es {tarea['prioridad']}")
    return tarea 

def estado_tarea(tarea : dict) -> str :
    if tarea ['prioridad'] == 1 or  tarea ['prioridad'] ==2:
        return "baja"
    elif tarea ['prioridad'] == 3:
        return "media"
    elif tarea ['prioridad'] ==  4:
        return "alta"
    elif tarea ['prioridad'] ==  5:
        return "critica"
    else :
        return "error"

def menu_interactivo ():
    lista = []
    pregunta = ""
    while (pregunta != "finalizar"):
        pregunta = input ("que desea hacer : crear -listar -finalizar : ")
        if (pregunta == "crear"):
            t = input ("introduzca un titulo: ")
            d = input ("introduzca una descripcion: ")
            p = int (input ("introduzca su prioridad : "))
            tarea2 = crear_tarea (t,d,p)
            lista.append (tarea2)

        if (pregunta == "listar"):
           for listas in lista :
               mostar_tarea(listas)





tarea1 = crear_tarea("mates", "lol" , 3)
mostar_tarea (tarea1)
print (estado_tarea (tarea1))
menu_interactivo ()




