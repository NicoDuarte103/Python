class figura():
    def __init__(self):
       self.resultado = 0
    def area(self):
        self.resultado = "asignar"
        print(self.resultado)

class circulo(figura):
    def __init__(self,radio):
        super().area()
        self.radio = radio**2 
        self.pi = 3.14
    def area(self):
        self.resultado2 = self.radio*self.pi
        print(self.resultado2)
class rectangulo(figura):
    def __init__(self,base,altura):
        self.base = base
        self.altura= altura
    def area(self):
        self.resultado = self.base*self.altura;
        print(self.resultado)

ejecucion1= figura()
ejecucion2= circulo(1)
ejecucion3 = rectangulo(2,2)

ejecucion1.area();
ejecucion2.area();
ejecucion3.area();