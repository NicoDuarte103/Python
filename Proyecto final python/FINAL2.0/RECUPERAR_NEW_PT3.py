import tkinter as tk 
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk


class aplication9():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("NUEVA CONTRASEÑA")
        self.ventana.geometry("700x600")
        self.ventana.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.ventana.rowconfigure((0), weight=1)

        # Cargar la imagen original
        self.imagen_1 = Image.open("imagenes_final2.0/logo.jpg")
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


            
        # Funciones de los botones
        def gmail():
            print("Bienvenido a gmail, REGISTRESE")

        # Cargar las imágenes de los botones
        self.imagen_google = Image.open("imagenes_final2.0/imagen_reintentar.png").resize((20, 20))
        self.imagen_google_tk = ImageTk.PhotoImage(self.imagen_google)


        # Crear el frame para los botones
        self.frame = ttk.Frame(self.ventana)
        self.frame.grid(column=0, row=0, sticky="nsew")

        #labels paar cada uno

        self.label_reasig=tk.Label(self.frame, text="Registrate:" ,font=("Sitka Text Semibold", 30), width=500)
        self.label_reasig.pack(pady=9)

        self.label_mail=tk.Label(self.frame, text="Ha habido un error.\n Por favor verifique si el\n Gmail/clave son\n correctos." ,font=("Sitka Text Semibold", 20), width=500)
        self.label_mail.pack(pady=10)

        self.boton_gmail = ttk.Button(self.frame, width=50, text="REINTENTAR", image=self.imagen_google_tk, compound="left", command=gmail)
        self.boton_gmail.pack(pady=24, padx=26)


        # Crear el canvas para la imagen
        self.canva1 = tk.Canvas(self.ventana, background="black")
        self.canva1.grid(column=1, row=0, columnspan=3, sticky="nsew")
        self.canva1.bind("<Configure>", agrandar_imagen)

        # Mostrar la imagen inicial (con el tamaño original)
        self.canva1.create_image(0, 0, image=self.imagen_tk, anchor="nw")

        # Ejecutar la ventana
        self.ventana.mainloop()


ejecutar = aplication9()