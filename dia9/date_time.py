from datetime import datetime, date

mi_fecha = datetime(2025,5,15,22,10,15,2500)
mi_fecha = mi_fecha.replace(month=11)
#print(mi_fecha)

nacimiento = date(1995,3,5)
defuncion = date(2025,6,19)

vida = nacimiento - defuncion

print(vida.days)

hoy = datetime.now().minute
print(hoy)

hoy2 = date.today()
print(hoy2)