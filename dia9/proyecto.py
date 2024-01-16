import os 
import re
from pathlib import Path
from datetime import datetime 

ruta = "D:\\Miguel\\informatica\\Cursos\\programaciónm\\Python-Curso-git\\Python-Curso\\dia9\\Mi_Gran_Directorio"
patron = r'N\D{3}-\d{5}'
numeros_encontrados =[]
archivos_encontrados = []

def buscar_patron():
    for principal, carpeta , archivo in os.walk(ruta):
        for arch in archivo:
            ruta_completa = Path(principal,arch)
            abrir = open(ruta_completa,'r')
            contenido = abrir.read()
            if re.search(patron,contenido):
                numero = re.search(patron,contenido)
                numeros_encontrados.append(numero.group())
                archivos_encontrados.append(arch)
            


def fecha_actual ():
    fecha_actual = datetime.now()
    fechar_personalizada = '%d/%m/%Y'
    fecha_formateada = fecha_actual.strftime(fechar_personalizada)
    print(f"\nFecha de búsqueda: [{fecha_formateada}]")

def imprimir_pantalla():
    print('''Archivo         NRO.Serie
-------         ----------  ''')

def recorer_listas():
    i=0
    for i in range(len(archivos_encontrados)):
        print(archivos_encontrados[i] + '\t' + numeros_encontrados[i])
        i += 1
    print(f'\nNúmeros encontrados: {i}')


buscar_patron()
fecha_actual()
imprimir_pantalla()
recorer_listas()