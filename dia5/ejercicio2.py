def palabras_repetidas(palabra):
    lista = []
    for letra in palabra.lower():
        if letra not in lista:
            lista.append(letra)
    lista.sort()
    print(lista)


palabras_repetidas("Paaaytoohon")