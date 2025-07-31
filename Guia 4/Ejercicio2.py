'''Escribir un programa que solicite ingresar 10 notas de alumnos y nos
informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
'''
cantidad = 0
cantidadmenorsiete=0
discriminante = 0
for numero in range (1,11):
    print ("ingrese la nota numero",numero,": ",end='')
    nota = float (input())
    if nota >= 7:
        #print ("el alumno numero ",numero,"tiene ",nota)
        cantidad = cantidad +1
        #print (cantidad)
    if nota < 7:
        cantidadmenorsiete = cantidadmenorsiete+1

print ("hay ",cantidad," alumnos que tienen notas mayores o iguales a 7")
print ("hay ",cantidadmenorsiete," alumnos que tienen notas menores a 7")
