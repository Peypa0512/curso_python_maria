########################################################
# Diferencia entre añadir y concatenar listas
########################################################

# lista=[1,2]
# print("Direccion memoria lista:",id(lista))
# lista2 = [3,4]
# lista.append(lista2)
# print("Direccion memoria lista despues de append:",id(lista))
# lista=[1,6]
# print("Direccion memoria lista:",id(lista))
# lista = lista + lista2
# print("Direccion memoria lista despues de concatenar con mas:",id(lista))

########################################################
# Construir Colecciones
########################################################

cuadrados = [x**2 for x in range(1,11)] # Lista
print(cuadrados)
cuadrados= tuple(x**2 for x in range(1,11)) # Tuplas
print(type(cuadrados))
print(cuadrados)
cuadrados = {x**2 for x in range(1,11) } # Set
print(cuadrados)
cuadrados = {x:x**2 for x in range(1,11) } # Diccionario
print(type(cuadrados))
print(cuadrados)
