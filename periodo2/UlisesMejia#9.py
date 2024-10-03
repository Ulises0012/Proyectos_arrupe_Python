from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sys
import mariadb
#-------------------Funcion para crear la conexion a la base de datos--------------------------
def crear_conexion():
    try:
        global conexion
        conexion = mariadb.connect(
            user=user_db_entry.get("1.0", "end-1c"), password=pass_db_entry.get("1.0", "end-1c"),
            host=host_db_entry.get("1.0", "end-1c"), port=int(port_db_entry.get("1.0", "end-1c")),
            database=Db_db_entry.get("1.0", "end-1c")
        )
        messagebox.showinfo("Éxito", "Conectado a la base de datos " + conexion.database)

    except mariadb.Error as error:
        messagebox.showerror("Error", "Error de conexión. Revisar los datos para la conexión")
        
#--------------------------Funcion para crear la ventana donde se muestran las entradas para la conexiona la base de datos------
def ventana_conexion():
    global conexionventana
    conexionventana = tk.Toplevel(root)
    conexionventana.title("Conexion a la BD")
    conexionventana.geometry("450x400")

    ancho_maximo_caracteres = 50

    Label(conexionventana, text="      ").grid(row=0, column=0, rowspan=11)

    global user_db_entry, pass_db_entry, host_db_entry, port_db_entry, Db_db_entry
    user_db_label = Label(conexionventana, text="Usuario:")
    user_db_label.grid(row=1, column=1)
    user_db_entry = Text(conexionventana, height=2, width=ancho_maximo_caracteres, wrap="word")
    user_db_entry.grid(row=2, column=1)

    pass_db_label = Label(conexionventana, text="Contraseña:")
    pass_db_label.grid(row=3, column=1)
    pass_db_entry = Text(conexionventana, height=2, width=ancho_maximo_caracteres, wrap="word")
    pass_db_entry.grid(row=4, column=1)

    host_db_label = Label(conexionventana, text="Nombre del host:")
    host_db_label.grid(row=5, column=1)
    host_db_entry = Text(conexionventana, height=2, width=ancho_maximo_caracteres, wrap="word")
    host_db_entry.grid(row=6, column=1)

    port_db_label = Label(conexionventana, text="Numero de puerto:")
    port_db_label.grid(row=7, column=1)
    port_db_entry = Text(conexionventana, height=2, width=ancho_maximo_caracteres, wrap="word")
    port_db_entry.grid(row=8, column=1)

    Db_db_label = Label(conexionventana, text="Nombre de la Base de datos:")
    Db_db_label.grid(row=9, column=1)
    Db_db_entry = Text(conexionventana, height=2, width=ancho_maximo_caracteres, wrap="word")
    Db_db_entry.grid(row=10, column=1)

    conectar_button = tk.Button(conexionventana, text="Conectar BD", command=crear_conexion)
    conectar_button.grid(row=11, columnspan=2, pady=5)

TIPOS_DATOS = ['VARCHAR', 'INT', 'FLOAT', 'DATE', 'BOOLEAN']  #Array con los tipos de datos que se pueden seleccionar.

# -----------------------------Función para la creación de una nueva tabla en la base de datos--------------------------
def crear_tabla():
    global conexion
    nombre_tabla = nombre_tabla_entry.get().strip()
    atributos = []

    for entry in atributos_entries:
        nombre_atributo = entry[0].get().strip()
        tipo_dato = entry[1].get()
        if nombre_atributo and tipo_dato:
            atributos.append(f"{nombre_atributo} {tipo_dato}")

    try:
        cursor = conexion.cursor()
        setenciaSQL = f"CREATE TABLE IF NOT EXISTS {nombre_tabla} ({', '.join(atributos)});"
        cursor.execute(setenciaSQL)
        conexion.commit()
        messagebox.showinfo("Éxito", f"Se creó la tabla '{nombre_tabla}' correctamente")
        crearventana.destroy()
    except mariadb.Error as error:
        messagebox.showerror("Error", f"Error al crear la tabla: {error}")

