import tkinter as tk
import customtkinter as ctk
root = ctk.CTk()
toplevel = ctk.CTkToplevel(root)
frametop=ctk.CTkFrame(toplevel,width=200,height=100,corner_radius=20,fg_color="green")
frametop.pack(pady = 20,padx=20)
paciente_label = ctk.CTkLabel(frametop,text="paciente:  medico:   fecha turno:   hora turno:  ",corner_radius=20)
paciente_label.pack(pady = 20,padx=20)
root.mainloop()