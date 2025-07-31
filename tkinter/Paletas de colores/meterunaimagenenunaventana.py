import customtkinter as ctk
from PIL import Image, ImageTk

# Crear la clase de la ventana principal
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.title("Imagen con CustomTkinter")
        self.geometry("400x400")

        # Cargar la imagen usando Pillow
        self.image = Image.open("E:\pillow\ejercicios\sala.jpg")  # Cambia esto a la ruta de tu imagen
        self.photo = ImageTk.PhotoImage(self.image)

        # Crear un Label para mostrar la imagen
        self.label = ctk.CTkLabel(self, image=self.photo)
        self.label.pack(pady=20)

        # Puedes agregar más elementos aquí

# Ejecutar la aplicación
if __name__ == "__main__":
    app = App()
    app.mainloop()
