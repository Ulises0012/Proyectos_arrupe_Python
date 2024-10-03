from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mariadb
import datetime

def Crearusuario():
    sql = "INSERT INTO Usuarios (Nombre, Apellido, Gmail, Pass, UserName) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(nombre_entry.get(),apellido_entry.get(),correo_entry.get(),pass_entry.get(),user_entry.get())
    try:
        cursor.execute(sql)
        conexion.commit()
        messagebox.showinfo(message='Usuario creado')
    except:
        conexion.rollback()
        messagebox.showinfo(message='Error al crear, usuario no creado')

def ventana_usuario():
    global usuarioventana
    usuarioventana = tk.Toplevel(root)
    usuarioventana.title("Creacion usuario")
    usuarioventana.geometry("450x400")

    global nombre_entry, apellido_entry, correo_entry, pass_entry, user_entry

    nombre_entry = StringVar()
    apellido_entry = StringVar()
    correo_entry = StringVar()
    pass_entry = StringVar()
    user_entry = StringVar()

    Label(usuarioventana, text="      ").grid(row=0, column=0, rowspan=11)
    nombre_label = Label(usuarioventana, text="Nombre:")
    nombre_label.grid(row=1, column=1)
    nombre_entry = Entry(usuarioventana, width=50)
    nombre_entry.grid(row=2, column=1)

    apellido_label = Label(usuarioventana, text="Apellido:")
    apellido_label.grid(row=3, column=1)
    apellido_entry = Entry(usuarioventana, width=50)
    apellido_entry.grid(row=4, column=1)

    correo_label = Label(usuarioventana, text="Correo:")
    correo_label.grid(row=5, column=1)
    correo_entry = Entry(usuarioventana, width=50)
    correo_entry.grid(row=6, column=1)
    
    pass_label = Label(usuarioventana, text="Contraseña:")
    pass_label.grid(row=7, column=1)
    pass_entry = Entry(usuarioventana, width=50, show="*")
    pass_entry.grid(row=8, column=1)

    user_label = Label(usuarioventana, text="Nombre usuario:")
    user_label.grid(row=9, column=1)
    user_entry = Entry(usuarioventana, width=50)
    user_entry.grid(row=10, column=1)

    conectar_button = tk.Button(usuarioventana, text="Crear Usuario", command=Crearusuario)
    conectar_button.grid(row=11, columnspan=2, pady=5)

def Login():
    cursor.execute("SELECT Pass FROM Usuarios WHERE UserName='"+user_verify.get()+"' and Pass='"+pass_verify.get()+"'")
    if cursor.fetchall():
        messagebox.showinfo(message="Bienvenido " + user_verify.get())
        Ventana_tema()
    else:
        messagebox.showinfo(message="Error al iniciar sesión, verificar contraseña o usuario")

def Ventana_tema():
    ventanaTema = tk.Toplevel(root)
    ventanaTema.title("FORUMASTER")
    ventanaTema.geometry("500x600")

    global Tema_combobox, respuestas_label, descripcion_label, all_responses_button

    Tema_label = Label(ventanaTema, text="Temas:")
    Tema_label.grid(row=0, column=0)
    Tema_combobox = ttk.Combobox(ventanaTema)
    Tema_combobox.grid(row=0, column=1)
    Tema_combobox.bind("<<ComboboxSelected>>", mostrar_descripcion)

    SeleccionarTema()

    descripcion_label = Label(ventanaTema, text="", wraplength=400, justify=LEFT)
    descripcion_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    entrar_button = tk.Button(ventanaTema, text="Entrar", command=cargar_discusiones)
    entrar_button.grid(row=2, columnspan=2, pady=5)

    all_responses_button = tk.Button(ventanaTema, text="Mostrar todas las respuestas", command=mostrar_todas_respuestas)
    all_responses_button.grid(row=3, columnspan=2, pady=5)
    all_responses_button.grid_remove()

    respuestas_frame = Frame(ventanaTema)
    respuestas_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    canvas = Canvas(respuestas_frame)
    scrollbar = Scrollbar(respuestas_frame, orient="vertical", command=canvas.yview)
    respuestas_label = Frame(canvas)

    respuestas_label.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=respuestas_label, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

