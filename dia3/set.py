#Solo admite valores únicos, no repetidos

# No tienen posición y son inmutables

#Solo admite tuplas ya que también son inmutables

mi_set = {1,2,3,4,5,(1,2,3)}
mi_set.add(6)
mi_set.discard(2)
print(mi_set)
print(len(mi_set))
print(3 in mi_set)


