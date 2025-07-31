#CLASES DEFINICIONES--cada clase debería ir en una archivo diferente--
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
class Camioneta(Vehículo):#herencia simple

	def __init__(self,marca,modelo,año,ruedas,peso):
		super().__init__(marca,modelo,año,ruedas)#reutilización constructor
		self.peso = peso
#DESDE EL CONSTRUCTOR DEL HIJO INVOCAMOS AL CONSTRUCTOR	DEL PADRE Y PASAMO LOS PARAMETRO DE ESTE
	def cargar(self,Kg):
		self.peso = Kg
		if self.peso:
			return "La camioneta está cargada con ",self.peso,'Kg'
		else:
			return "La camioneta está vacía..."


	#################################################################33
class Moto(Vehículo):#herencia

	def __init__(self,marca,modelo,año,ruedas):
		super()._init__(marca,modelo,año,ruedas)#reutilización constructor
		self.Willy = ""

	def hacerWilly(self):#sobreescritura del método muestra
		self.Willy = "El vehículo está haciendo Willy"

	def mostrarVehículo(self):#sobreescritura del método muestra del padre
		super().mostrarVehículo()#reutilización de mostrarvehiculo
		print(self.Willy)
		#NO TENEMOS QUE HACER print de 'get.estado', 'get.rueda', etc,
		#Sólo invocamos al 'mostrarVehiculo' del padre y hacemos el print de esta clase
##########################################################################
class Cuatriciclo(Moto):#herencia en cascada(de vehículo a moto)

	def __init__(self,marca,modelo,año,ruedas,cilindrada):
		super().__init__(marca,modelo,año,ruedas)#reutilización constructor
		self.cilindrada = cilindrada
		self.Willy = ""

	def setCil(self,cilindrada):
		self.cilindrada = cilindrada

	def getCil(self):
		return self.cilindrada

	def mostrarVehículo(self):#sobreescritura del método muestra del padre
		super().mostrarVehículo()#reutilizacion muestravehiculo
		print(self.Willy)

######################################################################
class Velectrico():#NO HEREDA DE NADIE
	autonomia = 1
	def __init__(self):
		self.autonomia = 100

	def getAutonomia(self):
		return self.autonomia

	def setAutonomia(self,autonimía):
		self.autonomia = autonimía

	def cargaBateria(self):
		self.cargando = True

#############################################################
class BiciElectrica(Vehículo,Velectrico):#HERENCIA MÚLTIPLE. Hereda de clases distintas
#ejecutamos el constructor de vehiculo que es el que escribimos primero	
	def __init__(self,marca,modelo,año,ruedas,rodado):
		super().__init__(marca,modelo,año,ruedas)#constructor de vehiculo
		self.rodado = rodado

	def setRodado(self,rodado):
		self.rodado = rodado

	def getRodado(self):
		return self.rodado

		def mostrarVehículo(self):#sobreescritura del método muestra del padre
			super().mostrarVehículo()
			print('RODADO: ',self.rodado)
			print('AUTONOMIA: ',self.getAutonomia())

	####################################################################

