#--------------RANGO DE ÍNDICE----------

"""mi_lista = ["manzana", " banana ", "cereza", "naranja", "kiwi", "melón", "mango"]
print (mi_lista [2: 5])
print('*'*50)
print(' ')

mi_lista = ["manzana", " banana ", "cereza", "naranja", "kiwi", "melón", "mango"]
print (mi_lista [: 4])
print('*'*50)
print(' ')

mi_lista = ["manzana", " banana ", "cereza", "naranja", "kiwi", "melón", "mango"]
print (mi_lista [2: ])
print('*'*50)
print(' ')

mi_lista = ["manzana", " banana ", "cereza", "naranja", "kiwi", "melón", "mango"]
print (mi_lista [-4:-1 ])
print('*'*50)
print(' ')"""

#---------------CAMBIAR ELEMENTOS DE LA LISTA--------

"""mi_lista2 = ["manzana", "banana", "cereza"]
mi_lista2[2]= "pera"
print (mi_lista2)
print('*'*50)
print(' ')


mi_lista2 = ["manzana", "banana", "cereza"]
mi_lista2[1:2]= ["pera", "ananá"]
print (mi_lista2)
print('*'*50)
print(' ')

mi_lista2 = ["manzana", "banana", "cereza"]
mi_lista2[1:3]= ["ananá"]
print (mi_lista2)
print('*'*50)
print(' ')

#------------INSERTAR ELEMENTOS---------

mi_lista2 = ["manzana", "banana", "cereza"]
mi_lista2.insert(2,"ananá")
print (mi_lista2)
print('*'*50)
print(' ')

#------------AGREGAR ELEMENTOS-------
mi_lista2 = ["manzana", "banana", "cereza"]
mi_lista2.append("ananá")
print (mi_lista2)
print('*'*50)
print(' ')

#---------------AMPLIAR LISTA------------

mi_lista_alumnas = ["Karina","Abril", "Keila","Iara", "Ale","Male","Fer",]
alumnas2 = ["Agus", "Evelin","Evelyn","Maria ", "Tere", "Mirta"]
mi_lista_alumnas.extend(alumnas2)
#alumnas2.extend(mi_lista_alumnas)
print(mi_lista_alumnas)
#print(alumnas2)
print('*'*50)
print(' ')

#------------ELIMINAR ARTÍCULO ESPECIFICADO-------

mi_lista_alumnos = ["Marcos", "Damian", "Santi","Alan", "Nico", "Rami", "Nahuel", "Santiago"]
mi_lista_alumnos.remove("Marcos","Rami","Nahuel")
print(mi_lista_alumnos)
print('*'*50)
print(' ')

#------------ELIMINAR ÍNDICE ESPECIFICADO------

alumnas = ["Iara", "Ale","Male","Fer"]
alumnas.pop (1)
print(alumnas)
print('*'*50)
print(' ')

L1 = ['a', 'b', 'c','d']
del L1[2]
print(L1)
print('*'*50)
print(' ')

L2 = ["Leo", "Escorpio", "Tauro"]
#del L2
print(L2)
print('*'*50)
print(' ')

#-----------------LISTAS Y FUNCIONES------

números = [3, 41, 12, 9, 74, 15]
print(len(números))
print('*'*50)
print(' ')
print(max(números))
print('*'*50)
print(' ')
print(min(números))
print('*'*50)
print(' ')
print(sum(números))
print('*'*50)
print(' ')
print(sum(números)/len(números))
print('*'*50)
print(' ')

#-----------CALCULO DE PROMEDIO--------

total = 0
contador = 0
while (True):
    num = input('Ingresa un número: ')
    if num == 'x': break
    valor = float(num)
    total = total + valor
    contador = contador + 1
promedio = total / contador
print('Promedio:', promedio)
print('*'*50)
print(' ')"""

#-----------CALCULO DE PROMEDIO CON FUNCIÓN SUMA--------

numlista = list()
while (True):
    num = input('Ingresa un número: ')
    if num == 'x': break
    valor = float(num)
    numlista.append(valor)

promedio = sum(numlista) / len(numlista)
print('Promedio:', promedio)
print('*'*50)
print(' ')

for x in range(len(numlista)):
    if numlista[x]<10:
        numlista[x]=0

print(numlista) 
print('*'*50)
print(' ')