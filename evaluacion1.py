from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mariadb
import sys
from tkinter import simpledialog
def mostrar_datos_empleados():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM empleados")
        datos = cursor.fetchall()

        # Crear una ventana secundaria para mostrar los datos en una tabla
        ventana_datos_empleados = Toplevel(root)
        ventana_datos_empleados.title("Datos de empleados")

        # Crear un Treeview para mostrar los datos en forma de tabla
        tabla_empleados = ttk.Treeview(ventana_datos_empleados, columns=("ID", "Nombre", "Apellido", "Edad"), show="headings")
        tabla_empleados.heading("ID", text="ID")
        tabla_empleados.heading("Nombre", text="Nombre")
        tabla_empleados.heading("Apellido", text="Apellido")
        tabla_empleados.heading("Edad", text="Edad")

        # Insertar los datos en la tabla
        for dato in datos:
            tabla_empleados.insert("", "end", values=dato)

        tabla_empleados.pack(expand=True, fill="both")

    except mariadb.Error as error:
        messagebox.showerror("Error", "Error al recuperar datos de empleados: " + str(error))

# Función para mostrar los datos de productos en una tabla
def mostrar_datos_productos():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        datos = cursor.fetchall()

        # Crear una ventana secundaria para mostrar los datos en una tabla
        ventana_datos_productos = Toplevel(root)
        ventana_datos_productos.title("Datos de productos")

        # Crear un Treeview para mostrar los datos en forma de tabla
        tabla_productos = ttk.Treeview(ventana_datos_productos, columns=("ID", "Nombre", "Precio", "Cantidad"), show="headings")
        tabla_productos.heading("ID", text="ID")
        tabla_productos.heading("Nombre", text="Nombre")
        tabla_productos.heading("Precio", text="Precio")
        tabla_productos.heading("Cantidad", text="Cantidad")

        # Insertar los datos en la tabla
        for dato in datos:
            tabla_productos.insert("", "end", values=dato)

        tabla_productos.pack(expand=True, fill="both")

    except mariadb.Error as error:
        messagebox.showerror("Error", "Error al recuperar datos de productos: " + str(error))

# Función para mostrar los datos de proveedores en una tabla
def mostrar_datos_proveedores():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM proveedor")
        datos = cursor.fetchall()

        # Crear una ventana secundaria para mostrar los datos en una tabla
        ventana_datos_proveedores = Toplevel(root)
        ventana_datos_proveedores.title("Datos de proveedores")

        # Crear un Treeview para mostrar los datos en forma de tabla
        tabla_proveedores = ttk.Treeview(ventana_datos_proveedores, columns=("ID", "Nombre", "Ciudad", "Código"), show="headings")
        tabla_proveedores.heading("ID", text="ID")
        tabla_proveedores.heading("Nombre", text="Nombre")
        tabla_proveedores.heading("Ciudad", text="Ciudad")
        tabla_proveedores.heading("Código", text="Código")

        # Insertar los datos en la tabla
        for dato in datos:
            tabla_proveedores.insert("", "end", values=dato)

        tabla_proveedores.pack(expand=True, fill="both")

    except mariadb.Error as error:
        messagebox.showerror("Error", "Error al recuperar datos de proveedores: " + str(error))

def crear_conexion():
    try:
        global conexion
        conexion=mariadb.connect(
            user=user_db_entry.get("1.0", "end-1c"), password=pass_db_entry.get("1.0", "end-1c"),
            host=host_db_entry.get("1.0", "end-1c"),  port=int(port_db_entry.get("1.0", "end-1c")),
            database=Db_db_entry.get("1.0", "end-1c")
        )
        Label(text="Conectado a la base de datos " + conexion.database, fg="green").grid()
    except mariadb.Error as error:
        messagebox.showerror("Error", "Error de conexion. Revisar losdatos para la conexion")
        sys.exit(1)

