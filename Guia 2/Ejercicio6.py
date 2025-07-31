'''Un empleado tiene un ingreso mensual en concepto de salario de
$185000 y desea guardar en concepto de ahorro una cantidad que no es
constante. Pregúntele cuanto quiere guardar e infórmele con cuánto
dinero se quedará'''

salario = 185000
ahorro = float(input("ingrese porcentaje de dinero a guardar para ahorro: "))
guardado = salario * (ahorro/100)
print ("se guardara la cantidad de: $",guardado)
