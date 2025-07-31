frase = input("ingrese frase: ")
lista_caracteres=list(frase) #la variable list individualiza los caracteres
contador = 0
for contador in range (0,len(frase)):
    print (lista_caracteres[contador],end=',')