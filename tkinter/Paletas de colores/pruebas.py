from PIL import Image

imagen = Image.open("E:\pillow\ejercicios\Paletas de colores\sala.jpg")

imagenre= imagen.resize((400,300))


imagenrotada=imagen.rotate(90)

imagenconvertida =imagen.convert("RGB")
imagenconvertida.show()