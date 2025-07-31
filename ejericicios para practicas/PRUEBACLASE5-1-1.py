from CLASES5 import *
'''Utilizamos métodos getters y setters, atributos y
métodos encapsulados
instanciación de objetos de la clase persona.'''

print('-'*50)
p1 = Persona(30,70,1.89,"Fernando")
#print('Nombre de la persona: ',p.__nombre)...error__nombre es privado
#print(p1.__estado())...error no se puede acceder a un 
#método encapsulado

print('Nombre de la persona: ',p1.getNombre())
p1.muestra()
p1.caminar()
p1.setAltura(1.95)
p1.muestra()

print('-'*50)
p2=Persona(24,50,1.62,'Sofía')
p2.muestra()
p2.setNombre('Samantha')
p2.setAltura(1.65)
p2.muestra()

print('-'*50)

#------------------Menú-----------------------