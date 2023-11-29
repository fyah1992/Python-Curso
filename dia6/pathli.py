from pathlib import Path

carpeta = Path("/home/miguel/Escritorio/alternativ") # / archivo.txt alternativa
archivo = carpeta / "archivo.txt"  #forma de concatenar la ruta y el directorio

mi_archivo = open(archivo)
print(mi_archivo.read())
