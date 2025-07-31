#LISTAS SE DEFINEN CON CORCHETES
auxlista = [1,'hola', 1.4 , 123]
colores = ['rojo', 'celeste','verde', 'amarillo']
numeros = list((1, 2, 3, 4, 5, 6,7))

print(numeros)

print(type(numeros))

R= list(range(1,120))
print(R)
print(auxlista)
print(colores)
print('*'*50)
print(' ')
#Son distintas formas de crear y mostrar una lista
#las listas, al igual que los string son una clase
#Para ver los métodos disponibles de la clase list, hago:
print(dir(colores))
print("--"*50)
#Y veo todos los métodos de la variable tipo lista de la variable colores
# ejemplo
print(len(colores)) #para saber cantidad de elementos que tiene una lista
#Las listas son vectores que arrancan en el índice 0
print("--"*50)
print(colores[1])

#Las listas son vectores que arrancan en el subíndice cero
print(colores[1])
print("amarillo"in colores) #devuelve true o false si es que amarillo está en la lista
print("_"*50)

#Puedo hacer
colores[1]="violeta"
print(colores)
colores.append("Ultimo color")
print(colores)
print("--"*50)

#OJO!!Si hago append de dos colores estoy agregando una sublista

#Ejemplo
colores.append(["color1", "color2"])
print(colores)
print("--"*50)
#Además se pueden insertar elementos en posiciones determinadas
#indicadas por el subíndice, de atrás hacia adelante los 
#subíndices son -1 -2 ... -n
#También se puden eliminar elementos con métodos pop (el último)
#o remove (uno en particular)

colores.reverse() #ordena. Hace diferencia entre mayúscula y minúscula. Las mayúsculas van primero
print(colores)
print("*"*50)
print(" ")
