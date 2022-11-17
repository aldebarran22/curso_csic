"""
Operaciones con conjuntos
"""
comida = set(['Jaime','Raul','Olga','María','Eva'])
cena = {'Raul','María','Sofia','Andrés'}

# Union |, inter &, diferencia -, 
# diferencia Sim ^
print('Quien va solo a cenar:',cena - comida)

print('Quien va solo a un evento:',cena ^ comida)
print((comida | cena)-(comida & cena))

print('Van a comer y a cenar:',comida & cena)

print('Quienes han participado en los eventos:',
comida | cena)

comida.add('Paula')
comida.remove('Raul')
print('Eva' in cena)
#print(comida[0]) Ojo No se puede indexar!
