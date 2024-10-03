import flet as ft
from imgTamaño import process_image  # Asegúrate de que este nombre coincida con el archivo donde está la función

def main(page: ft.Page):
    def on_process_click(e):
        if not file_picker.result.files or not object_width.value:
            result.value = "Please provide both image path and object width."
        else:
            file_path = file_picker.result.files[0].path
            width = float(object_width.value)
            side = side_selector.value
            processed_image_path = process_image(file_path, width, side)
            image_original.src = file_path
            image_processed.src = processed_image_path
            result.value = "Image processed successfully."
        page.update()

    def on_file_pick(e):
        if file_picker.result.files:
            file_path.value = file_picker.result.files[0].name
        page.update()

    file_picker = ft.FilePicker(on_result=on_file_pick)
    file_path = ft.TextField(label="Selected File", read_only=True)
    object_width = ft.TextField(label="Object Width (cm)", keyboard_type=ft.KeyboardType.NUMBER)
    side_selector = ft.Dropdown(
        options=[
            ft.dropdown.Option("Left"),
            ft.dropdown.Option("Right")
        ],
        label="Select Measurement Side"
    )
    result = ft.Text()
    process_button = ft.ElevatedButton(text="Process Image", on_click=on_process_click)
    select_file_button = ft.ElevatedButton(text="Select File", on_click=lambda _: file_picker.pick_files())

    image_original = ft.Image()
    image_processed = ft.Image()

    page.add(
        ft.Column(controls=[
            file_picker,
            select_file_button,
            file_path,
            object_width,
            side_selector,
            process_button,
            result,
            ft.Row(controls=[image_original, image_processed])
        ])
    )

ft.app(target=main)
