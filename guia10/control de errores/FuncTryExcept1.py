#from Libreria.funciones import dividir

'''def dividir(op1,op2):
	try:
		return op1/op2
	except:
		print('No se puede dividir por cero!! ')
		return "Operación inválida"

n1 = int(input('Ingrese el primer número: '))
n2 = int(input('Ingrese el segundo número´: '))
print('El resultado de la división es: ', dividir(n1,n2))'''

#----------------------------------------------------------------

def dividir1(op1,op2):
	try:
		return op1/op2
	except ZeroDivisionError:
		print('No se puede dividir por cero!! ')
		return "Operación inválida."

n3 = int(input('Ingrese el primer número: '))
n4 = int(input('Ingrese el segundo número´: '))
print('El resultado de la división es: ', dividir1(n3,n4))