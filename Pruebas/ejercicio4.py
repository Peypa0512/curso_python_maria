'''
Ejercicio 4: Prueba de igualdad aproximada
Escribe una función calcular_area_circulo(radio) que tome como argumento el radio de un círculo y 
devuelva el área correspondiente. 
Escribe una prueba unitaria para esta función, verificando si el resultado es igual a 50.265 aproximadamente.
'''

import unittest
import math

def calcular_area_circulo(radio):
    return math.pow(math.pi*radio,2)

class Test_calculo_area_circulo(unittest.TestCase):
    
    def test_calculo_area(self):
        radio = 2.2572
        resultado = calcular_area_circulo(radio)
        self.assertAlmostEqual(resultado, 50.265)
    def error_AssertionError(self):
        with self.assertRegex(AssertionError):
            radio = 2.2572
            resultado = calcular_area_circulo(radio)   

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main(verbosity=2)
        