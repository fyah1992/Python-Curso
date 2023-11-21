
texto = input("Introduce el texto a analizar: ").lower()

letras = input("Introduce tres letras: ").lower()



lista_letra = list(letras)

for letra in lista_letra:
     cuenta = texto.count(letra)
     print(f"La letra {letra} aparece {cuenta} veces")

largo_texto = len(texto)
print(largo_texto)
print(f"La primera letra del texto es {texto[0]}")
print(f"La última letra del texto es {texto[largo_texto-1]}")
print("**************************TEXTO EN ORDEN INVERSO*********************************************")
print(texto[::-1])
print("python" in texto)

