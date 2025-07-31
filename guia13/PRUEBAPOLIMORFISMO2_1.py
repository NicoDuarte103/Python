from POLIMORFISMO2 import *

class Concesionaria():
    def __init__(self):
        self.unidades = []  # Lista para almacenar vehículos

    def coches(self):
        print('Para el coche, ingrese marca, modelo, año y ruedas\n')
        ma = input('Marca: ')
        mo = input('Modelo: ')
        an = input('Año: ')
        ru = int(input('Ruedas: '))
        return Vehículo(ma, mo, an, ru)

    def camioneta(self):
        print('Para la camioneta, ingrese marca, modelo, año, ruedas y carga\n')
        ma = input('Marca: ')
        mo = input('Modelo: ')
        an = input('Año: ')
        ru = int(input('Ruedas: '))
        ca = int(input('Carga: '))
        return Camioneta(ma, mo, an, ru, ca)

    def MiMoto(self):
        print('Para la moto, ingrese marca, modelo, año y ruedas\n')
        ma = input('Marca: ')
        mo = input('Modelo: ')
        an = input('Año: ')
        ru = int(input('Ruedas: '))
        return Moto(ma, mo, an, ru)

    def MiCuatri(self):
        print('Para el cuatriciclo, ingrese marca, modelo, año, ruedas y cilindrada\n')
        ma = input('Marca: ')
        mo = input('Modelo: ')
        an = input('Año: ')
        ru = int(input('Ruedas: '))
        ci = int(input('Cilindrada: '))
        return Cuatriciclo(ma, mo, an, ru, ci)

    def bicicletas(self):
        print('Para la bicicleta, ingrese marca, modelo, año, ruedas y rodado\n')
        ma = input('Marca: ')
        mo = input('Modelo: ')
        an = input('Año: ')
        ru = int(input('Ruedas: '))
        ro = int(input('Rodado: '))
        return BiciElectrica(ma, mo, an, ru, ro)

    def crearTipoVehiculo(self):
        while True:
            print('-' * 50)
            print('\nIndique tipo de Vehículo a incorporar: \n')
            print('\t1 - Coches')
            print('\t2 - Camioneta')
            print('\t3 - Motos')
            print('\t4 - Cuatriciclos')
            print('\t5 - Vehículos eléctricos')
            print('\t6 - Bicicletas eléctricas')
            print('\t7 - Ver Listado de Unidades')
            print('\t0 - Finalizar aplicación\n')
            print('-' * 50)
            try:
                aux = int(input('Ingrese una opción: '))
                if 0 <= aux <= 7:
                    return aux
                else:
                    print("Opción inválida. Intente nuevamente.")
            except ValueError:
                print("Ingrese un número válido.")

    def CrearUnidades(self):
        while True:
            tipoVeh = self.crearTipoVehiculo()
            
            if tipoVeh == 0:  # Finalizar programa
                print("Saliendo del programa...")
                break
            elif tipoVeh == 1:
                self.unidades.append(self.coches())
            elif tipoVeh == 2:
                self.unidades.append(self.camioneta())
            elif tipoVeh == 3:
                self.unidades.append(self.MiMoto())
            elif tipoVeh == 4:
                self.unidades.append(self.MiCuatri())
            elif tipoVeh == 6:
                self.unidades.append(self.bicicletas())
            elif tipoVeh == 7:
                self.mostrarUnidades()

    def mostrarUnidades(self):
        if not self.unidades:
            print("No hay vehículos registrados.")
            return

        print("\nLista de vehículos registrados:")
        for i, vehiculo in enumerate(self.unidades, start=1):
            print(f"\nVehículo {i}:")
            vehiculo.mostrarVehiculos()
        
        input('\nPulse una tecla para continuar...')

# Crear una instancia de Concesionaria y ejecutar el programa
if __name__ == "__main__":
    a = Concesionaria()
    a.CrearUnidades()


