import tkinter as tk
import customtkinter as ctk
from PIL import Image,ImageTk
import time

class base():
    def __init__(self,root,toplevel):
        self.ventana = root
        self.entries = {}
        self.entriespack = {}
        self.labels = {}  # Diccionario para almacenar los Labels
        self.toplevel = toplevel
        self.listita = []
        #self.frametop = frametop
        
        self.lista_pacientes = []
        self.contador = 0
        self.cantidad = 0
        self.valor_final = 3
        self.frametop2=ctk.CTkFrame(self.toplevel,width=200,height=100,corner_radius=20,fg_color="red")
        self.frametop2.grid(pady = 20,padx=20,column=2,row=0)
        self.paciente_label2 = ctk.CTkLabel(self.frametop2,text="tetotin",corner_radius=20)
        self.paciente_label2.pack(padx=20,pady=20)

        self.frametop1=ctk.CTkFrame(self.toplevel,width=200,height=100,fg_color="blue")   
        self.borradora = self.frametop1.forget()


    def borrador(self):
        self.frametop1.destroy()

    
    def agregar_a_toplevel(self,paciente,medico,fecha_turno,hora_turno,rows,columns,listita,borrador):

        self.espaciador= ("-"*30)
        print ("soy la rows ",rows)
        print(listita)
        

        self.frametop1.grid(column=0,row=2,padx=20)
        self.label = ctk.CTkLabel(self.frametop1,text=f"tetan: {paciente}")
        self.label.grid(column=1,row=1,padx=10,pady=10)

        
        return self.frametop1,listita,self.label
        


    def borrar_label(self,cantidad,final):
        self.numero = 0
        self.contador = 0
        self.finale = final
        self.cantidad = cantidad-3
        
        for widget in self.toplevel.winfo_children():
            
            while self.contador < 3: #esto aumenta o disminuye la cantidad de turnos mosrtados,es un numero menos que el if de donde se llama esto
       
                widget.destroy()
                self.contador = self.contador+1
                print("soy el contador de widget",self.contador)
        
        self.contador = 0





    def agregar_boton(self,frame,titulo, comando, row, column):
        self.boton = tk.Button(frame, text=titulo, command=comando)
        self.boton.grid(row=row, column=column, padx=5, pady=5, sticky="w")

    def agregar_entry(self,frame ,nombre, row, column): 
        self.entry = tk.Entry(frame)
        self.entry.grid(row=row, column=column, padx=5, pady=5, sticky="ew")  # 'ew' para que el Entry se expanda horizontalmente
        self.entriespack[nombre] = self.entry

    def obtener_entry(self, nombre):
        self.entrada = self.entriespack[nombre].get()
        self.entries[nombre] = self.entrada
        print(self.entries[nombre])  # Verificar valor ingresado
        return self.entries[nombre]

    def agregar_label(self,frame ,cantidad_label, texto, row, column):
        for i in range(cantidad_label):
            self.agregar_texto = tk.Label(frame, text=texto)
            self.agregar_texto.grid(row=row, column=column, padx=5, pady=5, sticky="w")  # 'w' para alineación a la izquierda

    def actualizar_label(self, nombre_label, texto):
        if nombre_label in self.labels:
            self.labels[nombre_label].config(text=texto)  # Actualiza el texto del Label
        else:
            print(f"Label {nombre_label} no existe.")

