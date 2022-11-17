"""
Estudio sobre los nacimientos
en EEUU
"""
import os
path = "../practicas/pandas/names"

def filtro(fichero, ini, fin):
    # yob1990.txt
    # yob 1990
    fich, _, ext = fichero.partition('.')
    if ext == 'txt':
        yy = int(fich[-4:])
        return ini <= yy <= fin
    else:
        return False

def filtrarFicheros(ini, fin):
    L = os.listdir(path)
    L2 = [f for f in L if filtro(f,ini,fin)]
    L2.sort()
    return L2

if __name__ == '__main__':
    rango = filtrarFicheros(1990, 1995)
    print(rango)


