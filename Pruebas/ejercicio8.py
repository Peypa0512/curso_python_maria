'''
Ejercicio 8  Suma de Números Pares
Escribe una función sumar_pares(n: int) -> int que sume todos los números pares desde 1 hasta 
n (incluyendo n si es par).

'''

import unittest

def sumar_pares(n) :
    contador = 0
    
    if n < 1:
        return False
    
    for i in range(1, n+1):    
        if i % 2 == 0:
            contador += i
    return contador


class Ejercicio8_Test(unittest.TestCase):
    def test_sumar_pares(self):
        self.assertGreater(sumar_pares(13), 0)
        
    def test_valor_0(self):
        self.assertEqual(sumar_pares(0), False)
   
   
if __name__ == '__main__':    
    
    unittest.main(verbosity=2)
    