# Función para agregar campos de atributos dinámicamente
def agregar_atributos():
    num_atributos = int(atributos_entry.get().strip())
    for i in range(num_atributos):
        label_nombre = tk.Label(crearventana, text=f"Nombre Atributo {i+1}:")
        label_nombre.grid(row=4+i, column=1, sticky="e")
        entry_nombre = tk.Entry(crearventana)
        entry_nombre.grid(row=4+i, column=2)

        label_tipo = tk.Label(crearventana, text=f"Tipo Atributo {i+1}:")
        label_tipo.grid(row=4+i, column=3, sticky="e")
        combo_tipo = ttk.Combobox(crearventana, values=TIPOS_DATOS)
        combo_tipo.grid(row=4+i, column=4)

        # Configurar el evento de clic del Combobox
        combo_tipo.bind("<<ComboboxSelected>>", lambda event, combobox=combo_tipo: seleccionar_tipo(combobox))

        atributos_entries.append((entry_nombre, combo_tipo))

    # Mover el botón "Crear Tabla" hacia abajo según el número de atributos agregados
    crear_tabla_button.grid(row=4+num_atributos+1, columnspan=2, pady=5)

# Función para manejar la selección de tipo de dato en el Combobox
def seleccionar_tipo(combobox):
    tipo_seleccionado = combobox.get()
    if tipo_seleccionado == 'VARCHAR':
        combobox.config(state="normal")  # Permite escribir en el Combobox
    elif tipo_seleccionado=='INT':
        combobox.config(state="normal")
    elif tipo_seleccionado=='FLOAT':
        combobox.config(state="normal")
    elif tipo_seleccionado=='DATE':
        combobox.config(state="normal")
    elif tipo_seleccionado=='BOOLEAN':
        combobox.config(state="normal")
    else:
        combobox.config(state="readonly")

# Función para crear la ventana en la cual se ingresan los datos para crear la nueva tabla
def ventana_crear_tabla():
    global crearventana
    global atributos_entry
    global nombre_tabla_entry
    global atributos_entries
    
    crearventana = tk.Toplevel(root)
    crearventana.title("Crear tabla")
    crearventana.geometry("650x600")

    tk.Label(crearventana, text="      ").grid(row=0, column=0, rowspan=11)

    tk.Label(crearventana, text="Nombre tabla:").grid(row=0, column=1)
    nombre_tabla_entry = tk.Entry(crearventana)
    nombre_tabla_entry.grid(row=0, column=2)

    tk.Label(crearventana, text="Numero de atributos:").grid(row=3, column=1)
    atributos_entry = tk.Entry(crearventana)
    atributos_entry.grid(row=3, column=2)

    atributos_entries = []  # Lista para almacenar las entradas de atributos dinámicos

    # Botón para agregar campos de atributos dinámicamente
    agregar_atributos_button = tk.Button(crearventana, text="Agregar Atributos", command=agregar_atributos)
    agregar_atributos_button.grid(row=3, column=3)

    global crear_tabla_button
    crear_tabla_button = tk.Button(crearventana, text="Crear Tabla", command=crear_tabla)


    crear_tabla_button.grid(row=5, columnspan=2, pady=5)
#-------------Funcion para poder hacer consutas a la BD-----------
def acciones():
    def obtener_datos():
        tabla_seleccionada = tabla_combobox.get()
        for widget in frame_datos_tabla.winfo_children():
            widget.destroy()

        if tabla_seleccionada:
            try:
                cursor = conexion.cursor()
                cursor.execute(f"SELECT * FROM `{tabla_seleccionada}`")
                datos_tabla = cursor.fetchall()

                columnas = [i[0] for i in cursor.description]

                for i, columna in enumerate(columnas):
                    nombre_columna = columna
                    etiqueta_columna = Label(frame_datos_tabla, text=nombre_columna, font=("Arial", 10, "bold"))
                    etiqueta_columna.grid(row=0, column=i, padx=5, pady=5)

                for fila_idx, fila in enumerate(datos_tabla):
                    for columna_idx, valor in enumerate(fila):
                        etiqueta_valor = Label(frame_datos_tabla, text=valor)
                        etiqueta_valor.grid(row=fila_idx + 1, column=columna_idx, padx=5, pady=5)
            except mariadb.Error as e:
                messagebox.showerror("Error", f"Error al obtener los datos de la tabla: {e}")
        else:
            messagebox.showerror("Error", "Por favor, seleccione una tabla")

    ventana_mostrar_datos = tk.Toplevel()  
    ventana_mostrar_datos.title("Mostrar datos de la tabla")
    
    frame_combobox = Frame(ventana_mostrar_datos)
    frame_combobox.grid(row=0, column=0, padx=10, pady=10)
    
    tabla_combobox = ttk.Combobox(frame_combobox, values=[])  
    tabla_combobox.grid(row=0, column=0, padx=5, pady=5)

    obtener_datos_button = Button(frame_combobox, text="Obtener datos", command=obtener_datos)
    obtener_datos_button.grid(row=0, column=1, padx=5, pady=5)

    frame_datos_tabla = Frame(ventana_mostrar_datos)
    frame_datos_tabla.grid(row=1, padx=10, pady=10)
    
    try:
        cursor = conexion.cursor()
        cursor.execute("SHOW TABLES")
        tablas = [tabla[0] for tabla in cursor.fetchall()]
        tabla_combobox['values'] = tablas  
    except mariadb.Error as e:
        messagebox.showerror("Error", f"Error al obtener las tablas: {e}")
