diccionario={'Euro':'€','Dollar':'$','Yen':'¥'}
divisa = diccionario
seleccion =input("seleccione una divisa: ")
if seleccion in divisa and seleccion =='Euro':
    print("€")
elif seleccion in divisa and seleccion =='Dollar':
    print("$")
elif seleccion in divisa and seleccion =='Yen':
    print("¥")
else:
    print("divisa no encontrada")