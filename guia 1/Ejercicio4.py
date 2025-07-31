'''Leer una cadena de caracteres, donde en lugar de ñ se han utilizado los
caracteres ny. Crear una nueva cadena de caracteres sustituyendo ny por ñ'''
letra = 'ñ'
palabra =(input("escriba una palabra: "))
if letra in palabra:
    
    palabranueva= palabra.replace("ñ","ny",100)
    
    print (palabranueva)
   
else:
    print("la cadena no tiene Ñ")

