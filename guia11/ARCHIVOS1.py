#Para trabajar con archivos debemos importar
from io import*#Significa que importamos todo lo que hay dentro de
#la librería io.

archivoTxt = open('MiTxt.txt','w') #importar las funciones que están dentro
#de las librerias input - output (entrada-salida).

			#MiTxt.txt(es la ruta de donde se encientra el texto)
#--MODO r= lectura(lee y escribe), MODO w= nuevo, MODO a= append
#--MODO r+ se pisa el contenido de la primera línea si abrimos y escribimos.
frase= '''HAy que leer la documentación para estudiar 
		  Python\n La bibliografía importa...\n 
		  También debemos apoyarnos en internet...'''
archivoTxt.write(frase)
archivoTxt.close()
