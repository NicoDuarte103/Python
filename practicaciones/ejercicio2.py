class vehiculo():

    def __init__(self,marca,modelo,anio):
        
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

class carro(vehiculo):
    def __init__(self,marca,modelo,anio,combustible):
        super().__init__(marca,modelo,anio)
        self.combustible = combustible
    def __str__(self):
        return(f"marca: {self.marca} modelo: {self.modelo} año: {self.anio} combustible: {self.combustible}")
    
ejecucion = carro("toyota","teton","2003","nafta")
print(ejecucion)

