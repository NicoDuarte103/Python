def mincommultiplo():
    
    print("minimo comun multiplo")
    numero1= int (input("ingrese numero 1: "))
    numero2= int (input("ingrese numero 2: "))
    
    contador = 0
    conj1=set()
    conj2=set()
    resultado1= 0
    resultado2= 0
    multiplicador=0
    while contador == 0:
        
        multiplicador = multiplicador+1
        resultado1= numero1*multiplicador
        resultado2= numero2*multiplicador
        resultado1 = (resultado1)
        resultado2 = (resultado2)
        conj1.add(resultado1)
        conj2.add(resultado2)
        print (conj1)
        print (conj2)
        print (conj1&conj2)
        if conj1&conj2:
            minimomultiplo= conj1&conj2
            print (minimomultiplo)
        pregunta = input("seguir? y/n")
        if pregunta == "n":
            break
        
def mincomdivisor():
    print("maximo comun divisor")
    numero1= int (input("ingrese numero 1: "))
    numero2= int (input("ingrese numero 2: "))
    contador = 0
    conj1=set()
    conj2=set()
    resultado1= 0
    resultado2= 0
    divisor=0
    while contador == 0:
       
        divisor = divisor+1
        resultado1= numero1/divisor
        resultado2= numero2/divisor
        resultado1 = (resultado1)
        resultado2 = (resultado2)
        conj1.add(resultado1)
        conj2.add(resultado2)
        print (conj1)
        print (conj2)
        print (conj1&conj2)
        if conj1&conj2:
            minimomultiplo= conj1&conj2
            print (minimomultiplo)
        pregunta = input("seguir? y/n")
        if pregunta == "n":
            break
        
selector = input("seleccione opcion \n 1: minimo comun multiplo \n 2:maximo comun divisor \n")
if selector == "1":
    mincommultiplo()
else:
    mincomdivisor()