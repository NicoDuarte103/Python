#Confeccionar una clase que permita carga el nombre y la edad de una persona. 
#Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)

class Persona():

    def inicializar(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def imprimir(self):
        print("Nombre",self.nombre)
        print("Edad",self.edad)

    def mayor_edad(self):
        if self.edad>=18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")


# bloque principal

persona1=Persona()
persona1.inicializar("Rami",18)
persona1.imprimir()
persona1.mayor_edad()

print('-'*30)
print( )

#EJEMPLO 2

#Desarrollar un programa que cargue los lados de un triángulo e implemente 
#los siguientes métodos: inicializar los atributos, imprimir el valor del 
#lado mayor y otro método que muestre si es equilátero o no. 
#El nombre de la clase llamarla Triangulo.

class Triangulo:

    def inicializar(self):
        self.lado1=int(input("Ingrese primer lado:"))
        self.lado2=int(input("Ingrese segundo lado:"))
        self.lado3=int(input("Ingrese tercer lado:"))

    def imprimir(self):
        print("Valores de los lados del triangulo")
        print("Lado 1",self.lado1)
        print("Lado 2",self.lado2)
        print("Lado 3",self.lado3)

    def lado_mayor(self):
        print("Lado mayor")
        if self.lado1>self.lado2 and self.lado1>self.lado3:
            print(self.lado1)
        else:
            if self.lado2>self.lado3:
                print(self.lado2)
            else:
                print(self.lado3)

    def es_equilatero(self):
        if self.lado1==self.lado2 and self.lado1==self.lado3:
            print("El triangulo es equilatero")
        else:
            print("El triangulo no es equilatero")


# bloque principal

triangulo1=Triangulo()
triangulo1.inicializar()
triangulo1.imprimir()
triangulo1.lado_mayor()
triangulo1.es_equilatero()