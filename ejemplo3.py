from tkinter import *
ventana = Tk()
ventana.title("Mi tercer programa")
fondo="lightblue"

marco1 = Frame(ventana)
marco1.config(bg="purple",width=480, height=320, relief="sunken", bd=25)
texto = Label(marco1, text="El texto quedara dentro del marco 1 de color celeste", justify=CENTER, bg=fondo)
texto.pack(fill="both", expand=1)
marco1.grid(row=1, column=0)
marco1.pack_propagate(0)
marco1.columnconfigure(0, weight=1)
marco1.rowconfigure(0, weight=1)
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)
marco2 = Frame(ventana)
marco2.config(bg="black",width=480, height=320, relief="sunken", bd=25)
marco2.grid(row=2, column=0)

ventana.mainloop()