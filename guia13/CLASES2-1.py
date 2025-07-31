#CLASES, DEFINICIONES
class Vehiculo():
	marca = 'Fiat'
	modelo = 'Toro'
	año = 2022
	estado = False
	disponible = False
#----------------------------------- 
	def arrancar(self):
		self.estado = True

	def parar(self):
		self.estado = False
#-----------------------------------------------
#-----------MÉTODO CON PARÁMETROS---------------
	def habilitar(self,dato):
		self.disponible = dato
#-----------------------------------------------
	def mostrarVehiculo(self):
		print('Marca: ',self.marca)
		print('Modelo: ',self.modelo)
		print('Año de fabricación: ',self.año)
		if self.estado==True:
			print('Este vehículo está en marcha')
		else:
			print('Vehículo parado')
		if self.disponible:
			print('Este vehículo está disponible en el salón de ventas')
		else:
			print('Este vehículo no está disponible a la venta')
	#----------------------------------------------------------------
print('-'*50)
V = Vehiculo()
V.arrancar()
aux = int(input('Ingrese 1 si el vehículo está disponible a la venta, 0 si no lo está: '))
print('-'*50)
V.habilitar(aux)
V.mostrarVehiculo()
print('-'*50)

aux = int(input('Ingrese 1 si el vehículo está disponible a la venta, 0 si no lo está: '))
print('-'*50)
V.habilitar(aux)
V.parar()
V.mostrarVehiculo()
print(' ')
print('-'*50)