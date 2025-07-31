diccionario = {}
contador = 0

tupla = ("nombre","nota","materia")
while contador == 0:
    DNI = input ("ingrese numero de DNI: ")
    if DNI == "0": 
        contador = 1
        break
    estudiante = input ("ingrese nombre de estudiante: ")
    nota = input("ingrese nota: ")
    materia = input ("ingerese materia: ")
    detalle = {tupla[0]:estudiante,
                tupla[1]: nota,
                tupla[2]: materia
                }
    diccionario [DNI] = detalle
    print (diccionario)
  
   
consulta = input ("ingrese DNI del alumno a buscar: ")
print (diccionario[consulta])
