import tkinter as tk 
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
class aplication6():


    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("INICIO")
        self.ventana.geometry("700x600")
        self.ventana.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.ventana.rowconfigure((0), weight=1)

        # Cargar la imagen original
        self.imagen_1 = Image.open("imagenes_final2.0/carga.jpg")
        # Crear una variable global para almacenar la imagen redimensionada
        self.imagen_tk = ImageTk.PhotoImage(self.imagen_1)

        def agrandar_imagen(event):
            # Obtener el nuevo tamaño de la ventana
            self.width = event.width
            self.height = event.height
            #print(f"Nuevo tamaño: {width}x{height}")
            
            # Redimensionar la imagen con los nuevos valores de ancho y alto
            self.nueva_imagen = self.imagen_1.resize((self.width, self.height))
            self.nueva_imagen_tk = ImageTk.PhotoImage(self.nueva_imagen)
            
            # Actualizar la imagen en el canvas
            self.canva1.create_image(0, 0, image=self.nueva_imagen_tk, anchor="nw")
            
            # Necesitamos mantener la referencia a la nueva imagen para evitar que se elimine
            self.canva1.image = self.nueva_imagen_tk  # Esto es necesario para evitar que la imagen se borre


        # Crear el frame para lado vacio

        self.frame = ttk.Frame(self.ventana)
        self.frame.grid(column=0, row=0, sticky="nsew")

        #labels paar cada uno

        self.label_usuario=tk.Label(self.frame, text="¡BIENVENIDO!" ,font=("Sitka Text Semibold", 20), width=500)
        self.label_usuario.pack(pady=300)



        # Crear canvas para la imagen
        self.canva1 = tk.Canvas(self.ventana, background="black")
        self.canva1.grid(column=1, row=0, columnspan=3, sticky="nsew")
        self.canva1.bind("<Configure>", agrandar_imagen)

        # Mostrar la imagen inicial (origunal)
        self.canva1.create_image(0, 0, image=self.imagen_tk, anchor="nw")


        self.ventana.mainloop()

ejecutar = aplication6()