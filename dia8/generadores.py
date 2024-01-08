#tipo de función que va produciendo los resultados de a poco, para gastar menos memoria 

#una función normal crea los resultados golpe, una función generadora los va creando segun la necesidad
#asi ocupa menor espacio de memoria 


def mi_funcion():
    lista =  []
    for x in range(1,5):
        lista.append(x * 10)
    return lista

def mi_generador():
    for x in range(1,5):
        yield x * 10  #Lo va generando


print(mi_funcion())

#forma de ver el  generador, sabe donde lo ha dejado, 
g = mi_generador()
print(next(g))
print(next(g))