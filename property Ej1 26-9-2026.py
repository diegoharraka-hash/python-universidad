class Triangulo :
    def __init__(self , ancho : float , alto : float ):
        self.ancho = ancho
        self.alto = alto

    @property # Alguien lee el valor  
    def area (self):
        calculo =   self.ancho * self.alto
        return calculo



miTriangulo = Triangulo(22.0 , 33.0)
print (miTriangulo.area)



miTriangulo2 = Triangulo(2.0,3.0)
print (miTriangulo2.area)



