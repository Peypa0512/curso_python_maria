###############################3333
# Variable local
############################
# def sumar(numero1, numero2):
#     resultado = numero1 + numero2
#     return resultado
#
# resultado=15
# valor = sumar(1,2)
#
# print('El resultado es:',resultado)
# print('El valor es:',valor)

###############################3333
# Variable local
############################

resultado=15
def sumar(numero1, numero2):
    global resultado
    resultado =numero1 + numero2
    return resultado

valor = sumar(1,2)

print('El resultado es:',resultado)
print('El valor es:',valor)