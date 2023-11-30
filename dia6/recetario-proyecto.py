from pathlib import Path
import os

base = Path.home()
ruta_completa = Path(base,"Escritorio","recetas")

def bienvenida_usuario():
    nombre = input("Bienvenido al recetario,¿Podrías indicar tu nombre? ")
    print(f"Bienvenido {nombre} al directorio de recetas que se encuentra en {ruta_completa}")

def cantidad_recetas():
    total = 0
    for texto in ruta_completa.glob("**/*.txt"):
        total += 1
    print(f"En total hay {total} recetas")


def elegir_opcion():
    print("[1] LEER RECETA")
    print("[2] CREAR RECETA")
    print("[3] CREAR CATEGORÍA")
    print("[4] ELIMINAR RECETA")
    print("[5] ELIMINAR CATEGORIA")
    print("[6] FINALIZAR PROGRAMA")
    eleccion = input("Elige una opción de las anteriores:")
    return eleccion


def elegir_categoria():
    x = 0
    for directorio in ruta_completa.iterdir():
        print(directorio.name)
    categoria_elegida = input("Introduce la categoria a mostrar ")
    return Path(ruta_completa,categoria_elegida)

def mostrar_recetas():
    ruta = elegir_categoria()
    for receta in ruta.glob("**/*.txt"):
        print(receta.name)
    eleccion_usuario = input("Qué receta quieres leer: ")
    abrir = open(Path(ruta,eleccion_usuario),"r")
    print(abrir.read())
    abrir.close()



def crear_receta():
    ruta = elegir_categoria()
    nombre_fichero_nuevo = input("Cómo quieres llamar el fichero: ")
    contenido_fichero = input("Introduce el contenido de la receta \n")
    abrir = open(Path(ruta,nombre_fichero_nuevo),"w")
    abrir.write(contenido_fichero)
    abrir.close()
    print(f"Tu receta {nombre_fichero_nuevo} ha sido creada con existo")

def crear_categoria():
    nombre_categoria = input("Introduce el nombre de la categoría")
    direccion_carpeta = Path(ruta_completa,nombre_categoria)
    os.mkdir(direccion_carpeta)
    if os.path.exists(direccion_carpeta):
        print(f"La carpeta {nombre_categoria} ha sido creada")

def eliminar_archivo():
    ruta = elegir_categoria()
    for receta in ruta.glob("**/*.txt"):
        print(receta.name)
    receta_elegida = input("¿Qué receta quieres eliminar?")
    os.remove(Path(ruta,receta_elegida))
    print(f"El fichero {receta_elegida} ha sido eliminado")

def eliminar_categoria():
    for directorio in ruta_completa.iterdir():
        print(directorio.name)
    nombre_categoria = input("Introduce el nombre de la categoría")
    direccion_carpeta = Path(ruta_completa, nombre_categoria)
    os.system(f"rm -r {direccion_carpeta}")
    print(f"La categoria {nombre_categoria} ha sido eliminada")


salir = "0"
bienvenida_usuario()
while salir != "6":
    cantidad_recetas()
    salir = elegir_opcion()
    if salir == "1":
        os.system("clear")
        mostrar_recetas()
    elif salir == "2":
        os.system("clear")
        crear_receta()
    elif salir == "3":
        os.system("clear")
        crear_categoria()
    elif salir == "4":
        os.system("clear")
        eliminar_archivo()
    elif salir == "5":
        os.system("clear")
        eliminar_categoria()


