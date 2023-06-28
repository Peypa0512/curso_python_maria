'''
Ejercicio 5: Prueba de cadena vacía
Escribe una función es_cadena_vacia(cadena) que tome como argumento una cadena de texto y devuelva True 
si la cadena está vacía (no contiene ningún carácter), y False en caso contrario. 
Escribe una prueba unitaria para esta función.
'''
import unittest

def cadena_vacia(cadena):
    return True if cadena == ''  else  False 
        

class Ejercicio5_Test(unittest.TestCase):
    def test_cadena_vacia(self):
        self.assertTrue( cadena_vacia(''), True)
    
    def test_cadena(self):
        self.assertFalse(cadena_vacia('Hay cadena'), False)

# Ejecutar las pruebas
if __name__ == '__main__':    
    
    unittest.main(verbosity=2)
    
        