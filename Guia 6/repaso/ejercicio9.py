lista = [5,4,3,2,1,6,45,3,6,6,6,6,6]

ingreso = int (input("ingrese un numero: "))
repeticion = 0
for contador in range (len(lista)):
    if lista[contador] == ingreso:
        repeticion = repeticion+1
print(f"el numero {ingreso} se repite {repeticion} veces")