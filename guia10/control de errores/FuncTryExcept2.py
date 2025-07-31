#----------CONTROL DE DATOS(continuación)-------


def dividir2(op1,op2):
	try:
		return op1/op2
	except ZeroDivisionError:
		print('No se puede dividir por cero!! ')
		return "Operación Inválida."

while True:
	try:
		n1= int(input('Ingrese el primer valor: '))
		n2= int(input('Ingrese el segundo valor: '))
		break
	except ValueError:
		print("Tipo de datos incorrectos. Vuelva a ingresarlos.")

print("Resultado de la división1 es: ",dividir2(n1,n2))		