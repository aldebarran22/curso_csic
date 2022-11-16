"""
Cadenas: join, split
"""
import json

def convesor(path, sep=';'):
    """
    Convierte formato CSV a JSON
    """
    f = None
    L = []
    try:
        f = open(path, "r")
        cabs = None
        for linea in f:
            linea = linea.rstrip()
            if not cabs:
                cabs = linea.split(sep)
            else:
                datos = linea.split(sep)
                d = dict(zip(cabs, datos))
                L.append(d)
        cad = json.dumps(L)
        return cad
        
    except Exception as e:
        print(e)

    finally:
        if f: f.close()

if __name__ == '__main__':
    path = "../practicas/pandas/merge/Empresa.txt"
    print(convesor(path))