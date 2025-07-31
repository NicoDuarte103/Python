from CLASES5 import*
print('-'*50)
op=1
listado = []
while(op):
	print('Ingrese Nombre, edad, altura y peso de la persona: ')
	nom=input('Ingrese Nombre: ')
	ed=int(input('Ingrese edad: '))
	alt=float(input('Ingrese altura: '))
	pes=float(input('Ingrese peso: '))
	p=Persona(ed,pes,alt,nom)
	listado.append(p)
	op=int(input('Continúa? -presione 0 para NO Y 1 para SI'))

print('----------------COMENZAMOS A MOSTRAR LISTADO-----------')
for i in listado:
		i.muestra()

print('_'*50)	