def SeleccionarTema():
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT Nombre FROM Temas")
        Temas = [row[0] for row in cursor.fetchall()]
        Tema_combobox['values'] = Temas
    except mariadb.Error as error:
        messagebox.showerror("Error", f"Error al cargar títulos: {error}")
    finally:
        cursor.close()

def mostrar_descripcion(event=None):
    Tema_seleccionado = Tema_combobox.get()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT Descripcion FROM Temas WHERE Nombre = ?", (Tema_seleccionado,))
        descripcion = cursor.fetchone()
        if descripcion:
            descripcion_label.config(text=descripcion[0])
        else:
            descripcion_label.config(text="No hay descripción disponible para este tema.")
    except mariadb.Error as error:
        messagebox.showerror("Error", f"Error al cargar descripción: {error}")
    finally:
        cursor.close()

def cargar_discusiones():
    Tema_seleccionado = Tema_combobox.get()
    limpiar_respuestas()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT R.UserName, R.Respuestas, R.Fecha FROM Respuestas R JOIN Temas T ON R.TemaID = T.TemaID WHERE T.Nombre = ? LIMIT 5", (Tema_seleccionado,))
        respuestas = cursor.fetchall()
        for row in respuestas:
            respuesta_text = f"{row[0]} dijo: {row[1]} ({row[2]})"
            respuesta_label = Label(respuestas_label, text=respuesta_text, wraplength=400, justify=LEFT, bg="white")
            respuesta_label.pack(fill='x', padx=5, pady=5)
        all_responses_button.grid()
    except mariadb.Error as error:
        messagebox.showerror("Error", f"Error al cargar discusiones: {error}")
    finally:
        cursor.close()

def mostrar_todas_respuestas():
    Tema_seleccionado = Tema_combobox.get()
    limpiar_respuestas()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT R.UserName, R.Respuestas, R.Fecha FROM Respuestas R JOIN Temas T ON R.TemaID = T.TemaID WHERE T.Nombre = ?", (Tema_seleccionado,))
        respuestas = cursor.fetchall()
        for row in respuestas:
            respuesta_text = f"{row[0]} dijo: {row[1]} ({row[2]})"
            respuesta_label = Label(respuestas_label, text=respuesta_text, wraplength=400, justify=LEFT, bg="white")
            respuesta_label.pack(fill='x', padx=5, pady=5)
    except mariadb.Error as error:
        messagebox.showerror("Error", f"Error al cargar todas las discusiones: {error}")
    finally:
        cursor.close()


def limpiar_respuestas():
    for widget in respuestas_label.winfo_children():
        widget.destroy()

root = Tk()
root.title("Ventana principal")
root.geometry("640x150")

try:
    conexion = mariadb.connect(
        user="root", password="",
        host="127.0.0.1", port=3306,
        database="foro"
    )
except mariadb.Error as error:
    print(f"Error al conectar con la BD:{error}")

try:
    cursor = conexion.cursor()
    TablaUsuario = """
        CREATE TABLE IF NOT EXISTS Usuarios
        (UsuarioID INT NOT NULL AUTO_INCREMENT,
        Nombre VARCHAR(120) NOT NULL,
        Apellido VARCHAR(140) NOT NULL,
        Gmail VARCHAR(150) NOT NULL,
        Pass VARCHAR(40) NOT NULL,
        UserName VARCHAR(30) NOT NULL,
        PRIMARY KEY(UsuarioID)
        )
        """
    cursor.execute(TablaUsuario)
except mariadb.Error as error:
    messagebox.showerror("Error", "Error al crear las tablas: " + str(error))

