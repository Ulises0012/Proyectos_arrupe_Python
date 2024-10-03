import flet as ft
import cv2
import tempfile
import os

def main(page: ft.Page):
    text = ft.Text(value="Detección de rostros de gatos", size=20, color="#191970")
    text_row = ft.Row(controls=[text], alignment="center")
    img = ft.Image(width=500, height=500)
    img_row = ft.Row(controls=[img], alignment="center")
    error_text = ft.Text(value="", color="red")
    error_row = ft.Row(controls=[error_text], alignment="center")
    
    image_path_text = ft.TextField(label="Ruta de la imagen cargada", read_only=True)
    path_row = ft.Row(controls=[image_path_text], alignment="center")
    
    image_path = [None]
    
    def cargar_imagen(e):
        if e.files:
            image_path[0] = e.files[0].path
            filename = os.path.basename(image_path[0])
            image_path_text.value = filename
            error_text.value = ""
            page.update()
    
    def analizar_imagen(e):
        if image_path[0]:
            try:
                procesada_path = procesar_imagen(image_path[0])
                img.src = procesada_path
                error_text.value = ""
                page.update()
            except Exception as ex:
                error_text.value = str(ex)
                page.update()
        else:
            error_text.value = "Primero sube una imagen"
            page.update()    
    
    def procesar_imagen(image_path):
        cargar_gatos_harr = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("No se pudo cargar la imagen")
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        gatos = cargar_gatos_harr.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=10, minSize=(30, 30), maxSize=(100, 100))
        
        for (x, y, w, h) in gatos:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 4)
        
        temp_file = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
        cv2.imwrite(temp_file.name, image)
        
        return temp_file.name
    
    def subir_imagen(e):
        cargar_imagen_btn.pick_files()
        
    cargar_imagen_btn = ft.FilePicker(on_result=cargar_imagen)
    page.overlay.append(cargar_imagen_btn)
    subir_btn = ft.ElevatedButton(text="Subir imagen", on_click=subir_imagen)
    analizar_btn = ft.ElevatedButton("Analizar imagen", on_click=analizar_imagen)
    btn_row = ft.Row(controls=[subir_btn, analizar_btn], alignment="center")
    
    page.add(text_row, img_row, path_row, btn_row, error_row)

ft.app(main)
