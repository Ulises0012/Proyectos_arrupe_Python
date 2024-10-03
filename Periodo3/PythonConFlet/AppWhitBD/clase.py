import flet as ft
import time

def clase(page: ft.Page):
    t = ft.Text(value="Hola, mundo", color="Green")
    page.add(t)
    time.sleep(1)

    for i in range(10):
        t.value = f"contador : {i}"
        page.update()
        time.sleep(1)

    page.add(
        ft.Row(controls=[
            ft.Text("Bloque 1"),
            ft.Text("Bloque 2"),
            ft.Text("Bloque 3")
        ])
    )
    
    def button_Clicked(e):
        clicked_control = e.control
        page.add(ft.Text(f"Haz dado click al boton: {clicked_control.text}"))

    button = ft.ElevatedButton(text="Presiona el bóton", on_click=button_Clicked)
    page.add(button)
    
    nombre = ft.TextField(label="Nombre")
    apellido = ft.TextField(label="Apellido")
    page.add(nombre, apellido)

    async def button_clickeds(e):
        t.value = f"Checkboxes values are: {c1.value}, {c2.value}, {c3.value}, {c4.value}, {c5.value}."
        await t.update_async()

    t = ft.Text()
    c1 = ft.Checkbox(label="Unchecked by default checkbox", value=False)
    c2 = ft.Checkbox(label="Undefined by default tristate checkbox", tristate=True)
    c3 = ft.Checkbox(label="Checked by default checkbox", value=True)
    c4 = ft.Checkbox(label="Disabled checkbox", disabled=True)
    c5 = ft.Checkbox(
        label="Checkbox with rendered label_position='left'",
        label_position=ft.LabelPosition.LEFT,
    )
    b = ft.ElevatedButton(text="Submit", on_click=button_clickeds)

    page.add(ft.Column(controls=[c1, c2, c3, c4, c5, b, t]))

    def close_anchor(e):
        text = f"Color {e.control.data}"
        print(f"closing view from {text}")
        anchor.close_view(text)

    def open_anchor(e):
        anchor.open_view()

    def handle_change(e):
        print(f"handle_change e.data: {e.data}")

    def handle_submit(e):
        print(f"handle_submit e.data: {e.data}")

    def handle_tap(e):
        print(f"handle_tap")

    anchor = ft.SearchBar(
        view_elevation=4,
        divider_color=ft.colors.AMBER,
        bar_hint_text="Search colors...",
        view_hint_text="Choose a color from the suggestions...",
        on_change=handle_change,
        on_submit=handle_submit,
        on_tap=handle_tap,
        controls=[
            ft.ListTile(title=ft.Text(f"Color {i}"), on_click=close_anchor, data=i)
            for i in range(10)
        ],
    )

    page.add(ft.Column(
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.OutlinedButton(
                        "Open Search View",
                        on_click=open_anchor,
                    ),
                ],
            ),
            anchor,
        ]
    ))