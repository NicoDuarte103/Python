

class Vehículo():

	def __init__(self,ma,mo,an,ru):
		print("hola soy vehiculo")
		self.marca = ma;
		self.modelo = mo;
		self.anio = an;
		self.ruedas = ru;


	def mostrarVehiculos(self,cantidad):
		
		print(f"muestro el vehiculo {cantidad}")
		print(self.marca)
		print(self.modelo)
		print(self.anio)
		print(self.ruedas)

		

class Camioneta():

	def __init__(self,ma,mo,an,ru,ca):
		print("hola soy camioneta")

class Moto():

	def __init__(self,ma,mo,an,ru):
		print("hola soy moto")
class Cuatriciclo():

	def __init__(self,ma,mo,an,ru,ci):
		print("hola soy cuatri")

class BiciElectrica():

	def __init__(self,ma,mo,an,ru,ro):
		print("hola soy bici electrica")
class mostrarVehiculos():

	def __init__(self,ma,mo,an,ru,ro):
		print("muestro unidades")