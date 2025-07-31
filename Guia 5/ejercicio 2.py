'''Escribir un programa que solicite ingresar 10 notas de alumnos y nos
informe cuántos tienen notas mayores o iguales a 7 y cuántos menores'''
bucle0=0
bucle10 = 10
mayores7 = 0
menores7 = 0
while bucle10>bucle0:
    print("ingrese nota del alumno numero",bucle0+1,end='')
    nota = float(input(" "))
    if nota >= 7:
        mayores7=mayores7+1
        bucle0 = bucle0+1
    else:
        menores7=menores7+1
        bucle0 = bucle0+1
print ("la cantidad de gente que tiene mas de 7 es: ",mayores7)
print ("la cantidad de gente que tiene menos de 7 es: ",menores7)