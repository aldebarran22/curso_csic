"""
POO en Python. Herencia Simple
sobrecarga de operadores.
"""
class Persona:
    """
    Implementación de la clase persona
    """
    def __init__(self,nombre='',ape="",edad=0):
        # definir att:
        self.nombre = nombre
        self.ape = ape
        self.edad = edad
    
    def __str__(self):
        # Se liga a la función: str()
        return self.nombre+" "+self.ape+" " + \
            str(self.edad)

    def __repr__(self):
        # Se liga con la función: repr()
        return str(self)

    def __lt__(self,otro):
        if self.ape < otro.ape:
            return True

        elif self.ape == otro.ape:
            if self.nombre < otro.nombre:
                return True
            else:
                return False
        else:
            return False 

    def cumple(self):
        self.edad+=1

    def __del__(self):
        # Se liga con la función: del() 
        print('Se borra ',self.nombre)
    
class Empleado(Persona):

    def __init__(self,nombre='',ape="",edad=0, \
        empresa="",sueldo=0.0):
        Persona.__init__(self,nombre,ape,edad)
        self.empresa = empresa
        self.sueldo=sueldo

    def __str__(self):
        return Persona.__str__(self)+" "+ \
            self.empresa+" "+str(self.sueldo)

if __name__=='__main__':
    e1 = Empleado('Julio','Sanz',45,'csic',3000)
    print(e1)
    e1.cumple()
    print(e1)


    p1 = Persona('Julia','Sanz',56)
    #print(p1.__str__())
    print(p1)
    p1.cumple()
    print(p1)
    print(p1.__dict__)
    L = [p1, Persona('Andres','Sanz',4), \
         Persona('Eva','Gomez',24)]
    print(L)
    L.sort(key=lambda obj: obj.edad)     
    print(L)
    L.sort() # Necesita el operador: <  __lt__()
    print(L)
    exit()
    p1.__dict__['tno']=69944838
    print(p1.tno)
    L2 = [p.__dict__ for p in L]
    print(L2)

