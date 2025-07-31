Contador = 0
lista = []
for contador in range (0,4):
    ganadores = input ("ingrese los ganadores de la loteria")
    lista.append (ganadores)

print (lista)
lista.sort()
print (lista)