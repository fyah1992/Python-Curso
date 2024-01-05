# try --> intentar esto...
# except --> si sale mal, haz esto...
# finaly --> pase lo que pase haz esto 

def suma():
    n1 = int(input("numero 1:"))
    n2 = int(input("numero 2:"))
    print(n1+n2)
    print("Gracias por sumar")



try:
    suma()
except TypeError:
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Ese no es un número")
else:
    print("Hiciste todo bien")
finally:
    print("Eso fue todo")

def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un número"))
        except:
            print("Eso no es un número")
        else:
            print(f"Ingresaste el número {numero}")
            break
    print("Gracias")

pedir_numero()