'''Realizar un programa que permita cargar dos listas de 15 valores cada
una. Informar con un mensaje cuál de las dos listas tiene un valor
acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas
iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en
un algoritmo'''
lista1= 0
lista2 =0
valor1 =0
suma1=0
valor2 =0
suma2=0
while lista1<15:
    valor1 = int(input(("ingrese los valores de la lista 1: ")))
    suma1 =valor1+suma1
    lista1=lista1+1
while lista2<15:
    valor2 = int(input(("ingrese los valores de la lista 2: ")))
    suma2 =valor2+suma2
    lista2=lista2+1
if suma1>suma2:
    print ("la lista 1 tiene mayores valores acumulados")
    print("lista 1: ",suma1)
    print ("lista 2: ",suma2)
elif suma2>suma1:
    print ("la lista 2 tiene mayores valores acumulados")
    print("lista 1: ",suma1)
    print ("lista 2: ",suma2)
else:
    print ("las listas son iguales")
    print("lista 1: ",suma1)
    print ("lista 2: ",suma2)
    
