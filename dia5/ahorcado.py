import string
from random import choice

lista_palabras = ["manzana","pera","naraja","mandarina"]
palabra = choice(lista_palabras)
cantidad = len(palabra)
lista_abecedario = list(string.ascii_lowercase)
print(f"Bienvenido al juego del ahorcado \nDebes adivinar una palabra con {cantidad} de letras")
lista_adivinar = list("_"*cantidad)
print(lista_adivinar)
total = 0

while total < 5:
    def pedir_letra():
        letra_usuario = input("Di una leta de la a-z --> ").lower()
        return letra_usuario

    def comprobar_letra(letra_usuario):
        while letra_usuario not in lista_abecedario:
            letra_usuario = pedir_letra()
        return letra_usuario

    def chequear_letra(palabra, letra_usuario):
        lista_pa = list(enumerate(palabra))
        for x,y in lista_pa:
            if y == letra_usuario:
                lista_adivinar[x] = letra_usuario
        print(lista_adivinar)
        return(lista_pa)
    def ganador(lista_pa):
        if lista_pa == list(enumerate(lista_adivinar)):
            print("HAS GANADO")
            return True


    letra_usuario2 = pedir_letra()
    letra_usaurio3 = comprobar_letra(letra_usuario2)
    comprobar = chequear_letra(palabra,letra_usaurio3)
    if ganador(comprobar):
        break
    total += 1


else:
    print("VUELVE A INTENTARLO !!")