midic = {
  "marca": "Ford",
  "modelo": "Ranger",
  "año": 2020
}
print(midic)
print(" ")

#Los valores duplicados sobrescribirán los valores existentes:
midic = {
  "marca": "Ford",
  "modelo": "Ranger",
  "año": 2020,
  "año": 2023
}
print(midic)
print("-"*30)
print(" ")

#Imprimir el tipo de datos de un diccionario:
midic = {
  "marca": "Ford",
  "modelo": "Ranger",
  "año": 2020,
  "año": 2023
}
print(type(midic))
print("-"*30)
print(" ")

#También es posible utilizar el 
#constructor dict() para crear un diccionario.

midic = dict(nombre = "Julia", edad = 36, pais= "Italia")
print(midic)
print("-"*30)
print(" ")

#Puede acceder a los elementos de un diccionario 
#consultando su nombre clave, entre corchetes:
midic = {
  "marca": "Ford",
  "modelo": "Ranger",
  "año": 2020
}
x=["modelo"]
print(x)
print(" ")