def crear_tabla():
    try:
        cursor = conexion.cursor()
        tabla1_sql = """
           CREATE TABLE IF NOT EXISTS empleados
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
            CREATE TABLE IF NOT EXISTS productos (
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
        messagebox.showinfo("Éxito","Se creó correctamente la tabla")
    except mariadb.Error as error:
        messagebox.showerror("Error","Error al crear la tabla: " + str(error))

def insertar_datos():
    try:
        cursor = conexion.cursor()
        nombre_tabla = nombre_tabla_entry.get("1.0", "end-1c")
        atributos = atributos_entry.get("1.0", "end-1c").replace("\n", "").replace(" ", "")
        atributos_separados = ", ".join(atributos.split(","))

        # Solicitar al usuario que ingrese los valores correspondientes a cada atributo
        valores_entrada = []
        for atributo in atributos.split(","):
            valor = simpledialog.askstring("Ingresar valor", f"Ingrese el valor para '{atributo}':")
            valores_entrada.append(valor)

        # Formatear los valores ingresados para que se ajusten a la consulta SQL
        valores_formateados = ", ".join([f"'{valor}'" for valor in valores_entrada])

        # Sentencia SQL para insertar datos en la tabla
        insert_query = f"INSERT INTO {nombre_tabla} ({atributos_separados}) VALUES ({valores_formateados});"
        cursor.execute(insert_query)

        conexion.commit()
        messagebox.showinfo("Éxito", "Se insertaron correctamente los datos")
    except mariadb.Error as error:
        messagebox.showerror("Error", "Error al insertar datos: " + str(error))

root=Tk()
root.title("Gestion de Colegios")
top1=Label(root, text="Conexion a base de datos", fg="Blue")
top1.grid()

user_db_label =Label(root, text="Usuario:")
user_db_label.grid()
user_db_entry= Text(root, height=2, wrap="word")
user_db_entry.grid()

pass_db_label =Label(root, text="Contraseña:")
pass_db_label.grid()
pass_db_entry= Text(root, height=2, wrap="word")
pass_db_entry.grid()

host_db_label =Label(root, text="Nombre del host:")
host_db_label.grid()
host_db_entry= Text(root, height=2, wrap="word")
host_db_entry.grid()

port_db_label =Label(root, text="Numero de puerto:")
port_db_label.grid()
port_db_entry= Text(root, height=2, wrap="word")
port_db_entry.grid()

Db_db_label =Label(root, text="Nombre de la Base de datos:")
Db_db_label.grid()
Db_db_entry= Text(root, height=2, wrap="word")
Db_db_entry.grid()

crear_db_button=Button(root, text="Conectar", command=crear_conexion)
crear_db_button.grid()
crear_tabla_button=Button(root, text="Crear tabla", command=crear_tabla)
crear_tabla_button.grid()
top2=Label(root, text="Insertar datos.", fg="Blue")
top2.grid()
nombre_tabla_label = Label(root, text="Nombre de la tabla:")
nombre_tabla_label.grid()
nombre_tabla_entry = Text(root, height=2, wrap="word")
nombre_tabla_entry.grid()

atributos_label = Label(root, text="Atributos (Separados por comas):")
atributos_label.grid()
atributos_entry = Text(root, height=5, wrap="word")
atributos_entry.grid()

insertar_datos_button = Button(root, text="Insertar datos", command=insertar_datos)
insertar_datos_button.grid()

boton_mostrar_empleados = Button(root, text="Mostrar datos de empleados", command=mostrar_datos_empleados)
boton_mostrar_empleados.grid()

boton_mostrar_productos = Button(root, text="Mostrar datos de productos", command=mostrar_datos_productos)
boton_mostrar_productos.grid()

boton_mostrar_proveedores = Button(root, text="Mostrar datos de proveedores", command=mostrar_datos_proveedores)
boton_mostrar_proveedores.grid()

root.mainloop()
