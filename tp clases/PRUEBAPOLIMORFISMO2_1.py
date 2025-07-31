from POLIMORFISMO2 import*

class Concesionaria():
	def __init__(self):
		pass

	def coches(self):
		print('Para el coche, Ingrese marca, modelo, año y ruedas\n')
		ma = input('Marca:')
		mo = input('Modelo:')
		an = input('Año:')
		ru = int(input('Ruedas:'))
		MiCoche = Vehículo(ma,mo,an,ru)
		return MiCoche

	def camioneta(self):
		print('Para el camioneta, Ingrese marca, modelo, año, ruedas y carga\n')
		ma = input('Marca:')
		mo = input('Modelo:')
		an = input('Año:')
		ru = int(input('Ruedas:'))
		ca = int(input('Carga:'))
		MiCamio = Camioneta(ma,mo,an,ru,ca)
		return MiCamio

	def MiMoto(self):
		print('Para la moto, Ingrese marca, modelo, año y ruedas\n')
		ma = input('Marca:')
		mo = input('Modelo:')
		an = input('Año:')
		ru = int(input('Ruedas:'))
		MiMoto = Moto(ma,mo,an,ru)
		return MiMoto

	def MiCuatri(self):
		print('Para el cuatriciclo, Ingrese marca, modelo, año, ruedas y cilindrada\n')
		ma = input('Marca:')
		mo = input('Modelo:')
		an = input('Año:')
		ru = int(input('Ruedas: '))
		ci = int(input('Cilindrada:'))
		MiCuatri = Cuatriciclo(ma,mo,an,ru,ci)	
		return MiCuatri

	def bicicletas(self):
		print('Para la bicicleta, Ingrese marca, modelo, año, ruedas y rodado')
		ma = input('Marca:')
		mo = input('Modelo:')
		an = input('Año:')
		ru = int(input('Ruedas:'))
		ro = int(input('Rodado:'))
		MiBici = BiciElectrica (ma,mo,an,ru,ro)	
		return MiBici
#----------------------MENÚ DE VEHÍCULOS-----------------
	def crearTipoVehiculo(self):
		aux = 10
		while (aux < 0 or aux >7):
			print('-'*50)
			print('\nIndique tipo de Vehículo a incorporar: \n')
			print('\t1 para coches (clase vehículo)\n')
			print('\t2 para camioneta\n')
			print('\t3 para motos\n')
			print('\t4 para cuatriciclos\n')
			print('\t5 para vehículos tipo coches eléctricos\n')
			print('\t6 para bicicletas con baterías\n')
			print('\t7 para Ver Listado de Unidades\n\n')
			print('\t0 p finalizar aplicación\n')
			print('-'*50)
			aux=int(input('Ingrese una opción: '))
		return aux
#----------------CICLO PARA CREAR LOS DISTINTOS TIPOS DE VEHÍCULOS----
	def CrearUnidades(self):
		unidades = []
		tipoVeh = 1
		while(tipoVeh!=-1):
			print('#'*50)
			tipoVeh = self.crearTipoVehiculo()

			if (tipoVeh ==1):#coches
				unidades.append(self.coches())
			elif(tipoVeh ==2):#camioneta
				unidades.append(self.camionetas())
			elif(tipoVeh ==3):#motos
				unidades.append(self.Motos())
			elif(tipoVeh ==4):#cuatriciclo
				unidades.append(self.cuatriciclos())
			elif(tipoVeh ==6):#bicicletas
				unidades.append(self.bicicletas())
			elif(tipoVeh ==7):
				self.mostrarUnidades(unidades)

#------------MUESTRA DE UNIDADES DISPONIBLES--------------------
	def mostrarUnidades(self,unid):
		for i in unid:
			print('-'*50)
			i.mostrarVehiculos()
			print('#'*50)
		c = input('Pulse una tecla para continuar')

#--------------------------------------------------------------

a=Concesionaria()
a.CrearUnidades()		
#ver en el archivo HERENCIA5

