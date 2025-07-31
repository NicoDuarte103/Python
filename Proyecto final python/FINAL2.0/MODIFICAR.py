
import tkinter as tk 
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
class aplication8():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("ASIGNACIÓN DE TURNO")
        self.ventana.geometry("700x600")
        self.ventana.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.ventana.rowconfigure((0), weight=1)

        # Cargar la imagen original
        self.imagen_1 = Image.open("imagenes_final2.0/logo.jpg")
        # Crear una variable global para almacenar la imagen redimensionada
        self.imagen_tk = ImageTk.PhotoImage(self.imagen_1)

        self.imagen_confi = Image.open("imagenes_final2.0/confirmado.jpg").resize((30,30))
        self.imagen_confi_tk = ImageTk.PhotoImage(self.imagen_confi)

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


        # Crear el frame para los botones
        self.frame = ttk.Frame(self.ventana)
        self.frame.grid(column=0, row=0, sticky="nsew")

        ##########################

        # Función para asignar el turno 
        def asignar_turno():
            self.especialidad = self.especialidad_combobox.get()
            self.medico = self.medico_combobox.get()
            print(f"Turno asignado para {self.especialidad} con  {self.medico}")

        # Lista de especialidades y médicos 
        self.especialidades = ["Cardiología", "Pediatría", "Oftalmología", "Psicología", "Anticónceptivos"]
        self.medicos = ["Dr. Pérez", "Dra. Gómez", "Dr. López", "Dra. Suriano", "Dra. Mendez", "Rte. Salvatierra"]

        # Crear los combobox
        self.especialidad_label = ttk.Label(master=self.frame, text="Especialidad:", font=("Sitka Text Semibold", 30), foreground="Black")
        self.especialidad_label.pack(pady=10)
        self.especialidad_combobox = ttk.Combobox(master=self.frame, values=self.especialidades)
        self.especialidad_combobox.pack(pady=10)

        self.medico_label = ttk.Label(master=self.frame, text="Médico:", font=("Sitka Text Semibold", 30), foreground="Black")
        self.medico_label.pack(pady=10)
        self.medico_combobox = ttk.Combobox(master=self.frame, values=self.medicos)
        self.medico_combobox.pack(pady=10)
                    
        self.boton_confi = ttk.Button(master=self.frame, width=50, text="MODIFICAR", image=self.imagen_confi_tk, compound="left", command=asignar_turno)
        self.boton_confi.pack(pady=20, padx=25)

        #asignar_boton = ctk.CTkButton(master=ventana, text="Asignar Turno", command=asignar_turno)
        #asignar_boton.pack(pady=21)

        #########################
        # Crear el canvas para la imagen
        self.canva1 = tk.Canvas(self.ventana, background="black")
        self.canva1.grid(column=1, row=0, columnspan=3, sticky="nsew")
        self.canva1.bind("<Configure>", agrandar_imagen)

        # Mostrar la imagen inicial (con el tamaño original)
        self.canva1.create_image(0, 0, image=self.imagen_tk, anchor="nw")

        # Ejecutar la ventana
        self.ventana.mainloop()

ejecutar=aplication8()