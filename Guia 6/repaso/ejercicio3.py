
lista = []
valor = 0
promedion = 0
promedioa = 0
promediob= 0
for contador in range (0,5):
    alturas = float(input("ingrese alturas: "))
    lista.append(alturas)
    print (lista[contador])
    if lista[contador] < 1.80 and lista[contador] > 1.65:
        promedion = promedion+1
    if lista[contador] <1.65:
        promediob = promediob+1
    if lista[contador]> 1.80:
        promedioa=promedioa+1


resultado = sum (lista)
resultado = resultado/5
    
print (f"el resultado del promedio es: {resultado}")
print (f"la cantidad de gente dentro del promedio es {promedion}")
print (f"la cantidad de gente arriba del promedio es {promedioa}")
print (f"la cantidad de gente abajo del promedio es {promediob}")