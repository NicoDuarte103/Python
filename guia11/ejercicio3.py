from io import *
archivo=open ("guia11\misma carpeta\datos.txt","r")
contenido = archivo.read()
print(contenido)
print (len(contenido))
print (contenido.split())
print (len(contenido.split()))
