'''3. Leer el nombre de una persona y un carácter y comprobar si dicho carácter
está en su nombre.'''
nombre= (input ("escriba el nombre: "))
caracter = (input ("escriba un caracter: "))

if caracter in nombre:
    print ("el caracter esta en el nombre")
else:
    print ("el caracter no esta en el nombre")
   