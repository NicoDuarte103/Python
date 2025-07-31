'''Una planta que fabrica perfiles de hierro posee un lote de n piezas.
Confeccionar un programa que pida ingresar por teclado la cantidad de
piezas a procesar y luego ingrese la longitud de cada perfil; sabiendo
que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30
son aptas. Imprimir por pantalla la cantidad de piezas aptas que hay en
el lote'''

n=int (input ("seleccione la cantidad de piezas a procesar"))
longitud =float (input ("ingrese la longitud del perfil"))
m = n+1
aptas = 0
bucle = 0
while in range (0,n):
    if (longitud >= 1.20 and longitud <= 1.30):
        print ("La pieza es apta")
        aptas = aptas+1
print("cantidad de piezas aptas: ",aptas)
print ("cantidad de piezas no aptas: ",n - aptas)