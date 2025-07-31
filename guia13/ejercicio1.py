

class agenda():

    def __init__(self):
         self.diccionario = {}
         self.detalle = {}
         self.contador = 1
  
    
    def cargar_contacto(self):
        
        nombre = input("Ingrese nombre de contacto: ")
        telefono = input("Ingrese telefono de contacto: ")
        email = input("Ingrese email de contacto: ")
        detalle = {"nombre":nombre,
                   "telefono":telefono,
                   "email":email} 
        self.diccionario[nombre]=detalle
    def mostrar_contacto(self):
        
        self.diccionario[]



contador = 0
selector = 2

print("1- Carga un contacto en la agenda")
print("2- Listado completo de la agenda")
print("3- Consulta ingresando el nombre de la persona")
print("4-modificacion de su telefono o email")
print("5- Finalizar programa")

cargacontacto=agenda()
cargacontacto.cargar_contacto()
mostrarcontacto=agenda()
mostrarcontacto.mostrar_contacto()


    
