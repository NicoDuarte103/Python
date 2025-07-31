''') Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares.
'''

negativos = 0
positivos = 0
multiplos15=0
acumuladopares=0


for contador in range (1, 11):
    print ("ingrese el valor numero ",contador," : ",end='')
    valor = int (input(" "))
    if valor < 0:
        negativos = negativos+1
    if  valor >0:
        positivos= positivos+1
    if (valor%15) == 0:
        multiplos15 = multiplos15+1
    if (valor%2) == 0:
        acumuladopares = acumuladopares+1
    
        
print("la cantidade de numeros positivos es: ",positivos)
print ("la cantidad de numeros negativos es: ",negativos)
print ("la cantidad de multiplos de 15 es: ",multiplos15)
print ("la cantidad de pares acumulados es: ",acumuladopares)
