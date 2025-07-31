frase = input ("escribe una frase: ") #se escribe la frase
lista_caracteres=list(frase) #la variable list 

contador = 0 
for contador in range (len(lista_caracteres)): #len se usa para hacer enteros la cantaidad de caracteres
    if contador !=0: #para que no imprima comas en cero
     print(",",end=" ")
    print (lista_caracteres[contador],end=" ")

print()
 