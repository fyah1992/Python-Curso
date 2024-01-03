class CD:
    def __init__(self,autor,titulo,canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
    
    def __str__(self):  #Lo que devuelve al llamar al objeto 
        return f"Album: {self.titulo} de {self.autor}"
    
    def __len__ (self): #Evita que al hacer print(len(mi_cd)) de error y devuelva el número canciones
        return self.canciones
    
    def __del__(self): #Informa sobre la eliminación del objeto 
        print("Se ha eliminado el CD")

mi_cd = CD('Metallica','World',24)
print(mi_cd)
print(len(mi_cd))
del mi_cd #elimina el objeto