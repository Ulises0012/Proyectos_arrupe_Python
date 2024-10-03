import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

def seleccionar_archivo():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal
    archivo = filedialog.askopenfilename(title="Selecciona una imagen", filetypes=[("Imágenes", "*.jpg *.jpeg *.png *.bmp")])
    return archivo

def mostrar_imagenes(titulo, imagenes, cmap=None):
    plt.figure(figsize=(10, 5))
    for i, imagen in enumerate(imagenes):
        plt.subplot(1, len(imagenes), i + 1)
        plt.imshow(imagen, cmap=cmap)
        plt.title(f"{titulo} {i + 1}")
        plt.axis('off')
    plt.show()

# 1. Redimensionar la Imagen
def redimensionar_imagen(imagen):
    # Método 1: Redimensionar utilizando interpolación lineal
    imagen_redimensionada_linear = cv2.resize(imagen, (400, 300), interpolation=cv2.INTER_LINEAR)
    # Método 2: Redimensionar utilizando interpolación cúbica
    imagen_redimensionada_cubic = cv2.resize(imagen, (400, 300), interpolation=cv2.INTER_CUBIC)
    
    mostrar_imagenes('Redimensionada', [imagen_redimensionada_linear, imagen_redimensionada_cubic])
    return imagen_redimensionada_linear, imagen_redimensionada_cubic

# 2. Aplicar Desenfoques
def aplicar_desenfoque(imagen):
    # Aplicar desenfoque gaussiano
    imagen_desenfocada = cv2.GaussianBlur(imagen, (15, 15), 0)
    
    mostrar_imagenes('Desenfoque', [imagen, imagen_desenfocada])
    return imagen_desenfocada

# 3. Detección de Bordes
def detectar_bordes(imagen):
    # Convertir a escala de grises si no está ya en gris
    if len(imagen.shape) == 3:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Aplicar el detector de bordes de Canny
    bordes = cv2.Canny(imagen, 100, 200)
    
    mostrar_imagenes('Detección de Bordes', [imagen, bordes], cmap='gray')
    return bordes

# 4. Operaciones Aritméticas entre Imágenes
def operaciones_aritmeticas(imagen1, imagen2):
    # Asegurarse de que las imágenes tengan el mismo tamaño
    imagen1 = cv2.resize(imagen1, (500, 500))
    imagen2 = cv2.resize(imagen2, (500, 500))
    
    # Suma de las imágenes
    suma_imagenes = cv2.add(imagen1, imagen2)
    
    # Visualizar las imágenes originales y la suma
    mostrar_imagenes('Operaciones Aritméticas', [imagen1, imagen2, suma_imagenes])
    return suma_imagenes

if __name__ == "__main__":
    ruta_imagen = seleccionar_archivo()
    imagen = cv2.imread(ruta_imagen)

    # 1. Redimensionar la Imagen
    redimensionar_imagen(imagen)

    # 2. Aplicar Desenfoques
    aplicar_desenfoque(imagen)

    # 3. Detección de Bordes
    detectar_bordes(imagen)

    # Seleccionar dos imágenes para operaciones aritméticas
    ruta_imagen1 = seleccionar_archivo()
    ruta_imagen2 = seleccionar_archivo()

    imagen1 = cv2.imread(ruta_imagen1)
    imagen2 = cv2.imread(ruta_imagen2)

    # 4. Operaciones Aritméticas entre Imágenes
    operaciones_aritmeticas(imagen1, imagen2)
