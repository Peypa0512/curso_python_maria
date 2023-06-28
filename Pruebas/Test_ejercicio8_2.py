'''
Ejercicio 8  Suma de Números Pares
Escribe una función sumar_pares(n: int) -> int que sume todos los números pares desde 1 hasta 
n (incluyendo n si es par).

'''

import unittest

def sumar_pares(n=...) :
    n = int(n)
    lista = [num for num in range(n+1)if num % 2 ==0]    
    return sum(lista)

        

class Ejercicio8_Test(unittest.TestCase):
    def test_sumar_pares(self):
        self.assertGreater(sumar_pares(13), 0)
    
    def test_sumar_cadena(self):
        self.assertEqual(sumar_pares('2'), 2)
        
    def test_valor_0(self):
        self.assertEqual(sumar_pares(0), False)
        
    
    def test_valor_no_numero_ValueError(self):
        with self.assertRaises(Exception):
             n = 'abcd'
             sumar_pares(n)
    def test_valor_no_numero_TypeError(self):
        with self.assertRaises(Exception):            
            sumar_pares(' ')
    
         
   
   
if __name__ == '__main__':    
    
    unittest.main(verbosity=2)
    #sumar_pares(13)