from io import*

archivoTxt = open('MiTxt.txt','r')
print('-'*80)

miTxt = archivoTxt.read()
print(miTxt)
print('-'*80)

#seek me indica a partir de que caracter va a leer el archivo.

archivoTxt.seek(10)
	#Tiene como parámetro el número de caracter en la posición del archivo
	#Es el caracter número 0.
	#Si coloco 10 irá el puntero al décimo lugar
frase1= archivoTxt.read()
#read también puede tener hasta que letra leer número entero como
#parámetro real.
print('Segunda lectura frase1',frase1)
print('-'*80)

archivoTxt.seek(0)
print('Longitud del archivo: ',len(archivoTxt.read()))
archivoTxt.seek(100)
frase1 = archivoTxt.read()
print('Tercera lectura: ',frase1)

print('*'*80)
archivoTxt.close()
print('*'*80)
print(' ')

#---Contar cuantas vocales hay en el archivo txt-----

archivoTxt = open('MiTxt.txt','r')
print('-'*80)
print('Muestro de nuevo el texto: ',miTxt)
print('-'*80)

archivoTxt.seek(0)
contarVocales = 0
for letra in range(0,len(miTxt)):

	if miTxt[letra]== 'a' or miTxt[letra]== 'A' or miTxt[letra]== 'e' or miTxt[letra]== 'E' or miTxt[letra]== 'i'or miTxt[letra]== 'I' or miTxt[letra]== 'o' or miTxt[letra]=='O' or miTxt[letra]== 'u' or miTxt[letra]== 'U' :
		
		
		
		contarVocales = contarVocales+1 
		print(miTxt[letra],end='')

print(' "La cantidad de vocales es el archivo txt es: "',str(contarVocales))
print('Con string.count()...la cantidad de vocales es: ',miTxt.count('a') + miTxt.count('A') + miTxt.count('e') + miTxt.count('E') + miTxt.count('i') +
miTxt.count('I') + miTxt.count('o') + miTxt.count('O') + miTxt.count('u') + miTxt.count('U'))
	
	
	
