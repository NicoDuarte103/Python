'''Cadenas de Caracteres
1. Sustituir todos los espacios en blanco de un texto por asteriscos'''


palabra = input("escriba una palabra: ")
espacio_en_blanco = " "
if espacio_en_blanco in palabra:
    palabra_nueva = palabra.replace(" ","*",100)
    print ("palabra nueva: ",palabra_nueva)
else:
    print("no hay espacios")