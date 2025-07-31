[10,20, 30, 50, 90]
L1=["Hola", 4,5.5,"Adios"]
#[ ] Listas vacías
print([10, 20])
print(type([10, 20]))
#Tuplas
#son constantes a diferencia de las listas

(10,20,30,40)
print((10, 20))
print((10, 90))
print(L1[-2])

print(L1[0:3])#muestra el subrango
print('*'*50)
print( )

L1.append('Ultimo')#agrega al final
print(L1)
print('*'*50)

L1.insert(2, "Intermedio")#agrega y desplaza a los siguientes
print(L1)
print( )
print('*'*50)

L1.extend(["Fiamma","Antonella"])#agrega al final
print(L1)
print( )
print('*'*50)

print(L1.index("Antonella"))#Devuelve pos de la primera

print('*'*50)
print("Pepe" in L1)#Si se encuentra Pepe en L1

print('*'*50)
L1.remove("Antonella") #Elimina a Antonella de la L1
L1.pop()#quita el último elemento

print('*'*50)

L2=["Juan","José", "Pedro", "Ana", "Gabriel","Fernando"]
L3=L1+L2 #concatena listas
print(L3)

L2=L2*4 #multiplica las listas
print(L2)
print('*'*50)
print(dir(list))

print('*'*50)


