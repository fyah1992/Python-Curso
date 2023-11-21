texto = "Esto es un texto de prueba"

mayusculas = texto.upper()
minusculas = texto.lower()
lista = texto.split() #se puede específica el separador en el paréntesis('t)
buscar = texto.find("s") #Cuando no encuentra una letra o palabra devuelve -1 no un error como index
remplazar = texto.replace("prueba","miguel")


print(mayusculas)
print(minusculas)
print(lista)
print(buscar)
print(texto)
print(remplazar)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"

unir = " ".join([a,b,c,d]) #primero une dejando espacio como indicamos al inicio
print(unir)
