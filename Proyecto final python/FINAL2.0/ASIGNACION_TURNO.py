

import tkinter as tk 
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
from ELIMINACION import *
from ASIGANCION_PT3 import *
from turnos import *
class aplication3():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("ASIGNACIÓN DE TURNO")
        self.ventana.geometry("700x600")
        self.ventana.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.ventana.rowconfigure((0), weight=1)

        # Cargar la imagen original
        #self.imagen_1 = Image.open("imagenes_final2.0/logo.jpg")
        # Crear una variable global para almacenar la imagen redimensionada
        #self.imagen_tk = ImageTk.PhotoImage(self.imagen_1)

        #self.imagen_confi = Image.open("imagenes_final2.0/confirmado.jpg").resize((30,30))
        #self.imagen_confi_tk = ImageTk.PhotoImage(self.imagen_confi)

        def agrandar_imagen(event):
            # Obtener el nuevo tamaño de la ventana
            self.width = event.width
            self.height = event.height
            #print(f"Nuevo tamaño: {width}x{height}")
            
            # Redimensionar la imagen con los nuevos valores de ancho y alto
            #self.nueva_imagen = self.imagen_1.resize((self.width, self.height))
           # self.nueva_imagen_tk = ImageTk.PhotoImage(self.nueva_imagen)
            
            # Actualizar la imagen en el canvas
            #self.canva1.create_image(0, 0, image=self.nueva_imagen_tk, anchor="nw")
            
            # Necesitamos mantener la referencia a la nueva imagen para evitar que se elimine
            #self.canva1.image = self.nueva_imagen_tk  # Esto es necesario para evitar que la imagen se borre


        # Crear el frame para los botones
        self.frame = ttk.Frame(self.ventana)
        self.frame.grid(column=0, row=0, sticky="nsew")

        ##########################

        # Función para asignar el turno 
        def asignar_turno():
            self.especialidad = self.especialidad_combobox.get()
            self.medico = self.medico_combobox.get()
            print(f"Turno asignado para {self.especialidad} con  {self.medico}")

        # Lista de especialidades,medicos,fechas y horas
        
        self.paciente =  ["Juan Rodriguez", "Pedro Hernandez", "Joel Fernandez", "Miguel Fernandez"]
        self.medicos = ["Dr. Pérez (Cardiología)", "Dra. Gómez (Pediatría)", "Dr. López(Oftalmología)", "Dra. Suriano(Psicolgia)", "Dra. Mendez(Neurologia)", "Dr. Salvatierra(Traumatologia)"]
        self.fechas = ["17/12/24","18/12/24","19/12/24","20/12/24","21/12/24","22/12/24",]
        self.hora = ["10:30","11:30","12:30","13:30","14:30","15:30",]

        # Crear los combobox
        self.paciente_label = ttk.Label(master=self.frame, text="Paciente:", font=("Sitka Text Semibold", 15), foreground="Black")
        self.paciente_label.pack(pady=10)
        self.paciente_combobox = ttk.Combobox(master=self.frame, values=self.paciente)
        self.paciente_combobox.pack(pady=10)


        self.medico_label = ttk.Label(master=self.frame, text="Médico:", font=("Sitka Text Semibold", 15), foreground="Black")
        self.medico_label.pack(pady=10)
        self.medico_combobox = ttk.Combobox(master=self.frame, values=self.medicos)
        self.medico_combobox.pack(pady=10)

        self.fecha_label = ttk.Label(master=self.frame, text="Fecha:", font=("Sitka Text Semibold", 15), foreground="Black")
        self.fecha_label.pack(pady=10)
        self.fecha_combobox = ttk.Combobox(master=self.frame, values=self.fechas)
        self.fecha_combobox.pack(pady=10)
        
        self.hora_label = ttk.Label(master=self.frame, text="Hora:", font=("Sitka Text Semibold", 15), foreground="Black")
        self.hora_label.pack(pady=10)
        self.hora_combobox = ttk.Combobox(master=self.frame, values=self.hora)
        self.hora_combobox.pack(pady=10)
        
        
                    
        self.boton_asignar = ttk.Button(master=self.frame, width=50, text="ASIGNAR", compound="left", command=self.asignado)
        self.boton_asignar.pack(pady=5, padx=25)

        self.boton_modificar = ttk.Button(master=self.frame, width=50, text="MODIFICAR", compound="left", command=self.front_modificar)
        self.boton_modificar.pack(pady=5, padx=25)
        

        self.boton_eliminar = ttk.Button(master=self.frame, width=50, text="ELIMINAR", compound="left", command=self.front_eliminar_pacientes)
        self.boton_eliminar.pack(pady=5, padx=25)
        
        self.boton_nuevo = ttk.Button(master=self.frame, width=50, text="NUEVO", compound="left", command=self.front_nuevo)
        self.boton_nuevo.pack(pady=5, padx=25)


        #asignar_boton = ctk.CTkButton(master=ventana, text="Asignar Turno", command=asignar_turno)
        #asignar_boton.pack(pady=21)

        #########################
        # Crear el canvas para la imagen
        #self.canva1 = tk.Canvas(self.ventana, background="black")
        #self.canva1.grid(column=1, row=0, columnspan=3, sticky="nsew")
        #self.canva1.bind("<Configure>", agrandar_imagen)

        # Mostrar la imagen inicial (con el tamaño original)
        #self.canva1.create_image(0, 0, image=self.imagen_tk, anchor="nw")

        # Ejecutar la ventana
        self.ventana.mainloop()
    
    def front_modificar(self):
        self.ventana_modificar = tk.Toplevel(self.ventana)
        self.documento_paciente_modificar_label =ttk.Label(master=self.ventana_modificar, text="Documento paciente:", font=("Sitka Text Semibold", 15), foreground="Black") 
        self.documento_paciente_modificar_label.pack(pady=10)
        self.documento_paciente_modificar_entry =ctk.CTkEntry(master=self.ventana_modificar)
        self.documento_paciente_modificar_entry.pack(pady=10)
        

      

        self.fecha_modificar_label = ttk.Label(master=self.ventana_modificar, text="Fecha:", font=("Sitka Text Semibold", 15), foreground="Black")
        self.fecha_modificar_label.pack(pady=10)
        self.fecha_modificar_combobox = ttk.Combobox(master=self.ventana_modificar, values=self.fechas)
        self.fecha_modificar_combobox.pack(pady=10)
        
        self.hora_modificar_label = ttk.Label(master=self.ventana_modificar, text="Hora:", font=("Sitka Text Semibold", 15), foreground="Black")
        self.hora_modificar_label.pack(pady=10)
        self.hora_modificar_combobox = ttk.Combobox(master=self.ventana_modificar, values=self.hora)
        self.hora_modificar_combobox.pack(pady=10)
        self.boton_modificar_asignar = ttk.Button(master=self.ventana_modificar, width=50, text="ACEPTAR", compound="left",command=self.modificador_turnos_back)
        self.boton_modificar_asignar.pack(pady=5, padx=25)
    
    def front_nuevo(self):
        self.ventana_nuevo = tk.Toplevel(self.ventana)
        self.documento_paciente_nuevo_label =ttk.Label(master=self.ventana_nuevo, text="Documento paciente:", font=("Sitka Text Semibold", 15), foreground="Black") 
        self.documento_paciente_nuevo_label.pack(pady=10)
        self.documento_paciente_nuevo_entry = ttk.Entry(master=self.ventana_nuevo)
        self.documento_paciente_nuevo_entry.pack(pady=10)
        self.paciente_nuevo_label = ttk.Label(master=self.ventana_nuevo, text="Nombre de nuevo Paciente:", font=("Sitka Text Semibold", 15), foreground="Black")
        self.paciente_nuevo_label.pack(pady=10)
        self.paciente_nuevo_entry = ttk.Entry(master=self.ventana_nuevo)
        self.paciente_nuevo_entry.pack(pady=10)

        self.medico_nuevo_label = ttk.Label(master=self.ventana_nuevo, text="Médico:", font=("Sitka Text Semibold", 15), foreground="Black")
        self.medico_nuevo_label.pack(pady=10)
        self.medico_nuevo_combobox = ttk.Combobox(master=self.ventana_nuevo, values=self.medicos)
        self.medico_nuevo_combobox.pack(pady=10)

        self.fecha_nuevo_label = ttk.Label(master=self.ventana_nuevo, text="Fecha:", font=("Sitka Text Semibold", 15), foreground="Black")
        self.fecha_nuevo_label.pack(pady=10)
        self.fecha_nuevo_combobox = ttk.Combobox(master=self.ventana_nuevo, values=self.fechas)
        self.fecha_nuevo_combobox.pack(pady=10)
        
        self.hora_nuevo_label = ttk.Label(master=self.ventana_nuevo, text="Hora:", font=("Sitka Text Semibold", 15), foreground="Black")
        self.hora_nuevo_label.pack(pady=10)
        self.hora_nuevo_combobox = ttk.Combobox(master=self.ventana_nuevo, values=self.hora)
        self.hora_nuevo_combobox.pack(pady=10)
        self.boton_nuevo_asignar = ttk.Button(master=self.ventana_nuevo, width=50, text="ACEPTAR", compound="left",command=self.paciente_nuevo_back)
        self.boton_nuevo_asignar.pack(pady=5, padx=25)
        
    
    def front_eliminar_pacientes(self):
        self.ventana_eliminar = tk.Toplevel(self.ventana)
        

        self.documento_paciente_eliminar_label =ttk.Label(master=self.ventana_eliminar, text="Documento paciente:", font=("Sitka Text Semibold", 15), foreground="Black") 
        self.documento_paciente_eliminar_label.pack(pady=10)

        self.documento_paciente_eliminar_ = ttk.Entry(master=self.ventana_eliminar)
        self.documento_paciente_eliminar_.pack(pady=10)
        self.boton_eliminar = ttk.Button(master=self.ventana_eliminar, width=50, text="ACEPTAR", compound="left",command=self.cerrar_eliminar)
        self.boton_eliminar.pack(pady=5, padx=25)

   
       
    def cerrar_modificar(self):
        self.ventana_modificar.destroy()
    def cerrar_eliminar(self):
        self.ventana_eliminar.destroy()
        confirmar_eliminar()
    def asignado(self):
        confirmar_asignacion()
        paciente_nuevo_back()
    
    def asignador_turnos_back(self):
        
        self.nombres_entry=self.nombre_entry.get()
        self.documentos_entry=self.documento_entry.get() #este
        self.medicos_tratantes_entry=self.medico_tratante_entry.get()
        self.fechas_turnos_entry=self.fecha_turno_entry.get()
        self.horas_turnos_entry=self.hora_turno_entry.get()
        asignar_turno(self.nombres_entry,self.apellidos_entry,self.documentos_entry,self.medicos_tratantes_entry,self.fechas_turnos_entry,self.horas_turnos_entry)
    def eliminador_turnos_back(self):

        self.documentos_eliminar_turnos_entry=self.documento_eliminar_turno_entry.get()
        borrar_turno(self.documentos_eliminar_turnos_entry)

    def modificador_turnos_back(self):
        
        self.documentos_fechas_y_horas_a_modificar_entry=self.documento_paciente_modificar_entry.get()
        self.fechas_a_modificar_turnos_entry= self.fecha_modificar_combobox.get()
        self.horarios_a_modificar_turno_entry=self.hora_modificar_combobox.get()
        modificar_turno(self.fechas_a_modificar_turnos_entry,self.horarios_a_modificar_turno_entry,self.documentos_fechas_y_horas_a_modificar_entry)
        self.ventana_modificar.destroy()
    def paciente_nuevo_back(self):
        self.nombres_entry=self.paciente_nuevo_entry.get()
        self.documentos_entry=self.documento_paciente_nuevo_entry.get() #este
        self.medicos_tratantes_entry=self.medico_nuevo_combobox.get()
        self.fechas_turnos_entry= self.fecha_nuevo_combobox.get()
        self.horas_turnos_entry=self.hora_nuevo_combobox.get()
        asignar_turno(self.nombres_entry,self.documentos_entry,self.medicos_tratantes_entry,self.fechas_turnos_entry,self.horas_turnos_entry)
        self.ventana_nuevo.destroy()
        confirmar_asignacion()
#ejecutar3=aplication3()
def saludo():
    ejecutar3=aplication3()

