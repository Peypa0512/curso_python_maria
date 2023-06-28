'''
Ejercicio 6  Validar Palíndromos
Escribe una función es_palindromo(palabra: str) -> bool que tome una cadena de caracteres y 
determine si es un palíndromo (se lee igual de izquierda a derecha y de derecha a izquierda). 
Ignora los espacios en blanco y considera que la comparación no distingue entre mayúsculas y minúsculas

'''

import unittest

def es_palindromo(palabra: str) ->bool:
    palabra = palabra.replace(" ", '').lower()
    
    return  palabra == palabra[::1]   
    
    

class Ejercicio6_Test(unittest.TestCase):
    def test_es_palindromo(self):
        self.assertTrue(es_palindromo('amor'))
    
    
    def test_AssertionError(self):
        with self.assertRaises(AssertionError):
            es_palindromo('berenjena')


if __name__ == '__main__':    
    
    unittest.main(verbosity=2)
    

