import flet as ft
from clase import clase
from segunda_pagina import segundapagina
def example(page: ft.Page):
    def navigate_to_clase(e):
        page.clean()
        page.add(ft.Row([menubar]))
        clase(page)
    def navigate_to_segundaclase(e):
        page.clean()
        page.add(ft.Row([menubar]))
        segundapagina(page)
    def inicio(e):
        page.clean()
        example(page)
    
    menubar = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor=ft.colors.RED_100,
            mouse_cursor={
                ft.MaterialState.HOVERED: ft.MouseCursor.WAIT,
                ft.MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
            },
        ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("File"),
                controls=[
                        ft.MenuItemButton(
                        content=ft.Text("inicio"),
                        leading=ft.Icon(ft.icons.PAGEVIEW_OUTLINED),
                        style=ft.ButtonStyle(
                            bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}
                        ),
                        
                        on_click=inicio
                    ),

                        ft.MenuItemButton(
                        content=ft.Text("Clase"),
                        leading=ft.Icon(ft.icons.PAGEVIEW_OUTLINED),
                        style=ft.ButtonStyle(
                            bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}
                        ),
                        on_click=navigate_to_clase
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Segunda clase"),
                        leading=ft.Icon(ft.icons.PAGEVIEW_OUTLINED),
                        style=ft.ButtonStyle(
                            bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_100}
                        ),
                        on_click=navigate_to_segundaclase
                    ),
                ],
            ),
            ft.SubmenuButton(
                content=ft.Text("View"),
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("Zoom"),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Magnify"),
                                leading=ft.Icon(ft.icons.ZOOM_IN),
                                close_on_click=False,
                                style=ft.ButtonStyle(
                                    bgcolor={ft.MaterialState.HOVERED: ft.colors.PURPLE_200}
                                ),
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Minify"),
                                leading=ft.Icon(ft.icons.ZOOM_OUT),
                                close_on_click=False,
                                style=ft.ButtonStyle(
                                    bgcolor={ft.MaterialState.HOVERED: ft.colors.PURPLE_200}
                                ),
                            ),
                        ],
                    )
                ],
            ),
        ],
    )

    page.add(ft.Row([menubar]))

    texto = ft.Text(value="Bienvenido a la pagina de inicio", color="Green", size=40)
    page.add(texto)

ft.app(target=example)
