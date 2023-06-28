'''
Ejercicio 10  Divisores de un Número
Escribe una función divisores(numero: int) -> List[int] que tome un número entero y devuelva una lista 
con todos sus divisores.

'''

import unittest

def divisores(numero):
    # hace divisiones hasta que de 0
    lista = []
    for indice in range(numero, 0, -1):
        
        if numero % indice == 0:
            lista.append(indice)
            
    return lista    
        
        
        
class Ejercicio10_Test(unittest.TestCase):
    def test_divisores(self):
        self.assertEqual(divisores(18), [18,9,6,3,2,1])
        

if __name__ == '__main__':    
    
    unittest.main(verbosity=2)
    

