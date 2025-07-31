#MÉTODOS GETTERS Y SETTERS (poner y sacar;get:traer y set para modificar )
class Persona():
#atributos
	def __init__(self,edad, peso, altura, nombre,):
		self.__edad = edad
		self.__peso = peso
		self.__altura = altura
		self.__nombre = nombre
		self.camina = False
		self.lee = False
#--------------------------------------------------------------
#MÉTODOS
	def caminar(self):
		print('La persona cambia de posición ')
		self.camina = True

	def parar(self):
		print('La persona no cambia de posición ')
		self.camina = False

	def leer(self):
		self.lee =True

	def noLeer(self):
		self.lee = False

	def __estado(self):
		if (self.camina==True):
			if self.lee:
				return 'está caminando y leyendo...'
			else:
				return 'está caminando y sin leer...'
		else:
			if self.lee:
				return 'está parada y leyendo...'
			else:
				return 'está parada y sin leer...'
#--------------------------GETTERS-------------------------------
	def getNombre(self):
		return self.__nombre

	def getAltura(self):
	 	return self.__altura

	def getPeso(self):
		return self.__peso

	def getEdad(self):
		return self.__edad

#-----------------SETTERS------------------------

	def setNombre(self, nombre):
		self.__nombre = nombre
		
	def setAltura(self, altura):
		self.__altura = altura

	def setPeso(self, peso):
		self.__peso = peso

	def setEdad(self, edad):
		self.__edad = edad

#--------------MUESTRA DE UNA PERSONA------------------
	def muestra(self):
		print('-----------------------')
		print('Nombre: ',self.__nombre)
		print('Edad: ',self.__edad)
		print('Altura: ',self.__altura)
		print('Peso: ',self.__peso)
		print(self.__estado())#acceso al método encapsulado 
							  #desde el interior del objeto
		print('---------------------------------------------')

#-----------INSTANCIACIÓN DE OBJETOS-----------------
#------EJECUCIÓN/INVOCACIÓN GETTERS Y SETTERS--------