#Collections está integrado en python

from collections import Counter, defaultdict, namedtuple

numeros = [8,6,1,4,1,4,5,9,6,5]
print(Counter(numeros))  #Crea un diccionario donde dicen las veces que repite 
print(Counter('missisipi'))

frase = "al pan pan y al vino vino"
print(Counter(frase.split())) #Método split separa la frase por espacios

serie = Counter([1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,4])
print(serie.most_common(3)) #Aparecen los 3 más comunes
print(list(serie))

mi_dic =defaultdict(lambda: 'nada') #en caso de no tener esa clave sale nada
mi_dic['uno'] = 'verde'
print(mi_dic['dos'])

Persona = namedtuple('Persona',['nombre','altura','peso'])
ariel = Persona('ariel',1.76,79)
print(ariel.altura)