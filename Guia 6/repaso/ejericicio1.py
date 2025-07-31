'''Definir por asignación una lista con 8 valores enteros menores a 50. Contar cuantos de dichos 
valores son superiores a 25.'''


lista= [0]*8
contador = 0
valor = 0
for contador in range (0,8):
    lista[contador]= int(input ("ingresa el valor: "))
    if lista[contador]< 50 and lista [contador]>25:
        valor = valor+1
    else:
        print ("error numero fuera de rango")
    

print (f"la cantidad de numeros mayores a 25 son:{valor}")
for valor in range (0,valor):
    print (lista[valor])