from abc import ABC , abstractmethod
import math 
class Figura(ABC):
    @abstractmethod
    def area (self):
        pass 



class Rectangulo(Figura) :
    def __init__(self, ancho : float  , alto : float ):
        self.ancho = ancho 
        self.alto = alto 

    def area (self):
        return self.ancho * self.alto 


class Circulo (Figura):
    def __init__(self , radio : float ):
        self.radio = radio 


    def area (self):
        return math.pi * self.radio * self.radio 

r = Rectangulo (2.0 , 3.0)
c = Circulo(5.0)
print (r.area())
print (c.area())



