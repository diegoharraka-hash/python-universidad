class Cuentabancaria:
    def __init__(self , saldo : float):
        self.saldo = saldo 

    @property
    def saldo (self ):
        return self._saldo # _ es para que no se llame igual que el atributo y pueda pasar por el property 

    @saldo.setter
    def saldo (self , valor ):
        if (valor < 0 ):
            raise ValueError ("el saldo no puede ser negativo")

        self._saldo = valor 

        return valor 
    
  




mibanco = Cuentabancaria(1900.2)
print (mibanco.saldo)

mibanco2 = Cuentabancaria(-33)
print (mibanco2.saldo)