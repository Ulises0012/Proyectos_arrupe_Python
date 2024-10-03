import flet as ft
import mariadb
import bcrypt
from conection import Connection

def Register_page(page: ft.Page):
    db, cursor = Connection(page)

    def register_user(e):
        username = username_field.value  # Cambiado de usuario a username
        password = password_field.value
        confirm_password = confirm_password_field.value

        if password != confirm_password:
            page.snack_bar = ft.SnackBar(ft.Text("Passwords do not match!"), open=True)
            page.update()
            return

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        try:
            cursor.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", (username, hashed_password))  # Cambiado usuario a username
            db.commit()
            page.snack_bar = ft.SnackBar(ft.Text("Registration successful!"), open=True)
        except mariadb.Error as e:
            page.snack_bar = ft.SnackBar(ft.Text(f"Error: {e}"), open=True)

        page.update()

    def navigate_to_login_page(e):
        from navigation import navigate_to_login
        navigate_to_login(page)

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

    confirm_password_field = ft.TextField(
        width=280,
        height=40,
        hint_text="Confirm Password",
        border="underline",
        color="white",
        prefix_icon=ft.icons.LOCK,
        password=True
    )

    Container = ft.Container(
        ft.Column([
            ft.Container(
                ft.Text(
                    "Register",
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
            ft.Container(confirm_password_field, padding=ft.padding.only(20, 20)),
            ft.Container(
                ft.ElevatedButton(
                    text="Register",
                    width=280,
                    on_click=register_user
                ),
                padding=ft.padding.only(20, 20)
            ),
            ft.Container(
                ft.TextButton(
                    text="Already have an account? Login",
                    on_click=navigate_to_login_page
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
            ft.colors.PINK,
            ft.colors.PURPLE
        ]),
    )

    t = ft.Text(
        value="Create a new account",
        color="#0B636B",
        size=24,
        weight="bold",
        font_family="Impact",
        text_align=ft.TextAlign.CENTER
    )

    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.add(ft.Container(content=t, alignment=ft.alignment.center), Container)
