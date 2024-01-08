#funciones que modifican el funcionamiento de otras funciones 

def cambiar_letras(tipo):

    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == 'may':
        return mayuscula
    elif tipo == 'min':
        return minuscula
    
operacion = cambiar_letras('may')
operacion('palabra')
