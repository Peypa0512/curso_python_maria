'''
Ejercicio 2 Prueba de pertenencia en lista
Escribe una función esta_en_lista(elemento, lista) que tome como argumentos un elemento y una lista, 
y devuelva True si el elemento está presente en la lista, y False en caso contrario. 
Escribe una prueba unitaria para esta función.
'''

import unittest

def esta_en_lista(elemento,lista):
    if elemento in lista:
        return True
    else:
        return False
    
class Elemento_en_lista(unittest.TestCase):
    
    def test_elemento_en_lista(self):
        elemento = 'Casa'
        lista = ['Manzana', 'Pera', 'Melocotón', 'Casa']
        
        resultado = esta_en_lista(elemento,lista)
        
        self.assertTrue(resultado, True)
    
    def test_error(self):
        elemento = 'Albaricoque'
        lista = ['Manzana', 'Pera', 'Melocotón', 'Casa']
        resultado = esta_en_lista(elemento,lista)
        
        self.assertRaises(AssertionError)

# Ejecutar las pruebas
if __name__ == '__main__':    
    
    unittest.main(verbosity=2)
    
        