from tkinter import *
from tkinter import messagebox
import sys
import mariadb
root=Tk()
root.title("Ventana principal")
root.geometry("300x200")
try:
    conexion = mariadb.connect(
        user="root", password="",
        host="127.0.0.1", port=3306,
        database="prueba"
    )
    Label(root, text="Se conecto con la base de datos "+ conexion.database + ".").pack()

    try:
        cursor = conexion.cursor()
        tabla1_sql = """
           CREATE TABLE IF NOT EXISTS empleadosa
        (idEmpleado INT NOT NULL AUTO_INCREMENT,
        nombre VARCHAR(220) NOT NULL,
        apellido VARCHAR(240) NOT NULL,
        edad INT NOT NULL,
        PRIMARY KEY(idEmpleado)
        )
        """
        cursor.execute(tabla1_sql)

        # Sentencia SQL para la segunda tabla
        tabla2_sql = """
            CREATE TABLE IF NOT EXISTS productosa (
                idProductos INT NOT NULL AUTO_INCREMENT,
                nombre VARCHAR(40) NOT NULL,
                precio decimal(10,2) NOT NULL,
                cantidad INT NOT NULL,
                PRIMARY KEY(idProductos)
                )
        """
        cursor.execute(tabla2_sql)

        # Sentencia SQL para la tercera tabla
        tabla3_sql = """
            CREATE TABLE IF NOT EXISTS proveedor (
            idProveedor INT NOT NULL AUTO_INCREMENT,
            nombre VARCHAR(40) NOT NULL,
            ciudad VARCHAR(40) NOT NULL,
            codigo INT NOT NULL,
            PRIMARY KEY(idProveedor)
            )
        """
        cursor.execute(tabla3_sql)
        conexion.commit()
        messagebox.showinfo("Éxito", "Se crearon correctamente las tablas")
    except mariadb.Error as error:
        messagebox.showerror("Error", "Error al crear las tablas: " + str(error))
except mariadb.Error as error:
    print(f"Error al conectar con la BD:{error}")
mainloop()