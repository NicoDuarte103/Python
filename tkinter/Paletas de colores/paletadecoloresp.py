from PIL import Image
# Cargar la imagen original
img = Image.open("sala.jpg")

# Convertir la imagen a modo "P"
img_p = img.convert("P")

# Crear una nueva paleta de colores
palette = []

# Definir un color de teñido, por ejemplo, rojo
dye_color = (255, 0, 0)  # Rojo

# Llenar la paleta con varios tonos del color de teñido
for i in range(256):
    # Mezcla del color original con el color de teñido
    #la primera tupla define coordenadas
    #la primera lista define el color del pixel en esa coordenada (255,0,0),en este caso 255
    #255-i determina que tanto se tiñe
    #dyecolor es el color de teñido usa un indice para indicar su valor
    r = (img.getpixel((0, 0))[0] * (255 - i) + dye_color[0] * i) // 255 
    g = (img.getpixel((0, 0))[1] * (255 - i) + dye_color[1] * i) // 255 
    b = (img.getpixel((0, 0))[2] * (255 - i) + dye_color[2] * i) // 255
    palette.extend((r, g, b))

# Asignar la paleta a la imagen
img_p.putpalette(palette)

# Crear una nueva imagen teñida
img_dyed = img_p.point(lambda p: p)  # Aplicar la paleta

# Guardar la imagen resultante
img_dyed.save("imagen_teñida.png")

'''esto es util para crear un color especifico'''