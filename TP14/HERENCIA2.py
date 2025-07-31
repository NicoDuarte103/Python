#CLASES DEFINICIONES
#TODOS LOS ATRIBUTOS ENCAPSULADOS "DEBEN" TENER SUS CORRESPONDIENTES GETTERS Y SETTERS
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
print('-'*50)
miCoche = Vehículo('Fiat','Siena',2017,4)
miCoche.setAño(2015)
miCoche.mostrarVehículo()

print('-'*50)
M = Moto('Yamaha','Tenere',2017,2)
M.acelera()
M.hacerWilly()
M.mostrarVehículo()
print('*'*50)
		
miCamioneta = Camioneta('Toyota','Hilux',2021,4)	
miCamioneta.mostrarVehículo()	
miCamioneta.cargar(600) #COMO HAGO PARA VER LA CARGA??Haciendo un print de miCamioneta.cargar
print(miCamioneta.cargar(600))
miCamioneta.mostrarVehículo()
print('-'*50)

Concesionaria =[]
Concesionaria.append(M)
Concesionaria.append(miCamioneta)
Concesionaria.append(miCoche)

print('Mostramos la lista de vehículos\n')
'''Concesionaria[0].mostrarVehículo()
print('-'*50)
Concesionaria[1].mostrarVehículo()
print('-'*50)
Concesionaria[2].mostrarVehículo()
print('-'*50)
#LO CORRECTO SERÍA MOSTRARLO EN UN CICLO'''
for i in Concesionaria:
	i.mostrarVehículo()
	print('-'*50)


	  	