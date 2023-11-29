import os

os.chdir("/home/miguel/Escritorio/alternativ")
os.makedirs("/home/miguel/Escritorio/alternativ/otra")
archivo = open("archivo.txt")
print(archivo.read())