def crear_libro (titulo : str , autor : str , paginas : int ):
    leido = False 
 
    return {"titulo" : titulo , "autor" : autor , "paginas" : paginas , "leido" : leido }  

def mostar_libro (libro : dict):
    print (f"titulo : {libro ['titulo']} | autor: {libro ['autor']} | paginas : {calcular_tamanio('paginas')} | leido : {libro ['leido']}" )
    return libro 

def calcular_tamanio (libro:dict) -> str :
    if libro ['paginas'] < 100 :
        return "corto"
    elif libro ['paginas'] == 100 or libro ['paginas']  < 400:
        return "medio"
    elif libro ['paginas'] > 400 :
        return "largo"
    else :
        return "error"
    



libro1 = crear_libro("Quijote" , "Cervantes" , 120 )
mostar_libro (libro1)

