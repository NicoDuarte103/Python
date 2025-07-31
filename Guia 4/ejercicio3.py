'''Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados
iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
b) Cantidad de triángulos de cada tipo.'''


bucle = 0
bucle2=0
equilatero = 0
isoceles = 0
escaleno = 0

while bucle==0:
    bucle2 =0
    while bucle2 ==0:
     lado1 = float (input ("ingrese valor de lado 1 : "))
     lado2 = float (input ("ingrese valor de lado 2 : "))
     lado3 = float (input ("ingrese valor de lado 3 : "))
     if (lado1 == lado2)and (lado1==lado3) and (lado2==lado3):
        print ("el triangulo es equilatero")
        equilatero = equilatero+1
     
     elif (lado1 == lado2) or (lado1==lado3) or (lado2==lado3):
      print ("el triangulo es isoceles")
      isoceles= isoceles+1
     else:
         print ("el triangulo es escaleno")
         escaleno = escaleno+1
     rotura = input("continuar? y/n:")
     if rotura == 'n':
      
      print("cantidad de triangulos equilateros: ",equilatero)
      print ("cantidad de triangulos isoceles: ",isoceles)
      print ("cantidad de triangulos escalenos: ",escaleno)
      print ("cerrando sesion...")
      bucle = 1
      bucle2 = 1
     else:
        bucle2=1
        

      



    