class Tarea:
    def __init__(self, titulo : str , fecha : str):
        self.titulo = titulo 
        self.fecha = fecha 

    def resumen (self):
        return f"el titulo es : {self.titulo} , la fecha es : {self.fecha}"

class Tarea_recurrente(Tarea):

    def __init__(self, titulo, fecha , frecuencia: str ):
        super().__init__(titulo, fecha)
        self.frecuencia = frecuencia

    def resumen (self):
        super().resumen() # imprime lo de el padre 
        return f"la frecuenica es : {self.frecuencia}"


class Tarea_personal(Tarea):
        def __init__(self, titulo, fecha, lugar : str ):
            super().__init__(titulo, fecha)
            self.lugar = lugar 

        def resumen (self):
            super().resumen()
            return f"el lugar es: {self.lugar}"


class Tarea_trabajo(Tarea):
        def __init__(self, titulo, fecha , proyecto : str ):
            super().__init__(titulo, fecha)
            self.proyecto = proyecto


        def resumen(self):
          super().resumen()
          return f"el proyecto es : {self.proyecto}" 


miTarea = Tarea("mates" , "15 julio")
mostar1 =miTarea.resumen()
print (mostar1)

mirecurrente = Tarea_recurrente("castellano " , "17 de julio , "todos los viernes")
mostrar2 = mirecurrente.resumen()
print (mostrar2)






