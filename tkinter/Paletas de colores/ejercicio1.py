from PIL import Image

imagen = Image.open("E:\pillow\ejercicios\sala.jpg") #con esto importas la imagen para manipular

print(f"formato: {imagen.format} Tamanio: {imagen.size} Modo: {imagen.mode}") #muestra datos de imagen

imagen_redimensionada=imagen.resize((400,300))#con esto redimensionas la imagen
#imagen.show() #con esto mostras las imagenes
#imagen_redimensionada.show( ) #con esto mostras la imagen redimensionada,requerimso crear una nueva variable

imagen_redimensionada.save("imagen_redimensionada22.jpg") #con esto guardas las imagenes en un archivo

imagen_rotada = imagen.rotate(90)
#imagen_rotada.show()


