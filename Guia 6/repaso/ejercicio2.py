lista = []
contador=0
valor = 0
bucle=1
while bucle == 1:
   valor = int (input("ingrese valor"))
   print ("i")
   lista.append (valor)
   print (lista[contador])
   contador = contador+1
   if valor == 0:
    bucle = 0

for contador in range (0,contador):
    print (f"el valor de {contador} es: {lista[contador]}")