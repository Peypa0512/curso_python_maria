
############################################################
## Finally -> Siempre se lanzara ValueError
############################################################
try:
    numero1 = int(input('Dame numero1: '))
    numero2 = int(input('Dame numero2: '))
    if(numero2==0):
        raise ZeroDivisionError('Numero2 es cero')
    print('Hacemos la division')
    division=numero1/numero2
except ValueError:
    print('Has introducido un valor no válido - ValueError')
    raise ZeroDivisionError('Dato introducido no válido')
except ZeroDivisionError as zde:
    raise zde
except Exception as e:
    raise ZeroDivisionError('Error general')
finally:
    raise ValueError('Te has confundiooooooo')
    print('Me imprimo siempre')

