from io import*

archivoTxt2 = open('frase.txt','r') 

LaLista=archivoTxt2.readlines()
print('-'*80)
print(LaLista)

#LaLista= archivoTxt2.readline()
print('Lectura de la primer línea: ',LaLista[0])

print('Lectura de la tercer línea: ',LaLista[3])
archivoTxt2.close()
print('-'*80)

archivoTxt2 = open('frase.txt','r') 
LaLista = archivoTxt2.readline()
print('Leyendo la primer línea: ',LaLista)
print('-'*50)


#Fragmento del libro: Once minutos de Paulo Coelho...
