import numeros 

def preguntar():
    print ('Bienvenido a la farmacia de Miguel')
    while True:
        print ("[P]- Perfumeria \n[F] - Farmacia\n[C] - Cosmética")
        try:
            rubro = input ('Opción seleccionada: ').upper()
            ['P','F','C'].index(rubro)
        except ValueError:
            print('Opción incorrecta')
        else:
            break
    numeros.decorar_numero(rubro)        

def iniciar():
    while True:
        preguntar()
    
        try:
            continuar = input('Quieres continuar [S]/[N]: ').upper()
            ['S','N'].index(continuar)
        except ValueError:
            print('Opción no válida')
        else:
            if continuar == 'N':
                break


iniciar()