
contador25=0
lista = [0]*8 # se multiplica la lista por 8 para autoasignarla con cero
print (lista)
for contador in range(len(lista)):
    print ("ingrese el valor numero",contador," : ",end='')
    lista[contador] = int(input(" "))
    if (lista [contador] < 50 and lista[contador] > 25):
        contador25 = contador25+1 
print ("hay ",contador25," valores superior a 25 contador25")
print ("la lista es la siguiente post cambio: \n",lista)


