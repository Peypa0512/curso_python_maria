asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
print('Id con append')
for asignatura in asignaturas:
    nota = input("¿Qué nota has sacado en " + asignatura + "?")
    notas.append(nota)
    print(id(notas))
print(type(enumerate(asignaturas)))

for index,asignatura in enumerate(asignaturas):
    print("En la asignatura "+asignatura+" has sacado la nota "+notas[index])

##################################################################
# Otra forma
#################################################################
print('-------------- Otra forma--------------')
print('Id con concatenacion')
for asignatura in asignaturas:
    nota = input("¿Qué nota has sacado en " + asignatura + "?")
    notas = notas + [nota] # [nota]Convierte nota que es str a un elemento de lista
    print(id(notas))
print(type(enumerate(asignaturas)))

for index,asignatura in enumerate(asignaturas):
    print("En la asignatura "+asignatura+" has sacado la nota "+notas[index])