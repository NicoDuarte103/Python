from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('Aviso de messagebox')
ws.geometry('300x200')
ws.config(bg='#5FB691')

def msg1():
    messagebox.showinfo('información', '¡Hola! Tienes un aviso.')
    messagebox.showerror('error', '¡Algo salió mal!')
    messagebox.showwarning('advertencia', 'aceptar T&C')
    messagebox.askquestion('Haz una pregunta', '¿Quieres continuar?')
    messagebox.askokcancel('Ok Cancelar', '¿Estás seguro?')
    messagebox.askyesno('Sí|No', '¿Desea continuar?')
    messagebox.askretrycancel('reintentar', '¡Error! ¿quieres intentarlo de nuevo?')

Button(ws, text='Hacer Click', command=msg1).pack(pady=50)

ws.mainloop()