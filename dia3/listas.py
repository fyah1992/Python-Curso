lista = ['a','b','c']
lista2 = ['d','e','f']
lista3 = lista + lista2
desordenada = ["b","a","x","p"]
lista3.append("g")  #añadir elementos
borrado = lista3.pop(0)  #vacion interpreta que quieres borrar el último
desordenada.sort() #odena
desordenada.reverse() #ordena a la inversa 



print(lista3)
print(borrado)
print(desordenada)