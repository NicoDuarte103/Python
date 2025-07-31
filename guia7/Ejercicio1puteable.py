tupla = ("salir","enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")

contador = 0
buscador= 0
while contador == 0:
 buscador = int (input ("ingrese valor: "))
 if buscador >-1 and buscador < len(tupla):
    print (tupla[buscador])
 else:
   print ("error")
 if buscador == 0:
    contador =1


    

