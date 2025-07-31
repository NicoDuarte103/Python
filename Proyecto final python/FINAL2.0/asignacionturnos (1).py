import customtkinter as ctk

# Configuración de la apariencia
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  
class aplication4():
    def __init__(self):
        # Crear la ventana principal
        self.app = ctk.CTk()
        self.app.geometry("700x600")
        self.app.title("Asignación de Turnos")

        # Función para asignar el turno 
        def asignar_turno():
            self.especialidad = self.especialidad_combobox.get()
            self.medico = self.medico_combobox.get()
            print(f"Turno asignado para {especialidad} con  {medico}")

        # Lista de especialidades y médicos 
        self.especialidades = ["Cardiología", "Pediatría", "Oftalmología", "Psicología", "Anticónceptivos"]
        self.medicos = ["Dr. Pérez", "Dra. Gómez", "Dr. López", "Dra. Suriano", "Dra. Mendez", "Rte. Salvatierra"]

        # Crear los combobox
        self.especialidad_label = ctk.CTkLabel(master=self.app, text="Especialidad:")
        self.especialidad_label.pack(pady=10)
        self.especialidad_combobox = ctk.CTkComboBox(master=self.app, values=self.especialidades)
        self.especialidad_combobox.pack(pady=10)

        self.medico_label = ctk.CTkLabel(master=self.app, text="Médico:")
        self.medico_label.pack(pady=10)
        self.medico_combobox = ctk.CTkComboBox(master=self.app, values=self.medicos)
        self.medico_combobox.pack(pady=10)

        # Botón para asignar el turno
        self.asignar_boton = ctk.CTkButton(master=self.app, text="Asignar Turno", command=asignar_turno)
        self.asignar_boton.pack(pady=20)

        self.app.mainloop()
ejecutar4= aplication4()