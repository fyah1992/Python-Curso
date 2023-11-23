def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100,100):
            return True
        else:
            pass

resultado = chequear_3_cifras([52,69,6000])
print(resultado)