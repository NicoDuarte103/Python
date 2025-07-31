from io import *
archivo = open("guia11\misma carpeta\datos.txt","r")
contador = 0
contenido = archivo.read()
contenido =contenido.lower().strip()
palabras = contenido.split()
for palabra in palabras[:10]:
    
   
    print(palabra)
