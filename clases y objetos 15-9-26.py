class Tarea : 
    def __init__(self , titulo : str , descripcion : str , prioridad : int ): # creamos un constructor 
        self.titulo = titulo # guardamos el atributo:titulo y asi sucesivamente 
        self.descripcion = descripcion
        self.prioridad = prioridad

    def mostrar(self ):
        print(self.titulo) #mostramos el contenido guardado
        print (self.descripcion)
        print (self.prioridad)

    def buscar_titulo(lista , nombre):
        for i in lista: # recorremos todos los elementos de una lista
            if i.titulo == nombre: # si alguno de los elementos coincide con string:nombre
                print ("nombre encontrado") #muestra mensaje 
                return True # devuelve un verdadero


        print ("nombre no encontrado") # si no encunetra ese string 
        return False # devuelve un falso 
    


def crear_tarea(): #creamos una funcion externa que nos va a servir para darle un valor a ese atributo 
    titulo = input ("intoduzca un titulo : ") # es decir por ejemplo el string titulo->lo que teclee el usario 
    descripcion = input ("intoduzca una descripcion : ")
    prioridad = input ("intoduzca una prioridad : ")

    tarea = Tarea(titulo , descripcion , prioridad ) #indicamos que esos valores se guarden en los atributos de nuestra clase 
    return tarea


def tareas_en_lista():
    cuaderno = [] # creamos una lista vacia 
    for i in range(3): # va a generar 3 vueltas 
        anadir = crear_tarea() # por cada vuelta genera una tarea asi : Tarea1 , Tarea2 , Tarea3
        cuaderno.append(anadir) # las anade en una lista que contiene tres objetos 
        

    return cuaderno

def mostar_lista(lista):
    for i in lista:
        Tarea.mostrar(i)
    


    



    
nueva_tarea = crear_tarea()
nueva_tarea.mostrar()
tareas_en_lista()
listaTareas = tareas_en_lista()
mostar_lista(listaTareas)











