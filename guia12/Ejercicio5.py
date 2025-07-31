diccionario = {}
contador = 0
while contador == 0:
    continuar = input("continuar?")
    if continuar == "n":
        contador =1
        break
    documento= int(input("ingrese documento"))
    nombre= input("ingrese nombre: ")
    edad= input("ingrese edad: ")
    sexo= input("ingrese sexo: ")
    telefono= input("ingrese telefonjo: ")
    correo= input("ingrese correo: ")

    detalle= {"nombre":nombre,
            "Edad":edad,
            "sexo":sexo,
            "telefono":telefono,
            "correo electronico":correo
            
            }
    diccionario[documento] = detalle
    print(diccionario)