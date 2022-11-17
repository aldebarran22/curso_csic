"""
Funciones: llamadas y paso de parámetros
"""
from random import randint

def sumar(a,b):
    return a+b

def sumarRestar(a,b):
    return a+b, a-b

def hora(h=0,m=0,s=0):
    return "%02d:%02d:%02d" % (h,m,s)

s,r = sumarRestar(3,6)
print(s,r)
horas = [(randint(0,23),randint(0,59), \
    randint(0,59)) for _ in range(20)]
L=[hora(*t) for t in horas]
print(L)
L2=[hora(h,m,s) for h,m,s in horas]

# Formas de llamar:
# Posicional
print(sumar(4,5))    
# Nominal
print(sumar(b=5,a=4))
# Tupla:
t = (4,5)
print(sumar(*t)) # Desempaquetar la tupla
# Dict:
d = {"a":4, "b":5}
print(sumar(**d)) # Desempaquetar dict!






