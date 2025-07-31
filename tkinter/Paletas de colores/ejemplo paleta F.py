from PIL import Image

# Cargar tu imagen existente
image = Image.open("E:\pillow\ejercicios\Paletas de colores\sala.jpg")  # Cambia esto a la ruta de tu imagen
image = image.convert("RGB")  # Asegúrate de que está en formato RGB

# Convertir la imagen a modo "F"
float_image = image.convert("F")

# Manipulación de la imagen
width, height = float_image.size
for x in range(width):
    for y in range(height):
        # Obtener el valor de punto flotante
        value = float_image.getpixel((x, y))

        # Asegurarse de que el valor se normaliza adecuadamente
        # Aquí simplemente mantenemos el valor sin cambiar, ya que el modo "F" ya tiene valores entre 0.0 y 255.0.
        # Esto es importante para evitar que se vuelva negro.
        normalized_value = value  # No hacemos nada aquí para que mantenga el brillo original.

        # Asignar el valor normalizado de nuevo
        float_image.putpixel((x, y), normalized_value)

# Convertir la imagen de nuevo a modo "RGB"
rgb_image = float_image.convert("RGB")

# Guardar la imagen modificada
rgb_image.save("imagen_modificadaff.png")
