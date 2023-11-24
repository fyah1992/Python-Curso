def devolver_distintos(lista):
    suma = sum(lista)
    if suma > 15:
        maximo = max(lista)
        print(f"El núnmero mayor es {maximo}")
    elif suma < 10:
        print(f"El número más pequeño es {min(lista)}")
    else:
        lista.sort()
        print(lista[1])


lista_numeros = [1, 10, 5]
print(devolver_distintos(lista_numeros))
