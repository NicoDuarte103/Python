lista = "abcdefghijklmnñopqrstuvwxyz"
listado = list(lista)
contador = 0
borrador = 0
for contador in range (len(listado)):
    if contador%3 == 0:
        listado.pop (contador-borrador)
        borrador = borrador+1


      
    
print (listado)