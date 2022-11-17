"""
Dado un texto obtener un recuento
de cada letra.
Imprimir el resultado de mayor a
menor según el número de ocurrencias
"""

texto = """Dado un texto obtener un recuento
de cada letra"""

# Sol1:
d = dict()
for letra in texto:
    if letra in d:
        d[letra]+=1
    else:
        d[letra]=1
print(d)

# Sol2:
d = dict()
for letra in set(texto):
    d[letra] = texto.count(letra)
print(d)

d = {k:texto.count(k)  for k in set(texto)}
print(d)
L = sorted(d.items(), key=lambda t:(t[1],t[0]))
for letra,cuenta in L:
    print(letra, cuenta)

from collections import Counter
c = Counter(texto)
print(c)








