"""Son listas constantes, más rígidas y permiten menos métodos
   como extraer una porción de la tupla."""

miTupla = (12, 80, 12, "Juan", "Mar del Plata", 'La Plata')
print(miTupla[5]) #escribe lo de la linea 4,como vector,un solo elemento
print(' ')
print('*'*50)

miLista=list(miTupla) 
print(miLista) #escribe la tupla como lista
print(miTupla) #escribe la tupla como tupla
print(' ')
print('*'*50)

print("Mar del Plata"in miTupla) #muestra si ews verdadero
print('Pinamar' in miTupla) #muestra si es falso

print(' ')
print('*'*50)
#MÉTODO COUNT()
print("El 12 está: ", miTupla.count(12), "veces") #muestra la cantidad de veces queu n elemento esta en la tupla
print(' ')
print('*'*50)

#MÉTODO LEN()
print("La tupla tiene: ", len(miTupla),"elementos") #muestra la cantidad de elementos que contiene
print(' ')
print('*'*50)

#TUPLA UNITARIA
T1 = ("Pedro",)
print(T1)
print("T1 tiene", len(T1), 'elemento')
#La coma es obligatoria, de lo contrario tendrá 5 elementos.

T2 = ("Pedro")
print(T2)
print("T2 tiene", len(T2), 'elementos')
print(' ')
print('*'*50)

#DESEMPAQUETAR UNA TUPLA
frutas=("ananá", "banana", "naranja", "kiwi")
(blanco, amarillo, naranja, verde)= frutas
print(blanco)
print(amarillo)
print(naranja)
print(verde)
print(' ')
print('*'*50)

#USO DE *

frutas=("ananá", "banana", "naranja", "kiwi")
(blanco, amarillo, *naranja)= frutas
print(blanco)
print(amarillo)
print(naranja)
print(' ')
print('*'*50)

#LA TUPLA PUEDE NO TENER PARÉNTESIS!!
T2 = "Lunes", "Martes", "Miércoles"
print(T2)
dia1,dia2,dia3 = T2
print(dia2,"-",dia3,"-",dia1)
print(' ')
print('*'*50)

#NO SE PUEDE USAR APPEND NI INSERT
#T2.append("Jueves")
#T2.insert("Viernes")
print(' ')
print('*'*50)
