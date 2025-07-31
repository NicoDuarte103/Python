#Ejemplo de recorrido de una lista
#La forma más común de recorrer los elementos de una lista es con un bucle for.
#La sintaxis es la misma que para las cadenas:

L2=["lunes","martes","miercoles","jueves","viernes"]
for i in L2:
	if i[0]=='l' or i[0]=='v':
		print(i)

print('*'*50)
print( )

#Calculamos el promedio de una lista de números 
#ingresados por el usuario sin una lista

total = 0
contador = 0
while (True):
    aux = input('Ingresa un número: ')
    if aux == 'fin': break
    valor = float(aux)
    total = total + valor
    contador = contador + 1

promedio = total / contador
print('Promedio:', promedio)
print('-'*50)
print(' ')

#Cálculo del mismo promedio utilizando una lista
numlista = list()
while (True):
    aux = input('Ingresa un número: ')
    if aux == 'x': break
    valor = float(aux)
    numlista.append(valor)

promedio = sum(numlista) / len(numlista)
print('Promedio:', promedio)