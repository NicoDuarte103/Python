
diccionario = {}
contador = 0
bucle = 0
bucledebucle = 1
bucledebucle2 = 0
rompebucle = 0
menu = 0
while bucle == 0:
   
 
    print ("cargue DNI de la persona: ")
    for contador in range (bucledebucle2,bucledebucle):
        protopersonaN = input("escriba el dni ")
        if protopersonaN == "salir":
            bucle = 1
            break
        protopersona = input("escriba el nombre: ")
        diccionario[protopersonaN]= protopersona
        #rompebucle = int (input ("pulse 1 para romper el bucle "))
    print (diccionario)
    
    bucledebucle = bucledebucle+1 #modificadores para que no repita a cada rato los bucles dni
    bucledebucle2 = bucledebucle-1  #modificadores para que no repita a cada rato los bucles nombre
print('-'*50)
print(' ')
buscador = input ("escriba el dni a buscar: ")
if buscador in diccionario :

    print(f"{buscador} : {diccionario[buscador]}")

print ("la lista completa es:",diccionario)
print('-'*50)
print(' ')


