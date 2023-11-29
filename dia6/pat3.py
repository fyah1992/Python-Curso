from pathlib import Path

base = Path.home()
guia = Path (base,"Europa","España",Path("Barcelona", "Sagrada_Familia.txt"))
guia_2 = guia.with_name("La_Pedrera.txt")
print(guia)
print(guia_2)

print(guia.parent.parent)
