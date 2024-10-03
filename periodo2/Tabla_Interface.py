from tkinter import *
from tkinter import messagebox
import mariadb
import sys
def crear_tabla():
    nombre_tabla=nombre_tabla_entry.get("1.0","end-1c")
    atributos=atributos_entry.get("1.0","end-1c")

    try:
        cursor=conexion.cursor()
        sentenciaSQL=f"""CREATE TABLE IF NOT EXISTS {nombre_tabla}
            (  
                {atributos}
                );"""
        cursor.execute(sentenciaSQL)
        conexion.commit()
        messagebox.showinfo("Éxito",f"Se creó correctamente la tabla {nombre_tabla}")
    except mariadb.Error as error:
        messagebox.showerror("Error","Error al crear la tabla, revisar la sintaxis SQL")
root=Tk()
root.title("Gestion de Colegios")
nombre_tabla_label =Label(root, text="Nombre de la tabla:")
nombre_tabla_label.grid()
nombre_tabla_entry= Text(root, height=2, wrap="word")
nombre_tabla_entry.grid()

atributos_label=Label(root, text="Atributos (Ejemplo: nombre VARCHAR(40) NOT NULL,...):")
atributos_label.grid()
atributos_entry =Text(root, height=5,wrap="word")
atributos_entry.grid()

crear_tabla_button=Button(root, text="Crear tabla", command=crear_tabla)
crear_tabla_button.grid()

try:
    conexion=mariadb.connect(
        user="root", password="",
        host="127.0.0.1", port=3306,
        database="Prueba"
    )
    Label(text="Conectado a la base de datos " + conexion.database, fg="green").grid()
except mariadb.Error as error:
    messagebox.showerror("Error", "Error de conexion. Revisar losdatos para la conexion")
    sys.exit(1)
root.mainloop()
