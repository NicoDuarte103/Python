#MÉTODO CONSTRUCTOR Y ENCAPSULACIÓN DE ATRIBUTOS
class Vehículo(): 
	#Método constructor de la clase o estado inicial "de fábrica"
	def __init__(self):
		self.__marca = 'Ford'#atributos encapsulados en el __
		self.__modelo = 'Mondeo'#atributos encapsulados en el __
		self.año = 2010
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


V = Vehículo()
V.arrancar()
V.MostrarVehículo()
print('-'*50)
V.año=2020 #es válido, se puede porque año no está encapsulado(línea 7)
V.__modelo = 'Ranger' #no es válido No me da error pero no cambia porque está encapsulado
#V.modelo y V.marca no son accesibles desde afuera
V.MostrarVehículo()
print('_'*50)
V2 = Vehículo()
V2.MostrarVehículo()

		