from io import*

#APERTURA EN MODO AGREGAR

archivoTxt = open('MiTxt.txt','a')
linea="\n Última línea del párrafo!!"
archivoTxt.write(linea)#agrega una línea al final

archivoTxt.close( )
print('-'*80)
archivoTxt = open('MiTxt.txt','r')
#Modo lectura
frase=archivoTxt.read()
print('Archivo completo: ',frase)
print('-'*80)
archivoTxt.close( )
print('-'*80)
