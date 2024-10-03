import flet as ft
import mariadb
from conection import Connection
def Welcome (page: ft.Page):
    db, cursor = Connection(page)
    t=ft.Text(
        value="Welcome to the hotel gestion page",
        color="#0B636B",
        size=24,
        weight="bold",
        font_family="Impact",
        text_align=ft.TextAlign.CENTER
    )
    name = ft.TextField(label="Name", width=300)
    lastname = ft.TextField(label="LastName", width=300)
    table_name = ft.TextField(label="Name table", width=300)

    def create_table(e):
        if not table_name.value:
            page.add(ft.Text("Please, enter the name of the table", color="red"))
            return
        try:
            sql = f"""
            CREATE TABLE IF NOT EXISTS {table_name.value}(
                id INT  AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50),
                lastname vARCHAR(50)
            )"""
            cursor.execute(sql)
            db.commit()
            page.add(ft.Text(f"Table '{table_name.value}' Created correctly", color="#481473"))
        except mariadb.Error as err:
            page.add(ft.Text(f"Error to create the table: {err}", color="red"))
    def insert_table(e):
        clicked_control = e.control
        if not name.value or not lastname.value or not table_name.value:
            page.add(ft.Text("Please, complete all the camps", color="red"))
            return
        
        try:
            sql = f"INSERT INTO {table_name.value}(name, lastname) VALUES (%s,%s)"
            val = (name.value, lastname.value)
            cursor.execute(sql, val)
            db.commit()
            page.add(ft.Text("Data insertion successful", color="green"))
        except mariadb.Error as err:
            page.add(ft.Text(f"Error to insert: {err}", color="red"))
    insert_button = ft.ElevatedButton(text="insert user data", on_click=insert_table)
    create_table_button = ft.ElevatedButton(text="Create table", on_click=create_table)

    page.add(
        ft.Container(content=t,alignment=ft.alignment.center),
        ft.Container(content=table_name, alignment=ft.alignment.center),
        ft.Container(content=create_table_button, alignment=ft.alignment.center),
        ft.Container(content=name, alignment=ft.alignment.center),
        ft.Container(content=lastname, alignment=ft.alignment.center),
        ft.Container(content=insert_button, alignment=ft.alignment.center)
        )