#Primer ejemplo de funciones que devuelven valores
def dividir(dividendo,divisor):
	if divisor!=0:
		return dividendo/divisor
	else:
		print('Divisor es CERO')
		return 0
#------------------------------------------------------------
d1= float(input('Ingrese dividendo: '))
d2= float(input('Ingrese divisor: '))
print('*'*80)

d3= dividir(d1,d2)
if d3!=0:
	print('Resultado de dividir ',d1,'dividido',d2, 'es:',d3)
else:
	print('No se pudo ejecutar la operación...')

print('*'*80)
