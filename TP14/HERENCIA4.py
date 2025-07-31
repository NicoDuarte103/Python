#CLASES DEFINICIONES
class Vehículo():
	
	def __init__(self, marca,modelo,año,ruedas):
		self.__marca = marca
		self.__modelo = modelo
		self.__ruedas = ruedas
		self.__año = año
		self.estado = False
		self.acelerar = False
		self.frenar = False

	def setMarca(self,marca):
		self.__marca = marca

	def getMarca(self):
		return self.__marca

	def setModelo(self,modelo):
		self.__modelo = modelo

	def getModelo(self):
	 	return self.__modelo

	def setRuedas(self,ruedas):
	  	self.__ruedas = ruedas

	def getRueda(self):
	  	return self.__ruedas

	def setAño(self, año):
	  	self.año = año

	def getAño(self):
	  	return self.__año

	def arrancar(self):
	  	self.estado = True 

	def parar(self):
	  	self.estado = False

	def acelera(self):
	  		self.frenar=False
	  		self.acelerar=True

	def frena(self):
	  	self.frena=True
	  	self.acelera=False

	def mostrarVehículo(self):
	  	print('MARCA: ',self.getMarca())
	  	print('MODELO: ',self.getModelo())
	  	print('AÑO: ',self.getAño())
	  	if self.estado:
	  		print('Este vehículo está en marcha')
	  	else:
	  		print('Vehículo parado')
	  	if self.acelerar:
	  		print('El vehículo está acelerando')
	  	else:
	  		print('El vehículo está frenado')
##################################################################
class Camioneta(Vehículo):
	def cargar(self,Kg):
		self.peso = Kg
		if self.peso:
			return "La camioneta está cargada con ",self.peso,'Kg'
		else:
			return "La camioneta está vacía..."

##################################################################
class Moto(Vehículo): #HERENCIA SIMPLE
	Willy = "Anda normal"

	def hacerWilly(self):#MÉTODO PROPIO DE LA CLASE MOTO
		self.Willy = "El Vehículo está haciendo Willy"

	def mostrarVehículo(self):#SOBREESCRITURA DEL MÉTODO MUESTRA DEL PADRE(mismo nombre pero hace otra cosa)
		print('MARCA: ',self.getMarca())
		print('MODELO: ',self.getModelo())
		print('AÑO: ',self.getAño())
		if self.estado:
			print('Este vehículo está en marcha')
		else:
			print('Vehículo parado...')
		if self.acelerar:
			print('El vehículo está acelerando')
		else:
			print('El vehículo está frenado')
		print(self.Willy)

###################################################################
class Cuatriciclo(Moto):#HERENCIA EN CASCADA(de vehículo y de moto)
	cilindrada = 0
	def setCil(self,cilindrada):
		self.cilindrada = cilindrada
	def getCil(self):
		return self.cilindrada

	def mostrarVehículo(self):#sobreescritura del método muestra padre
		print('MARCA: ',self.getMarca())
		print('MODELO: ',self.getModelo())
		print('AÑO: ',self.getAño())
		print('CILINDRADA',self.getCil())
		if self.estado:
			print('Este vehículo está en marcha')
		else:
			print('Vehículo parado...')
		if self.acelerar:
			print('El vehículo está acelerando')
		else:
			print('El vehículo está frenado')
		print(self.Willy)

###################################################################
class Velectrico():#Vehiculos electricos-NO HEREDA DE NADIE
					#autonomia=1- Debería estar en otro archivo
					# es otra clase, tiene otro constructor
	def __init__(self):
		self.autonomia = 100 #suponemos que es en KM

	def getAutonomia(self):
		return self.autonomia

	def setAutonomia(self,autonomia):
		self.autonomia = autonomia

	def cargaBateria(self):
		self.cargando = True

##################################################
#CARACTERISTICA PROPIA DE PYTHON: HERENCIA MÚLTIPLE
class BiciElectrica(Vehículo,Velectrico):#HERENCIA MÚLTIPLE (hereda de dos clases distintas)
	rodado = 28
	def setRodado(self,rodado):
	 	self.rodado = rodado

	def getRodado(self):
	 	return self.rodado

#SIEMPRE HEREDA EL CONSTRUCTOR DE LA PRIMERA CLASE NOMBRADA
#se ejecuta primero el primero

######################################################################
print('#'*50)
MiBici = BiciElectrica('Curuchet','M450',2020,2)#CONSTRUCTOR HEREDADO DE CLASE VEHÍCULO
MiBici.setMarca('Shimano')#MÉTODO HEREDADO DE VEHÍCULO
MiBici.cargaBateria()#METODO HEREDADO DE VEHÍCULOS ELECTRICO
MiBici.setRodado(26)#MÉTODO PROPIO DE LA CLASE
MiBici.mostrarVehículo()#ver como mostrar bien...Faltan atributos de BiciElectrica
MiBici.setAutonomia(50)
print('Autonomia de mi bici: ',MiBici.getAutonomia())#También puedo sobreescribir
#el método MostrarVehículo después de la línea 138, en este ejemplo,obvio...
print('#'*50)
