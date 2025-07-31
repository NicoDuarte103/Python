#MOSTRAMOS UNA PROGRAMACION ESTRUCTURADA COMO EN C
from POLIMORFISMO2 import*

concesionaria = []
tipoVeh = 1
#----------------------MENÚ SELECCIONAR OPCIÓN------------------------
#Definimos una FUNCIÓN
def crearTipoVehiculo():
	aux = -1
	while (aux<0 or aux >6):
		print('-'*50)
		print('\tIndique tipo de vehículo a incorporar: \n')
		print('\t1 para coches (clase vehículo)\n')
		print('\t2 para camioneta\n')
		print('\t3 para motos\n')
		print('\t4 para cuatriciclos\n')
		print('\t5 para vehículos tipo coches eléctricos\n')
		print('\t6 para bicicletas con baterías\n')
		print('\t0 p finalizar\n')
		print('-'*50)
		aux=int(input('Ingrese una opción: '))
	return aux
	
#--------------Ciclo para crear los distintos tipos de vehículos----------
while (tipoVeh!=0):
	print('#'*50)
	#global concesionaria
	tipoVeh = crearTipoVehiculo()

	if (tipoVeh==1):#coche
		print('Ingrese marca, modelo, año y ruedas\n')
		ma = input('Marca:')
		mo = input('Modelo:')
		an = input('Año:')
		ru = int(input('Ruedas: '))
		MiCoche = Vehículo(ma,mo,an,ru)
		concesionaria.append(MiCoche)
	elif(tipoVeh==2): #camioneta
		print('Para camioneta, Ingrese marca, modelo, año, ruedas y carga\n')
		ma = input('Marca:')
		mo = input('Modelo:')
		an = int(input('Año:'))
		ru = int(input('Ruedas:'))
		ca = int(input('Carga:'))
		MiCamio = Camioneta(ma,mo,an,ru,ca)
		concesionaria.append(MiCamio)
	elif(tipoVeh==3): #moto
		print('Ingrese marca, modelo, año, ruedas y carga\n')
		ma = input('Marca:')
		mo = input('Modelo:')
		an = input('Año:')
		ru = int(input('Ruedas:'))
		MiMoto = Moto(ma,mo,an,ru)
		concesionaria.append(MiMoto)
	elif(tipoVeh==4): #cuatriciclo
		print('Ingrese marca, modelo, año, ruedas y cilindrada\n')
		ma = input('Marca:')
		mo = input('Modelo:')
		an = input('Año:')
		ru = int(input('Ruedas: '))
		ci = int(input('Cilindradas:'))
		MiCuatri = Cuatriciclo(ma,mo,an,ru,ci)
		concesionaria.append(MiCuatri)
		
	elif(tipoVeh==6): #bicicletas
		print('Ingrese marca, modelo, año, ruedas y rodado\n')
		ma = input('Marca:')
		mo = input('Modelo:')
		an = input('Año: ')
		ru = int(input('Ruedas:'))
		ro = int(input('Rodado: '))
		MiBici = BiciElectrica(ma,mo,an,ru,ro)
		concesionaria.append(MiBici)

#-----------MUESTRA DE LA LISTA DE OBJETOS CON POLIMORFISMO------------


for i in concesionaria:
	print('-'*50)
	i.mostrarVehículo()

