#Primer ejemplo de funciones

def sumar():
	n1=input('Ingrese un primer número a sumar: ')
	n2=input('Ingrese el segundo número a sumar:')
	print('La suma de',n1,'más',n2,'es',n1+n2)
	#esto concatena n1  y n2
	print('La suma de',n1,'más',n2,'es:',int(n1)+int(n2))
	#esto realiza una suma algebraica

#-------------------------------------------------------
print('*'*80)
sumar()
print('*'*80)

def sumar():
	n1=int(input('Ingrese un primer número a sumar: '))
	n2=int(input('Ingrese el segundo número a sumar:'))
	suma= n1+n2
	print('La suma entre n1 y n2 es: ',suma)

print('*'*80)
sumar()
print('*'*80)
#Segundo ejemplo de funciones con parámetros


def multiplicar(p1,p2):#parámetros separados por comas-
	print('El resultado de multiplicar es: ',p1*p2)
print('*'*50)
multiplicar(10,3)#parámetros literales

#respetar cantidad y orden de los parámetros
a1=float(input('Ingrese el primer factor para multiplicar: '))
a2=int(input('Ingrese el segundo factor para multiplicar: '))
print('*'*80)

multiplicar(a1,a2)
print('*'*80)


