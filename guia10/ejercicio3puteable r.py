def ivax (valor,iva):
    print ("el valor de la factura sin iva es",valor)
    
    print ("el valor del iva es ",iva)
    print ("el total de la factura con iva es ", valor*(iva/100)+valor)


valor = int(input("ingrese valor total de la factura"))
iva = input("ingrese el porcentaje de iva")
if iva=="":
    iva= 10
    print("hola")
else:
    iva= int(iva)

ivax(valor,iva)