class ventana1(base):
    def __init__(self, root,toplevel):
        super().__init__(root,toplevel)
        self.frame1 = tk.Frame(self.ventana)
        self.frame1.grid(row = 1 ,column = 0)
        self.frame2 = tk.Frame(self.ventana)
        self.frame2.grid(row = 0 ,column = 0)
        # Alinear "Usuario" y "Clave" encima de sus respectivos Entry
        self.agregar_label(self.frame1,1, "Usuario:", 1, 0)  # Label en la fila 0, columna 0
        self.agregar_entry(self.frame1,"usuario", 2, 0)      # Entry en la fila 1, columna 0

        self.agregar_label(self.frame1,1, "Clave:", 3, 0)    # Label en la fila 2, columna 0
        self.agregar_entry(self.frame1,"clave", 4, 0)        # Entry en la fila 3, columna 0

        # Botón de "Registrarse"
        self.agregar_boton(self.frame1,"Registrarse", self.siguiente, 5, 0)
        self.imagen = Image.open("ross.jpg")
        self.imagen2 =self.imagen.resize((100,100))
        self.imagentk = ImageTk.PhotoImage(self.imagen2)
        self.canvas1=tk.Canvas(self.frame2, width=100, height=100, background="black")
        self.canvas1.grid(column=0, row=0)
        self.canvas1.create_image(0, 0, image=self.imagentk, anchor="nw")


    def siguiente(self):
        # Obtener valores de los Entry
        self.obtener_entry("usuario")
        self.obtener_entry("clave")
        # le hace forgets a los widgets de la ventana
        for widget in self.ventana.winfo_children():
            if widget != self.toplevel:
                widget.destroy()

        # Crear una nueva ventana (ventana2)
   
        self.contador = 0
        self.valor_final = 0
        self.ventana2app = ventana2(root,toplevel,self.contador,self.valor_final)

class ventana2(base):
    def __init__(self, root,toplevel,contador,valor_final):
        super().__init__(root,toplevel)

        self.frame3 = tk.Frame(root)
        self.frame3.grid(row = 0 ,column = 0)
        self.frame2 = tk.Frame(root)
        self.frame2.grid(row = 0 ,column = 1)
        self.agregar_label(self.frame3, 1,"nombre paciente:", 0, 0)  # Label en la fila 0, columna 0
        self.agregar_entry(self.frame3,"paciente", 1, 0)      # Entry en la fila 1, columna 0

        self.agregar_label(self.frame3,1, "medico:", 2, 0)    # Label en la fila 2, columna 0
        self.agregar_entry(self.frame3,"medico", 3, 0) 
        self.agregar_label(self.frame3,1, "fecha_turno:", 4, 0)  # Label en la fila 0, columna 0
        self.agregar_entry(self.frame3,"fecha_turno", 5, 0)      # Entry en la fila 1, columna 0

        self.agregar_label(self.frame3,1, "Hora_turno:", 6, 0)    # Label en la fila 2, columna 0
        self.agregar_entry(self.frame3,"Hora_turno", 7, 0)     
        # Agregar un botón para regresar a ventana1
        self.agregar_boton(self.frame3,"Volver a ventana 1", self.anterior, 8, 0)
        self.agregar_boton(self.frame3,"ir a ventana 3", self.siguiente_ventana3, 9, 0)
        self.imagen = Image.open("ross.jpg")
        self.imagen2 =self.imagen.resize((300,300))
        self.imagentk = ImageTk.PhotoImage(self.imagen2)
        self.canvas1=tk.Canvas(self.frame2, width=300, height=300,background="black")
        self.canvas1.grid(column=0, row=0)
        self.canvas1.create_image(0, 0, image=self.imagentk, anchor="nw")
        self.contador=contador+1
        self.valor_final = valor_final+1


    def anterior(self):
        # le hace forgets a los widgets de la ventana
        for widget in self.ventana.winfo_children():
            if widget != self.toplevel:
                widget.destroy()
        # Crear una nueva ventana (ventana1)

        self.ventanaapp1 = ventana1(root)
    
        
    


    def siguiente_ventana3(self):

        self.obtener_entry("paciente")
        self.obtener_entry("medico")
        self.obtener_entry("fecha_turno")
        self.obtener_entry("Hora_turno")
        paciente = self.entries.get("paciente", "No ingresado")
        medico = self.entries.get("medico", "No ingresado")
        fecha_turno = self.entries.get("fecha_turno", "No ingresado")
        hora_turno = self.entries.get("Hora_turno", "No ingresado")
        # le hace forgets a los widgets de la ventana
        for widget in self.ventana.winfo_children():
            if widget != self.toplevel:
                widget.destroy()
                    
            else:
                self.contador_rows= self.contador
                self.listita.append(paciente)
                self.listita.append(medico)
                self.listita.append(fecha_turno)
                self.listita.append(hora_turno)
                self.agregar_a_toplevel(paciente,medico,fecha_turno,hora_turno,self.contador_rows,0,self.listita,self.borrador)
               
                if self.contador == 4:
                    print("soy el valor final bucle",self.valor_final)
                    self.cantidad = self.contador
                    self.valor_finalfunc = self.valor_final
                    self.multiplicador = int(((self.valor_finalfunc)/(self.cantidad))*3)
                    print("soy el cotnador del bucle",self.cantidad)
                    self.contador = 0
  
                    print("soy el multiplciador del bucle",self.multiplicador)
                    self.borrar_label(self.cantidad,self.multiplicador)
        
        print("soy el contador",self.contador)
        print("soy el valor final",self.valor_final)
        



          
        # Crear una nueva ventana (ventana1)
        self.ventanaapp3 = ventana3(root,paciente,medico,fecha_turno,hora_turno,toplevel,self.contador,self.valor_final)
        return paciente,medico,fecha_turno,hora_turno,self.listita
        