try:
    cursor = conexion.cursor()
    TablaTemas = """
        CREATE TABLE IF NOT EXISTS Temas
        (TemaID INT NOT NULL AUTO_INCREMENT,
        Nombre VARCHAR(120) NOT NULL UNIQUE,
        Descripcion VARCHAR(250) NOT NULL,
        PRIMARY KEY(TemaID)
        )
        """
    cursor.execute(TablaTemas)
except mariadb.Error as error:
    messagebox.showerror("Error", "Error al crear las tablas: " + str(error))

try:
    cursor = conexion.cursor()
    TablaRespuesta = """
        CREATE TABLE IF NOT EXISTS Respuestas
        (RespuestaID INT NOT NULL AUTO_INCREMENT,
        UserName VARCHAR(30) NOT NULL,
        TemaID INT NOT NULL,
        Respuestas VARCHAR(250) NOT NULL,
        Fecha DATE NOT NULL,
        PRIMARY KEY(RespuestaID),
        CONSTRAINT fk_Tema FOREIGN KEY (TemaID) REFERENCES Temas (TemaID)
        )
        """
    cursor.execute(TablaRespuesta)
except mariadb.Error as error:
    messagebox.showerror("Error", "Error al crear las tablas: " + str(error))

sql = '''INSERT INTO Temas (Nombre, Descripcion) VALUES
 ('Deportes', '¿Por qué Messi es el mejor futbolista?'),
 ('Cine', '¿Crees que Deadpool 3 estará a la altura de las expectativas?'),
 ('Musica', '¿Peso Pluma cambió por amor o por gusto personal?'),
 ('Vehiculos', '¿Qué opinas que Audi participará en la F1 la próxima temporada?')'''
try:
    cursor = conexion.cursor()
    cursor.execute(sql)
    conexion.commit()
except mariadb.Error as error:
    conexion.rollback()

sqlRespuestas1 = '''
    INSERT INTO Respuestas (UserName, TemaID, Respuestas, Fecha) VALUES (?, ?, ?, ?)
'''
respuestas = [
    ('Juancito22', 1, 'Yo diria que es el mejor ya que tiene un mundial', '2024-01-22'),
    ('Noobmaster69', 1, 'Yo diria que es el mejor ya que Messi hizo grande al barca', '2024-02-02'),
    ('El_Bichito_SIUUUU', 1, 'Yo diria que no es el mejor', '2024-01-12'),
    ('Marcos', 1, 'Cuando es el proximo mundial?', '2024-01-22'),
    ('Julian2', 1, 'POr sus goles y asistencias', '2024-01-20'),
    ('Marc23', 1, 'Algun dia hubo debate', '2024-01-21'),
    ('Juancito22', 1, 'Messi>CR7', '2024-02-22'),
    ('Luis', 1, 'Yo diria que es el mejor y ya', '2024-01-22'),
    ('Mariano', 1, 'Messi es Messi y ya', '2024-01-25'),
    ('Garfield', 1, 'Mañana juega el goat', '2024-03-12')
]

try:
    cursor = conexion.cursor()
    cursor.executemany(sqlRespuestas1, respuestas)
    conexion.commit()
    print("Datos insertados en la tabla Respuestas")
except mariadb.Error as error:
    conexion.rollback()


sqlRespuestas2 = '''
    INSERT INTO Respuestas (UserName, TemaID, Respuestas, Fecha) VALUES (?, ?, ?, ?)
'''
respuestas2 = [
    ('Juancito22', 2, 'Yo diria que si', '2024-01-22'),
    ('Noobmaster69', 2, 'No', '2024-02-02'),
    ('El_Bichito_SIUUUU', 2, 'Quizas', '2024-01-12'),
    ('Marcos', 2, 'No, no lo estara', '2024-01-22'),
    ('Julian2', 2, 'Si, estiy emocionado', '2024-01-20'),
    ('Marc23', 2, 'No y no lo discuto', '2024-01-21'),
    ('Juancito22', 2, 'Tal vez', '2024-02-22'),
    ('Luis', 2, 'Si', '2024-01-22'),
    ('Mariano', 2, 'NO', '2024-01-25'),
    ('Garfield', 2, 'Creeria y espero que si', '2024-03-12')
]

