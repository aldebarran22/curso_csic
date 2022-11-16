"""
Paso de parámetros a funciones
"""
# Globales:
m = "hola"
d = {"a":1,"b":2}
c = {1,2,3,4}
L = [1,2,3]

def imprimir():
    print(m)
    print(d)
    print(c)
    print(L)

def escribir():
    global m, L
    m = 500
    c.add(5) # obj mutable con metodo NO es necesario
    d['x']=120
    L += [55] # ojo es con una asignación!

imprimir()
escribir()
imprimir()
exit()

# Tipos anotados:
def modificar(n, L):
    L.extend([1,2,3])
    n += 10

def funcion(s:str, i:int)->None:
    print(s)

def func(ob1,ob2,op1=1.678,op2=2,*args,**kwargs):
    print('Obligatorios:',ob1,ob2)
    # fstring
    print(f'Opcionales:{round(op1,2)},{op2}')
    print(args)
    print(kwargs)
    print()

n = 100
L = [4,5,6]
print(n,L)
modificar(n,L)
print(n,L)
exit()

func(1,2)
func(1,2, op2=5)
func(1,2,3,4)
func(1,2,3,4,5,6,7,8,x=10,y=20)



