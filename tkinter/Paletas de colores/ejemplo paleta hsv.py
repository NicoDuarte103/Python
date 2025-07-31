from PIL import Image

def rgb_to_hsv(r, g, b):
    # Normalizar los valores a [0, 1]
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    diff = mx - mn

    # Matiz
    if diff == 0:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / diff) + 240) % 360

    # Saturación
    s = 0 if mx == 0 else (diff / mx)

    # Valor
    v = mx

    return int(h), int(s * 255), int(v * 255)

def hsv_to_rgb(h, s, v):
    h = float(h) / 360  # Convertir a [0, 1]
    s = float(s) / 255  # Convertir a [0, 1]
    v = float(v) / 255  # Convertir a [0, 1]

    if s == 0.0:  # Gris
        r = g = b = int(v * 255)
        return r, g, b

    i = int(h * 6)  # Sector del círculo
    f = (h * 6) - i  # Parte fraccionaria
    p = int(v * (1 - s) * 255)
    q = int(v * (1 - f * s) * 255)
    t = int(v * f * s * 255)
    v = int(v * 255)

    i = i % 6
    if i == 0:
        return v, t, p
    elif i == 1:
        return q, v, p
    elif i == 2:
        return p, v, t
    elif i == 3:
        return p, q, v
    elif i == 4:
        return t, p, v
    elif i == 5:
        return v, p, q

# Cargar tu imagen
image = Image.open("E:\pillow\ejercicios\sala.jpg")  # Cambia esto a la ruta de tu imagen
image = image.convert("RGB")  # Asegúrate de que está en formato RGB
width, height = image.size

# Teñir la imagen
dye_hue = 180  # Matiz del tinte que deseas aplicar (por ejemplo, cian)

for x in range(width):
    for y in range(height):
        # Obtener el color del píxel
        r, g, b = image.getpixel((x, y))

        # Convertir a HSV
        h, s, v = rgb_to_hsv(r, g, b)

        # Modificar el matiz
        h = (dye_hue + h) % 360  # Añadir el matiz del tinte

        # Convertir de nuevo a RGB
        new_r, new_g, new_b = hsv_to_rgb(h, s, v)

        # Asignar el nuevo color al píxel
        image.putpixel((x, y), (new_r, new_g, new_b))

# Guardar la imagen teñida
image.save("imagen_teñidada.png")
