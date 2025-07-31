
def cadenador ():
    
    palabras = input("ingrese frase ")
    palabras= palabras.split() #divide la frase en palabras
    frecuencia={}
    cantidadpalabras= len(palabras) #cuenta la cantidad de palabras
    for palabras in palabras: #recorre
        cantidadpalabras=len(palabras) #cuenta letras
        print (f"palabra: {palabras} cantidad de letras :  {cantidadpalabras}")
    
    for palabra in palabras: #SE itera sobre cada palabra en la lista palabras;;para cada palabra se verifica si ya existe en el diccionario frecuencia;si la palabra ya existe;se incrementa su valor en !;lo que indica que se ha encontrado otra vez;si la palabra no existe se agrega al diccioario con un valor de !;lo qe indica que se ha encontrado por primera vez
        if palabra in frecuencia:
            frecuencia[palabras]+=1
        else:
            frecuencia[palabras]=1
        
    for palabra,contador in frecuencia.items():
        
        print (f"la palabra {palabra} aparece {contador} veces")
    

cadenador()
    
    
