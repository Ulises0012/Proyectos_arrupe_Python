import cv2
import matplotlib.pyplot as plt

filename = 'Frutas-Verduras.jpg'
imagen = cv2.imread(filename)
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(imagen, cv2.COLOR_RGB2HSV)

# Máscara 1
umbral_bajo = (25, 0, 0)
umbral_alto = (70, 255, 255)
mask = cv2.inRange(img_hsv, umbral_bajo, umbral_alto)
res = cv2.bitwise_and(imagen, imagen, mask=mask)

# Máscara 2
umbral_bajo2 = (15, 0, 0)
umbral_alto2 = (30, 255, 255)
mask2 = cv2.inRange(img_hsv, umbral_bajo2, umbral_alto2)
res2 = cv2.bitwise_and(imagen, imagen, mask=mask2)

# Máscara 3
umbral_bajo3 = (10, 0, 0)
umbral_alto3 = (35, 255, 255)
mask3 = cv2.inRange(img_hsv, umbral_bajo3, umbral_alto3)
res3 = cv2.bitwise_and(imagen, imagen, mask=mask3)

# Mostrar las imágenes
plt.figure(figsize=(15, 10))

# Imagen original
plt.subplot(2, 4, 1)
plt.imshow(imagen)
plt.title('Imagen Original')
plt.axis('off')

# Máscara 1
plt.subplot(2, 4, 2)
plt.imshow(mask, cmap='gray')
plt.title('Máscara 1')
plt.axis('off')

# Resultado 1
plt.subplot(2, 4, 3)
plt.imshow(res)
plt.title('Resultado 1')
plt.axis('off')

# Máscara 2
plt.subplot(2, 4, 4)
plt.imshow(mask2, cmap='gray')
plt.title('Máscara 2')
plt.axis('off')

# Resultado 2
plt.subplot(2, 4, 5)
plt.imshow(res2)
plt.title('Resultado 2')
plt.axis('off')

# Máscara 3
plt.subplot(2, 4, 6)
plt.imshow(mask3, cmap='gray')
plt.title('Máscara 3')
plt.axis('off')

# Resultado 3
plt.subplot(2, 4, 7)
plt.imshow(res3)
plt.title('Resultado 3')
plt.axis('off')

plt.tight_layout()
plt.show()
