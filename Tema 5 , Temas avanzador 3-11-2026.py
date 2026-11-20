import time
class Tarea :
    def __init__(self , titulo , tipo):
        self.titulo = titulo 
        self.tipo = tipo 

def crear_medidor (): # Creamos un medidor que permita
    # medir cuanto tiepo tarda en crear / instanciar una tarea 
    total = 0 # variable pertenecienze a crear_medidor no a medir 

    def medir ():
        nonlocal total  # queremos acceder a una variable externa que pertenece a una funcion externa 
        inicio = time.perf_counter() # guardamos tiempo inicial 
        tarea = Tarea ("Hacer la compra" , "personal") # # creamos una Tarea 
        fin = time.perf_counter() # guardamos tiempo final 
        duracion = fin - inicio # calculamos la duracion 

        print (f"la tarea se ha creado en {duracion} segundos") # mostramos la duracion
        return tarea # devolvemos el objeto tarea 
    return medir # devolvemos el objeto medir 


creartarea = crear_medidor()
creartarea()
