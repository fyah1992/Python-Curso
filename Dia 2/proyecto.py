nombre = input('Nombre de empleado ')
ventas = int(input("Productos vendidos "))

comision = ((ventas*13) / 100)

print(f"{nombre} ha cobrado {comision} de comisiones")