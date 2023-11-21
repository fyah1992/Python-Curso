cliente = {"nombre":"juan","apellido":"López","peso":88}
consulta = cliente["apellido"]
print(consulta)
print(cliente)
print(cliente.keys())
print(cliente.values())
print(cliente.items())
cliente["edad"] = 27 #añadir

print(cliente)


dic = {"c1":55,"c2":[10,20,30],"c3":{'s1':100,'s2':200}}
print(dic["c3"]['s1'])


alf = {"c1":['a','b','c'], "c2":["d","e","f"]}

print(alf["c2"][1].upper())