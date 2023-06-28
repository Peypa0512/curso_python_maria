'''
Ejercicio 3: Prueba de lanzamiento de excepción
Escribe una función dividir(a, b) que tome como argumentos dos números y devuelva el resultado de dividir a entre b.
Si b es igual a cero, la función debe lanzar una excepción ZeroDivisionError. 
Escribe una prueba unitaria para esta función.
'''

import unittest

def dividir(a,b):
    if b == 0:
        raise ZeroDivisionError
    return a/b

class Test_division(unittest.TestCase):
    
    def test_division(self):
        a=5
        b=2
        resultado = dividir(a,b)
        self.assertIsNot(resultado, 0)
    
    def test_error(self):
        a=1
        b=0       
        with self.assertRaises(ZeroDivisionError):
             resultado = dividir(a,b)
            
        
# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main(verbosity=2)