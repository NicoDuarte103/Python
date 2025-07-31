asignaturas = []
bucle = 0

while bucle == 0:
    ingreso = (input("ingrese nombre de asignatura: "))
    asignaturas.append (ingreso)
    if ingreso== "salida":
        bucle = 1
print (asignaturas)