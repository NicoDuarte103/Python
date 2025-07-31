from io import*

archivoTxt2 = open('frase.txt','w') 

			#MiTxt.txt(es la ruta de donde se encuentra el texto)
#--MODO r= lectura(lee y escribe), MODO w= nuevo, MODO a= append
#--MODO r+ se pisa el contenido de la primera línea si abrimos y escribimos.
frase= '''Érase una vez una prostituta llamada María.
Como todas las prostitutas, había nacido virgen e inocente, 
y durante su adolescencia había soñado con encontrar al hombre 
de su vida (rico, guapo, inteligente), casarse (vestida de novia), 
tener dos hijos (que serían famosos cuando creciesen) y vivir en una bonita casa
(con vista al mar). Su padre era vendedor ambulante; su madre, costurera, 
su ciudad en el interior del Brasil tenía un solo cine, 
una discoteca, una sucursal bancaria, por eso María no dejaba de esperar el día
en que su príncipe encantado llegara sin avisar, arrebatara su corazón, 
y partiera con él a conquistar el mundo...'''
archivoTxt2.write(frase)
archivoTxt2.close()