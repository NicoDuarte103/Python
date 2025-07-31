#ejercicio 1
'''def saludar(nombre):
        print(f"¡¡Buenos días {nombre}!!")

nombre_usuario = input("Por favor, ingrese su nombre: ")
saludar(nombre_usuario)
print('-'*50)
print( )'''

#EJERCICIO 2
'''print ("Programa que calcula el factorial")
numero = int(input("Introduzca el número: "))
factorial = 1
i = 1
while (i <= numero):
    factorial = factorial * i
    i = i + 1
print ("El factorial de " + str(numero) + " es " + str(factorial))

print('-'*50)
print( )'''

#EJERCICIO 3
'''def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    # Calcular el total de la factura aplicando el IVA
    total_factura = cantidad_sin_iva + (cantidad_sin_iva * porcentaje_iva / 100)
    return total_factura

cantidad = float(input("Ingrese la cantidad sin IVA: "))
porcentaje = input("Ingrese el porcentaje de IVA (presione Enter para usar el 21% por defecto): ")

# Convertir el porcentaje a número si se ingresó uno
if porcentaje:
    porcentaje = float(porcentaje)
    total = calcular_total_factura(cantidad, porcentaje)
else:
    total = calcular_total_factura(cantidad)

print(f"El total de la factura es: {total:.2f}")
print('-'*50)
print( )'''


#EJERCICIO 4
'''def areaCirculo(radio):
	pi= 3.14
	return (pi* radio**2)

print(areaCirculo(6))

def volumenCilindro(radio, alto):
	return areaCirculo(radio)*alto

print(volumenCilindro(10,5))'''

'''import math

# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

# Función para calcular el volumen de un cilindro usando la función anterior
def calcular_volumen_cilindro(radio, altura):
    area_base = calcular_area_circulo(radio)
    volumen = area_base * altura
    return volumen

# Ejemplo de uso
radio = float(input("Ingrese el radio del círculo: "))
altura = float(input("Ingrese la altura del cilindro: "))

area = calcular_area_circulo(radio)
volumen = calcular_volumen_cilindro(radio, altura)

print(f"El área del círculo es: {area:.2f}")
print(f"El volumen del cilindro es: {volumen:.2f}")

print('-'*50)
print( )'''

#EJERCICIO 5
def MaximoComunDivisor(num1, num2):
	resto = 0
	while(num2 > 0):
		resto = num2
		num2 = num1 % num2
		num1 = resto
	return num1

print(MaximoComunDivisor(24,36))

def MinimoComunMultiplo(num1, num2):
	if num1 > num2:
		mayor = num1
	else:
		mayor = num2
	while(mayor % num1 !=0) or (mayor % num2 !=0):
		mayor += 1
	return mayor

print(MinimoComunMultiplo(24,36))

#EJERCICIO 6
'''def ContarPalabras(texto):
	texto = texto.split()
	palabras = {}
	for i in texto:
		if i in palabras:
			palabras[i] += 1
		else:
			palabras[i] = 1
	return palabras

def MasRepetida(palabras):
	CantPalabraDicha = ''
	CantRepeticiones = 0
	for palabra, repetida in palabras.items():
		if repetida > CantRepeticiones:
			PalabraDicha = palabra
			CantRepeticiones = repetida
	return CantRepeticiones, PalabraDicha
	
texto = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(ContarPalabras(texto))
print(MasRepetida(ContarPalabras(texto)))'''

#EJERCICIO 7
'''def superposicion(lista1, lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False

lista1 = [2,4,6,8]
lista2 = [3,5,7,9]

print(superposicion(lista1, lista2))'''

#EJERCICIO 8
'''def GenerarNCaracteres(n, letra):
    return letra * n
print(GenerarNCaracteres(7,'x'))'''

#EJERCICIO 9
'''def procedimiento(lista):
    for numero in lista:
        print('*' * numero)

# Ejemplo de uso
lista_numeros = [4, 9, 7, 1, 3]
procedimiento(lista_numeros)'''