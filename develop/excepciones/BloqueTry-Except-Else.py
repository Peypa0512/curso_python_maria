try:
    numero = int(input('Dame numero: '))

except ValueError as ve:
    print('Has introducido un valor no válido')
else:
    print('El número introducido es:',numero)
