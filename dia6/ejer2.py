def abrir_leer(archivo):
    abrir = open(archivo,"r")
    return (abrir.read())

#documento = "prueba.txt"
print(abrir_leer("prueba.txt"))