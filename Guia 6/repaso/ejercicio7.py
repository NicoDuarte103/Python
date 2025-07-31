numero = []
multiplicador = []
resultado = []
operacion= 0

contador = 0

multi = int(input("valor maxmimo tabla "))
valor = int(input("la tabla que quiere ver "))

for contador in range (0,multi+1):
    multiplicador.append(contador)
    numero.append(contador)
for contador in range(0,multi+1):
    
    operacion = numero[contador]*multiplicador[valor]
    resultado.append (operacion)


print (f"el valor del numero{numero}")
print (f"el valor del multiplicador{multiplicador}")
print(f"el valor del resultado{resultado}")

