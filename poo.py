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

    def hablarCon(self, otro=None):
        if not otro:
            print(self.nombre+" está hablando solo")
        else:
            print(self.nombre+" y "+otro.nombre+ \
                " están hablando")        

    def __del__(self):
        # Se liga con la función: del()
        pass 
        #print('Se borra ',self.nombre)
    
class Empleado(Persona):

    def __init__(self,nombre='',ape="",edad=0, \
        empresa="",sueldo=0.0, idiomas=[]):
        #Persona.__init__(self,nombre,ape,edad)
        super().__init__(nombre,ape,edad)
        self.empresa = empresa
        self.sueldo=sueldo
        self.idiomas = idiomas

    def __str__(self):
        return Persona.__str__(self)+" "+ \
            self.empresa+" "+str(self.sueldo)

    def hablarCon(self, otro=None):
        if not otro:
            Persona.hablarCon(self, otro)
        else:
            c1 = set(self.idiomas)
            c2 = set(otro.idiomas)
            inter = c1 & c2
            if len(inter)==0:
                raise ValueError('No tienen idioma común')
            else:
                print(self.nombre+" y "+otro.nombre + \
                    " hablan en: " + " o ".join(inter))


if __name__=='__main__':
    e1 = Empleado('Julio','Sanz',45,\
        'csic',3000,['alemán','polaco'])
    e2 = Empleado('Carmen','Gomez',45,\
        'csic',3000,['inglés','francés'])
    e1.hablarCon()
    e1.hablarCon(e2)

    """
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
    """
