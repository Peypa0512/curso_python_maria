#cesta_compra = None
cesta_compra = [] #No es necesario la inicialización de la lista, es solo para este ejemplo

print(cesta_compra)
cesta_compra += ['Pan',2,'Leche']
print(cesta_compra)
cesta_compra *=3
print(cesta_compra)



##Ejemplo para recorrer listas
numeros=[0,1,2,3,4,5,6,7,8,9]
for item in numeros[1:]:
    if(item % 2 == 0):
        break
    print(item)
print('------------------------')
for index in range(1,10,2):
    print(numeros[index])

