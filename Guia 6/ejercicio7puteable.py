lista1 =[]
lista2 = []
multiplicacion= 0
tamaño = int (input("escribe la tabla de que numero quieres ver: "))
maximo = int (input("escribe el valor maximo a multiplicar: "))

contador = 0
for contador in range (0,maximo+1): #definis las listas con append con un contador,usas +1 para que recorra todos los numeros

    lista1.append(contador)
    lista2.append(contador)
for contador in range (0,maximo+1):
    print(lista1[contador] * lista2[tamaño]) #multiplica las listas ya definidas

#queda pendiente hacer que 10*12 exista


    
    
     