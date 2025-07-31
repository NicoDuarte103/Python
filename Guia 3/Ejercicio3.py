'''Hacer un programa que permita saber si un año es bisiesto'''
año = int(input("Ingrese año: "))
contador = 0
if año%4 == 0:
    print ("Es año bisiesto")
else:
     print ("No es año bisiesto")
