'''Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos
tiene un promedio de edades mayor'''
estudiantesM= 0
estudiantesT = 0
estudiantesN = 0
contadorM = 0
contadorT = 0
contadorN = 0
estudiantesMsuma=0
estudiantesTsuma=0
estudiantesNsuma=0
promedioM = 0
promedioT = 0
promedioN = 0
for contadorM in range (1,6):
    print ("ingrese la edad del estudiante ",contadorM," : ",end=' ')
    estudiantesM = int (input (''))
    estudiantesMsuma=estudiantesMsuma+ estudiantesM
for contadorT in range (1,7):
    print ("ingrese la edad del estudiante ",contadorT," : ",end=' ')
    estudiantesT = int (input (''))
    estudiantesTsuma=estudiantesTsuma+ estudiantesT
for contadorN in range (1,12):
    print ("ingrese la edad del estudiante ",contadorN," : ",end=' ')
    estudiantesN = int (input (''))
    estudiantesNsuma=estudiantesNsuma+ estudiantesN

promedioM= estudiantesMsuma/contadorM
promedioT = estudiantesTsuma/contadorT
promedioN = estudiantesNsuma/contadorN
print ("estudiantes del turno mañana promedio: ",promedioM)
print ("estudiantes del turno tarde promedio: ",promedioT)
print ("estudiantes del turno noche promedio: ",promedioN)
if (promedioM > promedioT and promedioM > promedioN):
    print ("el turno mañana tiene el mayor promedio:",promedioM)
elif (promedioT>promedioM and promedioT>promedioN):
    print ("el turno tarde tiene el mayor promedio: ",promedioT)
elif (promedioN>promedioM and promedioN>promedioT):
    print ("el turno noche tiene el mayor promedio: ",promedioN)
else:
    if (promedioM == promedioT):
        print ("el turno mañana y tarde tienen el mismo promedio")
        print ("turno mañana: ",promedioM)
        print("turno tarde:",promedioT)
    if (promedioM == promedioN):
        print ("el turno mañana y noche tienen el mismo promedio")
        print ("turno mañana: ",promedioM)
        print("turno noche:",promedioN)
    if (promedioT== promedioN):
        print ("el turno tarde y noche tienen el mismo promedio")
        print ("turno tarde: ",promedioT)
        print("turno noche:",promedioN)