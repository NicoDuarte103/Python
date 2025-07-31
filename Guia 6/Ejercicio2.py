
print ("escriba tamaño de lista: ")
tamaño= int (input (" "))
contador = 0


lista = [] #las listas se pueden definir vacias para agregar mas tarde elementos
for contador in range (0,tamaño):
  print ("ingrese valor: ")
  Valor= int (input (" "))
  lista.append(Valor) #este metodo agrega valores a la lista

print (lista)