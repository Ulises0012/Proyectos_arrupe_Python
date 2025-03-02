import cv2
import tkinter as tk
from tkinter import filedialog

def procesar_imagen():
    file_path = filedialog.askopenfilename()
    
    if file_path:
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')
        upperbody_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')

        img = cv2.imread(file_path)
        if img is None:
            print("No se pudo leer la imagen. Verifique la ruta proporcionada.")
            return
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        upperbody = upperbody_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in upperbody:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

root = tk.Tk()
root.title("Selección de Imagen")

btn_select_image = tk.Button(root, text="Seleccionar Imagen", command=procesar_imagen)
btn_select_image.pack(pady=20)

root.mainloop()
