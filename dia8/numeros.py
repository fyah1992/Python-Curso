


def nunero_perfumeria():
    for x in range (1,100):
        yield f"P:{x}"


def nunero_farmacia():
    for x in range (1,100):
        yield f"F:{x}"


def nunero_cosmeticos():
    for x in range (1,100):
        yield f"C:{x}"

p = nunero_perfumeria()
f = nunero_farmacia()
c = nunero_cosmeticos()

def decorar_numero(rubro):
    print('Su número es:')
    if rubro == 'P':
        print (next(p))
    elif rubro == 'F':
        print (next(f))
    else:
        print (next(c))
    print ('Aguarde su número')

