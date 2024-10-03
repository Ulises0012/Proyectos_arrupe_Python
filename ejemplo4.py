from tkinter import *
ventana = Tk()


marco_principal1 =Frame()
marco_principal1.grid(row=0, column=0)
marco_principal1.config(width="100", height='100')
marco_principal1.config(bg="red")

marco_principal2 = Frame()
marco_principal2.grid(row=1, column=0)
marco_principal2.config(width="100", height='100')
marco_principal2.config(bg="blue")


marco_principal3 = Frame()
marco_principal3.grid(row=1, column=1)
marco_principal3.config(width="100", height='100')
marco_principal3.config(bg="yellow")


marco_principal3 = Frame()
marco_principal3.grid(row=2, column=0)
marco_principal3.config(width="100", height='100')
marco_principal3.config(bg="green")

ventana.mainloop()