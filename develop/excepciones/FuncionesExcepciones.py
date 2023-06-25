def dividir(numerador,denominador):
    try:
        resultado= numerador/denominador
        return resultado
    except ZeroDivisionError:
        return 'Se ha intentado dividir por cero'


def pedirNumero():
    while True:
        try:
            resultado = int(input('Dame numero:'))
            return resultado
        except ValueError:
            print('Ha introducido un dato erroneo')



try:
    numero1=pedirNumero()
    numero2=pedirNumero()
    print('Resultado:',dividir(numero1,numero2))

except Exception:
    print('Excepcion General')
