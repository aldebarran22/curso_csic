"""
Tuplas en Python
sql = "select * from clientes where pais=?" 
% ("España",)
"""

# Inicialización múltiples
a,b,c=1,2,3
print(a,b,c)

# Intercambio de variables:
a,b = b,a
print(a,b)

# Expandir tuplas:
L = (1,2,3,5,6)
a,b,*resto = L
print(a,b,resto)

L = (1,2,3,5,6)
a,b,*_ = L
print(a,b)

path = "libro1.csv"
t = path.partition('.')
print(t)
fich, _, ext = t
print(fich,ext)

import re
path = "na2co3"
print(re.split("[0-9]",path))






