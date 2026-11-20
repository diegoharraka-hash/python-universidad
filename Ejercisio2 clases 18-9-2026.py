class Banco:
    def __init__(self , titular : str , saldo : int = 0  ):
        self.titular = titular 
        self.saldo = saldo

    def ingresar(self , cantidad):
        self.saldo = cantidad + self.saldo # aca lo que estamos es cambiando el valor interno de la variable 
        # en cambio si creamos una nueva varible el sueldo como tal nunca cambia 
        

    def retirar (self , cantidad : int ):
     if cantidad > self.saldo:
        print("fondo insuficiente")


     else :
        self.saldo =  self.saldo - cantidad

    def mostar(self):
       print ( "titular:" + self.titular)
       print ("el saldo es :" , self.saldo )


       

      


c1 = Banco("Diego" , 500)
print ("datos: ")
c1.mostar()

c1.ingresar(200)
print (c1.saldo)
c1.retirar(300)
print (c1.saldo)

print ("------cuenta2-------")

c2 = Banco("juan" , 100)
c2.ingresar(100)
print (c2.saldo)

c2.retirar(300)
print (c2.saldo)








        




      


