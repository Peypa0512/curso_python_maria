asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for asignatura in asignaturas:
    notas += [input("¿Qué nota has sacado en " + asignatura + "?")]
print(type(enumerate(asignaturas)))

for index,asignatura in enumerate(asignaturas):
    print("En la asignatura "+asignatura+" has sacado la nota "+notas[index])