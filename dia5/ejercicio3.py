def cero_repetido(*args):
    n_anterior = 2
    for n in args:
        if n == n_anterior:
            return True
        else:
            n_anterior = n
    return False

print(cero_repetido(1,2,0,5,6,0))