'''2. Leer el nombre y los dos apellidos de una persona (en tres cadenas de
caracteres diferentes) y unirlo en una única cadena. Luego muestre:
a) La cadena resultante
b) La cantidad de caracteres resultante
c) Convierta todo su contenido a mayúsculas y minúsculas
d) Verifique si la cadena “Fernández” se encuentra en el texto
e) Muestre en Mayúsculas la primera letra de cada palabra'''



nombre = (input("ingrese su nombre: "))
apellido1 = (input("ingrese su primer apellido: "))
Apellido2 = (input("ingrese su segundo apellido: "))
contenido = nombre + " " + apellido1 + " " + Apellido2
verificacion_cadena = contenido.split()
print ("PUNTO A ")
print (f'{nombre} {apellido1} {Apellido2}')
print (nombre,apellido1,Apellido2)
print ("PUNTO B la cantidad de caracteres es: ",end='')
print (len(nombre+apellido1+Apellido2))
print ("PUNTO C conversion de mayusculas a minusculas: ")
print (contenido.lower())
print ("PUNTO C conversion de minusculas a mayusculas: ")
print (contenido.upper())
print ("punto D")
if 'Fernandez' in contenido:
    print ("la palabra 'Fernandez' esta en la cadena")
else:
    print ("la palabra 'Fernandez' no esta en la cadena")
print ("Punto E: muestre en mayusculas la primera letra de cada palabra: ")
print (contenido.title())