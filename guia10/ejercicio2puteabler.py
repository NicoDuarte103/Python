def factorial():
    numero = 0
    numeroaux=0
    contador = 0
    bucle = 0
    buclemulti= 0
    lista= []
    multiplicador = 10
    for contador in range (0,1):
        numero= int (input("ingrese numero "))
        if numero < 100:
            for contador in range(0,1):
                digito = numero%multiplicador
                digito2= (numero-digito)/10
                multiplicador =multiplicador*10
                lista.append(digito)
                lista.append(digito2)
                print ("hol")
        else:
            for contador in range(1,4):
                
                digito = numero%10**contador
                digito2= digito -10
                auxdigito= digito2
                
                print("multiplciador: ",multiplicador)
                print ("digito: ",digito)
                print ("digito 2: ",digito2)
                print ("auzdigito : ",auxdigito)
                print("-"*100)
                if contador == 0:
                    lista.append(digito)
                    print ("hola")
                else:
                    lista.append(digito2)
        
    print( lista)
    

factorial()