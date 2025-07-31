contador = 0
diccionario ={1:"enero",2:"febrero",3:"marzo",4:"abril",5:"mayo",6:"junio",7:"julio",8:"agosto",9:"septiembre",10:"octubre",11:"noviembre",12:"diciembre"}
print (f"DIA/ ",end="")
dia= input("") 
print (f"{dia}/MES ",end="")
mes = int(input (""))
print (f"{dia}/{mes}/AÑO/",end="")
año = input ("")
print (f"{dia}/{mes}/{año}")

print(f"{dia}/{diccionario[mes]}/{año}")