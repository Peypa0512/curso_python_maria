meses ={1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
               5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
               9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
fecha = input('Dame fecha (formato dd/mm/aaaa):')

fechaList = fecha.split("/");
fechaList[1] = int(fechaList[1])

print('La fecha es el '+fechaList[0] + ' de ' + meses[fechaList[1]] + ' del ' + fechaList[2])