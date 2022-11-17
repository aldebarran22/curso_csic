"""
Entrada / Salida con numpy
"""
import numpy as np

def grabar(m, fichero='matriz',formato='npy',**kwargs):
    t = ('npy','npz','txt')
    path = f'{fichero}.{formato}'
    if formato not in t:
        raise ValueError('Extensión no soportada')

    elif formato=='npy':
        np.save(path, m)

    elif formato=='txt':
        if 'delim' in kwargs:
            delim = kwargs['delim']  
            np.savetxt(path, m, fmt='%d',delimiter=delim)
        else:
            raise ValueError('Clave delim no encontrada')

    elif formato=='npz':
        if 'key' in kwargs:
            key = kwargs['key']        
            np.savez_compressed(path,m=m)
        else:
            raise ValueError('Clave npz no encontrada')

def cargar(fichero='matriz', formato='npy', **kwargs):
    path = f'{fichero}.{formato}'
    if formato=='npy':
        return np.load(path)

    elif formato=='txt':
        if 'delim' in kwargs:
            delim = kwargs['delim']
            return np.loadtxt(path, dtype=np.int16, delimiter=delim)
        else:
            raise ValueError('Clave delim no encontrada')
    else: # npz
        loaded = np.load(path)
        return loaded['m']

if __name__ == "__main__":
    m = np.random.randint(1,1000,(100,100))
    print(m[:3,:3])
    print()

    grabar(m, formato='txt',delim=';')
    grabar(m)
    grabar(m, formato='npz',key='M')

    m2 = cargar(formato='txt',delim=';')    
    print(m2[:3,:3])
    print()

    m3 = cargar(formato='npy')
    print(m3[:3,:3])
    print()

    m4 = cargar(formato='npz')
    print(m4[:3,:3])
    print()



