from io import*
archivoTxt = open('MiTxt.txt','r')
print('-'*80)

#---LECTURA DE UNA CADENA DE CARCTERES---
frase1= archivoTxt.read
print('+'*80)
print(frase1)
print('+'*80)
print(frase1)
print('+'*80)
archivoTxt.close( )
print('+'*80)

archivoTxt = open('MiTxt.txt','r')

#--EJEMPLO PARA SITUARNOS Y LEER EN UNA LISTA--
MiLista= archivoTxt.readlines()
		#agrega elemntos a una L el elemento de la lista y lo concatena
		#CADA LÍNEA ES UN ELEMENTO PARA UNA LISTA
print('-'*80)
print(MiLista)
print('-'*80)

#---PARA  MOSTRAR LA PRIMERA LÍNEA----
print('Primera línea de mi lista: ',MiLista[0])

#PODEMOS MOSTRAR CUALQUIER LÍNEA INDICANDO LA UBICACIÓN
print('Tercera línea de mi lista: ',MiLista[2])
print('-'*80)
print(' ')
archivoTxt.close( )
print('+'*80)

#---PARA SITUARNOS Y LEER EN UNA LISTA---
archivoTxt = open('MiTxt.txt','r')
MiLista= archivoTxt.readline()
print('-'*80)
print(' ')
print('Primera línea leyendo de a una: ',MiLista)
print('-'*80)
print(' ')












