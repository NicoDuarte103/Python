'''Calcule un programa que al ingresar un número entre 1 y 4 muestre
las estaciones del año (1= invierno; 2= otoño; 3= primavera; 4 = verano)'''

numero=int(input(" Seleccione estacion: \n 1= invierno \n 2= otoño \n 3= primavera \n 4= verano \n ingrese un numero: "))
if numero==1:
    print("Es invierno")
elif numero == 2:
    print ("Es otoño")
elif numero == 3:
    print ("Es primavera")
elif numero == 4:
    print ("Es verano")
else:
    print ("error")