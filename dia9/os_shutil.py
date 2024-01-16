import os
import shutil
import send2trash

#shutil.move('curso.txt',"c:\\Users\\Miguel Ángel\\Desktop") #Para mover archivo

# send2trash.send2trash("curso.txt") #eliminar fichero a la basura

ruta = "d:\\Miguel\\Personal"

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta: {ruta}")
    print(f"Las subcarpetas son:")
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son: ')
    for arch in archivo:
        print (f'\t{arch}')
    print('n')