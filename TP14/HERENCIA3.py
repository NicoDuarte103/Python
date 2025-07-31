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
		self.Willy = "La Moto está haciendo Willy"

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

#######################################################################
print('-'*50)
M = Moto('Yamaha','Tenere',2017,2)
M.acelera()
M.hacerWilly()
M.mostrarVehículo()
print('*'*50)
miCuatri = Cuatriciclo('Honda','Modelo III',2018,4)	
miCuatri.setCil(350) #Método propio de la clase cuatriciclo	
miCuatri.acelera() #Método heredado de la clase vehículo
miCuatri.hacerWilly()#Método heredado de la clase moto
miCuatri.mostrarVehículo()
print('-'*50)
print('-'*50)

