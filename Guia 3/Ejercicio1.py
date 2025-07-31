'''1. Convertir kilómetros a millas
Escribir un programa para convertir una distancia en kilómetros en una
distancia en millas o viceversa. Realice la conversión sabiendo que
1km=0.6214 millas. Imprima un mensaje diciéndole al usuario cuáles son
las millas o los km correspondientes.'''

print ("seleccione que valor desea convertir: ")
print ("1- KM a MILLAS")
print ("2- MILLAS A KM")
condicion = float (input())
if condicion == 1:
    distanciaKM = float(input("escriba la distancia en kilometros: "))
    calculomillas = (distanciaKM*0.6214)/1
    print ("son",calculomillas,"millas")
elif condicion == 2:
    distanciamillas= float(input("escriba la distancia en millas: "))
    calculokm= (distanciamillas*1)/0.6214
    print ("son",calculokm,"kilometros" )
else:
    print("error")