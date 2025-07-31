
contador= 0
while contador == 0:
    for contador in range(0,1):
    
     turno = input ("ingrese nombre para turno: ")
     if turno == "salir":
        contador = 1
        break
     horario = input ("ingrese hora para turno: ")
     dia = input ("ingrese dia para turno: ")
     lista = []
     lista.append (turno)
     lista.append (horario)
     lista.append (dia)
     
print (lista)