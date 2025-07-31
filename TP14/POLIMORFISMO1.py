class Coche():
	def desplazamiento(self):
		print("Ando en 4 Ruedas")


class Moto():
	def desplazamiento(self):
		print("Ando en 2 Ruedas")


class Camión():
	def desplazamiento(self):
		print("Ando en 10 Ruedas")

'''MiVehiculo1 = Moto()
MiVehiculo1.desplazamiento()
MiVehiculo2 = Coche()
MiVehiculo2.desplazamiento()
MiVehiculo3 = Camión()
MiVehiculo3.desplazamiento()'''	

#FUNCIÓN QUE RECIBE UN OBJETO Y EJECUTA UN MÉTODO
def movimientoVehículo(vehículo):#Se reemplaza por el objeto con el que sea llamado
	vehículo.desplazamiento()

#NO PUEDO GARANTIZAR QUE MÉTODO DE QUE CLASE ESTOY EJECUTANDO
#OJO!!NO ES NECESARIO INDICAR DE QUE TIPO ES MiVehículo
#MiVehïculo PODRÍA SER DE CUALQUIERA DE LAS 3 CLASES

MiVehiculo1 = Moto()

movimientoVehículo(MiVehiculo1) 	

MiVehiculo = Camión()

movimientoVehículo(MiVehiculo)