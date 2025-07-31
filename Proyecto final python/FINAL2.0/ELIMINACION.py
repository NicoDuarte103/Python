


import tkinter as tk 
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
import time
class aplication5():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("ASIGNACIÓN DE TURNO")
        self.ventana.geometry("700x600")
        self.ventana.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.ventana.rowconfigure((0), weight=1)

        # Cargar la imagen original
        #self.imagen_1 = Image.open("imagenes_final2.0/logo.jpg")
        #self.imagen_tk = ImageTk.PhotoImage(self.imagen_1)

        def agrandar_imagen(event):
            # Obtener el nuevo tamaño de la ventana
            self.width = event.width
            self.height = event.height
            #print(f"Nuevo tamaño: {width}x{height}")
            
            # Redimensionar la imagen con los nuevos valores de ancho y alto
           # self.nueva_imagen = self.imagen_1.resize((self.width, self.height))
            #self.nueva_imagen_tk = ImageTk.PhotoImage(self.nueva_imagen)
            
            # Actualizar la imagen en el canvas
        
           # self.canva1.create_image(0, 0, image=self.nueva_imagen_tk, anchor="nw")
                
            # Necesitamos mantener la referencia a la nueva imagen para evitar que se elimine
           # self.canva1.image = self.nueva_imagen_tk  # Esto es necesario para evitar que la imagen se borre


        

        # Cargar las imágenes de los botones
       # self.imagen_confir = Image.open("imagenes_final2.0/confirmado.jpg").resize((40,40))
       # self.imagen_confir_tk = ImageTk.PhotoImage(self.imagen_confir)

        #self.imagen_cance = Image.open("imagenes_final2.0/imagenx.png").resize((30, 30))
      #  self.imagen_cance_tk = ImageTk.PhotoImage(self.imagen_cance)

        
        # Crear el frame para los botones
        self.frame = ttk.Frame(self.ventana)
        self.frame.grid(column=0, row=0, sticky="nsew")
        
        #labels paar cada uno
        
        self.label_reasig=tk.Label(self.frame, text="Agendado:" ,font=("Sitka Text Semibold", 30), width=500)
        self.label_reasig.pack(pady=9)

        self.label_mail=tk.Label(self.frame, text="¿Esta seguro de que\n quiere eliminar su\n turno?" ,font=("Sitka Text Semibold", 20), width=500, foreground="red")
        self.label_mail.pack(pady=10)

        self.label_horario=tk.Label(self.frame, text="PARA:--------------\n MÉDICO:----------\n ESPECIALIDAD:----------\n FECHA:--/--/---- \n HORA: --:--" ,font=("Sitka Text Semibold", 20), width=500)
        self.label_horario.pack(pady=11)

        self.boton_modificar = ttk.Button(self.frame, width=50, text="SI", compound="left")
        self.boton_modificar.pack(pady=24, padx=26)

        self.boton_eliminar = ttk.Button(self.frame, width=50, text="CANCELAR", compound="left")
        self.boton_eliminar.pack(pady=25, padx=26)


        # Crear el canvas para la imagen
        #self.canva1 = tk.Canvas(self.ventana, background="black")
        #self.canva1.grid(column=1, row=0, columnspan=3, sticky="nsew")
       # self.canva1.bind("<Configure>", agrandar_imagen)

        # Mostrar la imagen inicial (con el tamaño original)
        #self.canva1.create_image(0, 0, image=self.imagen_tk, anchor="nw")

        # Ejecutar la ventana
        self.ventana.mainloop()
def confirmar_eliminar():
    ejecutar=aplication5()