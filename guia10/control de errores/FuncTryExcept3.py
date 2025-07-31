#----OTROS EJEMPLOS DE EXCEPCIÓN DE ERRORES------


def dividir3():
	try:
		op1 = float(input("Ingrese el primer valor: "))
		op2 = float(input("Ingrese el segundo valor: "))
		print('El resultado de la división  es: '+str(op1/op2))

	except ValueError:
		print('Error en el tipo de valor ingresado. ')
	except ZeroDivisionError:
		print('No se puede dividir por cero!! ')
	except IOError:
		print("No se puede abrir el archivo. ")
	finally:#esto se ejecuta en caso que no hayan existido errores
		print('Fin de la operación.')

while True:
	dividir3() #invoco a la función