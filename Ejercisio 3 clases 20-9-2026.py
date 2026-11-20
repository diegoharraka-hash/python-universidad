class Libro:
    def __init__(self , titulo : str , autor :str , disponible : bool = True ):
        self.titulo = titulo
        self.autor = autor 
        self.disponible = disponible


class Biblioteca:
    def __init__(self , nombre : str):
        self.nombre = nombre 
        self.lista = [] 

    def anadir (self , Libro):
      self.lista.append(Libro)

    def prestar (self , titulo):
        for libro in self.lista:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False 
                print ("libro disponible")
                return 
        print ("libro no disponible")

    def mostrar_disponible(self):
        for libro in self.lista :
            if libro.disponible:
                print (libro.titulo)



milibro = Libro("maria y jose" , "Diego" , True )
mibiblioteca = Biblioteca("juan")
mibiblioteca.anadir(milibro)
mibiblioteca.prestar("la vaca lola")
mibiblioteca.mostrar_disponible()   

nuevolibro = Libro ("la vaca lola" , "Juan" )
nuvabiblioteca = Biblioteca("pepe")
nuvabiblioteca.anadir(nuevolibro)
nuvabiblioteca.prestar("lol")
nuvabiblioteca.mostrar_disponible()

    


            


          




        



        

