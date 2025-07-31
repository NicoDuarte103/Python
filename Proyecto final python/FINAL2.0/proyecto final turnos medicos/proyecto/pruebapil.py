


import customtkinter as ctk
import tkinter as ttk
import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
ventana = ctk.CTk()


ventana.geometry(f"{800}x{600}")

# Crear un Canvas para colocar la imagen y el Entry
canvas = ctk.CTkCanvas(ventana, width=600, height=800)
canvas.pack(padx=10, pady=10,fill="both",expand=True)  # Empaquetar el Canvas dentro de la ventana

def obtener_ancho():
    ancho_ventana = ventana.winfo_width()  # Obtiene el ancho de la ventana
    alto_ventana = ventana.winfo_height()
    print(f"Ancho de la ventana: {ancho_ventana} píxeles")
    print(f"Ancho de la ventana: {alto_ventana} píxeles")
    return ancho_ventana,alto_ventana
# Usamos 'after' para esperar que la ventana se haya redibujado completamente

ventana.after(100, obtener_ancho)
resultado = ancho


print(ancho_ventana)


    
# Cargar la imagen (reemplaza con la ruta de tu imagen)
imagen = Image.open("D:/proyecto final kei y fer/proyecto final turnos medicos/imagenes/hospital_fondo.jpg")
imagen= imagen.resize((800,600))
imagen_tk = ImageTk.PhotoImage(imagen)

# Colocar la imagen en el Canvas
canvas.create_image(0, 0, anchor="nw", image=imagen_tk)

# Crear un Entry sobre la imagen en el Canvas
# Aquí estamos usando el Entry como un widget que se coloca directamente en el Canvas
usuario = ctk.CTkEntry(ventana, placeholder_text="Escribe aquí")
contraseña= ctk.CTkEntry(ventana, placeholder_text="Escribe aquí")
texto_usuario = ctk.CTkLabel(ventana,text="usuario")

texto_password = ctk.CTkLabel(ventana,text="contraseña")

ingresar = ctk.CTkButton(ventana,text= "ingresar")
registrarse = ctk.CTkButton(ventana,text="registrarse")
olvidocontraseña = ctk.CTkButton(ventana,text="recuperar_contraseña")

canvas.create_window(400,170 , window=texto_usuario)
canvas.create_window(400,300 , window=usuario)
canvas.create_window(400,270 , window=texto_password)
canvas.create_window(400, 200, window=contraseña) # Ubicar el Entry en las coordenadas deseadas
canvas.create_window(400, 330, window=ingresar)
canvas.create_window(400, 360, window=registrarse)
canvas.create_window(400, 390, window=olvidocontraseña)

# Mostrar la ventana
ventana.mainloop()
