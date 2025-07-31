examenes = {"mirta","ramiro","malena","nico"}
proyecto = {"santiago","marcos","nahuel","samuel","mirta","nico"}
print("examenes: ",examenes)
print ("proyecto: ",proyecto)
#que estudiantes realizaron el examen y presentaron el proyecto
print (examenes&proyecto)
ambos = examenes&proyecto
#que estudiantes solo rindieron el examen
print (examenes-proyecto)
soloexamen= examenes-proyecto
#que estudiantes solo hicieron proyecto
print (proyecto-examenes)
soloproyecto = proyecto-examenes
#estudiantes que tomaron examen y proyecto
lista = [ambos]
print(lista)