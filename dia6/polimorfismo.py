# Muchas formas, objetos con diferentes formas
#Objetos de diferentes clases pueden compartir métodos 

class Vaca:
    def __init__(self, nombre) :
        self.nombre = nombre

    def hablar (self):
        print (self.nombre + "dice muuu")

class Oveja:
    def __init__(self, nombre) :
        self.nombre = nombre

    def hablar (self):
        print (self.nombre + "dice beee")


vaca1 = Vaca("Martín")
oveja1 = Oveja('Nube')


#En una iteración permite llamar a objetos de nombre  distinto que comparten método 

'''animales = [vaca1, oveja1]    
for animal in animales:
    animal.hablar() '''

def animal_hablar(animal):
    animal.hablar()

animal_hablar(oveja1)