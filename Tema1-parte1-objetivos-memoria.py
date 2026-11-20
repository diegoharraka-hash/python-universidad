titulo = input ("intoduzca un titulo : ")
descripcion = input ("intoduzca una descripcion : ")
prioridad = int (input ("intoduzca un numero:"))

if prioridad > 5 or prioridad < 0:
    print ("error su prioridad no puede ser ni mayor a 5 ni menor que 0")

# parte 1 
print (f"el titulo es : {titulo} , la descripcion es : {descripcion} , y la prioridad es : {prioridad}")

# parte 2 

estado = input ("introduzca el estado de su tarea : pendiente | en progreso | finalizada ")


match (estado):
    case "pendiente":
        print   ("el estado de su tarea es pendiente")
    case "en progreso":
        print ("el estado de su tarea es en progreso")

    case "finalizada":
            print ("el estado de su tarea es finalizada")

    case _:
      print ("Error")


dias_restantes = int (input("introduzca cuantos dias restantes le falta a su tarea:"))

if dias_restantes < 3 :
    print ("urgente")

elif dias_restantes >= 3:
    print ("proxima")
else :
    print ("sin prisa")

estados_validos = ["pendiente" , "en progerso" , "finalizada"]


contador = 0.0 
tareas = int (input ("introduzca el numero de tareas a realizar: "))
for i in range (tareas):
   estado = input ("introduzca el estado de su tarea : ")

   if estado == "finalizada":
       contador += 1 
    



porcentaje = contador / tareas * 100

print  (f"El numero de tareas completadas es de {porcentaje}")




  






















    

    
    





















   