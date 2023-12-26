#Herencia  de padres a hijos 

#Crear clase genéricas para utilizar en otras clases, ejemplo clase animal aplicable a mamíferos, aves...

class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")
    

class Pajaro(Animal):
    pass


piolin = Pajaro(2, 'rojo')

piolin.nacer()
print(piolin.color)

#print(Pajaro.__bases__)  #Para saber de quien hereda
#print(Animal.__subclasses__)