class ventana3(base):
    def __init__(self, root,paciente,medico,fecha,hora,toplevel,contador,valor_final):
        super().__init__(root,toplevel)
        self.frame1 = tk.Frame(self.ventana)
        self.frame1.grid(row = 0 ,column = 0)
        self.frame2 = tk.Frame(self.ventana)
        self.frame2.grid(row = 0 ,column = 1)

        print(paciente,medico,fecha,hora)  
        # Imprimir el valor ingresado en el Entry
        self.agregar_label(self.frame1,1, "Paciente:", 1, 0)
        self.agregar_label(self.frame1,1, paciente, 2, 0)
        self.agregar_label(self.frame1,1, "Medico:", 3, 0)
        self.agregar_label(self.frame1,1, medico, 4, 0)
        self.agregar_label(self.frame1,1, "Fecha:", 5, 0)
        self.agregar_label(self.frame1,1, fecha, 6, 0)
        self.agregar_label(self.frame1,1, "Hora:", 7, 0)
        self.agregar_label(self.frame1,1, hora, 8, 0)

        

        self.agregar_boton(self.frame1,"Volver a ventana 2", self.anterior, 9, 0)
        self.agregar_boton(self.frame1,"siguente ventana 2 para pruebas", self.siguiente_ventana4, 10, 0)

            


        self.contador = contador
        self.valor_final = valor_final
        self.imagen = Image.open("ross.jpg")
        self.imagen2 =self.imagen.resize((300,300))
        self.imagentk = ImageTk.PhotoImage(self.imagen2)
        self.canvas1=tk.Canvas(self.frame2, width=300, height=300,background="black")
        self.canvas1.grid(column=0, row=0)
        self.canvas1.create_image(0, 0, image=self.imagentk, anchor="nw")

    def anterior(self):

        # le hace forgets a los widgets de la ventana
        for widget in self.ventana.winfo_children():
  
            widget.destroy()

        self.ventanaapp1 = ventana2(root)

    def siguiente_ventana4(self):
        # le hace forgets a los widgets de la ventana
        for widget in self.ventana.winfo_children():
            if widget != self.toplevel:
                widget.destroy()

        # Crear una nueva ventana (ventana1)
        self.ventanaapp1 = ventana2(root,toplevel,self.contador,self.valor_final)






# Ejecutar la ventana inicial
root = ctk.CTk()
toplevel = ctk.CTkToplevel(root)


ejecutar = ventana1(root,toplevel)








root.mainloop()
