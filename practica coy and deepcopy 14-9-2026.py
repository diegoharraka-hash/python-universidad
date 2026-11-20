import copy
def crear_producto():
  producto ={}
  categorias = []
   
  producto["nombre"] =  input ("introduzca un nombre: ")
  producto["precio"] = input ("intoduzca un precio: ")
  categorias.append (input("categoria 1 : "))
  categorias.append (input("categoria 2 : "))
  producto["categorias"] = categorias

  return producto

def crear_inventario(n): # el in range es el cual le va a indicar cuantas iteraciones va a dar 
  inventario = []
  for i in range(n):
    p = crear_producto()
    inventario.append(p)


  return inventario


def mostar_inventario(inventario):
  for i, producto in  enumerate(inventario):
   print (i , producto)


def clonar_superficial(inventario): # aca unicamente estamos copiando la direccion de memoria de el inventario 
  copia = copy.copy(inventario)
  return copia


def clonacion_profunda(inventario): # aca si estamos copiando el contenido 
  copia_profunda = copy.deepcopy (inventario)

  return copia_profunda


nuevo_producto = crear_inventario(1)
mostar_inventario(nuevo_producto)
producto_clonado = nuevo_producto()
clonar_superficial(producto_clonado)
clonacion_profunda(producto_clonado)







  
  
  


 



  
