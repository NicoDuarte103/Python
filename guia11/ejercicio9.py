import re 
from io import *
archivo = open("guia11\misma carpeta\datos.txt","r")
contenido = archivo.read()
palabras = contenido.split()
frecuencia={}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra]+=1
    else:
        frecuencia[palabra]=1
palabras_comunes = sorted(frecuencia.items(),key=lambda x:x[1],reverse=True)[:10]
for palabra,frec in palabras_comunes:
    print(f"{palabra}: {frec}")