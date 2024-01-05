# Realizar operaciones cuenta bancaria 
# clase persona (nombre, apellidos)
# clase cliente (hereda de persona + numero_cuenta + balance) + 3 métodos
# 1 metodo imprimir en pantalla todos sus datos 
# 2 metodo depositar --> dinero a agregar a la cuenta
# 3 metodo retirar --> dinero para retirar
# codigo para elegir Depositar, Retirar o Salir 
# Llevar la cuenta de cuanto dinero hay en el balance, nunca puede ser negativo 
# Dos funciones --> crear cliente pidiéndole la información y crea un objeto 
#Función inicio la que genera todo el código 
import random

class Persona:
     def __init__(self,nombre,apellidos):
          self.nombre = nombre
          self.apellidos = apellidos
class Cliente(Persona):
     def __init__(self, nombre, apellidos,numero_cuenta,balance = 0):
          super().__init__(nombre, apellidos)
          self.numero_cuenta = numero_cuenta
          self.balance = balance
     def __str__(self):
          return f"Bienvenido {self.nombre} {self.apellidos} a su cuenta bancaria en la cual dispone de un total de {self.balance} euros"
     def depositar(self, cantidad):
            self.balance = self.balance + cantidad
            print(f"{self.balance}")

     def retirar(self,dinero):
            if ((self.balance - dinero) >= 0):
                self.balance = self.balance - dinero
                print (f"Te queda {self.balance}")
            else:
                 print ("No tienes suficiente saldo para realizar la operación")


def crear_cliente():
    nombre = input("Introduce tu nombre:")
    apellidos = input("Introduce tus apellidos")
    numero_cuenta = random.randint(1000,50000)
    cliente = Cliente(nombre,apellidos,numero_cuenta)
    return cliente

def inicio():
     mi_cliente = crear_cliente()
     print(mi_cliente)
     i = "0"
    
     while i != "3":
        print ("Elige la operación a realizar")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Salir")
        i = input("Introduce el número seleccionado")
        if i == "1":
            dinero = int(input("Introduce el dinero a depositar"))
            mi_cliente.depositar(dinero)
        elif i == "2":
             dinero = int(input("Introduce el dinero a sacar"))
             mi_cliente.retirar(dinero)
    
inicio()