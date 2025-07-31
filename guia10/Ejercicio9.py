def procedimiento(numero):
    print (numero)
    contador = 0
    resultado = "*"
    for contador in range(len(numero)):
        print("*"*numero[contador])

contador = 0
numero = [4,9,7]
procedimiento(numero)