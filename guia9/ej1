"""La definición se hace con {llaves}
Diccionarios pares de clave - valor. No tienen orden, a cada valor
se le asigna una clave
Similares a Tuplas y Listas"""

a ={
	'Nombre':"Luis",
	'Nombre2': "Hernán",
	"Apellido": 'Barci',
	"Apodo": "El doc"
}

b={
	"Latitud": '22 23 13',
	"Longitud": '00 00 00'

}
print('-'*50)
print('')
print(a)
print('*'*50)
print(' ')
print(b)
print('*'*50)
print(' ')

#EJEMPLO
capitales ={"Alemania":"Berlín","Argentina":"Buenos Aires", "Francia":"Paris", "Australia":"Sydney"}
print(capitales)
print("_"*50)

print("Capital de Argentina:", capitales["Argentina"])
print('Capital de Australia', capitales["Australia"])

print('*'*50)
print(' ')
 #OPERACIONES: AGREGAR
capitales["Uruguay"]= "Montevideos"
print(capitales)
print('*'*50)
print(' ')

#MODIFICAR-Se sobreescribe 
capitales["Uruguay"]= "Montevideo"
print(capitales)
print('*'*50)
print(' ')

capitales = {"Alemania":"Berlín",
			 "Argentina":"Buenos Aires", 
			 "Francia":"Paris", 
			 "Australia":"Sydney",
			 "Italia":"Roma"}
print('*'*50)
print(' ')

print("Error!! Sydney no es la capital de Australia")
print("Modificamos el valor")

capitales["Australia"]= "Canberra"
print(capitales)
print('*'*50)
print(' ')

#ELIMINAR UN ELEMENTO DEL DICCIONARIO
del capitales["Alemania"]
print("Capitales sin Alemania: ",capitales)
print('*'*50)
print(' ')

#UTILIZANDO DISTINTOS TIPOS
curso = { 1:"Fabi",
		      2:"Brenda", }

print('Las profes de Informática son: ', curso)
print('*'*50)
print(' ')

equipo = {"Los mejores":"Progra",
		 1:"Santi.B",
		 2:"Rami",
		 3:"Nahuel",
		 4:"Nico",
		 5:"Marcos",
		 6:"Santi.V",
		 7:"Alan"}
print("Jugadores del equipo: ", equipo)
	

#UTILIZANDO UNA TUPLA
posiciones = ("Arquero(1)", "Defensor lat izquierdo (3)", "Central(2)",'Defensor lat derecho(4) ',"volante central(5)","Delantero central(9)","extremo izquiedo(10)" )
jugadores= {posiciones[0]:equipo[1],posiciones[1]:"Rami" , posiciones[2]:"Nahuel", posiciones[3]:"Nico", posiciones[4]:"Marcos", 
posiciones[5]:"Alan", posiciones[6]:"Santi.V",}
print("Mostramos el equipo y sus posiciones utilizando tuplas....: ")
print("Posiciones y sus jugadores: ",jugadores)
print('*'*50)
print(' ')

#LISTAS DENTRO DEL DICCIONARIO
jugador = {"Posicion 6": "Santi V.", 
					"Apodo": 'El ayudante de la profe',
					"Equipo": "Progra",
					"Torneo":[2023, 2024] }
print('*'*50)
print("Datos de un jugador utilizando listas dentro de un dicionario: ", jugador)
print('*'*50)
print("Mostramos elementos seleccionados de un diccionario: ",jugador["Apodo"],"Juega en el equipo: ",jugador["Equipo"])

#DICCIONARIO DENTRO DE DICCIONARIO
jugador = {"Posicion 6": "Santi V.", 
					"Apodo":'El ayudante de la profe', 
					"Equipo":"Progra",
					"Torneo":[2023,2024]}
print('Mostramos un diccionario anidado: ',jugador["Torneo"])
print('*'*50)
print(' ')

Hija_Mayor = {
  "nombre" : "Fiamma",
  "año" : 1992
}

Hijo_menor = {
  "nombre" : "Fede",
  "año" : 1998
}

Mis_hijos = {
  "Hija_Mayor" : Hija_Mayor,
  "Hijo_menor" : Hijo_menor,
}

print(Mis_hijos)

#MÉTODOS
print("Clave acceso: ", jugador.keys())
print("Valores de los jugadores: ", jugadores.values())
print("Cantidad de jugadores: ", len(jugadores))

