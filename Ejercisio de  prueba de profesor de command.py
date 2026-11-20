class Ganadores: # una clase ganadores 
    def __init__(self , ganador : list ) -> None:
        if ganador == None: # creamos una lista que contenag el ganador
            ganador = []

        self.ganador = ganador # guardamos la lista 


from abc import ABC , abstractmethod # creamos la clase abstracta
class Comando (ABC):
    @abstractmethod
    def ejecutar (self)->None: # metodo ejecutar 
        pass
    @abstractmethod
    def deshacer (self)-> None: # metodo deshacer 
        pass


class Completar_ganador(Comando):
    def __init__(self , ganador : Ganadores):
        self._ganador = ganador

    def ejecutar(self) -> None:
        self._ganador.ganador.append ("Harry Kane") 

    def deshacer (self) -> None:
        self._ganador.ganador.remove ("Harry Kane")

historial :  list[Comando] = []

def ejecutar_comando (comando : Comando) -> None:
    comando.ejecutar()
    historial.append(comando)


def deshacer_ganador()-> None:
    if historial:
        historial.pop().deshacer()










        

    

