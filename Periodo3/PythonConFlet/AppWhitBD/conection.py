import flet as ft
import mariadb

def Connection(page: ft.Page):
    try:
            db= mariadb.connect(
                host= "localhost",
                user = "root",
                password = "",
                database = "reservahoteles"

            )
            cursor = db.cursor()
            return db,cursor
    except mariadb.Error as err:
        page.add(ft.Text(f"Error al conectar a la base de datos: {err}", color="red"))
        return None, None