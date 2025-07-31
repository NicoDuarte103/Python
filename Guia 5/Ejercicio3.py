'''EJERCICIOS DE REPASO -CICLO WHILE
3) En una empresa trabajan n empleados cuyos sueldos oscilan entre $100
y $500, realizar un programa que lea los sueldos que cobra cada
empleado e informe cuántos empleados cobran entre $100 y $300 y
cuántos cobran más de $300. Además, el programa deberá informar el
importe que gasta la empresa en sueldos al personal.'''

bucle0 = 0
empleados = int(input("escriba el numero de empleados: "))
sueldo = 0
sueldosuma = 0
empleado100300 = 0
empleadomas300= 0
while bucle0 < empleados:
    print ("escriba el sueldo del empleado numero",bucle0+1,end='')
    sueldo= int(input(" "))
    sueldosuma = sueldosuma+sueldo
    if (sueldo < 300 and sueldo > 100):
        empleado100300 = empleado100300+1
    elif (sueldo>300):
        empleado300 = empleadomas300+1
    bucle0=bucle0+1
print ("la cantidad de empleados que gana mas de 300 es",empleado300)
print ("la cantidad de empleados que gana entre 100 y 300 es: ",empleado100300)
print ("la cantidad de dinero que gasta la empresa en sueldos es: ",sueldosuma)