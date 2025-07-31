#MÉTODO CONSTRUCTOR CON PARÁMETRO
class Vehículo(object):
	"""MÉTODO CONSTRUCTOR DE LA CLASE O ESTADO INICIAL..."DE FÁBRICA" """
	def __init__(self, mar, mod, año):
		self.__marca = mar #atributo encapsulado con el __
		self.__modelo = mod
		self.año = año
		self.__estado = False

	def arrancar(self):
		self.__estado = True

	def parar(self):
		self.__estado = False

	def MostrarVehículo(self):
		print(self.__marca)
		print(self.__modelo)
		print(self.año)
		if self.__estado==True:
			print('Este vehículo está en marcha')
		else:
			print('Vehículo parado')
