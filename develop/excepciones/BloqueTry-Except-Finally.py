try:
    numero = int(input('Dame numero: '))
except ValueError as ve:
    print('Has introducido un valor no válido')
finally:
    print('La operación se ha ejecutado')
