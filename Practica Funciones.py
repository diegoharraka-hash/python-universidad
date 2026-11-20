

#nueva_lista = [1,2,3]
#nueva_lista = nueva_lista +[4] # si lo hacemos de esta forma estariamos creando una nueva lista 
#print (nueva_lista)

#lista_vieja = [1,2,3]
#lista_vieja.append(4) # en cambio con esta estariamos modificando una lista ya existente 
#print (lista_vieja)



def solicitar_numero(numero ):
    numero = int (input("introduzca un numero: ")) # convertimos a entero para trabajar puros enteros 
    if (numero == 1 or numero == 2):
        return "baja"
    elif(numero == 3):
        return "media"
    elif(numero==4):
        return "alta"
    elif(numero==5):
        return "critica"
    
def es_estado_valido(estado : str) ->bool:
    match estado:
        case "pendiente" | "progreso"| "finalizada":
            return True
        case _:
            return False




  