#------------Funcion para mostrar atributos--------
atributo_entries = {}  # Definir el diccionario de atributo_entries fuera de las funciones

def atributos():
    ventanaAtributos = tk.Toplevel(root)
    ventanaAtributos.title("Atributos de la Tabla")
    ventanaAtributos.geometry("450x400")

    Label(ventanaAtributos, text="Seleccione una tabla:").grid(row=0, column=0, columnspan=2)

    # Obtener la lista de tablas de la base de datos
    try:
        cursor = conexion.cursor()
        cursor.execute("SHOW TABLES;")
        tablas = [tabla[0] for tabla in cursor.fetchall()]
    except mariadb.Error as error:
        messagebox.showerror("Error", f"Error al obtener las tablas: {error}")
        return

    # Crear combobox para seleccionar la tabla
    combobox_tablas_atributos = ttk.Combobox(ventanaAtributos, values=tablas)
    combobox_tablas_atributos.grid(row=1, column=0, columnspan=2, pady=5)

    # Definir función para mostrar los atributos
    def mostrar_atributos(event=None):
        tabla_seleccionada = combobox_tablas_atributos.get()
        if tabla_seleccionada:
            try:
                cursor = conexion.cursor()
                cursor.execute(f"DESCRIBE {tabla_seleccionada};")
                atributos = [atributo[0] for atributo in cursor.fetchall()]

                for i, atributo in enumerate(atributos):
                    atributo_label = Label(ventanaAtributos, text=atributo)
                    atributo_label.grid(row=i + 3, column=0, pady=5)

                    atributo_entry = Entry(ventanaAtributos)
                    atributo_entry.grid(row=i + 3, column=1, pady=5)

                    atributo_entries[atributo] = atributo_entry  # Guardar el Entry en el diccionario

                # Botón para enviar los datos a la BD
                boton_insertar = Button(ventanaAtributos, text="Insertar Datos", command=lambda: insertar_datos(tabla_seleccionada, atributos))
                boton_insertar.grid(row=i + 4, columnspan=2, pady=5)

            except mariadb.Error as error:
                messagebox.showerror("Error", f"Error al obtener los atributos de la tabla: {error}")
        else:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tabla")

    # Asociar la función mostrar_atributos al evento de selección del combobox
    combobox_tablas_atributos.bind("<<ComboboxSelected>>", mostrar_atributos)

def insertar_datos(tabla, atributos):
    valores = []
    for atributo in atributos:
        valor = atributo_entries[atributo].get()
        valores.append(valor)

    try:
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO {tabla} ({', '.join(atributos)}) VALUES ({', '.join(['%s']*len(atributos))})", valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Datos insertados correctamente en la tabla.")
    except mariadb.Error as error:
        messagebox.showerror("Error", f"Error al insertar datos en la tabla: {error}")

    # Limpiar los campos de entrada después de la inserción
    for entry in atributo_entries.values():
        entry.delete(0, 'end')
root = Tk()
root.title("Ventana principal")
root.geometry("250x400")

Label(root, text="      ").grid(row=0, column=0, rowspan=11)

bienvenidaLabel = Label(root, text="Bienvenido/a al menú de selección")
bienvenidaLabel.grid(row=0, column=1)

# Centrar el botón en la ventana principal
boton_conexion = Button(root, text="Conexion a la BD", command=ventana_conexion)
boton_conexion.grid(row=2, column=1, pady=20)  # Añadir pady para espacio vertical

boton_crear_tabla = Button(root, text="Crear tabla nueva", command=ventana_crear_tabla)
boton_crear_tabla.grid(row=3, column=1, pady=20)  # Añadir pady para espacio vertical


boton_accion = Button(root, text="Consulta", command=acciones)
boton_accion.grid(row=4, column=1, pady=20)  # Añadir pady para espacio vertical


boton_accion = Button(root, text="Agregar elementos", command=atributos)
boton_accion.grid(row=5, column=1, pady=20)  # Añadir pady para espacio vertical

root.mainloop()