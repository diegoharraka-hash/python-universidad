titulo = input("introduzca un titulo: ")
descripcion= input("introduzca una descripcion: ")
prioridad = int(input("intoduzca una prioridad: "))

if prioridad > 5 or prioridad <= 0 :
    print ("Error")
else :
    print (f"el titulo es : {titulo} , la descripcion : {descripcion} , prioridad :  {prioridad}")

estado = input("introduzca el estado: ")

match estado:
    case "pendiente" |"Pendiente":
        print ("su Tarea esta pendiente")

    case "en progreso" | "En progreso":
        print ("su Tarea esta en progreso")

    case "finalizada" | "Finalizada":
        print ("su Tarea esta finalizada")

    case _:
        print ("Ese estado no existe o no fue asignado")


dias_restantes = int(input("introduzca los dias restantes: "))
if dias_restantes <= 0 :
    print ("Lo siento la tarea ya no se puede entregar ")
elif dias_restantes < 3:
    print ("urgente ")

elif dias_restantes <= 7:
    print ("proxima")

else:
    print ("sin prisa")


contador = 0 
tareas = int (input("introduzca el numero de  tareas:  "))
for i in range(tareas) :
    estado2 = input ("introduzca el estado: ")
    match estado2:
     case "pendiente" |"Pendiente":
        print ("su Tarea esta pendiente")

     case "en progreso" | "En progreso":
        print ("su Tarea esta en progreso")

     case "finalizada" | "Finalizada":
        print ("su Tarea esta finalizada")
        contador +=1

     case _:
        print ("Ese estado no existe o no fue asignado")


porcentaje = contador  / tareas  * 100

print (f"tus tareas pendientes eran : {tareas} , has echo {contador} , es decir un {porcentaje}")
