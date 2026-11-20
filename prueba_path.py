from pathlib import Path 

ruta_archivo = Path.home() / "Desktop" / "Python" / "clase 14-9-2026.py"

if ruta_archivo.exists():
    contenido = ruta_archivo.read_text(encoding="utf-8")
    print (contenido)

else :
    print (f"el archivo no se encontro : {ruta_archivo}")
