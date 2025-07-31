from PIL import Image

# Crear una imagen azul de 100x100 píxeles
img = Image.new("RGB", (100, 100), (0, 0, 255))  # Azul puro

# Definir el color de teñido (rojo)
dye_color = (255, 0, 0)  # Rojo

# Crear una nueva imagen para el resultado
teñida = Image.new("RGB", img.size)

# Parámetro de mezcla (0-255)
i = 125  # Por ejemplo, teñido al 50%

# Procesar cada píxel
for x in range(img.width):
    for y in range(img.height):
        # Obtener el color del píxel original
        original_color = img.getpixel((x, y))
        
        # Calcular el nuevo componente rojo
        r = (original_color[0] * (255 - i) + dye_color[0] * i) // 255
        g = (original_color[1] * (255 - i) + dye_color[1] * i) // 255
        b = (original_color[2] * (255 - i) + dye_color[2] * i) // 255
        
        # Establecer el nuevo color en la imagen teñida
        teñida.putpixel((x, y), (r, g, b))

# Guardar la imagen resultante
teñida.save("teñida.png")

# Mostrar la imagen resultante (opcional)
teñida.show()
