numero = int (input("escribe un numero"))
lista = []
lista2= []
contador =0
tamaño = int (input(" "))

for contador in range (0,10):
    lista.append(contador)
    lista2.append(contador)
for contador in range (0,10):
      print(lista[contador] * lista2[numero]) #multiplica las listas ya definidas
