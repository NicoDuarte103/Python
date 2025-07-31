asignaturas = []
asignaturasA = []
asignaturasD = []
bucle = 0
asignador = 0
nota = 0
while bucle == 0:
    asignador = input("ingrese asignatura: ")
    if asignador == "salir":
        bucle = 1
        break
    asignaturas.append (asignador)

    nota = input("esta aprobada? s/n: ")
    if nota == "s":
        asignaturasA.append(asignador)
    if nota == "n":
        asignaturasD.append(asignador)
    
print (f"asignaturas: {asignaturas}")
print (f"aprobadas: {asignaturasA}")
print (f"desaprobadas: {asignaturasD}")
