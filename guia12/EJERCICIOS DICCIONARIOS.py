#EJERCICIO 1
# Diccionario con las divisas y sus símbolos
divisas = {'Euro': '€', 'Dollar': 'u$s', 'Yen': '¥'}

# Solicitar al usuario que ingrese una divisa
divisa = input("Por favor, ingrese una divisa (Euro, Dollar, Yen): ")

# Verificar si la divisa está en el diccionario y mostrar el símbolo o un mensaje de aviso
if divisa in divisas:
    print(f"El símbolo de {divisa} es: {divisas[divisa]}")
else:
    print("La divisa ingresada no está en el diccionario.")
print('-'*30)
print( )

#EJERCICIO 2
nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
direccion = input('¿Cuál es tu dirección? ')
telefono = input('¿Cuál es tu número de teléfono? ')
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])
print('-'*50)
print( )

#EJERCICIO 3
frutas = {'Plátano':750, 'Manzana':1050, 'Pera':850, 'Naranja':500}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '$')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")

print('-'*50)
print( )

#EJERCICIO 4
meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])

print('-'*50)
print( )

#EJERCICIO 5
persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"

print('-'*50)
print( )
