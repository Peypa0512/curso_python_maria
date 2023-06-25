##############################################################################3
# OTRA SOLUCION QUE NO UTILA DICCIONARIOS
#######################################################################
meses = ['Enero', 'Febrero',  'Marzo',  'Abril',
         'Mayo',  'Junio',  'Julio',  'Agosto',
         'Septiembre',  'Octubre',  'Noviembre', 'Diciembre']
fecha = input('Dame fecha (formato dd/mm/aaaa):')

fechaList = fecha.split("/");
fechaList[1] = int(fechaList[1])

print('La fecha es el '+fechaList[0] + ' de ' + meses[fechaList[1]-1] + ' del ' + fechaList[2])