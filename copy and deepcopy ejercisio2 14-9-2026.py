import copy

def crear_contacto():
    contacto = {}
    intereses = []

    contacto["nombre"] = input ("indique el nombre: ")
    contacto ["Telefono"] = input ("teclee el numero: ")
    intereses.append(input("intereses1 : "))
    intereses.append(input("intereses2 : "))

    contacto["intereses"] = intereses

    return contacto


def crear_agenda(n):
    agenda = []
    for i  in range (n):
        p = crear_contacto()
        agenda.append(p)


    return agenda


def mostar_agenda(agenda): #agenda es la que contiene el diccionario y la que vas a imprmir 
    for i , contacto in enumerate(agenda):
        print (i , contacto)



def copia(contacto):
    copia_contacto = copy.copy(contacto)

    return copia_contacto


def copia_profunda(contacto):
    c_profunda = copy.deepcopy(contacto)
    return c_profunda



contacto = crear_agenda(1)
mostar_agenda(contacto)
copia(contacto)
copia_profunda(contacto)



    


