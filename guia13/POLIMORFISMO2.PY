
class Vehículo():
    def __init__(self,ma,mo,an,ru):
        
        self.marca = ma
        self.modelo = mo
        self.anio = an
        self.rueda = ru
        self.listita = []
        self.listita.append(self.marca)
        self.listita.append(self.modelo)
        self.listita.append(self.anio)
        self.listita.append(self.rueda)

        
    def __str__(self):
        return f"Vehiculo(MA: {self.marca}, MO: {self.modelo},AN: {self.anio},ru{self.rueda})"    
   
    def mostrarVehiculos(self):
        print(self.listita)


       
       

class Camioneta():
    def __init__(self,ma,mo,an,ru,ca):
        print("estoy en clase camioneta")


class Moto():
    def __init__(self,ma,mo,an,ru):
        print("estoy en clase moto")


class Cuatriciclo():
    def __init__(self,ma,mo,an,ru,ci):
        print("estoy en clase cuatriciclo")


class BiciElectrica():
    def __init__(self,ma,mo,an,ru,ro):
        print("estoy en clase bici electrica")


