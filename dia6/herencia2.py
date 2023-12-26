class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")
    


class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)  #evita la necesidad de tener que definir otra vez los parámetros
        self.altura_vuelo = altura_vuelo
    
    def hablar(self):
        print('pio')
    
    def volar(self, metros):
        print(f"El pajoro vuela {metros} metros")


piolin = Pajaro(3,"amarillo", 60)
piolin.nacer()
piolin.volar(100)

piolin.hablar()

mi_animal = Animal(5 , 'negro')

