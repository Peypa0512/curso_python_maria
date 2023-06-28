'''
Ejercicio 9 Ordenar Palabras
Escribe una función ordenar_palabras(palabras: List[str]) -> List[str] que tome una lista de palabras y 
las ordene en orden alfabético, ignorando las mayúsculas y minúsculas.

'''
import unittest

def ordenar_palabras(palabras: list[str]):    
    lista = []
    
    for i,valor in enumerate(palabras):
        
        lista.append(valor.lower())
    lista.sort()   
    
    return lista

class Ejercicio9_Test(unittest.TestCase):
    def test_ordenar_palabras(self):
        lista = ['Abedul', 'Zapato', 'Jabali', 'Hormiga']
        self.assertListEqual(ordenar_palabras(lista), ['abedul', 'hormiga', 'jabali', 'zapato'])
        
    def test_palabras_no_ordenadas(self):
        lista = ['Abedul', 'Zapato', 'Jabali', 'Hormiga']
        msg = 'No corresponden los valores de la lista comparada'
        self.assertCountEqual(ordenar_palabras(lista), ['hormiga', 'jabali', 'abedul'], msg)

if __name__ == '__main__':    
    
    unittest.main(verbosity=2)
    