A= {"Hidrogeno","Helio","Litio","Berilio","Boro","Carbono","Nitrogeno","Oxigeno"}
B= {"Fluor","Neon","Sodio","Magnesio","Aluminio","Litio","Silicio","Fosforo"}
C= {"Cloro","Argon","Helio","Litio","Berilio","Potasio","Calcio","Escandio","Titanio"}

gases = {"Hidrogeno","Nitrogeno","Oxigeno","Fluor","Neon","Cloro","Argon"}

conC = {"Carbono","Cloro","Calcio"}
#muestra todos los elementos en un solo conjunto
todojunto = A | B | C
print (todojunto)

#muestra solo solidos
print (todojunto-gases)
#muestra solo gases
print (gases&todojunto)
#muestra elementos comunes
print (A&B&C)
#muestra elemenos sin los que comienzan con c
print(todojunto-conC)
