from random import *


aleatorio = randint(1,50)
print(aleatorio)

aleatorio2 = uniform(1,5)  #Numero aleatorio de tipo float
print(aleatorio2)

aleatorio3 = random()  #Numero random del 0 al 1
print(aleatorio3)

colores = ["azul","rojo","amarillo"]
color_aleatorio = choice(colores)
print(color_aleatorio)

numeros = list(range(5,50,5))
shuffle(numeros) #Modificación en el lugar, solo puede modificar numbers no string
print(numeros)