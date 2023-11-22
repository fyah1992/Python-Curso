palabra = "python"
lista = [letra for letra in palabra]

print(lista)

lista_numeros = [n if n * 2 > 10 else "no" for n in range(1,50,2)]
print(lista_numeros)
