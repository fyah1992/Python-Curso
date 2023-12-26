class Padre():
    def hablar(self):
        print ('Hola')


class Madre():
    def reir (self):
        print ('Ja Ja')
    
    def hablar(self):
        print('Qué tal?')

class Hijo (Padre, Madre):
    pass

class Nieto(Hijo):
    pass


mi_nieto = Nieto()

mi_nieto.hablar()  #Dice hola dado que primero heredo de padre y después de madre
mi_nieto.reir()

print(Nieto.__mro__)  #Orden búsqueda, el primero método que encuentra es el que imprime (mas de un método hablar)

