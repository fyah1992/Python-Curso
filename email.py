import re

def verificar_email(email):
    patron = '\w*\@\w*\.com$|\w*\@\w*\.com.br$'
    if re.search(patron,email):
        print("Correcto")
    else:
        print('incorrecto')

respuesta =verificar_email('miguel362@gmail.com.br')
