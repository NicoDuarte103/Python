def factorial():
    contador = 0
    lista = []
    continuar= 0
    while contador == 0:
        print("ingrese salir para salir")
        numero = input ("ingrese un numero: ")
        rango = str(numero)
        if (rango == "salir"):
            contador = 1
            break
        numero = int(rango)
        potencia= 0
        contadorfor = 0
        digito1= 0
        digito2 = 0
        lista.clear()
       
        for contadorfor in range (len(rango)):
            potencia = potencia+1
            digito2= (numero%(10**potencia)-digito1)/10**contadorfor
            digito1= numero%(10**potencia)
            print (digito1)
            print (digito2)
            print ("potencia ",potencia)
            lista.append(digito2)
            print(lista)
            print ("-"*50)
    
    print(sum(lista))
factorial()
