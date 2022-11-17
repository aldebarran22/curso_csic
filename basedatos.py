"""
Poo con Bases de datos
"""
import sqlite3 as dbapi
from os.path import isfile

class BaseDatos:

    def __init__(self, path):
        self.conexion = None
        if not isfile(path):
            raise ValueError(f'El fichero:{path} no existe')
        else:
            self.conexion = dbapi.connect(path)
    
    def export(self, *tablas, formato='csv'):
        for tabla in tablas:
            fich = None
            try:            
                L = self.select(tabla)
                nombreFich = f"{tabla}.{formato}"
                fich = open(nombreFich, "w")
                for t in L:
                    t2 = [str(i) for i in t]
                    linea = ";".join(t2)+"\n"
                    fich.write(linea)
            except Exception as e:
                raise e
            finally:
                if fich: fich.close()
    
    def select(self, tabla):
        cur = None
        try:
            sql = f"select * from {tabla}"
            cur = self.conexion.cursor()            
            cur.execute(sql)
            cabs = tuple([t[0] for t in cur.description])
            datos = [t for t in cur.fetchall()]
            datos.insert(0, cabs)
            return datos
        except Exception as e:
            raise e # Relanzar la exception
        finally:
            if cur: cur.close()

    def __del__(self):
        if self.conexion:
            self.conexion.close()

if __name__ == "__main__":
    try:
        bd = BaseDatos('../practicas/BBDD/empresa3.db')
        L = bd.select('clientes')
        for p in L:
            print(p)
        #bd.export('clientes')
        bd.export('clientes','empleados','categorias')
    except Exception as e:
        print(e)





