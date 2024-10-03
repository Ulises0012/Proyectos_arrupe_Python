import flet as ft
import mariadb
import bcrypt
from conection import Connection
from navigation import navigate_to_welcome  # Importa la función de navegación adecuada

def Login_page(page: ft.Page):
    db, cursor = Connection(page)

    def navigate_to_register_page(e):
        from navigation import navigate_to_register
        navigate_to_register(page)

    def login_user(e):
        username = username_field.value
        password = password_field.value

        cursor.execute("SELECT contrasena FROM usuarios WHERE usuario = ?", (username,))
        result = cursor.fetchone()

        if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
            navigate_to_welcome(page)  # Redirige a la página de bienvenida
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Invalid username or password!"), open=True)
            page.update()

    username_field = ft.TextField(
        width=280,
        height=40,
        hint_text="Username",
        border="underline",
        color="white",
        prefix_icon=ft.icons.PERSON,
    )

    password_field = ft.TextField(
        width=280,
        height=40,
        hint_text="Password",
        border="underline",
        color="white",
        prefix_icon=ft.icons.LOCK,
        password=True
    )

    Container = ft.Container(
        ft.Column([
            ft.Container(
                ft.Text(
                    "Login",
                    width=320,
                    size=30,
                    color="white",
                    text_align="center",
                    weight="bold"
                ),
                padding=ft.padding.only(20, 20)
            ),
            ft.Container(username_field, padding=ft.padding.only(20, 20)),
            ft.Container(password_field, padding=ft.padding.only(20, 20)),
            ft.Container(
                ft.ElevatedButton(
                    text="Login",
                    width=280,
                    on_click=login_user
                ),
                padding=ft.padding.only(20, 20)
            ),
            ft.Container(
                ft.TextButton(
                    text="Don't have an account? Register",
                    on_click=navigate_to_register_page
                ),
                padding=ft.padding.only(20, 20)
            )
        ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        ),
        border_radius=20,
        width=320,
        height=500,
        gradient=ft.LinearGradient([
            ft.colors.GREEN,
            ft.colors.BLUE
        ]),
    )

    t = ft.Text(
        value="Welcome to the hotel gestion page",
        color="#0B636B",
        size=24,
        weight="bold",
        font_family="Impact",
        text_align=ft.TextAlign.CENTER
    )

    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.add(ft.Container(content=t, alignment=ft.alignment.center), Container)
