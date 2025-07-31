lista = []
contador = 0
valor = 0
for contador in range (0,10):
    valor = int (input("ingrese el valor: "))
    lista.append(valor)


print (f"lista desordenada: {lista}")
lista.sort()
print (f"lista menor a mayor: {lista}")
lista.reverse()
print (f"lista mayor a menor: {lista}")

