from pathlib import Path
class Tarea:
    contador = 0 
    def __init__(self , titulo : str , descripcion : str , prioridad : int ):
        self.titulo = titulo 
        self.descripcion = descripcion
        self.prioridad = prioridad
        Tarea.contador += 1
        self.estado = "pendiente"

def crear_lista(self , tarea : list[Tarea]):
        self._tareas = tarea

        for c in tarea:
            if c.estado == "pendiente":
                 print (f"la tarea{c.titulo} esta pendiente")

            
                 
















        

