from tkinter import *

ventana=Tk()
ruta_image=r"C:\Users\ulise\OneDrive\Desktop\hola.gif"
ventana.title("Primer programa")
fondo="#000080"

ventana.config(bg=fondo)
ventana.geometry("250x250")
texto =Label(ventana, text="Bienvenidos a la primera interfaz con Python", bg=fondo, fg="white")

imagen=PhotoImage(file=ruta_image)
imagen_escalada=imagen.subsample(2,2)
texto.pack(side=LEFT)
imagen=Label(ventana, image=imagen_escalada)
imagen.pack(side=RIGHT)
ventana.mainloop()