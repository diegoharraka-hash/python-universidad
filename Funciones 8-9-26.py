import copy 
def miTarea(): 
    Tarea = {} # diccionario vacio 
    Tarea["titulo"] = input ("Titulo: ")
    Tarea["descripcion"] = input ("Descripcion: ")
    Tarea["prioridad"] = input ("prioridad: ")

    return Tarea

def mostrar_Tarea(Tarea):
   print ("-----------Los datos son :-------------")
   print (f"titulo:  {Tarea['titulo']}")
   print (f"descripcion:  {Tarea['descripcion']}")
   print (f"prioridad {Tarea['prioridad']}")

  
 

def calcular_Prioridad(Tarea):
       print ("-------su Prioridad es:------")
       if Tarea['prioridad'] == '1' or Tarea['prioridad'] == '2':
           print ("baja")

       elif Tarea['prioridad'] == '3':
           print ("media")

       elif Tarea['prioridad'] == '4':
               print ("alta")

       elif Tarea['prioridad'] == '5':
                   print ("crutica")

def duplicar_tarea(Tarea):
      copia_profunda = copy.deepcopy(Tarea)
      return copia_profunda






      
nueva_tarea = miTarea()
mostrar_Tarea(nueva_tarea)
calcular_Prioridad(nueva_tarea)
tarea_duplicada = duplicar_tarea(nueva_tarea)
mostrar_Tarea(tarea_duplicada)


    

               
       










    



    




