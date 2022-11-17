"""
Pruebas con listas
"""
from random import randint

L = [1,3,4,5,6,-1]
L2 = list('hola que tal')
L[0] = 1000
print(L)

for i in L:
    print(i,  end=' ')

for pos, i in enumerate(L):
    print(pos, i)

L2 = [randint(1,100) for i in range(10)]
print(L2)    

# OJO con los tipos mutables: list, set , dict
L3 = L2
L2[0] = 1000
print(L3, id(L3))
print(L2, id(L2))
print()


L2 = [randint(1,100) for i in range(10)]
L3 = L2.copy()
L2[0] = 1000
print(L3, id(L3))
print(L2, id(L2))
print()
exit()

L2 = [[1,2],[3,4],[5,6]]
L3 = L2.copy()
L2[0] = 1000
L2[-1].append(999)
print(L3)
print(L2)
print()

import copy
L2 = [[1,2],[3,4],[5,6]]
L3 = copy.deepcopy(L2)
L2[0] = 1000
L2[-1].append(999)
print(L3)
print(L2)
print()

L = [(1,2),(3,5),(9,8)]
# Desempaquetar tuplas
for a,b in L:
    print(a,b)

#slicing: para str, tuples
L = list(range(10))
print(L)
print('3 primeros', L[0:3], L[:3])
print('3 ultimos:', L[-3:])
print('todos de 2 en 2:',L[::2])
print('invertida:',L[::-1])
print('quitar extremos:',L[1:-1])

#funciones sobre list
print('len:',len(L))
print('suma:',sum(L))
print('min:',min(L))
print('max:',max(L))
print('media:',sum(L)/len(L))

# Conversiones a otras cols.
t = tuple(L)
print(t, type(t))

L = [1,12,2,2,2,1,88,88]
c = set(L)
print(c, type(c))


#métodos





