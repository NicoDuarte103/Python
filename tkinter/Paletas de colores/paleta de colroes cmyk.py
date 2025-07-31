from PIL import Image

# Cargar una imagen en RGB
image_rgb = Image.new("RGB", (100, 100), (255, 0, 0))  # Crear una imagen roja

# Convertir la imagen a CMYK
image_cmyk = image_rgb.convert("CMYK")

# Guardar la imagen convertida
image_cmyk.save("output_image_cmyk.jpg")

# Mostrar información de la imagen
print("Imagen original (RGB):", image_rgb.size, image_rgb.mode)
print("Imagen convertida (CMYK):", image_cmyk.size, image_cmyk.mode)
