import cv2
import matplotlib.pyplot as plt

filename = 'FlorColores.jpg'
imagen = cv2.imread(filename)
imagen.shape
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
umbral_bajo = (25, 0,0)
umbral_alto=(70,255,255)
mask = cv2.inRange(img_hsv, umbral_bajo, umbral_alto)
res = cv2.bitwise_and(imagen, imagen, mask=mask)
plt.subplot(1,3,1)
plt.imshow(imagen)
plt.subplot(1,3,2)
plt.imshow(mask, cmap='gray')
plt.subplot(1,3,3)
plt.imshow(res)
plt.show()