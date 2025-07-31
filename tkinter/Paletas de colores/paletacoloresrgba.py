from PIL import Image

# Crear una imagen de 100x100 píxeles con fondo rojo y 50% de opacidad
img = Image.new("RGBA", (100, 100), (255, 0, 0, 210))  # Rojo con 50% de opacidad

# Guardar la imagen resultante
img.save("rgba_image.png")

# Mostrar la imagen resultante (opcional)
img.show()
