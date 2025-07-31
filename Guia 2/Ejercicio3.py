'''Calcular la hipotenusa de un triángulo rectángulo sabiendo que:
A= hipotenusa
B= cateto mayor que es igual a 3 veces el cateto menor'''

BM = float(input ("escriba el valor del cateto MENOR: "))

B=BM*3
hipotenusa= ((BM**2)+(B**2))**0.5
print (hipotenusa)
