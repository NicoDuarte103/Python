números=[3,6,9,12,15]
print(números)
for i in range(len(números)):
	números[i] = números[i] * 2
print(números)

print("-"*30)

meses=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print(meses[0]) # se muestra enero
print(meses[3]) # se muestra abril
print(meses[3:5]) # se muestra abril y mayo
print("-"*30)

lista=["Ana", 7, 9,6,6]
print("Nombre del alumno:")
print(lista[0])
promedio=(lista[1]+lista[2]+lista[3]+lista[4])//4
print("Promedio de sus cuatro notas:",promedio)
print()

promedio=(lista[1]+lista[2])//2
print("Promedio de sus dos notas:", promedio)
print()