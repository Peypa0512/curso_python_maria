


def saludar(nombre,apellido,anio=1978):
    cadena_saludo='Hola '+nombre+' '+apellido
    print('Estamos en el anio',anio)
    return cadena_saludo

print('Inicio programa')
mi_funcion=saludar
print(type(mi_funcion))
saludo=mi_funcion('Pepe','Gomez Tejera')
print(saludo)