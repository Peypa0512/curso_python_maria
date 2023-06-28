'''
Ejercicio 9 Ordenar Palabras
Escribe una función ordenar_palabras(palabras: List[str]) -> List[str] que tome una lista de palabras y 
las ordene en orden alfabético, ignorando las mayúsculas y minúsculas.

'''
import unittest
import logging


def ordenar_palabras(palabras: list[str]) ->list[str]:    
    lista = []
    # for i,valor in enumerate(palabras):        
    #     lista.append(valor.lower())
    
    lista =[x.lower() for x in lista]
    
    lista.sort() 
    return lista

class MiObjeto:
    def __init__(self,nombre):
        self.nombre = nombre
    def __eq__(self,obj):
        return self.nombre == obj
    
    def __str__(self) -> str:
        return f'MiObjeto [nombre ={self.nombre}]'
    
def miFuncion():
    return 'Maria'



class Ejercicio9_Test(unittest.TestCase):
    
    mi_objeto = MiObjeto('Maria')
    
        
    def test_1(self):
        logging.basicConfig(level=logging.DEBUG, filename='mistrazas.log', format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info('{Ejercicio9_Test}- {test_1}') 
        logging.debug(MiObjeto('Pepe'))
        logging.info('me lo han devuelto') 
        self.assertEqual(miFuncion(), self.mi_objeto, )
    
    

if __name__ == '__main__':    
    
    unittest.main(verbosity=2)
    