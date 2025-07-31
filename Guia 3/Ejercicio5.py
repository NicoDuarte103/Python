'''Escriba un programa donde le pida al usuario que genere una
contraseña con más de 8 caracteres. La contraseña puede ser correcta
y un mensaje se lo indicará. Puede ser corta e insegura, un mensaje le
dirá que no es lo suficientemente larga. O incorrecta y entonces le pide
que vuelva a intentarlo'''



contador = 0
repetir_bucle=0
while repetir_bucle == 0:
    contraseña = input ("escriba la contraseña: ")
    contador = 0
    while contador == 0:
        if len (contraseña) > 8:
            print ("contraseña correcta!")
            contador = 1
            repetir_bucle = 1
   
        else:
            print ("La contraseña es demasiado corta")
            contador = 1
 


