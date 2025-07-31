
lista = []
tupla = (lista)
bucle = 0
valor = 0
repetidor = 0

contador = 0
while bucle == 0:
    valor = (input (" valor "))
    lista.append(valor)
    if valor == "-1":
        bucle = 1
buscador = input("ingrese el valor a buscar")
for contador in range (len(tupla)):
    
    if tupla[contador]==buscador:
        repetidor = repetidor+1
        encontrado = buscador
print(tupla)
print(f"el numero{buscador} se reptie {repetidor} veces")