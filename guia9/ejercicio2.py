
diccionario = {}
contador = 0
buscador = 0

while contador == 0:
    documento = int( input ("ingrese documento : "))
    nombre = input ("ingrese nombre ")
    apellido = input ("ingrese apellido ")
    telefono = input ("ingrese telefono ")
    nota = input ("ingrese nota ")
    cursos = input ("ingrese cursos ")
    detalle = { "nombre:",nombre,
                     "apellido",apellido,
                     "telefono",telefono,
                     "nota",nota,
                     "cursos",cursos
                      }

    diccionario [documento]= detalle
    print (diccionario)
    buscador = int (input ("ingrese codigo a buscar: "))
    if buscador == documento:
        print (diccionario[documento])

   

