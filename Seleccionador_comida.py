#Seleccionador de comidas.

from tkinter import * #Importación de la librería de Tkinter
from tkinter import messagebox


def huevo():
    messagebox.showinfo("Desyuno de huevo", "El precio es de $5")

def tostadas():
    messagebox.showinfo("Desyuno de huevo", "El precio es de $5")


ventana=Tk()
ventana.title("Primer programa")
fondo="#FF5733"
#Definimos el color de fondo, tamaño de ventana y el primer label
ventana.config(bg=fondo)
ventana.geometry("600x600") 
texto =Label(ventana, text="Bienvenidos al seleccionador de comidas", bg=fondo, fg="white", font=(16))
texto.grid(row=0, column=1)

#Definimos la primera imagen y su boton y texto descriptivo
imagen01_desayuno=r"C:\Users\ulise\OneDrive\Desktop\python\desayuno1.png"
imagen1_desayuno=PhotoImage(file=imagen01_desayuno)
redimencion1=imagen1_desayuno.subsample(4,5)
imagen1=Label(ventana, image=redimencion1)
imagen1.grid(row=1, column=0)
Button(text="Ordenar", width=30, command=huevo, activebackground="green").grid(row=2,column=0, pady=3.5)

imagen02_desayuno=r"C:\Users\ulise\OneDrive\Desktop\python\desayuno2.png"
imagen2_desayuno=PhotoImage(file=imagen02_desayuno)
redimencion2=imagen2_desayuno.subsample(4,6)
imagen2=Label(ventana, image=redimencion2)
imagen2.grid(row=1, column=1)
Button(text="Ordenar", width=30, command=tostadas, activebackground="green").grid(row=2,column=1, pady=3.5)

ventana.mainloop()