class Rectangulo:
    def __init__(self , ancho : float , alto : float ): # init es la creacion de el objeto , mientras 
        self.ancho = ancho 
        self.alto = alto 

    def area (self ):

        return  self.ancho * self.alto


    def perimetro (self):
        return 2 * (self.ancho + self.alto) # con los return, pasa que alguien siempre algo   tiene que recibir el valor por eso creamos una variable que reciba esos datos 

    def es_cuadrado(self):
         return self.ancho == self.alto 
         
    

        


r = Rectangulo(1.0,5.0)
area = r.area()
perimetro = r.perimetro()
cuadrado = r.es_cuadrado()

print (area)
print (perimetro)
print (cuadrado)
print ("-------valores segundo rectangulo------")
r2 = Rectangulo(2.0,6.0)
area2 = r2.area()
perimetro2 = r2.perimetro()
cuadrado2 = r2.es_cuadrado()


print (area2)
print (perimetro2)
print (cuadrado2)











    


    


