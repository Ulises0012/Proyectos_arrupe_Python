import tkinter as tk
from tkinter import messagebox
import mariadb

def conectar_db():
    global conexion
    try:
        conexion = mariadb.connect(
            user="root", password="",
            host="localhost",port=3306,
            database="prueba"
        )
    except mariadb.Error as error:
        messagebox.showerror("Error de conexión", str(error))
        return None
    
def ejecutar_consulta_fecthone(query):
    try:
        conectar_db()
        cursor=conexion.cursor()
        cursor.execute(query)
        mostrar_resultado(cursor.fetchmany())
    except mariadb.Error as error:
        messagebox.showerror("Error de consulta", str(error))
def ejecutar_consulta_fetchmany(query, num_resultados):
    try:
        conectar_db()
        cursor=conexion.cursor()
        cursor.execute(query)
        mostrar_resultados(cursor.fetchmany(num_resultados))
    except mariadb.Error as error:
        messagebox.showerror("Error de consulta", str(error))
def ejecutar_consulta_fetcall(query):
    try:
        conectar_db()
        cursor=conexion.cursor()
        cursor.execute(query)
        mostrar_resultados(cursor.fetchall())
    except mariadb.Error as error:
        messagebox.showerror("Error de consulta", str(error))


def mostrar_resultado(resultado):
    ventana_resultado = tk.Toplevel()
    ventana_resultado.title("Resultado de la consulta")

    if resultado:
        mensaje_resultado= f"Resultado de la consulta :\n\nNombre: {resultado[0]},  Ciudad: {resultado[0]}"
        etiqueta_resultado = tk.Label(ventana_resultado, text=mensaje_resultado)
        etiqueta_resultado.pack()
    else:
        etiqueta_resultado=tk.Label(ventana_resultado, text="No se encontró ningún resultado")
        etiqueta_resultado.pack()
def mostrar_resultados(resultados):
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultados de la consulta")

    if resultados: 
        mensaje_resultados = "resultados de la consulta:\n\n"
        for resultado in resultados:
            mensaje_resultados+= f"Nombre:{resultado[0]}, Ciudad{resultado[1]}\n"
        etiqueta_resultados =tk.Label(ventana_resultados, text=mensaje_resultados)
        etiqueta_resultados.pack()

def obtener_resultados():
    query = entrada_consulta.get()
    ejecutar_consulta_fecthone(query)


def obtener_resultado():
    query = entrada_consulta.get()
    ejecutar_consulta_fecthone(query)

def obtener_resultados():
    query = entrada_consulta.get()
    ejecutar_consulta_fetchmany(query,2)

def obtener_todos():
    query = entrada_consulta.get()
    ejecutar_consulta_fetcall(query)


ventana = tk.Tk()
ventana.title("Gestor deBase de datos")
etiqueta_consulta = tk.Label(ventana, text="Introduce una consulta SQL")
etiqueta_consulta.pack()
entrada_consulta = tk.Entry(ventana,width=50)
entrada_consulta.pack()

boton_resultado = tk.Button(ventana, text="Obtener un solo resultado", command=obtener_resultado)
boton_resultado.pack()


boton_resultado = tk.Button(ventana, text="Obtener mas de un resultado", command=obtener_resultados)
boton_resultado.pack()


boton_resultado = tk.Button(ventana, text="Todos los resultados", command=obtener_todos)
boton_resultado.pack()

ventana.mainloop()