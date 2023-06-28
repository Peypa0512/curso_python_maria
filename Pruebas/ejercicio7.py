'''
Ejercicio 7 Contar Ocurrencias
Escribe una función contar_ocurrencias(lista: List[int], elemento: int) -> int que tome una lista de enteros y 
cuente cuántas veces aparece un elemento específico en ella.

'''
import unittest

def contar_ocurrencias(lista, elemento: int):
    if elemento not in lista:
        return -1

    count = 0
    
    for i, e in enumerate(lista):
        if e == elemento:
            count += 1
            
    return count

class Ejercicio7_Test(unittest.TestCase):
    def test_contar_ocurrencias(self):
        self.assertGreaterEqual(contar_ocurrencias([1,5,3,2,5,1,35], 5),0)
    
    def test_menos_ocurrencias(self):
        self.assertLess(contar_ocurrencias([1,5,3,2,5,1,35], 4),1)
        
if __name__ == '__main__':    
    
    unittest.main(verbosity=2)
    