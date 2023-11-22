from random import randint
import os
numero_aleatorio = randint(1,50)
n=0
nombre_usuario = input("¿Cómo te llamas? ")

instrucciones = (f"Bienvenido {nombre_usuario} a continuación le explicos las normas:  \n"
                 f"1. Indica un número ente el 1 y el 50 \n"
                 f"2. Tendrás 8 intentos")
print(instrucciones)

while n < 8:
    numero_usuario = int(input("Qué número estoy pensando"))
    if numero_usuario < 1 or numero_usuario > 50:
        print("Debe introducir un número comprendido entre el 1 y el 50")
        n += 1
    elif numero_usuario > numero_aleatorio :
        print("El número introducidco es mayor que el número a descubrir")
        n += 1
    elif numero_usuario < numero_aleatorio :
        print("El número introducido es menor que el número a introducir")
        n += 1

    elif numero_usuario == numero_aleatorio:
        print("HAS ACERTADO !!!")
        break

print(f"El número ha descubir era el {numero_aleatorio}")