
lista= []
contador = 0
valor = 0
suma = 0
for contador in range (0,5):
    print ("cargar los valores de la lista: ")
    valor = float (input(" "))
    lista.append (valor) 
    print (lista[0])

suma = sum (lista)
suma = suma/5
print("el promedio es: ",suma)
if suma > 1.70 and suma > 1.81:
    print ("la altura de hombres esta dentro del promedio")
if suma > 1.40 and suma < 1.65:
    print ("la altura de mujeres esta dentro del promedio")
else:
    print ("la altura esta fuera del promedio")


