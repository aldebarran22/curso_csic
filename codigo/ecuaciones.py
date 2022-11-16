"""
Resolución de ecuaciones con numpy
3x + 9y - 10z = 24
1x - 6y + 4z = -4
10x - 2y + 8z = 20
"""
import numpy as np
import re

class Ecuaciones:

    letras = "xyztvw"

    def __init__(self, L):
        self.L = [s.replace(' ','') for s in L]        
        self.incognitas = f"[{Ecuaciones.letras[:len(L)]}]"
        print(self.L)
        self.b = self.getTerminos()
        print(self.b)
        self.A = self.getCoeficientes()
        print(self.A)

    def getTerminos(self):
        aux = [[int(t.partition('=')[2])] \
            for t in self.L]
        return np.array(aux)

    def getCoeficientes(self):
        aux = []
        for e in self.L:
            ecu = e.partition('=')[0]
            incog = re.split(self.incognitas,ecu)
            ecu_aux = [int(i) if i!='' else 1 \
                for i in incog[:-1]]
            aux.append(ecu_aux)
        return np.array(aux)

    def resolver1(self):
        return np.linalg.solve(self.A, self.b)    


if __name__ == "__main__":
    Lecu = ['3x + 9y - 10z = 24', \
            'x - 6y + 4z = -4', \
            '10x - 2y + 8z = 20']

    Lecu = ['x+4y-8z=-8', \
            '4x+8y-z=76', \
            '8x-y-4z=110']
    ecu = Ecuaciones(Lecu)
    print(ecu.resolver1())
    exit()
    #print(ecu.resolver2())

    Lecu = ['2x + 3y = 8','x - 2y = -10']
    ecu = Ecuaciones(Lecu)
    print(ecu.resolver1())

