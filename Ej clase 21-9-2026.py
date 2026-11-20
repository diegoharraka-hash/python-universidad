class Tarea_profesor: # clase padre
    def __init__(self, titulo : str , prioridad : int , lugar : str  ):
        self.titulo = titulo 
        self.prioridad = prioridad
        self.lugar = lugar
    def mostar (self):
        return (f"titulo : {self.titulo} , prioridad:  {self.prioridad} , lugar: {self.lugar} ")



class Tarea_trabajo (Tarea_profesor): # clase hija 

    def __init__(self, titulo, prioridad , lugar, proyecto : str):
        super().__init__(titulo, prioridad , lugar) # permite acceder a los atributos de la clase padre 
        self.proyecto = proyecto

class Tarea_estudio(Tarea_profesor):
    def __init__(self, titulo, prioridad , lugar, asignatura : str):
        super().__init__(titulo, prioridad , lugar )
        self.asignatura = asignatura




nuevo_profesor = Tarea_profesor("mates" , 5 , "estanteria")
nuevo_profesor.mostar()


    