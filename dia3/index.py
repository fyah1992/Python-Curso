mi_texto = "Esta es una prueba de commit"

#resultado = mi_texto[-4]  #Devuelve la letra en la posición indicada

#resultado = mi_texto.index('a',5,11)

resultado = mi_texto.rindex('a')  #Muestra la última aparición
print(resultado)

resultado = mi_texto.replace("es","era")
resultado2 = resultado.replace("Esta","Casa")
print(resultado2)