import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as compare_ssim

# Función para cargar y mostrar imágenes con matplotlib
def load_and_display(image_path):
    image = cv2.imread(image_path)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Cargar las dos imágenes de entrada
imageA = load_and_display("ID1.jpg")
imageB = load_and_display("ID2.jpg")
briggerA = cv2.resize(imageA, (479,304))

briggerB = cv2.resize(imageB, (479,304))

# Aplicar filtro de desenfoque gaussiano a las imágenes
blurA = cv2.GaussianBlur(briggerA, (25, 25), 2.2)
blurB = cv2.GaussianBlur(briggerB, (25, 25), 2.2)
#Decidi utilizar el filtro Gausiano ya que despues de probar todos los filtros era el que mejor funcionaba para poder definir las diferencias

# Convertir las imágenes a escala de grises
grayA = cv2.cvtColor(blurA, cv2.COLOR_RGB2GRAY)
grayB = cv2.cvtColor(blurB, cv2.COLOR_RGB2GRAY)

# Calcular el Índice de Similitud Estructural (SSIM) entre las dos imágenes
score, diff = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))  # Mostrar el SSIM (Similitud Estructural)

# Umbralizar la imagen de diferencia
_, thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Mostrar las imágenes en una sola ventana utilizando matplotlib
plt.figure(figsize=(12, 8))

# Imagen original 1
plt.subplot(1, 3, 1)
plt.imshow(imageA)
plt.title('Primer Imagen')
plt.xticks([]), plt.yticks([])

# Imagen original 2
plt.subplot(1, 3, 2)
plt.imshow(imageB)
plt.title('Segunda Imagen '  + "SSIM: {}".format(score))
plt.xticks([]), plt.yticks([])
# Regiones de diferencia (umbralizadas)
plt.subplot(1, 3, 3)
plt.imshow(thresh, cmap='gray')
plt.title('Regiones de Diferencia')
plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()

cv2.imwrite('prueba.png',thresh)

cv2.imwrite('ID2_pro.png',imageB)
#DataSmarts. (2021, 3 noviembre). Cómo Cargar y Guardar Imágenes en OpenCV [Vídeo]. YouTube. https://www.youtube.com/watch?v=mXCjS4kXaWw