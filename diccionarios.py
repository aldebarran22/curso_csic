"""
Diccionarios en Python
"""
d = {"1":1, "2":2, "3":3}
print(d, type(d))
d["4"]=4
d["1"]=100
print(d)

cad = "adios"
L = list(range(8))
d2 = dict(zip(cad,L))
print(d2)

d2 = dict(zip(L,cad))
print(d2)

d3 = dict.fromkeys("hola",0)
print(d3)
# Cuidado con los objetos MUTABLES!!!
d3 = dict.fromkeys("hola",list())
print(d3)
d3['h'].append(5)
print(d3)
d3['h']=[100]
print(d3)

# Intercambiar k,v
cad = "adios"
L = list(range(8))
d2 = dict(zip(cad,L))
print(d2)
d3 = dict(zip(d2.values(), d2.keys()))
print(d3)

#iterar:
for k, v in d3.items():
    print(k,v)

# actualizar
d4 = {10:'z',4:'x'}
d3.update(d4)
print(d3)

print(d3.popitem())
d3.clear()





