'''
Ejercicio 1 Prueba de igualdad
Escribe una función es_mayor_de_edad(edad) 
que tome como argumento un entero que representa la edad de una persona y devuelva True si es mayor o igual a 18, 
y False en caso contrario. Escribe una prueba unitaria para esta función.
'''

import unittest

def es_mayor_de_edad(edad):
    if edad < 0:
        return False
    
        
    
    if edad >= 18:
        return True
    else:
        return False

class Ejercicio1_Test(unittest.TestCase):
    
    def test_es_mayor_de_edad(self):
        edad = 20
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado,True)
    
    def test_es_18_de_edad(self):
        edad = 18
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado,True)  
    
    def test_es_menor_de_edad(self):
        edad = 15
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado,False) 
    
    def test_es_numero_de_negativo(self):
        edad = -5
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado,False)     
    
    def test_es_espacio_y_valor(self):
        edad =  5
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado,False)   
    
    def test_es_cadena(self):
        
        with self.assertRaises(TypeError):  
            edad = 'cadena'
            es_mayor_de_edad(edad)  
    
    def test_es_vacio(self):
        
        with self.assertRaises(TypeError):             
            es_mayor_de_edad()  
        
    def test_es_nulo(self):
        
        with self.assertRaises(TypeError):              
            es_mayor_de_edad(None)  
    
    # def test_error(self):
    #     with self.assertRaises(AssertionError):
    #         edad = 16
    #         resultado = es_mayor_de_edad(edad)
    #         self.assertEqual(resultado,True)       
        

# Ejecutar las pruebas
if __name__ == '__main__':
    
    
    unittest.main(verbosity=2)
    