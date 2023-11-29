archivo = open("prueba1.txt","a")
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
for linea in registro_ultima_sesion:
    archivo.writelines(linea +'\t')
archivo.close()

archivo = open("prueba1.txt","r")
print(archivo.read())
archivo.close()