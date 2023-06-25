import time

print('*** EJERCICIO 4 ***')

entero = int(input('Entero: '))
counter = 0
cuentaAtras = ''

while(entero<0):
	entero = int(input('Entero: '))


print('\nCuenta atras con timer: ')

while (counter <= entero):
	print(entero)
	# esto en realidad no es tiempo real porque no tiene en cuenta
	# el tiempo de procesamiento
	time.sleep(0.5)

	if (counter==entero):
		cuentaAtras += str(entero)
	else:
		cuentaAtras += (str(entero) +',')

	entero -= 1


print('\nCuenta atras:', cuentaAtras)