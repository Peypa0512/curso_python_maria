'''
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha
en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

'''
fecha = {}
mes =['','Enero','Febrero', 'Marzo','Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre',
      'Noviembre', 'Diciembre']
calendario = input('Por favor introduce una fecha en formato dd/mm/aa: > ')
contador=1
fecha_recortada = calendario.split('/')
for item in fecha_recortada:
    fecha[contador] = item
    contador += 1
print(fecha)


print(f'La fecha que has elegido es {fecha[1]} del mes de {mes[int(fecha_recortada[1])]} del año {fecha[3]}')