try:
    cursor = conexion.cursor()
    cursor.executemany(sqlRespuestas2, respuestas2)
    conexion.commit()
except mariadb.Error as error:
    conexion.rollback()


sqlRespuestas3 = '''
    INSERT INTO Respuestas (UserName, TemaID, Respuestas, Fecha) VALUES (?, ?, ?, ?)
'''
respuestas3 = [
    ('Juancito22', 3, 'Yo diria que si fue por amor', '2024-01-22'),
    ('Noobmaster69', 3, 'No se', '2024-02-02'),
    ('El_Bichito_SIUUUU', 3, 'Quizas amor', '2024-01-12'),
    ('Marcos', 3, 'No, no lo se pero esta mejor', '2024-01-22'),
    ('Julian2', 3, 'Si, fue por amor', '2024-01-20'),
    ('Marc23', 3, 'No se pero mejoro su apariencia', '2024-01-21'),
    ('Juancito22', 3, 'Tal vez por amor', '2024-02-22'),
    ('Luis', 3, 'Si definitivo amor', '2024-01-22'),
    ('Mariano', 3, 'NO me gusta este wey', '2024-01-25'),
    ('Garfield', 3, 'No se, no opinare', '2024-03-12')
]

try:
    cursor = conexion.cursor()
    cursor.executemany(sqlRespuestas3, respuestas3)
    conexion.commit()
except mariadb.Error as error:
    conexion.rollback()


sqlRespuestas4 = '''
    INSERT INTO Respuestas (UserName, TemaID, Respuestas, Fecha) VALUES (?, ?, ?, ?)
'''
respuestas4 = [
    ('Juancito22', 4, 'Yo diria que si es buena opcion que participe', '2024-01-22'),
    ('Noobmaster69', 4, 'No, audi no debe de competir', '2024-02-02'),
    ('El_Bichito_SIUUUU', 4, 'No me gusta la F1', '2024-01-12'),
    ('Marcos', 4, 'No veo la F1', '2024-01-22'),
    ('Julian2', 4, 'Que es un nuevo comienzo para AUDI', '2024-01-20'),
    ('Marc23', 4, 'No opinare mejor', '2024-01-21'),
    ('Juancito22', 4, 'Te amo Carlos SAINS', '2024-02-22'),
    ('Luis', 4, 'Odio la F1', '2024-01-22'),
    ('Mariano', 4, 'No me gusta AUDO', '2024-01-25'),
    ('Garfield', 4, 'Creeria que es bueno, pero no me gusta la decision', '2024-03-12')
]

try:
    cursor = conexion.cursor()
    cursor.executemany(sqlRespuestas4, respuestas4)
    conexion.commit()
except mariadb.Error as error:
    conexion.rollback()

bienvenida_label = Label(root, text="Bienvenido a ForumMaster")
bienvenida_label.grid(row=0, column=2)

user_verify = StringVar()
pass_verify = StringVar()

users_label = Label(root, text="Nombre usuario:")
users_label.grid(row=3, column=1)
users_entry = Entry(root, width=50, textvariable=user_verify)
users_entry.grid(row=3, column=3)

espacio = Label(root, text=" ")
espacio.grid(row=1, column=4)

passs_label = Label(root, text="Contraseña:")
passs_label.grid(row=5, column=1)
passs_entry = Entry(root, width=50, textvariable=pass_verify, show="*")
passs_entry.grid(row=5, column=3)

Button_crearusuario = Button(text='Crear usuario', command=ventana_usuario)
Button_crearusuario.grid(row=7, column=1, pady=20)

Button_login = Button(text='Login', command=Login)
Button_login.grid(row=7, column=3, pady=20)

root.mainloop()
