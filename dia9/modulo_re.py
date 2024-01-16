#Expresiones regulares 
#patron = r'\d\d' para indicar que eso es una expresión regular

#caracteres especial 
#/d --> digito numérico  --> ejem v\d.\d\d
#/w --> carácter alfanumérico --> ejemplo \w\w\w-\w\w
#/s --> espacion en blanco --> número\s\d\d
#/D --> no numérico
#W --> NO alfanumérico
#/S --> NO espacio blanco 


#cuantificadores 
# + --> una o más veces --> código_\d-\d+
#{n} --> se repite n veces --> \d\d{2}
#{n,m} --> se repite de n a m veces 
#{n, } --> desde n hasta arriba
# * 0 o más veces 
# ? 1 o 0 

import re
texto = 'si necesita ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online'

patron = 'ayuda'

busqueda = re.findall(patron,texto)  #busca todos

'''for hallazgo in re.finditer(patron,texto):   #para mostrar la ubicación de los elementos
    print (hallazgo.span())'''

texto2 = "llama al 654-597-4122 ya mismo"
patron2 = re.compile(r'(\d{3})-(\d{3})-(\d{4})') #los agrega en grupos
resultado2 = re.search(patron2,texto2)
print(resultado2.group())

#requisitos de clave de segurdidad

clave = input("Clave: ")

patron = r"\D{1}\w{7}"

chequear = re.search(patron,clave)
print(chequear)


texto3 = 'No atendemos el lunes por la tarde'
buscar = re.search(r'\D$', texto3)
print(buscar)