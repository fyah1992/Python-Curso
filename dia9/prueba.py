import os
import re

texto = "Fusce at ornare sapien. Curabitur vestibulum nibh in neque tincidunt, non interdum ante semper. Vivamus eget scelerisque eros. Vestibulum egestas elementum congue. Ut hendrerit ultrices nunc, quis elementum arcu. Nmrn-20155 Fusce"

patron = re.compile(r'(N[a-zA-Z]{3})-([0-9]{5})')
resultado = re.search(patron,texto)
print(resultado.group())