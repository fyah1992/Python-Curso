
def contador_primos(num):
    lista_numeros = list(range(0,num+1))
    lista_no_primos = []
    for n in lista_numeros:
        for n2 in range(2,n):
            if n % n2 == 0:
                lista_no_primos.append(n)
    lista_ordenada = list(set(lista_no_primos))






contador_primos(15)
