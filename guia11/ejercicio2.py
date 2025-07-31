from io import *
archivo = open("guia11\misma carpeta\datos.txt","a")
contador = 0
for contador in range (0,2):
    ingreso = input("ingrese frase: \n")
    archivo.write(f"\n{ingreso}")
