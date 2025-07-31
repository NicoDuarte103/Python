class Persona():
	#atributos
	nombre = "Pedro"
	edad = 20
	peso = 60
	altura = 1.75
	camina = False
	lee = True
#-------------------------------------------------
#Métodos
	def caminar(self):
		#print("La persona cambia de posición")
		self.camina = True

	def parar(self):
		#print('La peronsa no cambia de posición')
		self.camina= False

	def leer(self):
		self.lee= True

	def noleer(self):
		self.lee= False
#-------------------------------------------------

	def estado(self):
		if (self.camina == 	True):
			if self.lee:
				return ' caminando y leyendo...'
			else:
				return ' caminando y sin leer...'
		else:
			if self.lee:
				return ' parado y leyendo...'
			else:
				return ' parado y sin leer...'

#-------------Instaciación O declaración de objetos-
#Instanciar,en este caso sería declarar una variable de tipo persona------------
#---------Ejecución/invocación de objetos---------

print('-'*50)

p=Persona()
#EJECUTO DOS ATRIBUTOS DE LA VARIABLE p
print('Nombre de la Persona: ', p.nombre)#donde 'p' es la persona '.nombre' que es su atributo
print('Altura de la Persona: ', p.altura)

#EJECUTO DOS MÉTODOS INSTANCIADOS EN LA VARIABLE p
p.leer()
p.caminar()
print( p.nombre, 'está ', p.estado())
print('-'*50)
p.parar()
#p.noleer()
print('La persona de nombre', p.nombre, 'está ', p.estado())
print('-'*50)
#----------Mas objetos de la misma clase----------
#INSTANCIO OTRA PERSONA- EN ESTE CASO TIENE LOS MISMOS ATRIBUTOS-
p1=Persona()
print( p1.nombre, 'esta ', p1.estado())
#-------------------------------------------------