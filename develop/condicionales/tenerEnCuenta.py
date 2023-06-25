####################################################
# Operador ternario
#####################################################
def mayor0():
    print('Numero mayor que 0')
def menorIgual0():
    print('Numero menor que 0')

numero=int(input('Dame numero:'))

mayor0() if numero>0 else menorIgual0()


####################################################
#Tanto el numero 0 como la cadena None o vacía daran
# resultado False
#####################################################
# numero = 0
# cadena = ''
# cadenaNula= None
# if numero:
#     print('Es cierto')
# else:
#     print('Es falso') #Resultado
# if cadena:
#     print('Es cierto')
# else:
#     print('Es falso') #Resultado
# if cadenaNula:
#     print('Es cierto')
# else:
#     print('Es falso') #Resultado
