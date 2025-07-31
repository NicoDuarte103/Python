class Persona:

    def inicializar(self,nom):#self hace referencia al objeto del que estoy hablando
        self.nombre=nom

    def imprimir(self):
        print("Nombre",self.nombre)


# bloque principal

persona1=Persona()
persona1.inicializar("Rami")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Keila")
persona2.imprimir()
