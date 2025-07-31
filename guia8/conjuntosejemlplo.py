#-------PARA AGREGAR UN ELEMENTO A UN CONJUNTO-----
Frutas = {"Banana","Manzana", "Mandarina", "Sandia","Higo", "Melones", "Kiwi", "Sandia", "Uva"}
Frutas.add('pweon')
print("Frutas con Maracuyá: ",Frutas)
print(' ')
print('*'*80)

#----Para agregar más de un elemento se hace con una lista de frutas.---
Frutas.update(['Frutilla', 'Durazno', 'ananá'])
print("Frutas después del update: ", Frutas)
print(' ')
print('*'*80)

#---LONGITUD DEL CONJUNTO-----
print('CANTIDAD DE TIPOS DE FRUTAS EN EL CONJUNTO:',len(Frutas))
print(' ')
print('*'*80)

#---MÁXIMOS Y MÍNIMOS EN UN CONJUNTO----(ordena por orden alfabético)
print('Elemento mínimo: ',min(Frutas), 'y mayor: ',max(Frutas))
print(' ')
print('*'*80)

#---PARA ELIMINAR UN ELEMENTO DE UN CONJ. "remove"(DA ERROR SI NO ESTÁ)--
Frutas.remove('Sandia')
print('Frutas sin Sandia:', Frutas)
Frutas.remove('Higo')
print('Frutas sin Higo:', Frutas)
print(' ')
print('*'*80)
#--DISCARD, TAMBIÉN ELIMINA PERO NO TIRA ERROR SI NO ESTÁ--
Frutas.discard('Sandia')
print('Frutas sin Sandia:', Frutas)
Frutas.discard('Higo')
print('Frutas sin Higo:', Frutas)
print(' ')
print('*'*80)

#--ASIGNACIÓN DE CONJUNTOS-----
FF=Frutas
print('Conjunto FF es...:',FF)
print(' ')
print('*'*80)

#BORRADO...OJOO!! BORRA TODOS LOS CONJUNTOS---
FF.clear( )
print('Conjunto FF:' ,FF)
print('Conjunto Frutas:' ,Frutas)
print(' ')
print('*'*80)
