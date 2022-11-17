"""
Métodos de list
"""
from random import randint,seed
L2 = [randint(1,100) for i in range(10)]
L2.sort()# Modifica el obj original
print(L2)

s = "hola"
print(s.upper())#Devuelve una copia!

L2.sort(reverse=True) # DESC
print(L2)

L = ['Jose','Jaime','Ana Maria','Eva','Angela']
L.sort(key=len)
print(L)

L = [('Jose',45,1.77) \
,('Jaime',56,2.05),('Ana Maria',23,1.9)]
L.sort(key=lambda t:t[1]) # ASC por edad
print(L)

L.sort(key=lambda t:t[2],reverse=True) # DESC por altura
print(L)

# insertar:por el final
L = list(range(10))
L.extend((1,2,3))
L.append((1,2,3))
L += [777]
print(L)

# en una pos:
L.insert(0, 555)
print(L)

# Buscar y contar:
try:
    print('pos del 7:', L.index(77))
except Exception as e:
    print(e.__class__.__name__,e)

print(L.count(3))
# Borrados:
del(L[0])
print(L)
L.remove(9)
print(L)
print(L.pop())

# invertir: 
L.reverse()
print(L)

# Iteradores:
def cuadrado(n):
    return n**2

# Recorrer una lista y aplicar la func cuadrado
L = list(range(10))
L2 = list(map(cuadrado, L))
L3 = [cuadrado(i) for i in L]
L4 = [i**2 for i in L]
print(L)
print(L2)
print(L3)
print(L4)

# Filtrar elementos.
seed(5)
L = [randint(1,100) for i in range(10)]
seed(5)
L2 = [randint(1,100) for i in range(10)]
# Numeros entre 20 y 50
L3 = list(filter(lambda n:20<=n<=50,L))
print(L)
print(L2)
print(L3)
L4 = [i for i in L if (20<=i<=50) and (i%11==0)]
print(L4)

# Reducir:
from functools import reduce
def minimo(a,b):
    print(a,b)
    return a if a < b else b

print(reduce(minimo, L)) 


























